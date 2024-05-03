# json_converter.py

import csv  # Import the csv module for working with CSV files
import json  # Import the json module for working with JSON files

# Convert JSON to CSV
def json_to_csv(json_file, csv_file):
    try:
        # Open the JSON file in read mode
        with open(json_file, 'r') as file:
            # Load JSON data from the file into a Python data structure
            data = json.load(file)
        
        # Check if the JSON data is empty
        if not data:
            print("JSON file is empty.")  # Print a message if the JSON file is empty
            return  # Exit the function
        
        # Check if the JSON data is a single object (dictionary)
        if isinstance(data, dict):
            data = [data]  # Convert the single object to a list containing one object
        
        # Open the CSV file in write mode, with newline='' to prevent extra newline characters
        with open(csv_file, 'w', newline='') as file:
            # Create a CSV writer object with field names from the keys of the first object in the data list
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            # Write the header row to the CSV file using the field names
            writer.writeheader()
            # Write the remaining rows to the CSV file from the data list
            writer.writerows(data)
        
        print("JSON to CSV conversion completed.")  # Print a message indicating successful conversion
    except FileNotFoundError:
        print("JSON file not found.")  # Print a message if the JSON file is not found
    except json.decoder.JSONDecodeError:
        print("Invalid JSON data in the file.")  # Print a message if the JSON data is invalid
