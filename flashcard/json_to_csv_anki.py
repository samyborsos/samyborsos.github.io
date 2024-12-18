import csv
import json
import random

# Input JSON file name
input_file = "./flashcard/new_vir_flashcards.json"

# Output CSV file names
output_file_original = "./flashcard/anki_cards5_original.csv"
output_file_shuffled = "./flashcard/anki_cards5_shuffled.csv"

# Read JSON data from the file
with open(input_file, mode="r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Function to write a deck to a CSV file
def write_to_csv(data, output_file):
    with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file)

        # Write header
        writer.writerow(["question", "title", "QType", "Q_1", "Q_2", "Q_3", "Q_4", "Q_5", "Answers"])

        # Write each question-answer pair
        for item in data:
            question = item["question"]
            title = "VIR (igaz/hamis)"
            qtype = "2"  # Default to Single Choice (2)
            q_1 = "igaz"
            q_2 = "hamis"
            q_3 = ""
            q_4 = ""
            q_5 = ""

            # Determine the correct answer format as "0 1" or "1 0"
            if item["answer"] == "igaz":
                answers = "1 0"
            else:
                answers = "0 1"

            writer.writerow([question, title, qtype, q_1, q_2, q_3, q_4, q_5, answers])

# Write the original deck
write_to_csv(data, output_file_original)

# Shuffle the data and write to a new shuffled deck
shuffled_data = data.copy()
random.shuffle(shuffled_data)
write_to_csv(shuffled_data, output_file_shuffled)

print(f"Original deck written to {output_file_original}")
print(f"Shuffled deck written to {output_file_shuffled}")
