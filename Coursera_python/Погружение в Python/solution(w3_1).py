class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        str_of_file = ""
        try:
            with open(self.file_path, 'r') as f:
                str_of_file = f.read()
            return str_of_file
        except FileNotFoundError:
            return str_of_file
