# import argparse
import os
from evolvus.rdf.JSONWriter import JSONWriter
from evolvus.rdf.RDFParser import RDFParser
from evolvus.rdf.JsonParser import JsonParser
from evolvus.rdf.SDFFile import SDFFile


# def parse_args():
#     parser = argparse.ArgumentParser(description="Parsing and Converting Program")
#     parser.add_argument("-i", "--input", help="Input path to a file or a directory")
#     parser.add_argument("-o", "--output", help="Output path to a file or a directory")
#     parser.add_argument("-if", "--inputformat", choices=["rdf"], help="Input format")
#     parser.add_argument("-of", "--outputformat", choices=["json"], help="Output format")

# args = parser.parse_args()
# if args.input is None or args.output is None or args.inputformat is None or args.outputformat is None:
#     parser.print_help()
#     exit(0)
# return args.input, args.output, args.inputformat, args.outputformat


def main(input_file, output_file, input_format, output_format):
    # input_file, output_file, input_format, output_format = parse_args()
    if input_format == "rdf" and output_format == "json":
        if not os.path.exists(output_file):
            os.makedirs(output_file)
        if os.path.isdir(input_file):
            for filename in os.listdir(input_file):
                if filename.endswith(".rdf"):
                    file1 = os.path.join(input_file, filename)
                    file2 = os.path.join(output_file, filename.replace(".rdf", "_ks.json"))
                    convert_to_json(file1, file2)
            print("All RDF files in the directory are successfully converted to JSON.")
        else:
            # Handle single file conversion
            convert_to_json(input_file, output_file)
            print("File is successfully converted to JSON.")

    elif input_format == "json" and output_format == "rdf":
        if not os.path.exists(output_file):
            os.makedirs(output_file)
        if os.path.isdir(input_file):
            for filename in os.listdir(input_file):
                if filename.endswith(".json"):
                    file1 = os.path.join(input_file, filename)
                    file2 = os.path.join(output_file, filename.replace(".json", ".rdf"))
                    convert_to_rdf(file1, file2)
            print("All JSON files in the directory are successfully converted to RDF.")

    elif input_format == "rdf" and output_format == "sdf":
        if not os.path.exists(output_file):
            os.makedirs(output_file)
        if os.path.isdir(input_file):
            for filename in os.listdir(input_file):
                if filename.endswith(".rdf"):
                    file1 = os.path.join(input_file, filename)
                    file2 = os.path.join(output_file, filename.replace(".rdf", ".sdf"))
                    convert_rdf_to_sdf(file1, file2)
            print("All RDF files in the directory are successfully converted to SDF.")

    elif input_format == "json" and output_format == "sdf":
        if not os.path.exists(output_file):
            os.makedirs(output_file)
        if os.path.isdir(input_file):
            for filename in os.listdir(input_file):
                if filename.endswith(".json"):
                    file1 = os.path.join(input_file, filename)
                    file2 = os.path.join(output_file, filename.replace(".json", ".sdf"))
                    convert_json_to_sdf(file1, file2)
            print("All JSON files in the directory are successfully converted to SDF.")
    else:
        print("Please Choose Currect Format")


def convert_to_rdf(input_file, output_file):
    json_parse = JsonParser()
    json_parse.convert_json_to_rdf(input_file, output_file)


def convert_rdf_to_sdf(input_file, output_file):
    sdf_parser = SDFFile(input_file, output_file)
    sdf_parser.rdf_to_sdf()


def convert_json_to_sdf(input_file, otput_file):
    sdf_json_parser = SDFFile(input_file, otput_file)
    sdf_json_parser.json_to_sdf()


def convert_to_json(input_file, output_file):
    parser = RDFParser(input_file)

    parser.parse()
    print("Number of Records ", parser.get_num_records())

    rdf_records = parser.get_records()
    for rdf_record in rdf_records:
        if rdf_record.process_data() is False:
            print("Not able to process records")
            exit(1)
        else:
            print("Processed Data ", rdf_record.get_processed_data())
            print("Result Data ", rdf_record.get_result_data())
    writer = JSONWriter()
    writer.write_json(output_file, rdf_records)


if __name__ == "__main__":
    main()
