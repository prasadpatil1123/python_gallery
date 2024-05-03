import json  # Importing the json module


class JsonParser:

    def convert_json_to_rdf(self, input_file, output_file):
        with open(input_file, 'r') as input_json:  # Opening the input JSON file in read mode
            data = json.load(input_json)  # Loading JSON data from the input file

        with open(output_file, 'w') as output_rdf:  # Opening the output RDF file in write mode
            output_rdf.write("$RDFILE\n")  # Writing RDF file header
            output_rdf.write("$DATM\n")  # Writing DATM tag
            index = 1  # Initialize index
            for record in data:  # Iterating through each record in the JSON data
                output_rdf.write(f"$MFMT $MIREG {index}\n")  # Writing initial tags with index
                output_rdf.write("\n")  # Writing a blank line
                structure_data = record["molstructure"].split('\r\n')  # Splitting structure data
                for line in structure_data:  # Iterating through structure data lines
                    if line:  # Checking for non-empty lines
                        if "-ISIS- " in line:  # Checking for specific condition
                            line = line + "\n"  # Appending newline if condition met
                        output_rdf.write(line + "\n")  # Writing structure data line by line

                for key, value in record.items():  # Iterating through record items
                    if key != "molstructure" and key != "bioactivity":  # Excluding specific keys
                        output_rdf.write(f"$DTYPE MOL:{key.upper()}\n")  # Writing data type tag
                        output_rdf.write(f"$DATUM {value}\n")  # Writing data value

                if "bioactivity" in record:  # Checking for existence of "bioactivity" key
                    for item in record["bioactivity"]:  # Iterating through bioactivity items
                        if isinstance(item, dict):  # Checking if item is a dictionary
                            for key, value in item.items():  # Iterating through dictionary items
                                output_rdf.write(f"$DTYPE MOL:RESULT({index}):{key.upper()}\n")  # Writing data type tag
                                if "\r\n" in value:  # Checking for specific condition in value
                                    parts = value.split("\r\n")  # Splitting value
                                    for i, part in enumerate(parts):  # Iterating through parts
                                        if len(part) > 73:  # Checking length of part
                                            remaining_chars = part  # Assigning remaining characters
                                            while len(remaining_chars) > 73:  # Loop until characters are less than 73
                                                output_rdf.write(
                                                    "$DATUM " + remaining_chars[:73] + "+\n")  # Writing part
                                                remaining_chars = remaining_chars[74:]  # Updating remaining characters
                                            output_rdf.write(remaining_chars + "\n")  # Writing remaining characters
                                        else:
                                            if i > 0:  # Checking if not the first part
                                                output_rdf.write(f"{part}\n")  # Writing part
                                            else:
                                                output_rdf.write(f"$DATUM {part}\n")  # Writing part
                                else:
                                    if len(value) > 73:  # Checking length of value
                                        remaining_chars = value  # Assigning remaining characters
                                        while len(remaining_chars) > 73:  # Loop until characters are less than 73
                                            output_rdf.write("$DATUM " + remaining_chars[:73] + "+\n")  # Writing value
                                            remaining_chars = remaining_chars[73:]  # Updating remaining characters
                                        output_rdf.write(remaining_chars + "\n")  # Writing remaining characters
                                    else:
                                        output_rdf.write(f"$DATUM {value}\n")  # Writing value
                        else:
                            print("Invalid bioactivity item format:", item)  # Printing error message if item format is invalid
                index += 1  # Increment index for next record

        print("File is successfully converted to RDF output")  # Printing success message after conversion
