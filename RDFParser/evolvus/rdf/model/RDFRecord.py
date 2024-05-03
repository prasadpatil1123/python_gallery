from evolvus.rdf.model.RDFStructure import RDFStructure
from evolvus.rdf.model.RDFData import RDFData


class RDFRecord:

    def __init__(self):
        self._rdf_structure = RDFStructure()
        self._rdf_data = RDFData()

    def process_data(self) -> bool:
        ret_val_1 = self._rdf_structure.process_data()
        ret_val_2 = self._rdf_data.process_data()
        return ret_val_1 and ret_val_2

    def get_processed_data(self):
        return self._rdf_data.get_processed_data()

    def get_result_data(self):
        return self._rdf_data.get_result_data()

    def get_structure(self) -> RDFStructure:
        return self._rdf_structure

    def get_data(self) -> RDFData:
        return self._rdf_data
