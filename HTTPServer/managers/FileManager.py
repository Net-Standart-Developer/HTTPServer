import os

class FileManager:
    @staticmethod
    def read_file(path):
        with open(path, "r") as file:
            return file.read()

    @staticmethod
    def file_is_exist(path):
        return os.path.isfile(path)

    