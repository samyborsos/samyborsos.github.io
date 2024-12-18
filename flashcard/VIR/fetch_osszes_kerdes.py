import json
from bs4 import BeautifulSoup

def read_html_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
        return html_content
    except Exception as e:
        print(f"Error reading the HTML file: {e}")
        return None

def extract_questions_answers(html_content):
    try:
        soup = BeautifulSoup(html_content, 'html.parser')
        questions = soup.find_all('div', class_='s1slt1zj')
        results = []

        for question in questions:
            question_text = question.find('span', class_='s1q0b356')
            if question_text:
                question_text = question_text.text.strip()
            else:
                continue

            answer_text = question.find_next('span', class_='hcszxtp')
            if answer_text:
                answer_text = answer_text.text.strip()

                # Normalize answers
                if answer_text == "I":
                    answer_text = "igaz"
                elif answer_text == "H":
                    answer_text = "hamis"
                elif answer_text.upper() == "IGAZ":
                    answer_text = "igaz"
                elif answer_text.upper() == "HAMIS":
                    answer_text = "hamis"
            else:
                continue

            results.append({"question": question_text, "answer": answer_text})

        return results
    except Exception as e:
        print(f"Error extracting data: {e}")
        return []

def save_to_json(data, output_file):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Data successfully saved to {output_file}")
    except Exception as e:
        print(f"Error saving JSON file: {e}")



# Example usage
file_path = r'C:\Users\samyb\OneDrive\SZE\OneDrive - Széchenyi István Egyetem\VSC\samyborsos.github.io\samyborsos.github.io\flashcard\VIR\osszes_vir_kerdes.html'  # Replace with the path to your HTML file
output_file = 'quizlet_data.json'
html_content = read_html_file(file_path)

if html_content:
    extracted_data = extract_questions_answers(html_content)
    if extracted_data:
        save_to_json(extracted_data, output_file)

