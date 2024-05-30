import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
start_time = time.time()

print("\nWebscraping started...\n")

english_to_hungarian_month = {
    "January": "január", "February": "február", "March": "március", "April": "április",
    "May": "május", "June": "június", "July": "július", "August": "augusztus",
    "September": "szeptember", "October": "október", "November": "november", "December": "december"
}

def get_page_contents(url):
    response = requests.get(url)
    return response.text

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

# Function to scrape Emerald CFP
def scrape_emerald_cfp(url, subject_name):
    # Your existing code for scraping Emerald CFP goes here
    page_contents = get_page_contents(url)
    doc = BeautifulSoup(page_contents, "lxml")
    topics = []
    for tag in doc.select("a[role='article']"):
        header_div = tag.select_one('div.cfp-card__header')
        if header_div:
            title = tag.select_one("span.field.field--name-title.field--type-string.field--label-hidden").text.strip()
            desc = tag.select_one("div.cfp-card__content-body").text.strip()
            close_date = datetime.strptime(tag.select_one("time.datetime").text.strip(), "%d %b %Y").strftime("%Y. ") + english_to_hungarian_month[datetime.strptime(tag.select_one("time.datetime").text.strip(), "%d %b %Y").strftime("%B")] + " " + datetime.strptime(tag.select_one("time.datetime").text.strip(), "%d %b %Y").strftime("%d.")
            url = 'https://www.emeraldgrouppublishing.com/' + tag['href']
            clickable_url = f'<a class="text-blue-500 hover:underline" href="{url}" target="_blank">Link</a>'
            publisher = "<img src='https://www.emeraldgrouppublishing.com/themes/custom/emerald_publishing/logo.svg' width='50px' height='50px'> <br> Emerald"
            topics.append({'Title': title, 'Description': desc, 'Close date': close_date, 'Url': clickable_url, 'Publisher': publisher, 'Subject': subject_name})
    return topics

# Function to scrape Elsevier CFP
def scrape_elsevier_cfp(url, subject_name):
    topics = []
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    publications = soup.find_all('li', {'class': 'publication u-padding-xs-ver js-publication u-margin-s-bottom'})
    for publication in publications:
        title = publication.find('a', {'class': 'anchor js-publication-title anchor-default'}).text.strip()
        description = publication.find('p', {'class': 'publication-text'}).text.strip()
        deadline_tag = publication.find('strong')
        deadline = deadline_tag.text.strip() if deadline_tag else None
        if deadline:
            deadline = datetime.strptime(deadline, "%d %B %Y").strftime("%Y. ") + english_to_hungarian_month[datetime.strptime(deadline, "%d %B %Y").strftime("%B")] + " " + datetime.strptime(deadline, "%d %B %Y").strftime("%d.")
        url = 'https://www.sciencedirect.com' + publication.find('a', {'class': 'anchor js-publication-title anchor-default'})['href']
        clickable_url = f'<a class="text-blue-500 hover:underline" href="{url}" target="_blank">Link</a>'
        publisher = "<img src='https://sdfestaticassets-eu-west-1.sciencedirectassets.com/shared-assets/24/images/elsevier-non-solus-new-grey.svg' width='50px' height='50px'> <br> Elsevier"
        topics.append({'Title': title, 'Description': description, 'Close date': deadline, 'Url': clickable_url, 'Publisher': publisher, 'Subject': subject_name})
    driver.quit()
    return topics



