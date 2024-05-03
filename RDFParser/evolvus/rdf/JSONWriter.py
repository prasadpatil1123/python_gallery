class JSONWriter:
    KEY_MOL_REMOVER = "mol:"

    def write_json(self, output_file, records):
        try:
            with open(output_file, 'w') as output:
                output.write("[")
                for i in range(len(records)):
                    record = records[i]

                    output.write("{")
                    output.write("\"molstructure\":\"")

                    # Concatenate the lines in the structure data list into a single string
                    structure_string = ''.join(record.get_structure()._structure_data)

                    # Replace newline and carriage return characters after "M END"
                    if "M  END" in structure_string:
                        structure_string = structure_string.replace("M  END\n", "M  END")

                    # Replace newline and carriage return characters
                    structure_string = structure_string.replace("\n", "\\r\\n")

                    # Write the modified structure string to the output
                    output.write(structure_string)

                    output.write("\",")

                    for key, value in record.get_data().get_processed_data().items():
                        key = key[len(JSONWriter.KEY_MOL_REMOVER):].lower()
                        output.write("\"" + key + "\":\"" + value + "\",")

                    if record.get_data().get_result_data():
                        output.write("\"bioactivity\":[")
                        result_counter = 0

                        for result_key, result_item in record.get_data().get_result_data().items():
                            output.write("{")
                            for item_key, item_value in result_item.items():
                                if ":" in item_key:
                                    item_key = item_key.replace(":", "")
                                output.write(
                                    "\"" + item_key.lower() + "\":\"" + item_value + "\"")
                                if item_key != list(result_item.keys())[-1]:
                                    output.write(",")
                            output.write("}")
                            if result_key != list(record.get_data().get_result_data().keys())[-1]:
                                output.write(",")
                            result_counter += 1
                        output.write("]")

                    output.write("}")

                    if i != len(records) - 1:
                        output.write(",")

                output.write("]")
                print("File is successfully converted to JSON")
        except IOError as e:
            print("I/O error :", e)
