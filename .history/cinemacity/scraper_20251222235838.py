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
import re

# --- CONFIGURATION ---
OUTPUT_FOLDER = "cinemacity"
OUTPUT_FILE = "index.html"
MOZIK = { "Győr": "1125" }
MAX_IMDB_WORKERS = 10 
FAVICON_FILENAME = "https://images.icon-icons.com/1381/PNG/512/popcorntime_94336.png" 
# ---------------------

imdb_map = {}

HU_MONTHS = {
    "január": "01", "február": "02", "március": "03", "április": "04",
    "május": "05", "június": "06", "július": "07", "augusztus": "08",
    "szeptember": "09", "október": "10", "november": "11", "december": "12",
    "jan": "01", "feb": "02", "már": "03", "ápr": "04", "máj": "05", "jún": "06",
    "júl": "07", "aug": "08", "sze": "09", "okt": "10", "nov": "11", "dec": "12"
}

def clean_title(title):
    clean = re.sub(r'\(.*?\)', '', title)
    clean = clean.split(" - ")[0]
    clean = clean.split("|")[0]
    return clean.strip()

def resize_imdb_image(url):
    if not url or "media-amazon.com" not in url: return url
    if "._V1" in url:
        base = url.split("._V1")[0]
        return f"{base}._V1_UX600_.jpg"
    return url

def get_imdb_data_worker(title):
    search_title = clean_title(title)
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
            
            raw_poster = item.get('primaryImage', {}).get('url', '')
            optimized_poster = resize_imdb_image(raw_poster)
            
            info = {
                'rating': str(item.get('ratingSummary', {}).get('aggregateRating', 'N/A')),
                'votes': item.get('ratingSummary', {}).get('voteCount', 0),
                'plot': item.get('plot', ''),
                'year': item.get('releaseYear', 0),
                'poster': optimized_poster,
                'id': item.get('titleId', '')
            }
            return search_title, info
    except: return search_title, None

def get_valid_dates(driver, cinema_id):
    print("📅 Opening calendar...")
    today = datetime.date.today().strftime("%Y-%m-%d")
    url = f"https://www.cinemacity.hu/cinemas/cinema/{cinema_id}#/buy-tickets-by-cinema?in-cinema={cinema_id}&at={today}&view-mode=list"
    
    driver.get(url)
    time.sleep(3)
    
    valid_dates = set()
    valid_dates.add(today)
    
    try:
        wait = WebDriverWait(driver, 10)
        datepicker_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".datepicker-toggle")))
        driver.execute_script("arguments[0].click();", datepicker_btn)
        
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".datepicker-days")))
        active_days = driver.find_elements(By.CSS_SELECTOR, "td.day:not(.disabled)")
        for day in active_days:
            try:
                btn = day.find_element(By.TAG_NAME, "button")
                label = btn.get_attribute("aria-label").lower()
                parts = label.split()
                if len(parts) >= 3:
                    d, m_name, y = parts[0].zfill(2), parts[1], parts[2]
                    m = HU_MONTHS.get(m_name, "01")
                    full_date = f"{y}-{m}-{d}"
                    if full_date >= today:
                        valid_dates.add(full_date)
            except: continue
    except Exception as e:
        print(f"⚠️ Calendar error: {e}")
        for i in range(8):
            d = datetime.date.today() + datetime.timedelta(days=i)
            valid_dates.add(d.strftime("%Y-%m-%d"))

    sorted_dates = sorted(list(valid_dates))
    print(f"✅ Active Dates: {len(sorted_dates)} ({sorted_dates[0]} to {sorted_dates[-1]})")
    return sorted_dates