def scrapeTaylorAndFrancis(website_url):
    topics = []
    # Start a new instance of Chrome WebDriver
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)

    # Open the website
    driver.get(website_url)

    try:
        # Accept the cookie consent if it exists
        try:
            cookie_consent_button = WebDriverWait(driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-accept-btn-handler"]'))
            )
            cookie_consent_button.click()
        except:
            pass

            # Wait for the subject dropdown to be clickable
        subject_dropdown = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jtf-cfptool-checkbox-behavioral_sciences"]'))
        )

        # Select the subject "Behavioral Sciences"
        subject_dropdown.click()

        # Wait for the second dropdown button to be clickable
        second_dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jtf-cfptool-filters-dropdown-dg"]/button'))
        )

        # Click the second dropdown button
        second_dropdown_button.click()

        # Wait for the checkbox "Economics, Finance, Business & Industry" to be clickable
        economics_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jtf-cfptool-checkbox-economics_finance_business_industry"]'))
        )

        # Click the checkbox "Economics, Finance, Business & Industry"
        economics_checkbox.click()

        # Wait for the third dropdown button to be clickable
        third_dropdown_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jtf-cfptool-filters-dropdown-nz"]/button'))
        )

        # Click the third dropdown button
        third_dropdown_button.click()

        # Wait for the checkbox "Tourism, Hospitality and Events" to be clickable
        tourism_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jtf-cfptool-checkbox-tourism_hospitality_and_events"]'))
        )

        # Click the checkbox "Tourism, Hospitality and Events"
        tourism_checkbox.click()

        # Wait for the checkbox "Urban Studies" to be clickable
        urban_studies_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="jtf-cfptool-checkbox-urban_studies"]'))
        )

        # Click the checkbox "Urban Studies"
        urban_studies_checkbox.click()

        # Finally, wait for the search button to be clickable and click it
        search_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[3]/div/div/div/div/section/div[2]/div[1]/section/div/div/div/div[6]/button[1]'))
        )
        search_button.click()

        # Wait for the papers to load (you might need to adjust the wait time)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/main/div[3]/div/div/div/div/section/div[2]/div[2]/section/div[1]'))
        )
        
        # Get the HTML content of the section with the papers
        papers_section = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[3]/div/div/div/div/section/div[2]/div[2]/section')
        papers_html = papers_section.get_attribute('innerHTML')
        
        # Parse HTML content with BeautifulSoup
        soup = BeautifulSoup(papers_html, 'html.parser')
        
        # Extract information (title, description, deadline, URL) from each paper
        
        for paper in soup.find_all('div', class_='jtf__cfptool_post'):
            title = paper.select_one("h3.jtf__cfptool_post--title a").text.strip()
            description = paper.select_one("div.jtf__cfptool_post--content p").text.strip()
            deadline = paper.select_one("p:-soup-contains('Manuscript deadline')").text.split(':')[-1].strip()
            url = paper.select_one("a.jtf__cfptool_post--button")['href']
            clickable_url = f'<a class="text-blue-500 hover:underline" href="{url}" target="_blank">Link</a>'
            publisher = "<img style='filter: invert(100%) grayscale(100%) brightness(0%) sepia(100%);' src='https://authorservices.taylorandfrancis.com/wp-content/themes/JTF3/img/tfgroup-logo-rev.svg' width='120px' height='120px'> <br> Taylor & Francis"
            
            # Find the subject from the HTML of the paper
            subject_element = paper.find('div', class_='jtf__cfptool_post--categories')
            subjects = [subject.text.strip() for subject in subject_element.find_all('div')]
        
            desired_subjects = ['Behavioral Sciences', 'Economics, Finance, Business & Industry', 'Tourism, Hospitality and Events', 'Urban Studies']
            selected_subject = next((subject for subject in subjects if subject in desired_subjects), None)
            if selected_subject:
                topics.append({'Title': title, 'Description': description, 'Close date': deadline, 'Url': clickable_url, 'Publisher': publisher, 'Subject': selected_subject})
                
                
    finally:
        # Close the browser
        driver.quit()
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
        "HR, learning & organisation studies": "&field_journal_category_target_id%5B40172%5D=40172",
        "Information & knowledge management": "&field_journal_category_target_id%5B40174%5D=40174",
        "Marketing": "&field_journal_category_target_id%5B40180%5D=40180",
        "Tourism & hospitality management": "&field_journal_category_target_id%5B40187%5D=40187",
        "Operations, logistics & quality": "&field_journal_category_target_id%5B40182%5D=40182"
    }

    topics = []

    # EMERALD ✅
    for subject_name, subject_codes in filter_subjects.items():
        url = f"{base_url}{journal_filter}{subject_codes}"
        for i in range(10):
            url_with_page = f"{url}&page={i}"
            topics.extend(scrape_emerald_cfp(url_with_page,subject_name))
    print("Emerald scraped successfully")


    # ElSEVIER ✅
    elsevier_base_url = "https://www.sciencedirect.com/browse/calls-for-papers?subject=business-management-and-accounting"
    elsevier_topics_Business = scrape_elsevier_cfp(elsevier_base_url, "Business, Management and Accounting")
    topics.extend(elsevier_topics_Business)

    elsevier_base_url = "https://www.sciencedirect.com/browse/calls-for-papers?subject=finance"
    elsevier_topics_Economics = scrape_elsevier_cfp(elsevier_base_url, "Economics, Econometrics and Finance - (Finance)")
    topics.extend(elsevier_topics_Economics)
    print("Elsevier scraped successfully")


    # Taylor & Francis ✅   
    website_url = "https://authorservices.taylorandfrancis.com/call-for-papers/"
    topics.extend(scrapeTaylorAndFrancis(website_url))
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
