from evolvus.rdf.model.RDFRecord import RDFRecord


class RDFParser:
    RECORD_START_STRING = "$MFMT $MIREG"
    STRUCTURE_END_STRING = "M  END"

    def __init__(self, input_file):
        self._input = input_file
        self._rdf_records = []

    def get_records(self):
        return self._rdf_records

    def get_num_records(self):
        return len(self._rdf_records)

    def parse(self):
        read_header_yet = False
        processing_structure = False
        processing_data = False
        current_record = None
        f = open(self._input, "r", encoding='cp1252')
        while True:
            line = f.readline()
            if not line:
                break

            if len(line.strip()) == 0 and not processing_structure:
                continue
            if line=="" and processing_structure:
                current_record.get_structure().add_to_structure(line)

            # parse rdf file
            # line = line.strip()
            if read_header_yet is False and line.startswith(RDFParser.RECORD_START_STRING) is False:
                continue

            if line.startswith(RDFParser.RECORD_START_STRING):
                if read_header_yet is False:
                    read_header_yet = True

                if current_record is not None:
                    self._rdf_records.append(current_record)

                current_record = RDFRecord()
                processing_structure = True
                processing_data = False
                continue

            if line.startswith(RDFParser.STRUCTURE_END_STRING):
                current_record.get_structure().add_to_structure(line)
                processing_structure = False
                processing_data = True
                continue

            if processing_structure:
                current_record.get_structure().add_to_structure(line)
                continue

            if processing_data:
                current_record.get_data().add_to_data(line)
                continue

        self._rdf_records.append(current_record)
