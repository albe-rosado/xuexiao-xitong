import json

class GetFile:
    def __init__(self, fileDir):
        self._fileDir = fileDir
    # Reads the given file
    def Read(self):
        with open(self._fileDir) as file:
            data = json.load(file)
        return data
