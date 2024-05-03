# Importing the required modules
import json
from evolvus.rdf.model.RDFRecord import RDFRecord


# Defining a class SDFFile
class SDFFile:
    # Class variables
    RECORD_START_STRING = "$MFMT $MIREG"
    STRUCTURE_END_STRING = "M  END"

    # Constructor method
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self._rdf_records = []  # List to hold RDFRecord objects

    # Method to get RDF records
    def get_records(self):
        return self._rdf_records

    # Method to convert RDF to SDF format
    def rdf_to_sdf(self):
        read_header_yet = False
        processing_structure = False
        current_record = None

        # Opening the input file in read mode
        with open(self.input_file, "r") as f:
            while True:
                line = f.readline()  # Reading a line from the file
                if not line:  # If the line is empty, break the loop
                    break

                # If the line is empty and processing_structure is True,
                # add the line to the current_record's structure
                if line == "" and processing_structure:
                    current_record.get_structure().add_to_structure(line)

                # If read_header_yet is False and the line does not start with RECORD_START_STRING,
                # continue to the next iteration of the loop
                if read_header_yet is False and not line.startswith(SDFFile.RECORD_START_STRING):
                    continue

                # If the line starts with RECORD_START_STRING
                if line.startswith(SDFFile.RECORD_START_STRING):
                    if read_header_yet is False:
                        read_header_yet = True  # Set read_header_yet to True
                    if current_record is not None:
                        self._rdf_records.append(current_record)  # Append the current_record to _rdf_records list
                    current_record = RDFRecord()  # Create a new RDFRecord object
                    processing_structure = True  # Set processing_structure to True
                    continue

                # If the line starts with STRUCTURE_END_STRING
                if line.startswith(SDFFile.STRUCTURE_END_STRING):
                    current_record.get_structure().add_to_structure(line)  # Add the line to current_record's structure
                    processing_structure = False  # Set processing_structure to False
                    continue

                # If processing_structure is True, add the line to current_record's structure
                if processing_structure:
                    current_record.get_structure().add_to_structure(line)
                    continue

        # Append the last current_record to _rdf_records list
        self._rdf_records.append(current_record)

        # Writing SDF data to the output file
        with open(self.output_file, 'w') as output:
            for i in range(len(self._rdf_records)):
                record = self._rdf_records[i]
                structure_record = record.get_structure()._structure_data
                structure_string = ''.join(structure_record)
                output.write(structure_string)  # Writing structure data to output file
                output.write("> <unique_id>\n")  # Writing unique_id tag
                output.write(f"{i + 1}\n")  # Writing unique_id value
                output.write("\n$$$$\n")  # End of record marker
            # print("File converted RDF to SDF")

    # Method to convert JSON to SDF format
    def json_to_sdf(self):
        # Opening the input JSON file
        with open(self.input_file, 'r') as input_json:
            data = json.load(input_json)  # Loading JSON data

        # Writing SDF data to the output file
        with open(self.output_file, 'w') as output_sdf:
            for i, record in enumerate(data, start=1):  # Iterating over JSON records
                structure_data = record["molstructure"].split('\r\n')  # Extracting structure data
                for line in structure_data:
                    output_sdf.write(line + "\n")  # Writing structure data to output file
                output_sdf.write("> <unique_id>\n")  # Writing unique_id tag
                output_sdf.write(f"{i}\n")  # Writing unique_id value
                output_sdf.write("\n$$$$\n")  # End of record marker
            # print("File converted JSON to SDF")
