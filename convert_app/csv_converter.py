# csv_converter.py

import csv  # Import the csv module for working with CSV files
import json  # Import the json module for working with JSON files

# Convert CSV to JSON
def csv_to_json(csv_file, json_file):
    data = []  # Create an empty list to store the CSV data
    
    # Open the CSV file in read mode
    with open(csv_file, 'r') as file:
        # Create a CSV reader object that reads rows from the file and interprets them as dictionaries
        csv_reader = csv.DictReader(file)
        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Append each row (dictionary) to the data list
            data.append(row)
    
    # Open the JSON file in write mode
    with open(json_file, 'w') as file:
        # Write the data list to the JSON file, with indentation for readability
        json.dump(data, file, indent=4)
