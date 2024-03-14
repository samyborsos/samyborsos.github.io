import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import winsound


start_time = time.time()




def scrape_emerald_cfp(url, subject_name):
    response = requests.get(url)
    page_contents = response.text
    doc = BeautifulSoup(page_contents, "lxml")

    topics = []

    for tag in doc.select("a[role='article']"):
        header_div = tag.select_one('div.cfp-card__header')
        if header_div:
            # TITLE
            title_tag = tag.select_one("span.field.field--name-title.field--type-string.field--label-hidden")
            title = title_tag.text if title_tag else None

            # DESCRIPTION
            desc_tag = tag.select_one("div.cfp-card__content-body")
            desc = desc_tag.text if desc_tag else None

            # CLOSE DATE
            close_date_tag = tag.select_one("time.datetime")
            close_date = close_date_tag.text if close_date_tag else None

            # URL
            url = 'https://www.emeraldgrouppublishing.com/' + tag['href']
            clickable_url = f'<a href="{url}" target="_blank">Link</a>'

            topics.append({
                'Title': title,
                'Description': desc.replace("\n", ""),
                'Close date': close_date,
                'Url': clickable_url,
                'Kiadó': "<img src='https://www.emeraldgrouppublishing.com/themes/custom/emerald_publishing/logo.svg' width='50px' height='50px'>",
                'Filter': subject_name
            })

    return topics

def scrape_elsevier_cfp(url, subject_name):
    response = requests.get(url)
    page_contents = response.text
    doc = BeautifulSoup(page_contents, "lxml")

    topics = []

    for li_tag in doc.select("li.publication"):
        # TITLE
        title_tag = li_tag.select_one("a.anchor--js-publication-title--anchor-default")
        title = title_tag.text if title_tag else None

        # GUEST EDITORS
        editors_tag = li_tag.select_one("div.text-s.u-text-italic")
        editors = editors_tag.text if editors_tag else None

        # JOURNAL INFO
        journal_info_tag = li_tag.select_one("p.publication-text")
        journal_info = journal_info_tag.text if journal_info_tag else None

        # SUBMISSION DEADLINE
        deadline_tag = li_tag.select_one("div.text-s strong")
        deadline = deadline_tag.text if deadline_tag else None

        topics.append({
            'Title': title,
            'Guest Editors': editors,
            'Journal Info': journal_info,
            'Submission Deadline': deadline,
            'Kiadó': "<img src='https://sdfestaticassets-eu-west-1.sciencedirectassets.com/shared-assets/24/images/elsevier-non-solus-new-grey.svg' width='50px' height='50px'>",
            'Filter': subject_name
        })

    return topics



