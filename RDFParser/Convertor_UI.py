import os
import tkinter as tk
from tkinter import ttk, filedialog
import customtkinter
from alive_progress import alive_bar

from main import main


customtkinter.set_default_color_theme("dark-blue")
customtkinter.set_appearance_mode("System")


def get_input_folder_path():
    folder_selected = filedialog.askdirectory()
    input_directory.set(folder_selected)
    print(input_directory)


def get_output_folder_path():
    folder_selected = filedialog.askdirectory()
    output_directory.set(folder_selected)


def input_format(choice):
    print("dropdown clicked:", choice)


def output_format(choice):
    print("dropdown clicked:", choice)


def conversion():
    global input_path, output_directory, input_selected, output_selected
    global total_file  # Add this line to define total_file as a global variable

    input_path = input_directory.get()
    output_path = output_directory.get()
    in_selected_type = input_selected.get()
    if in_selected_type == "RDF":
        in_selected_type = "rdf"
    else:
        in_selected_type = "json"
    out_selected_type = output_selected.get()
    if out_selected_type == "RDF":
        out_selected_type = "rdf"
    elif out_selected_type == "JSON":
        out_selected_type = "json"
    else:
        out_selected_type = "sdf"

    print(input_path, output_path, in_selected_type, out_selected_type)

    if input_path and output_path:  # Check if both file path and directory path are not empty
        progress_bar.config(mode="determinate")  # Change mode to determinate
        progress_bar["value"] = 0  # Set initial progress value
        # Get the total number of steps in the conversion process
        total_steps = calculate_total_steps()

        with alive_bar(total_steps) as bar:

            for i in range(total_steps):
                # Perform your conversion logic here
                main(input_path, output_path, in_selected_type, out_selected_type)

                # Update progress bar
                progress_bar["value"] = (i + 1) * 100 / total_steps

                # Update GUI to reflect changes
                app.update()

                bar()  # Update the progress bar for each iteration


def calculate_total_steps():
    global total_file
    total_file = 0
    if os.path.isdir(input_path):
        for filename in os.listdir(input_path):
            if filename.endswith(".rdf") or filename.endswith(".json"):
                total_file += 1
    return total_file


# creating app
app = customtkinter.CTk()
app.geometry("1080x720")
app.title("Evolvus-Convertor")

content_frame = tk.Frame(app, borderwidth=10, relief="ridge")
content_frame.pack(padx=110, pady=110)

heading_label = tk.Label(content_frame, text="Evolvus File Converter", font=("Helvetica", 12, "bold"))
heading_label.grid(row=0, column=0, padx=10, pady=10)

input_title = customtkinter.CTkLabel(content_frame, text="Input File or Directory")
input_title.grid(row=1, column=0, padx=10, pady=10)

input_directory = tk.StringVar()
input_entry = customtkinter.CTkEntry(content_frame, width=350, textvariable=input_directory)
input_entry.grid(row=1, column=1, padx=10, pady=10)

select_button = customtkinter.CTkButton(content_frame, text="Browse", command=get_input_folder_path, width=25)
select_button.grid(row=1, column=2, padx=10, pady=0)

output_title = customtkinter.CTkLabel(content_frame, text="Output File or Directory")
output_title.grid(row=2, column=0, padx=10, pady=10)

output_directory = tk.StringVar()
output_entry = customtkinter.CTkEntry(content_frame, width=350, textvariable=output_directory)
output_entry.grid(row=2, column=1, padx=10, pady=10)

output_button = customtkinter.CTkButton(content_frame, text="Browse", command=get_output_folder_path, width=25)
output_button.grid(row=2, column=2, padx=10, pady=10)

label3 = customtkinter.CTkLabel(content_frame, text="Input Format", justify="right")
label3.grid(row=3, column=0)

select_input_format = ["RDF", "JSON"]
input_selected = customtkinter.StringVar(value=select_input_format[0])
combobox = customtkinter.CTkOptionMenu(content_frame, values=select_input_format, command=input_format,
                                       variable=input_selected)
combobox.grid(row=3, column=1)

output_format_label = customtkinter.CTkLabel(content_frame, text='Output Format', width=5)
output_format_label.grid(row=4, column=0, padx=10, pady=10)

select_output_format = ["RDF", "JSON", "SDF"]
output_selected = customtkinter.StringVar(value=select_output_format[0])
combobox = customtkinter.CTkOptionMenu(content_frame, values=select_output_format, command=output_format,
                                       variable=output_selected)
combobox.grid(row=4, column=1)

convert_button = customtkinter.CTkButton(content_frame, text="Convert", command=conversion)
convert_button.grid(row=5, column=0, columnspan=5, padx=10, pady=10)

progress_bar = ttk.Progressbar(content_frame, orient="horizontal", mode="determinate", length=500)
progress_bar.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

app.mainloop()
