import csv
import os

input_file = "input.csv"
output_file = "output.csv"

def convert_csv():
    if not os.path.exists(input_file):
        print("Input CSV file not found!")
        return

    cleaned_data = []

    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        for row in reader:
          
            new_row = [value if value != "" else "N/A" for value in row]
            cleaned_data.append(new_row)

    with open(output_file, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_data)

    print("Conversion successful!")
    print("Open", output_file, "in Excel.")

convert_csv()