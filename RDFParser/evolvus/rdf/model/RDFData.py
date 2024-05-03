class RDFData:
    KEY_START_STRING = "$DTYPE"
    VALUE_START_STRING = "$DATUM"
    RESULT_KEY_MARKER = "MOL:RESULT("
    VALUE_WRAP_LENGTH = 81

    def __init__(self):
        self._data = []
        self._processed_data = {}
        self._result_data = {}

    def get_processed_data(self):
        return self._processed_data

    def get_result_data(self):
        return self._result_data

    def add_to_data(self, line):
        self._data.append(line)

    def extract_result_data(self):
        keys_to_remove = []
        for key in self._processed_data.keys():
            if RDFData.RESULT_KEY_MARKER in key:
                data = key[len(RDFData.RESULT_KEY_MARKER):]
                index = data[0:data.index(")")]
                parameter = data[data.index(":") + 1:]
                item = self._result_data.get(index, {})
                item[parameter] = self._processed_data[key]
                self._result_data[index] = item
                keys_to_remove.append(key)

        for key in keys_to_remove:
            self._processed_data.pop(key)

    def process_data(self) -> bool:
        key = ""
        value = ""
        process_key_flag = True
        for i in range(0, len(self._data)):
            line = self._data[i].strip()
            if len(line) == 0:
                continue
            if process_key_flag and line.startswith(RDFData.KEY_START_STRING):
                key = line[len(RDFData.KEY_START_STRING):]
                process_key_flag = False
            elif process_key_flag is False and line.startswith(RDFData.VALUE_START_STRING):
                value = line[len(RDFData.VALUE_START_STRING):]
                for j in range(i + 1, len(self._data)):
                    additional_line = self._data[j].strip()
                    if additional_line.startswith(RDFData.KEY_START_STRING):
                        break
                    if additional_line == "":
                        continue
                    else:
                        if value.endswith("+"):
                            value = value[0: len(value) - 1] + additional_line
                        else:
                            value = value+"\\r\\n"+additional_line
                        continue
                process_key_flag = True
            self._processed_data[key.strip()] = value.strip()
        self.extract_result_data()
        return True
