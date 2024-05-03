class RDFStructure:
    STRUCTURE_END_STRING = "M  END"

    def __init__(self):
        self._structure_data = []

    def add_to_structure(self, line):
        self._structure_data.append(line)
        if line.endswith(RDFStructure.STRUCTURE_END_STRING):
            self._structure_data.remove("\\r\\n")

    def process_data(self) -> bool:
        return True