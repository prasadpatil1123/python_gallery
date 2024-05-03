import tkinter as tk  # Import the Tkinter module for creating GUI
from tkinter import filedialog  # Import the filedialog submodule for opening file dialogs
from csv_converter import csv_to_json  # Import the csv_to_json and csv_to_excel functions from csv_converter.py
from json_converter import json_to_csv  # Import the json_to_csv function from json_converter.py
from excel_converter import csv_to_excel
# Function to convert CSV to JSON
def convert_csv_to_json():
    # Open a file dialog to select a CSV file and get its path
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    # Open a file dialog to select a location to save the JSON file and get its path
    json_file_path = filedialog.asksaveasfilename(defaultextension=".json")
    # Call the csv_to_json function with the selected file paths
    csv_to_json(csv_file_path, json_file_path)
    # Update the status label to indicate that CSV to JSON conversion is completed
    status_label.config(text="CSV to JSON conversion completed.")

# Function to convert JSON to CSV
def convert_json_to_csv():
    # Open a file dialog to select a JSON file and get its path
    json_file_path = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
    # Open a file dialog to select a location to save the CSV file and get its path
    csv_file_path = filedialog.asksaveasfilename(defaultextension=".csv")
    # Call the json_to_csv function with the selected file paths
    json_to_csv(json_file_path, csv_file_path)
    # Update the status label to indicate that JSON to CSV conversion is completed
    status_label.config(text="JSON to CSV conversion completed.")

# Function to convert CSV to Excel
def convert_csv_to_excel():
    # Open a file dialog to select a CSV file and get its path
    csv_file_path = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
    # Open a file dialog to select a location to save the Excel file and get its path
    excel_file_path = filedialog.asksaveasfilename(defaultextension=".xlsx")
    # Call the csv_to_excel function with the selected file paths
    csv_to_excel(csv_file_path, excel_file_path)
    # Update the status label to indicate that CSV to Excel conversion is completed
    status_label.config(text="CSV to Excel conversion completed.")

# Create GUI window
root = tk.Tk()
root.title("CSV to JSON, JSON to CSV, and CSV to Excel Converter")  # Set window title

# Buttons for conversion
csv_to_json_button = tk.Button(root, text="Convert CSV to JSON", command=convert_csv_to_json)
csv_to_json_button.pack()  # Pack the button into the GUI window

json_to_csv_button = tk.Button(root, text="Convert JSON to CSV", command=convert_json_to_csv)
json_to_csv_button.pack()  # Pack the button into the GUI window

csv_to_excel_button = tk.Button(root, text="Convert CSV to Excel", command=convert_csv_to_excel)
csv_to_excel_button.pack()  # Pack the button into the GUI window

# Status label to display conversion status
status_label = tk.Label(root, text="")
status_label.pack()  # Pack the label into the GUI window

root.mainloop()  # Start the Tkinter event loop to run the GUI
