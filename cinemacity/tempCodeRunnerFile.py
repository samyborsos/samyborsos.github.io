from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import concurrent.futures
import datetime
import os
import urllib.request
import urllib.parse
import json
import time

# --- BEÁLLÍTÁSOK ---
OUTPUT_FOLDER = "cinemacity"
OUTPUT_FILE = "index.html"

# Csak Győr maradt a listában
MOZIK = {
    "Győr": "1125"
}

# Megnövelt napok száma (teljes hét lefedése)
DAYS_TO_SCRAPE = 8  
MAX_IMDB_WORKERS = 10 
# ---------------------

# Gyorsítótár az IMDb adatokhoz
imdb_map = {}

def get_imdb_data_worker(title):
    """
    IMDb adatokat keres a __NEXT_DATA__ JSON-ból.
    """
    search_title = title.replace(" - ", " ").split("|")[0].strip()
    if search_title in imdb_map: return search_title, imdb_map[search_title]

    try:
        encoded = urllib.parse.quote(search_title)
        url = f"https://www.imdb.com/find/?q={encoded}"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36', 'Accept-Language': 'en-US,en;q=0.9'}
        
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response:
            html = response.read().decode('utf-8')
            start_marker = '<script id="__NEXT_DATA__" type="application/json">'
            idx = html.find(start_marker)
            if idx == -1: return search_title, None
            
            idx += len(start_marker)
            end = html.find('</script>', idx)
            data = json.loads(html[idx:end])
            
            results = data.get('props', {}).get('pageProps', {}).get('titleResults', {}).get('results', [])
            if not results: return search_title, None
                
            item = results[0].get('listItem', {})
            info = {
                'rating': str(item.get('ratingSummary', {}).get('aggregateRating', 'N/A')),
                'votes': item.get('ratingSummary', {}).get('voteCount', 0),
                'plot': item.get('plot', ''),
                'poster': item.get('primaryImage', {}).get('url', ''),
                'id': item.get('titleId', '')
            }
            return search_title, info
    except:
        return search_title, None

def run_scraper():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--log-level=3")
    
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 5) # Gyors timeout, ha nincs műsor

    weekly_data = {}
    all_unique_titles = set()
    
    today = datetime.date.today()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    print(f"🚀 Győri moziműsor letöltése {DAYS_TO_SCRAPE} napra...")

    # --- 1. FÁZIS: MŰSOR BEGYŰJTÉSE ---
    for i in range(DAYS_TO_SCRAPE):
        target_date = today + datetime.timedelta(days=i)
        date_str = target_date.strftime("%Y-%m-%d")
        
        # Magyar napok
        days_hu = ["Hétfő", "Kedd", "Szerda", "Csütörtök", "Péntek", "Szombat", "Vasárnap"]
        day_name = days_hu[target_date.weekday()]
        display_date = f"{day_name}, {target_date.strftime('%b %d')}"
        
        print(f"\n📅 Dátum feldolgozása: {date_str} ({display_date})")
        
        mozi_nev = "Győr"
        mozi_id = MOZIK[mozi_nev]
        url = f"https://www.cinemacity.hu/cinemas/cinema/{mozi_id}#/buy-tickets-by-cinema?in-cinema={mozi_id}&at={date_str}&view-mode=list"
        
        movies_found = []
        try:
            driver.get(url)
            wait.until(EC.presence_of_element_located((By.CLASS_NAME, "movie-row")))
            elements = driver.find_elements(By.CLASS_NAME, "movie-row")
            
            for m in elements:
                try:
                    title = m.find_element(By.CLASS_NAME, "qb-movie-name").text.strip()
                    all_unique_titles.add(title)
                    
                    poster = "https://www.cinemacity.hu/xmedia/img/10102/film.placeholder.poster.jpg"
                    try:
                        img = m.find_element(By.CSS_SELECTOR, "div.movie-poster-container img")
                        src, dsrc = img.get_attribute("src"), img.get_attribute("data-src")
                        if src and "placeholder" not in src: poster = src
                        elif dsrc: poster = dsrc
                    except: pass
                    
                    trailer, info_link = "", ""
                    try:
                        t_el = m.find_element(By.CSS_SELECTOR, "a.youtube-video")
                        if "youtu" in t_el.get_attribute("href"): trailer = t_el.get_attribute("href").replace("watch?v=", "embed/")
                    except: pass
                    try: info_link = m.find_element(By.CSS_SELECTOR, "a.qb-movie-link").get_attribute("href")
                    except: pass

                    genre, duration, rating_src = "", "", ""
                    try: genre = m.find_element(By.CSS_SELECTOR, "span.mr-sm").text.replace("|", "").strip()
                    except: pass
                    try: duration = m.find_element(By.CSS_SELECTOR, "span.mr-xs").text.strip()
                    except: pass
                    try: rating_src = m.find_element(By.CSS_SELECTOR, "img.rating-icon").get_attribute("src")
                    except: pass

                    screenings = []
                    for row in m.find_elements(By.CLASS_NAME, "type-row"):
                        fmts = [s.text for s in row.find_elements(By.CSS_SELECTOR, "ul.qb-screening-attributes li span")]
                        times = [{'t': b.text.split("\n")[0], 'l': b.get_attribute("data-url")} for b in row.find_elements(By.CSS_SELECTOR, "a.btn-primary")]
                        if times: screenings.append({'fmt': fmts, 'times': times})

                    movies_found.append({
                        'title': title, 'poster': poster, 'trailer': trailer, 'info': info_link,
                        'genre': genre, 'dur': duration, 'rate_img': rating_src, 'scr': screenings
                    })
                except: continue
            
            print(f"  ✅ {len(movies_found)} film található.")
            
        except:
            print(f"  ❌ Nincs műsor vagy hiba.")
        
        # Csak akkor mentjük el a napot, ha van film
        if movies_found:
            weekly_data[date_str] = {
                'display': display_date,
                'movies': movies_found
            }

    driver.quit()

    # --- 2. FÁZIS: IMDB ADATOK (Párhuzamosan) ---
    if all_unique_titles:
        print(f"\n⚡ IMDb adatok letöltése {len(all_unique_titles)} filmhez...")
        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_IMDB_WORKERS) as executor:
            futures = {executor.submit(get_imdb_data_worker, t): t for t in all_unique_titles}
            for future in concurrent.futures.as_completed(futures):
                t, d = future.result()
                if d: imdb_map[t] = d

    # --- 3. FÁZIS: HTML GENERÁLÁS ---
    render_weekly_html(weekly_data, timestamp)