def run_scraper():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--log-level=3")
    
    driver = webdriver.Chrome(options=chrome_options)
    movies_db = {}
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    print(f"🚀 Starting Győr Scraper (Final Layout Fix)...")

    # 1. DATES
    target_dates = get_valid_dates(driver, MOZIK["Győr"])

    # 2. SCRAPE
    for date_str in target_dates:
        print(f"🎥 Scanning: {date_str}...", end=" ", flush=True)
        driver.get("about:blank")
        time.sleep(0.5)
        
        mozi_id = MOZIK["Győr"]
        url = f"https://www.cinemacity.hu/cinemas/cinema/{mozi_id}#/buy-tickets-by-cinema?in-cinema={mozi_id}&at={date_str}&view-mode=list"
        
        try:
            driver.get(url)
            time.sleep(2.5) 
            
            if len(driver.find_elements(By.CLASS_NAME, "movie-row")) == 0:
                 driver.refresh()
                 time.sleep(3)

            elements = driver.find_elements(By.CLASS_NAME, "movie-row")
            
            count = 0
            for m in elements:
                try:
                    title = m.find_element(By.CLASS_NAME, "qb-movie-name").text.strip()
                    count += 1
                    
                    if title not in movies_db:
                        movies_db[title] = {
                            "meta": {
                                "title": title,
                                "poster": "https://www.cinemacity.hu/xmedia/img/10102/film.placeholder.poster.jpg",
                                "trailer": "", "info": "", "genre": "", "dur": "", "rate_img": "", "new": False
                            },
                            "schedule": {}
                        }

                    meta = movies_db[title]["meta"]
                    
                    try:
                        img = m.find_element(By.CSS_SELECTOR, "div.movie-poster-container img")
                        src, dsrc = img.get_attribute("src"), img.get_attribute("data-src")
                        if "placeholder" in meta["poster"]:
                            if src and "placeholder" not in src: meta["poster"] = src
                            elif dsrc: meta["poster"] = dsrc
                    except: pass
                    
                    if not meta["trailer"]:
                        try:
                            t_el = m.find_element(By.CSS_SELECTOR, "a.youtube-video")
                            if "youtu" in t_el.get_attribute("href"): meta["trailer"] = t_el.get_attribute("href").replace("watch?v=", "embed/")
                        except: pass
                    
                    if not meta["info"]:
                        try: meta["info"] = m.find_element(By.CSS_SELECTOR, "a.qb-movie-link").get_attribute("href")
                        except: pass

                    if not meta["genre"]:
                        try: meta["genre"] = m.find_element(By.CSS_SELECTOR, "span.mr-sm").text.replace("|", "").strip()
                        except: pass
                        
                    if not meta["dur"]:
                        try: meta["dur"] = m.find_element(By.CSS_SELECTOR, "span.mr-xs").text.strip()
                        except: pass
                    
                    try: 
                        rate_img = m.find_element(By.CSS_SELECTOR, "img.rating-icon").get_attribute("src")
                        if rate_img: meta["rate_img"] = rate_img
                    except: pass
                    
                    if "2024" in meta["genre"] or "2025" in meta["genre"]: meta["new"] = True

                    daily_screenings = []
                    for row in m.find_elements(By.CLASS_NAME, "type-row"):
                        fmts = [s.text for s in row.find_elements(By.CSS_SELECTOR, "ul.qb-screening-attributes li span")]
                        for b in row.find_elements(By.CSS_SELECTOR, "a.btn-primary"):
                             daily_screenings.append({
                                 "time": b.text.split("\n")[0],
                                 "link": b.get_attribute("data-url"),
                                 "fmt": fmts
                             })
                    
                    if daily_screenings:
                        daily_screenings.sort(key=lambda x: x['time'])
                        movies_db[title]["schedule"][date_str] = daily_screenings

                except: continue
            print(f"✅ {count} movies")
        except: print("❌ Error")

    driver.quit()

    # 3. IMDB ENRICHMENT
    print(f"\n⚡ Enriching {len(movies_db)} movies with IMDb...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_IMDB_WORKERS) as executor:
        futures = {executor.submit(get_imdb_data_worker, t): t for t in movies_db.keys()}
        for future in concurrent.futures.as_completed(futures):
            t, d = future.result()
            if d: imdb_map[t] = d

    # 4. RENDER
    render_movie_centric_html(movies_db, timestamp, target_dates)

def render_movie_centric_html(movies_db, timestamp, all_dates):
    print("📝 Saving HTML...")
    
    def sort_key(t):
        search = clean_title(t)
        imdb = imdb_map.get(search, {})
        year = imdb.get('year', 0) if imdb else 0
        try: rating = float(imdb.get('rating', 0)) if imdb and imdb.get('rating') != 'N/A' else 0
        except: rating = 0
        return (year, rating, t)

    sorted_titles = sorted(movies_db.keys(), key=sort_key, reverse=True)
    
    grid_html = ""
    current_year = datetime.date.today().year

    for title in sorted_titles:
        data = movies_db[title]
        meta = data["meta"]
        schedule = data["schedule"]
        
        search = clean_title(title)
        imdb = imdb_map.get(search)
        
        poster = meta['poster']
        rating_val, votes, plot, imdb_link = "N/A", "", "", f"https://www.imdb.com/find/?q={urllib.parse.quote(title)}"
        
        is_really_new = False
        if imdb:
            if imdb['poster']: poster = imdb['poster']
            rating_val = imdb['rating']
            if imdb['votes']: votes = f"({imdb['votes']/1000:.1f}K)" if imdb['votes'] > 1000 else f"({imdb['votes']})"
            plot = imdb['plot']
            if imdb['id']: imdb_link = f"https://www.imdb.com/title/{imdb['id']}/"
            if imdb['year'] and int(imdb['year']) >= current_year - 1: is_really_new = True

        new_badge = '<span class="bg-green-100 text-green-700 dark:bg-green-900 dark:text-green-300 text-[10px] font-extrabold px-2 py-0.5 rounded border border-green-200 dark:border-green-800 ml-2 uppercase tracking-wider">ÚJ</span>' if is_really_new else ''
        
        rating_badge = f'<a href="{imdb_link}" target="_blank" class="{"bg-yellow-400 text-black" if rating_val!="N/A" and float(rating_val)<8 else "bg-yellow-300 border-2 border-yellow-500 text-black" if rating_val!="N/A" else "bg-gray-100 text-gray-500 dark:bg-gray-700 dark:text-gray-300"} text-[11px] font-bold px-1.5 py-0.5 rounded flex items-center shadow-sm ml-2 hover:opacity-80"><i class="fas fa-star text-[10px] mr-1"></i> {rating_val} <span class="text-[9px] font-normal ml-1 opacity-70">{votes}</span></a>'

        act_btn = ""
        if meta['trailer']:
            act_btn = f'''<button onclick="openModal('{meta['trailer']}', '{title.replace("'", "")}')" class="text-xs font-bold text-red-600 hover:text-red-800 dark:text-red-400 dark:hover:text-red-300 flex items-center mt-3 bg-red-50 dark:bg-red-900/20 border border-red-100 dark:border-red-800 w-fit px-3 py-1.5 rounded-md"><i class="fas fa-play-circle mr-1.5 text-lg"></i> Előzetes</button>'''
        elif meta['info']:
            act_btn = f'''<a href="{meta['info']}" target="_blank" class="text-xs font-bold text-blue-600 hover:text-blue-800 dark:text-blue-400 dark:hover:text-blue-300 flex items-center mt-3 bg-blue-50 dark:bg-blue-900/20 border border-blue-100 dark:border-blue-800 w-fit px-3 py-1.5 rounded-md"><i class="fas fa-info-circle mr-1.5 text-lg"></i> Adatlap</a>'''

        schedule_html = '<div class="space-y-2 mt-4 border-t border-gray-100 dark:border-gray-700 pt-3">'
        has_showings = False
        
        for date_str in all_dates:
            if date_str in schedule:
                has_showings = True
                screenings = schedule[date_str]
                dt_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
                days_hu = ["HÉT", "KED", "SZE", "CSÜ", "PÉN", "SZO", "VAS"]
                short_day = days_hu[dt_obj.weekday()]
                nice_date = f"{short_day}, {dt_obj.strftime('%b %d').upper()}"
                
                times_html = ""
                for s in screenings:
                    fmt = " ".join(s['fmt'])
                    bst, lbl = "bg-gray-100 dark:bg-gray-700 text-gray-600 dark:text-gray-300", "2D"
                    if "4DX" in fmt: bst, lbl = "bg-red-50 dark:bg-red-900/30 text-red-600 dark:text-red-400 font-bold", "4DX"
                    elif "IMAX" in fmt: bst, lbl = "bg-blue-50 dark:bg-blue-900/30 text-blue-600 dark:text-blue-400 font-bold", "IMAX"
                    elif "3D" in fmt: bst, lbl = "bg-teal-50 dark:bg-teal-900/30 text-teal-600 dark:text-teal-400", "3D"
                    
                    times_html += f'''
                    <a href="{s['link']}" target="_blank" class="inline-flex items-center group text-sm font-bold border dark:border-gray-600 rounded-lg px-3 py-2 bg-white dark:bg-gray-800 hover:bg-orange-50 dark:hover:bg-orange-900/20 hover:border-orange-200 dark:hover:border-orange-800 hover:text-orange-600 dark:hover:text-orange-400 transition-all mr-1.5 mb-1.5 shadow-sm dark:text-gray-200">
                        <span class="mr-1.5 {bst} text-[9px] px-1 rounded uppercase tracking-wider">{lbl}</span> {s['time']}
                    </a>
                    '''
                
                schedule_html += f'''
                <div class="flex flex-col sm:flex-row sm:items-start border-b border-gray-50 dark:border-gray-700 last:border-0 pb-3 last:pb-0">
                    <div class="w-24 shrink-0 text-xs font-bold text-gray-500 dark:text-gray-400 pt-2">{nice_date}</div>
                    <div class="flex flex-wrap flex-grow">{times_html}</div>
                </div>
                '''
        
        schedule_html += '</div>'
        if not has_showings: continue 

        grid_html += f"""
        <div class="bg-white dark:bg-gray-800 rounded-2xl shadow-sm border border-gray-200 dark:border-gray-700 hover:shadow-xl transition-all duration-300 overflow-hidden flex flex-col md:flex-row group will-change-transform">
            <div class="w-full md:w-56 shrink-0 relative bg-gray-100 dark:bg-gray-900 aspect-[2/3] md:self-start">
                <img src="{poster}" loading="lazy" decoding="async" fetchpriority="low" class="absolute inset-0 w-full h-full object-cover rounded-t-2xl md:rounded-l-2xl md:rounded-tr-none">
            </div>
            
            <div class="p-5 flex-grow flex flex-col">
                <div class="flex justify-between items-start">
                    <div>
                        <div class="flex items-center mb-2 flex-wrap gap-y-2">
                            <h3 class="font-bold text-gray-900 dark:text-white text-xl md:text-2xl leading-tight group-hover:text-orange-600 dark:group-hover:text-orange-400 transition-colors mr-2">{title}</h3>
                            {new_badge}{rating_badge}
                        </div>
                        <div class="flex items-center text-xs text-gray-500 dark:text-gray-400 mb-3 font-medium uppercase tracking-wide">
                            {f'<img src="{meta["rate_img"]}" class="h-4 w-auto mr-2 opacity-70">' if meta['rate_img'] else ''}
                            <span class="mr-2 truncate max-w-[200px]">{meta['genre']}</span>
                            <span>{meta['dur']}</span>
                        </div>
                        {f'<p class="text-sm text-gray-600 dark:text-gray-300 leading-relaxed line-clamp-3 md:line-clamp-none">{plot}</p>' if plot else ''}
                    </div>
                </div>
                
                <div class="mt-4 md:mt-auto">
                    {act_btn}
                    {schedule_html}
                </div>
            </div>
        </div>
        """

    full_html = f"""
    <!DOCTYPE html><html lang="hu"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Mozi Győr</title>
    <link rel="icon" type="image/webp" href="{FAVICON_FILENAME}">
    <script src="https://cdn.tailwindcss.com"></script><link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet"><script>tailwind.config = {{ darkMode: 'media' }}</script><style>.modal {{ transition: opacity 0.25s ease; }} body.modal-active {{ overflow: hidden; }} ::-webkit-scrollbar {{ width: 8px; }} ::-webkit-scrollbar-track {{ background: transparent; }} ::-webkit-scrollbar-thumb {{ background: #888; border-radius: 4px; }} .will-change-transform {{ will-change: transform; }}</style></head><body class="bg-gray-50 dark:bg-gray-900 min-h-screen font-sans text-gray-900 dark:text-gray-100">
    <div id="trailer-modal" class="modal opacity-0 pointer-events-none fixed inset-0 flex items-center justify-center z-50"><div class="modal-overlay absolute inset-0 bg-gray-900 opacity-95"></div><div class="modal-container bg-black w-full md:max-w-4xl mx-auto rounded shadow-lg z-50 overflow-y-auto"><div class="modal-content py-4 text-left px-6 relative"><div class="flex justify-between items-center pb-3"><p class="text-2xl font-bold text-white" id="modal-title">Előzetes</p><div class="cursor-pointer z-50 text-white" onclick="closeModal()"><i class="fas fa-times text-2xl"></i></div></div><div class="aspect-w-16 aspect-h-9"><iframe id="trailer-iframe" class="w-full h-[50vh] md:h-[60vh]" src="" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe></div></div></div></div>
    
    <div class="max-w-5xl mx-auto px-2 md:px-4 py-6 md:py-8">
        <div class="flex flex-col md:flex-row justify-between items-end mb-6 md:mb-8 border-b pb-4 border-gray-200 dark:border-gray-700">
            <div><h1 class="text-3xl md:text-4xl font-extrabold text-gray-900 dark:text-white mb-1">Cinema City <span class="text-orange-600 dark:text-orange-500">Győr</span></h1><p class="text-gray-500 dark:text-gray-400 text-sm">Frissítve: <span class="font-mono bg-gray-200 dark:bg-gray-800 px-2 py-0.5 rounded text-gray-700 dark:text-gray-300 font-bold">{timestamp}</span></p></div>
        </div>
        <div class="grid grid-cols-1 gap-6 md:gap-8">
            {grid_html}
        </div>
    </div>
    <script>
        const modal = document.getElementById('trailer-modal'); const iframe = document.getElementById('trailer-iframe'); const modalTitle = document.getElementById('modal-title');
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