def main():
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

    # EMERALD
    for subject_name, subject_codes in filter_subjects.items():
        url = f"{base_url}{journal_filter}{subject_codes}"
        for i in range(2):
            url_with_page = f"{url}&page={i}"
            topics.extend(scrape_emerald_cfp(url_with_page,subject_name))

    # ElSEVIER (NOT WORKING)
    elsevier_base_url = "https://www.sciencedirect.com/browse/calls-for-papers"
    elsevier_topics = scrape_elsevier_cfp(elsevier_base_url, "Elsevier")

    print("Elsevier Topics:", elsevier_topics)

    topics.extend(elsevier_topics)


    if topics:
        topics_df = pd.DataFrame(topics)

        # Construct file paths
        #csv_path = os.path.join(script_dir, 'topics.csv')
        #xlsx_path = os.path.join(script_dir, 'topics.xlsx')
        html_path = os.path.join(script_dir, 'generated_table_with_python.html')

        # Save to files
        #topics_df.to_csv(csv_path, index=None)
        #topics_df.to_excel(xlsx_path, index=None, header=True)

        # Save HTML with clickable links
        html_content = f"""
                <!DOCTYPE html>
                <html lang="en" class="h-full bg-gray-100">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Kiadók</title>
                    <script src="https://cdn.tailwindcss.com"></script>
                    <link rel="icon" href="/pictures/sze_logo.png" sizes="144x144">
                </head>
                <style>
                        table {{
                            font-family: Arial, sans-serif;
                            border-collapse: collapse;
                            
                            margin: auto;
                        }}
                        th, td {{
                            border-bottom: 1px solid #dddddd;
                            text-align: left;
                            padding: 16px;
                        }}
                        
                        a {{
                            color: #007BFF;
                            text-decoration: none;
                            cursor: pointer;
                        }}
                        #subjectDropdown {{
                            margin-bottom: 50px;
                        }}
                        .min-h-screen {{
                            /* Prevent vertical centering */
                            display: flex;
                            align-items: flex-start; /* Align content to the start (top) of the container */
                        }}
                        tr:hover td {{
                          background-color: lightgrey;
                        }}            
                </style>
                <body class="h-full">
                <div class="min-h-full">
                    <nav class="bg-gray-800">
                    <div class="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
        <div class="flex h-16 items-center justify-between">
          <div class="flex items-center">
            <div class="flex-shrink-0">
              <img class="h-8 w-8" src="https://tailwindui.com/img/logos/mark.svg?color=indigo&shade=500" alt="Your Company">
            </div>
            <div class="hidden md:block">
              <div class="ml-10 flex items-baseline space-x-4">
                
              </div>
            </div>
          </div>
          <div class="hidden md:block">
            <div class="ml-4 flex items-center md:ml-6">
              <button type="button" class="relative rounded-full bg-gray-800 p-1 text-gray-400 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800">
                <span class="absolute -inset-1.5"></span>
                <span class="sr-only">View notifications</span>
                <svg class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                  <path stroke-linecap="round" stroke-linejoin="round" d="M14.857 17.082a23.848 23.848 0 005.454-1.31A8.967 8.967 0 0118 9.75v-.7V9A6 6 0 006 9v.75a8.967 8.967 0 01-2.312 6.022c1.733.64 3.56 1.085 5.455 1.31m5.714 0a24.255 24.255 0 01-5.714 0m5.714 0a3 3 0 11-5.714 0" />
                </svg>
              </button>
  
              <!-- Profile dropdown -->
              <div class="relative ml-3">
                <div>
                  <button type="button" class="relative flex max-w-xs items-center rounded-full bg-gray-800 text-sm focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" id="user-menu-button" aria-expanded="false" aria-haspopup="true">
                    
                    <span class="sr-only">Open user menu</span>
                    <img class="h-8 w-8 rounded-full" src="SzSzG-profile-picture.jpg" alt="">
                  </button>
                </div>
  
                <!--
                  Dropdown menu, show/hide based on menu state.
  
                  Entering: "transition ease-out duration-100"
                    From: "transform opacity-0 scale-95"
                    To: "transform opacity-100 scale-100"
                  Leaving: "transition ease-in duration-75"
                    From: "transform opacity-100 scale-100"
                    To: "transform opacity-0 scale-95"
                -->
                
              </div>
            </div>
          </div>
          <div class="-mr-2 flex md:hidden">
            <!-- Mobile menu button -->
            <button type="button" class="relative inline-flex items-center justify-center rounded-md bg-gray-800 p-2 text-gray-400 hover:bg-gray-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-white focus:ring-offset-2 focus:ring-offset-gray-800" aria-controls="mobile-menu" aria-expanded="false">
              <span class="absolute -inset-0.5"></span>
              <span class="sr-only">Open main menu</span>
              <!-- Menu open: "hidden", Menu closed: "block" -->
              <svg class="block h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 6.75h16.5M3.75 12h16.5m-16.5 5.25h16.5" />
              </svg>
              <!-- Menu open: "block", Menu closed: "hidden" -->
              <svg class="hidden h-6 w-6" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hidden="true">
                <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
              </svg>
            </button>
          </div>
        </div>
      </div>
                    </nav>
                
                    <header class="bg-white shadow">
                    <div class="mx-auto max-w-7xl px-4 py-6 sm:px-6 lg:px-8">
                        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Kiadók</h1>
                    </div>
                    </header>
                    
                    <main>
                    <div class="mx-auto max-w-7xl py-6 sm:px-6 lg:px-8">
                    
                            
                            <p class="text-base mb-4">   </p>
                            <div class="flex justify-between">
                              <div>
                                  <label for="searchInput" class="text-sm font-medium text-gray-500">Search for title</label><br>
                                  <input type="text" id="searchInput" onkeyup="searchFunction()" placeholder="Search title..." title="Type in a name" class="p-2 mb-4">
                              </div>
                              <div>
                                  <label for="subjectDropdown" class="text-sm font-medium text-gray-500">Select Subject:</label>
                                  <select id="subjectDropdown" onchange="filterTable()" class="block mt-1 p-2 border-gray-300 rounded-md">
                                      <option value="all">All Subjects</option>
                                       <!-- Add options for each subject_key -->
                                      <option value="Accounting finance & economics">Accounting finance & economics</option>
                                      <option value="Business, management & strategy">Business, management & strategy</option>
                                      <option value="HR, learning & organisation studies">HR, learning & organisation studies</option>
                                      <option value="Information & knowledge management">Information & knowledge management</option>
                                      <option value="Marketing">Marketing</option>
                                      <option value="Tourism & hospitality management">Tourism & hospitality management</option>
                                      <option value="Operations, logistics & quality">Operations, logistics & quality</option>
                                      <!-- Add other subjects as needed -->
                                  </select>
                              </div>
                          </div>

                        <div class="">

                            {topics_df.to_html(index=False, escape=False, border=0)}
                        
                        </div>
                    </div>
                    </main>
                </div>
                <script>
        function filterTable() {{
                  var input, filter, table, tr, td, i, txtValue;
                  input = document.getElementById("subjectDropdown");
                  filter = input.value.toUpperCase();
                  table = document.getElementsByTagName("table")[0];
                  tr = table.getElementsByTagName("tr");

                  

                  // Loop through all table rows, and show those that match the selected subject
                  for (i = 0; i < tr.length; i++) {{
                      td = tr[i].getElementsByTagName("td")[5]; // Assuming the search is based on the fifth column (subject_key)
                      if (td) {{
                          txtValue = td.textContent || td.innerText;
                          if (filter === "all" || txtValue.toUpperCase().indexOf(filter) > -1) {{
                              tr[i].style.display = "";
                          }} else {{
                              tr[i].style.display = "none";
                          }}
                      }}
                  }}
              }}

        
         function searchFunction() {{
        // Declare variables
        var input, filter, table, tr, td, i, txtValue;
        input = document.getElementById("searchInput");
        filter = input.value.toUpperCase();
        table = document.getElementsByTagName("table")[0];
        tr = table.getElementsByTagName("tr");

        // Loop through all table rows, and hide those who don't match the search query
        for (i = 0; i < tr.length; i++) {{
            td = tr[i].getElementsByTagName("td")[0]; // Assuming the search is based on the first column (title)
            if (td) {{
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {{
                    tr[i].style.display = "";
                }} else {{
                    tr[i].style.display = "none";
                }}
            }}
        }}
    }}
    </script>
                </body>
                </html>
                """

        with open(html_path, 'w', encoding='utf-8') as html_file:
            html_file.write(html_content)
        print(f"\n\t 🟢 Process finished! 🟢\n")
        print("\tRun time --> {:.2f} seconds \n".format(time.time() - start_time))
        duration = 1250  # milliseconds
        freq = 400  # Hz
        winsound.Beep(freq, duration)
    else:
        print("No topics found.")
        

if __name__ == "__main__":
    main()