def render_weekly_html(weekly_data, timestamp):
    print("📝 HTML generálása...")
    
    # Dátumfülek generálása
    tabs_html = '<div class="flex space-x-3 overflow-x-auto pb-2 mb-6 scrollbar-hide snap-x">'
    grid_containers = ""
    
    sorted_dates = sorted(weekly_data.keys())
    if not sorted_dates:
        print("Hiba: Nincs megjeleníthető adat.")
        return

    first_date = sorted_dates[0]
    
    for date_key in sorted_dates:
        day_data = weekly_data[date_key]
        is_active = (date_key == first_date)
        
        # Aktív/Inaktív stílus
        active_class = "bg-orange-600 text-white shadow-lg scale-105" if is_active else "bg-white text-gray-600 border border-gray-200 hover:bg-orange-50"
        
        tabs_html += f'''
        <button onclick="switchDate('{date_key}')" id="btn-{date_key}" class="date-tab snap-center min-w-[120px] px-4 py-3 rounded-2xl font-bold text-sm transition-all duration-200 {active_class}">
            {day_data['display']}
        </button>
        '''
        
        # Műsor rács (Grid)
        hidden_class = "" if is_active else "hidden"
        grid_containers += f'<div id="grid-{date_key}" class="date-grid {hidden_class} grid grid-cols-1 gap-6 animate-fade-in">'
        
        # --- FILMEK LISTÁZÁSA ---
        for m in day_data['movies']:
            search = m['title'].replace(" - ", " ").split("|")[0].strip()
            imdb = imdb_map.get(search)
            
            poster = m['poster']
            rating_val = "N/A"
            votes = ""
            plot = ""
            imdb_link = f"https://www.imdb.com/find/?q={urllib.parse.quote(m['title'])}"
            
            if imdb:
                if imdb['poster']: poster = imdb['poster']
                rating_val = imdb['rating']
                if imdb['votes']:
                    v = imdb['votes']
                    votes = f"({v/1000:.1f}K)" if v > 1000 else f"({v})"
                plot = imdb['plot']
                if imdb['id']: imdb_link = f"https://www.imdb.com/title/{imdb['id']}/"

            is_new = "2024" in m['genre'] or "2025" in m['genre']
            new_badge = '<span class="bg-green-100 text-green-700 text-[10px] font-extrabold px-2 py-0.5 rounded border border-green-200 ml-2 uppercase tracking-wider">ÚJ</span>' if is_new else ''
            
            rating_badge = ""
            if rating_val != "N/A":
                col = "bg-yellow-400 text-black" if float(rating_val) < 8 else "bg-yellow-300 border-2 border-yellow-500 text-black"
                rating_badge = f'<a href="{imdb_link}" target="_blank" class="{col} text-[11px] font-bold px-1.5 py-0.5 rounded flex items-center shadow-sm ml-2 hover:opacity-80"><i class="fas fa-star text-[10px] mr-1"></i> {rating_val} <span class="text-[9px] font-normal ml-1 opacity-70">{votes}</span></a>'
            else:
                rating_badge = f'<a href="{imdb_link}" target="_blank" class="bg-gray-100 text-gray-500 text-[10px] font-bold px-1.5 py-0.5 rounded flex items-center border border-gray-200 ml-2"><i class="fas fa-search text-[10px] mr-1"></i> IMDb</a>'

            act_btn = ""
            if m['trailer']:
                act_btn = f'''<button onclick="openModal('{m['trailer']}', '{m['title'].replace("'", "")}')" class="text-xs font-bold text-red-600 hover:text-red-800 flex items-center mt-3 bg-red-50 border border-red-100 w-fit px-3 py-1.5 rounded-md"><i class="fas fa-play-circle mr-1.5 text-lg"></i> Előzetes</button>'''
            elif m['info']:
                act_btn = f'''<a href="{m['info']}" target="_blank" class="text-xs font-bold text-blue-600 hover:text-blue-800 flex items-center mt-3 bg-blue-50 border border-blue-100 w-fit px-3 py-1.5 rounded-md"><i class="fas fa-info-circle mr-1.5 text-lg"></i> Adatlap</a>'''

            scr_html = ""
            for s in m['scr']:
                fmt = " ".join(s['fmt'])
                bst, lbl, icn = "bg-gray-100 text-gray-600 border-gray-200", "2D", ""
                if "4DX" in fmt: bst, lbl, icn = "bg-red-50 text-red-600 border-red-100 font-black", "4DX", "⚡"
                elif "IMAX" in fmt: bst, lbl, icn = "bg-blue-50 text-blue-600 border-blue-100 font-black", "IMAX", "🎬"
                elif "3D" in fmt: bst, lbl, icn = "bg-teal-50 text-teal-600 border-teal-100", "3D", "👓"

                times = "".join([f'<a href="{t["l"]}" target="_blank" class="group relative inline-flex items-center justify-center bg-white border border-gray-200 hover:border-orange-500 hover:bg-orange-50 text-gray-800 text-sm font-bold px-3 py-1.5 rounded-lg transition-all mb-1 mr-1 shadow-sm">{t["t"]}</a>' for t in s['times']])
                scr_html += f'<div class="mb-3 last:mb-0 flex flex-col sm:flex-row sm:items-center"><div class="flex items-center mb-1 sm:mb-0 sm:mr-3 w-24 shrink-0"><span class="text-xs font-bold px-2 py-1 rounded border {bst} w-full text-center block shadow-sm">{icn} {lbl}</span></div><div class="flex flex-wrap gap-1.5">{times}</div></div>'

            grid_containers += f"""
            <div class="p-5 bg-white rounded-2xl shadow-sm border border-gray-200 hover:shadow-lg transition-all duration-300 flex gap-5 group">
                <div class="hidden sm:block w-28 flex-shrink-0 relative"><img src="{poster}" class="w-full rounded-lg shadow-md border border-gray-200 object-cover group-hover:scale-105 transition-transform duration-300"></div>
                <div class="flex-grow">
                    <div class="flex flex-col">
                        <div class="flex justify-between items-start">
                            <div>
                                <div class="flex items-center mb-1"><h3 class="font-bold text-gray-900 text-xl leading-tight group-hover:text-orange-600 transition-colors">{m['title']}</h3>{new_badge}{rating_badge}</div>
                                <div class="flex items-center text-xs text-gray-500 mb-2 font-medium uppercase tracking-wide">{f'<img src="{m["rate_img"]}" class="h-5 w-auto mr-2 opacity-80">' if m['rate_img'] else ''}<span class="mr-2 truncate max-w-[200px]">{m['genre']}</span><span>{m['dur']}</span></div>
                                {f'<p class="text-sm text-gray-600 mb-3 leading-snug line-clamp-2">{plot}</p>' if plot else ''}
                            </div>
                        </div>
                        <div class="bg-gray-50/50 rounded-xl p-2 border border-gray-100">{scr_html if scr_html else '<span class="text-gray-400 italic text-sm">Nincs időpont.</span>'}</div>
                        {act_btn}
                    </div>
                </div>
            </div>
            """
        
        grid_containers += "</div>" # Grid vége
    
    tabs_html += "</div>"

    full_html = f"""
    <!DOCTYPE html><html lang="hu"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Mozi Győr</title><link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🍿</text></svg>"><script src="https://cdn.tailwindcss.com"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><style>.modal {{ transition: opacity 0.25s ease; }} body.modal-active {{ overflow: hidden; }} .scrollbar-hide::-webkit-scrollbar {{ display: none; }} .scrollbar-hide {{ -ms-overflow-style: none; scrollbar-width: none; }} @keyframes fadeIn {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: translateY(0); }} }} .animate-fade-in {{ animation: fadeIn 0.3s ease-out forwards; }}</style></head><body class="bg-gray-50 min-h-screen font-sans text-gray-900">
    <div id="trailer-modal" class="modal opacity-0 pointer-events-none fixed inset-0 flex items-center justify-center z-50"><div class="modal-overlay absolute inset-0 bg-gray-900 opacity-95"></div><div class="modal-container bg-black w-full md:max-w-4xl mx-auto rounded shadow-lg z-50 overflow-y-auto"><div class="modal-content py-4 text-left px-6 relative"><div class="flex justify-between items-center pb-3"><p class="text-2xl font-bold text-white" id="modal-title">Előzetes</p><div class="cursor-pointer z-50 text-white" onclick="closeModal()"><i class="fas fa-times text-2xl"></i></div></div><div class="aspect-w-16 aspect-h-9"><iframe id="trailer-iframe" class="w-full h-[50vh] md:h-[60vh]" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div></div></div></div>
    
    <div class="max-w-4xl mx-auto px-4 py-8">
        <div class="flex flex-col md:flex-row justify-between items-end mb-6">
            <div>
                <h1 class="text-4xl font-extrabold text-gray-900 mb-1">Cinema City <span class="text-orange-600">Győr</span></h1>
                <p class="text-gray-500 text-sm">Frissítve: <span class="font-mono bg-gray-200 px-2 py-0.5 rounded text-gray-700 font-bold">{timestamp}</span></p>
            </div>
            <div class="mt-4 md:mt-0">
                </div>
        </div>
        
        {tabs_html}
        
        {grid_containers}
    </div>

    <script>
        function switchDate(dateKey) {{
            document.querySelectorAll('.date-grid').forEach(el => el.classList.add('hidden'));
            const target = document.getElementById('grid-' + dateKey);
            if(target) target.classList.remove('hidden');
            
            document.querySelectorAll('.date-tab').forEach(el => {{
                el.classList.remove('bg-orange-600', 'text-white', 'shadow-lg', 'scale-105');
                el.classList.add('bg-white', 'text-gray-600', 'border', 'border-gray-200');
            }});
            const btn = document.getElementById('btn-' + dateKey);
            if(btn) {{
                btn.classList.remove('bg-white', 'text-gray-600', 'border', 'border-gray-200');
                btn.classList.add('bg-orange-600', 'text-white', 'shadow-lg', 'scale-105');
            }}
        }}

        const modal = document.getElementById('trailer-modal');
        const iframe = document.getElementById('trailer-iframe');
        const modalTitle = document.getElementById('modal-title');
        function openModal(url, title) {{ if(!url)return; iframe.src = url + "?autoplay=1"; modalTitle.innerText = title; modal.classList.remove('opacity-0', 'pointer-events-none'); document.body.classList.add('modal-active'); }}
        function closeModal() {{ modal.classList.add('opacity-0', 'pointer-events-none'); iframe.src = ""; document.body.classList.remove('modal-active'); }}
        document.onkeydown = function(evt) {{ evt = evt || window.event; if (evt.keyCode == 27) closeModal(); }};
    </script>
    </body></html>
    """

    if not os.path.exists(OUTPUT_FOLDER): os.makedirs(OUTPUT_FOLDER)
    full_path = os.path.join(OUTPUT_FOLDER, OUTPUT_FILE)
    with open(full_path, "w", encoding="utf-8") as f: f.write(full_html)
    print(f"✅ Kész! Fájl mentve: {full_path}")

if __name__ == "__main__":
    run_scraper()