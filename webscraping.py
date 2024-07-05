import os
from pprint import pprint
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
import lxml
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry # type: ignore
import concurrent.futures


start_time = time.time()
# Function to read HTML content from file
def read_html_template():
    # Open the HTML template file and read its contents
    with open('html_template.html', 'r', encoding='utf-8') as html_file:
        html_content = html_file.read()
    return html_content
# Function to generate table HTML from Pandas DataFrame
def generate_table_html(topics_df):
    # Convert DataFrame to HTML table
    table_html = topics_df.to_html(index=False, escape=False, border=0)
    return table_html

# Function to insert table HTML into the HTML content
def insert_table_into_html(html_content, table_html):
    # Replace the placeholder with the table HTML
    modified_html_content = html_content.replace('{{TABLE_PLACEHOLDER}}', table_html).replace('<table class="dataframe">', '<table class="dataframe mt-5" id="myTable">')
    return modified_html_content



urls = [
    {"subject": "Physical Sciences and Engineering", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=physical-sciences-and-engineering"},
    {"subject": "Chemical Engineering", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=chemical-engineering"},
    {"subject": "Chemistry", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=chemistry"},
    {"subject": "Computer Science", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=computer-science"},
    {"subject": "Earth and Planetary Sciences", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=earth-and-planetary-sciences"},
    {"subject": "Energy", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=energy"},
    {"subject": "Engineering", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=engineering"},
    {"subject": "Materials Science", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=materials-science"},
    {"subject": "Mathematics", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=mathematics"},
    {"subject": "Physics and Astronomy", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=physics-and-astronomy"},
    {"subject": "Life Sciences", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=life-sciences"},
    {"subject": "Agricultural and Biological Sciences", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=agricultural-and-biological-sciences"},
    {"subject": "Biochemistry, Genetics and Molecular Biology", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=biochemistry-genetics-and-molecular-biology"},
    {"subject": "Environmental Science", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=environmental-science"},
    {"subject": "Immunology and Microbiology", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=immunology-and-microbiology"},
    {"subject": "Neuroscience", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=neuroscience"},
    {"subject": "Health Sciences", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=health-sciences"},
    {"subject": "Medicine and Dentistry", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=medicine-and-dentistry"},
    {"subject": "Nursing and Health Professions", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=nursing-and-health-professions"},
    {"subject": "Pharmacology, Toxicology and Pharmaceutical Science", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=pharmacology-toxicology-and-pharmaceutical-science"},
    {"subject": "Veterinary Science and Veterinary Medicine", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=veterinary-science-and-veterinary-medicine"},
    {"subject": "Social Sciences and Humanities", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=social-sciences-and-humanities"},
    {"subject": "Arts and Humanities", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=arts-and-humanities"},
    {"subject": "Business, Management and Accounting", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=business-management-and-accounting"},
    {"subject": "Decision Sciences", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=decision-sciences"},
    {"subject": "Economics, Econometrics and Finance", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=economics-econometrics-and-finance"},
    {"subject": "Psychology", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=psychology"},
    {"subject": "Social Sciences", "url": "https://www.sciencedirect.com/browse/calls-for-papers?subject=social-sciences"}
]




def get_page_contents(url):
    session = requests.Session()
    retry = Retry(total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    response = session.get(url, timeout=10)
    response.raise_for_status()  # Raises a HTTPError for bad responses (4xx and 5xx)
    return response.text



# Function to scrape Emerald CFP
def scrape_emerald_cfp(url, subject_name):
    page_contents = get_page_contents(url)
    doc = BeautifulSoup(page_contents, "lxml")
    topics = []
    for tag in doc.select("a[role='article']"):
        header_div = tag.select_one('div.cfp-card__header')
        if header_div:
            title = tag.select_one("span.field.field--name-title.field--type-string.field--label-hidden").text.strip()
            desc = tag.select_one("div.cfp-card__content-body").text.strip()
            close_date = datetime.strptime(tag.select_one("time.datetime").text.strip(), "%d %b %Y").strftime("%Y. %m. %d.") # Modified date format
            url = 'https://www.emeraldgrouppublishing.com/' + tag['href']
            publisher_image_url = "https://www.emeraldgrouppublishing.com/themes/custom/emerald_publishing/logo.svg"
            publisher_name = "Emerald"
            journal_name = tag.select_one("div.cfp-card__content-journal").text.strip()

            topics.append({
                    'Title': title, 
                    'Description': desc, 
                    'Close date': close_date, 
                    'Url': url, 
                    'Publisher': publisher_image_url, 
                    'Publisher Name':publisher_name, 
                    'Subject': subject_name, 
                    'Journal Name':journal_name
                    })
    return topics



# Function to scrape Elsevier CFP
def scrape_elsevier_cfp(url, subject_name):


    topics = []
    options = Options()

    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument("start-maximized"); 
    options.add_argument("disable-infobars"); 
    options.add_argument("--disable-extensions"); 
    options.add_argument("--disable-gpu"); 
    options.add_argument("--disable-dev-shm-usage"); 
    
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    publications = soup.find_all('li', {'class': 'publication u-padding-xs-ver js-publication u-margin-s-bottom'})
    for publication in publications:
        title = publication.find('a', {'class': 'anchor js-publication-title anchor-default'}).text.strip()
        desc = 'No description'
        deadline = publication.find('strong').text.strip() if publication.find('strong') else None
        if deadline:
            deadline = datetime.strptime(deadline, "%d %B %Y").strftime("%Y. %m. %d.")  # Modified date format
        url = 'https://www.sciencedirect.com' + publication.find('a', {'class': 'anchor js-publication-title anchor-default'})['href']
        publisher_image_url = "https://sdfestaticassets-eu-west-1.sciencedirectassets.com/shared-assets/24/images/elsevier-non-solus-new-grey.svg"
        publisher_name = "Elsevier"
        journal_name = publication.find('p', {'class': 'publication-text'}).text.split('•')[0].strip()

        topics.append({
            'Title': title,
            'Description': desc,
            'Close date': deadline,
            'Url': url,
            'Publisher': publisher_image_url,
            'Publisher Name': publisher_name,
            'Subject': subject_name,
            'Journal Name': journal_name
        })
        
    driver.quit()
    return topics

def scrape_all_elsevier(urls):
    all_topics = []

    for url in urls:
        all_topics.extend(scrape_elsevier_cfp(url['url'],url['subject']))

        os.system('taskkill /IM chrome.exe /F')


    return all_topics



def scrape_taylor_and_francis(url):
    topics = []
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    
    options.add_argument("start-maximized"); 
    options.add_argument("disable-infobars"); 
    options.add_argument("--disable-extensions"); 
    options.add_argument("--disable-gpu"); 
    options.add_argument("--disable-dev-shm-usage"); 
    
    driver = webdriver.Chrome(options=options)
            
    driver.get(url)
    
    try:
        # Wait longer for the cookie consent button
        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
        ).click()
    except Exception as e:
        print(f"Error clicking cookie consent: {e}")
    
    try:
        # Click on A-C dropdown and select all checkboxes
        checkboxes_hm = driver.find_elements(By.CSS_SELECTOR, '#jtf-cfptool-filters-checkboxes-ac input[type="checkbox"]')
        for checkbox in checkboxes_hm:
            checkbox.click()
            time.sleep(0.1)  # Add a small delay between clicks

        # Click on D-G dropdown and select all checkboxes
        print("Clicking D-G dropdown...")
        driver.find_element(By.ID, "jtf-cfptool-filters-dropdown-dg").click()
        time.sleep(1)  # Add a short delay to ensure checkboxes are loaded
        
        checkboxes_dg = driver.find_elements(By.CSS_SELECTOR, '#jtf-cfptool-filters-checkboxes-dg input[type="checkbox"]')
        for checkbox in checkboxes_dg:
            checkbox.click()
            time.sleep(0.1)  # Add a small delay between clicks
        
        # Click on H-M dropdown and select all checkboxes
        print("Clicking H-M dropdown...")
        driver.find_element(By.ID, "jtf-cfptool-filters-dropdown-hm").click()
        time.sleep(1)  # Add a short delay to ensure checkboxes are loaded
        
        checkboxes_hm = driver.find_elements(By.CSS_SELECTOR, '#jtf-cfptool-filters-checkboxes-hm input[type="checkbox"]')
        for checkbox in checkboxes_hm:
            checkbox.click()
            time.sleep(0.1)  # Add a small delay between clicks
        
        # Click on N-Z dropdown and select all checkboxes
        print("Clicking N-Z dropdown...")
        driver.find_element(By.ID, "jtf-cfptool-filters-dropdown-nz").click()
        time.sleep(1)  # Add a short delay to ensure checkboxes are loaded
        
        checkboxes_nz = driver.find_elements(By.CSS_SELECTOR, '#jtf-cfptool-filters-checkboxes-nz input[type="checkbox"]')
        for checkbox in checkboxes_nz:
            checkbox.click()
            time.sleep(0.1)  # Add a small delay between clicks
        
        # Click on the submit button
        print("Clicking the submit button...")
        driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div/div/div/section/div[2]/div[1]/section/div/div/div/div[6]/button[1]').click()
        
        # Wait for the papers section to load
        print("Waiting for the papers section to load...")
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[3]/div/div/div/div/section/div[2]/div[2]/section/div[1]'))
        )
        time.sleep(15)  # Adjust sleep time as needed
        
        # Get the papers section HTML and parse it with BeautifulSoup
        papers_section = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div/div/div/section/div[2]/div[2]/section')
        soup = BeautifulSoup(papers_section.get_attribute('innerHTML'), 'html.parser')
        
        # Extract data from each paper element
        for paper in soup.find_all('div', class_='jtf__cfptool_post'):
            try:
                title = paper.select_one("div.jtf__cfptool_post--content p strong").text.strip()
                description = paper.select_one("div.jtf__cfptool_post--content p").text.strip()
                deadline = paper.select_one("p:-soup-contains('Manuscript deadline')").text.split(':')[-1].strip()
                if deadline:
                    deadline = datetime.strptime(deadline, "%d %B %Y").strftime("%Y. %m. %d.")  # Corrected date format
                url = paper.select_one("a.jtf__cfptool_post--button")['href']
                publisher_image_url = "https://authorservices.taylorandfrancis.com/wp-content/themes/JTF-child/img/logo_tandf_as_icon.svg"
                publisher_name = "Taylor & Francis"
                
                # Extract subjects based on simplified mapping
                subject_mapping = {
                    "Accounting & Finance": "Economics & Business",
                    "Agriculture & Food Security": "Environmental Studies & Forestry",
                    "Aquaculture & Fisheries": "Environmental Studies & Forestry",
                    "Behavioral Sciences": "Behavioral Sciences",
                    "Built Environment": "Urban Studies",
                    "Business & Management": "Economics & Business",
                    "Chemical Engineering": "Engineering",
                    "Chemistry": "Chemistry",
                    "Civil Engineering": "Engineering",
                    "Communication & Media Studies": "Social Sciences",
                    "Computer Science": "Computer Science",
                    "Development Studies": "Social Sciences",
                    "Earth Sciences": "Environmental Studies & Forestry",
                    "Economics, Finance, Business & Industry": "Economics & Business",
                    "Education": "Education",
                    "Electrical & Electronic Engineering": "Engineering",
                    "Energy & Clean Technology": "Energy",
                    "Engineering": "Engineering",
                    "Environmental Studies & Forestry": "Environmental Studies & Forestry",
                    "Geography": "Geography",
                    "Health & Social Care": "Health Sciences",
                    "Hospitality, Leisure, Sport & Tourism": "Tourism & Hospitality",
                    "Information & Knowledge Management": "Library & Information Sciences",
                    "Language & Literature": "Language & Linguistics",
                    "Law": "Law",
                    "Materials Science": "Materials Science",
                    "Mathematics & Statistics": "Mathematics",
                    "Mechanical Engineering": "Engineering",
                    "Neuroscience": "Neuroscience",
                    "Nursing & Allied Health": "Health Sciences",
                    "Pharmaceutical Science": "Pharmaceutical Sciences",
                    "Philosophy": "Philosophy",
                    "Physical Sciences": "Physical Sciences",
                    "Politics & International Relations": "Political Science & International Relations",
                    "Psychology": "Psychology",
                    "Public & Nonprofit Management": "Public Administration",
                    "Social Sciences": "Social Sciences",
                    "Sociology & Social Policy": "Sociology",
                    "Sport & Leisure Management": "Sport Sciences",
                    "Strategy & Strategic Management": "Business & Management",
                    "Transport": "Transport",
                    "Tourism, Hospitality and Events": "Tourism & Hospitality",
                    "Urban Studies": "Urban Studies"
                }

                
                subject_element = paper.select_one("div.jtf__cfptool_post--categories").text.strip()
                subject = next((subject_mapping[category] for category in subject_mapping if category in subject_element), None)
                
                journal_name = paper.select_one("h3.jtf__cfptool_post--title a").text.strip()
                
                topics.append({
                    'Title': title, 
                    'Description': description, 
                    'Close date': deadline, 
                    'Url': url, 
                    'Publisher': publisher_image_url, 
                    'Publisher Name': publisher_name, 
                    'Subject': subject, 
                    'Journal Name': journal_name
                })
            except Exception as e:
                print(f"Error parsing Taylor & Francis CFP: {e}")
    finally:
        driver.quit()
        os.system('taskkill /IM chrome.exe /F')


    return topics




# Main function
def main():
    

    # Your existing code continues below...
    script_dir = os.path.dirname(os.path.abspath(__file__))
    base_url = "https://www.emeraldgrouppublishing.com/publish-with-us/calls-for-papers"
    journal_filter = "?field_journal_type_target_id=43877"

    filter_subjects = {
        "Accounting finance & economics": "&field_journal_category_target_id%5B40162%5D=40162",
        "Business, management & strategy": "&field_journal_category_target_id%5B40164%5D=40164",
        "Education": "&field_journal_category_target_id%5B40168%5D=40168",
        "Engineering": "&field_journal_category_target_id%5B40185%5D=40185",
        "Health & social care": "&field_journal_category_target_id%5B40171%5D=40171",
        "HR, learning & organisation studies": "&field_journal_category_target_id%5B40172%5D=40172",
        "Information & knowledge management": "&field_journal_category_target_id%5B40174%5D=40174",
        "Library & information sciences": "&field_journal_category_target_id%5B40177%5D=40177",
        "Marketing": "&field_journal_category_target_id%5B40180%5D=40180",
        "Operations, logistics & quality": "&field_journal_category_target_id%5B40182%5D=40182",
        "Property management & built environment": "&field_journal_category_target_id%5B40175%5D=40175",
        "Public policy & environmental management": "&field_journal_category_target_id%5B40169%5D=40169",
        "Tourism & hospitality management": "&field_journal_category_target_id%5B40187%5D=40187",
    }

    topics = []

    # EMERALD ✅ 

    for subject_name, subject_codes in filter_subjects.items():
        page_number = 0  # Start with page 0
        last_page_number = 0
        
        while True:
            url = f"{base_url}{journal_filter}{subject_codes}&page={page_number}"
            
            # Fetch the webpage
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find the last page number
            pager_items = soup.find('ul', class_='pager__items')
            if pager_items:
                pager_links = pager_items.find_all('a', href=True)
                for link in pager_links:
                    try:
                        page = int(link['href'].split('=')[-1])
                        if page > last_page_number:
                            last_page_number = page
                    except ValueError:
                        continue
            
            if last_page_number is None:
                last_page_number = 0  # Set to 0 if no pager items found
            
            # Print progress information
            print(f"Subject: {subject_name}, Page: {page_number+1}/{last_page_number+1}")
            
            # Scrape data from the current page
            scraped_data = scrape_emerald_cfp(url, subject_name)
            
            if not scraped_data:
                break  # Exit the loop if no data is returned
            
            topics.extend(scraped_data)
            
            page_number += 1  # Move to the next page
            
            if page_number and page_number > last_page_number:
                break  # Exit the loop if we've reached the last page

    print("Emerald scraped successfully")

    
    # ElSEVIER ✅ 
    topics.extend(scrape_all_elsevier(urls))
    print("Elsevier scraped successfully")


    # Taylor & Francis ✅ 
    website_url = "https://authorservices.taylorandfrancis.com/call-for-papers/"
    topics.extend(scrape_taylor_and_francis(website_url))
    print("Taylor & Francis scraped successfully") 




    if topics:
        topics_df = pd.DataFrame(topics)

        # Read HTML template
        html_content = read_html_template()

        # Generate table HTML
        table_html = generate_table_html(topics_df)

        # Insert table HTML into HTML content
        modified_html_content = insert_table_into_html(html_content, table_html)


        # Construct file paths
        html_path = os.path.join(script_dir, 'publishers.html')

        # Save HTML
        with open(html_path, 'w', encoding='utf-8') as html_file:
            html_file.write(modified_html_content)

        print(f"\n\t 🟢 Process finished!🟢\n")
        print("\tRun time --> {:.2f} seconds \n".format(time.time() - start_time))
    else:
        print("No topics found.")

    return topics

if __name__ == "__main__":
    main()
