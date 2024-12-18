import json
import unicodedata

def normalize_text(text):
    """
    Normalize the text by removing accents, converting to lowercase, and trimming trailing dots.
    """
    text = text.strip().rstrip('.')  # Remove trailing spaces and dots
    return ''.join(
        c for c in unicodedata.normalize('NFD', text)
        if unicodedata.category(c) != 'Mn'
    ).lower()

def contains_accents(text):
    """
    Check if the text contains accents.
    """
    normalized = unicodedata.normalize('NFD', text)
    return any(unicodedata.category(c) == 'Mn' for c in normalized)

def remove_duplicates_and_accentless(json_file, output_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as file:
            data = json.load(file)

        question_map = {}
        filtered_data = []

        for entry in data:
            if not contains_accents(entry['question']):
                continue

            normalized_question = normalize_text(entry['question'])
            answer = entry['answer']

            if normalized_question in question_map:
                if question_map[normalized_question] != answer:
                    continue  # Ignore conflicting duplicates
            else:
                question_map[normalized_question] = answer
                filtered_data.append(entry)

        with open(output_file, 'w', encoding='utf-8') as file:
            json.dump(filtered_data, file, ensure_ascii=False, indent=4)

        print(len(filtered_data))

        print(f"Filtered data successfully saved to {output_file}")

    except Exception as e:
        print(f"Error processing data: {e}")




# Example usage
json_file = r'C:\Users\samyb\OneDrive\SZE\OneDrive - Széchenyi István Egyetem\VSC\samyborsos.github.io\samyborsos.github.io\quizlet_data.json'  # Replace with the path to your HTML file
output_file = 'new_vir_flashcards.json'
remove_duplicates_and_accentless(json_file, output_file)


