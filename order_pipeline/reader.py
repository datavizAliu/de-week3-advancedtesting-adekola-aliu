import json
import os.path

class Reader:
    def __init__(self):
        pass

    def read_json(self, path):
        #existence
        if not os.path.isfile(path):
            raise ValueError("File not found")
        #read
        try:
            with open(path, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("Not valid JSON")
        #not empty
        if len(data) == 0:
                raise ValueError("File is empty")
        #format validation
        if not isinstance(data, list) or not all(isinstance(d,dict) for d in data):
             raise ValueError("JSON format must be list of dictionaries")
        return data
    


        
    