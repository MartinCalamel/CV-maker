"""
Author: Martin Calamel
Created: 2024-11-05
Description: file for use json DB
TODO: read json file
      modify json file
      write json file
"""


import json
from turtle import update

class Data:
    def __init__(self, file_name) -> None:
        self.file_name : str = file_name
        self.data = self.read()

    def read(self) -> dict:
        """
        fonction for read a json file and return the data in dict
        """
        with open(self.file_name, mode="r", encoding="utf-8") as read_file:
            data = json.load(read_file)
        return data
    
    def write(self, data) -> None:
        """
        fonction for write a dict data on a json file 
        """
        with open(self.file_name, mode="w", encoding="utf-8") as write_file:
            json.dump(data, write_file)
        return None
    
    def update_data(self,data):
        """
        fonction for update the json DB and the data variable
        """
        self.write(data)
        self.data = self.read()
    
    def add_data(self, param : str, data : list) -> None:
        """
        fonction to add data to a keys of the data dict and update the DB
        """
        data_prov=self.data
        if param in data_prov.keys():
            if type(data_prov[param]) == list:
                for i in data :
                    data_prov[param].append(i)
            else:
                data_prov[param]=[data_prov[param],]+data
            self.update_data(data_prov)

    def modify_data(self, param : str, data : list) -> None:
        """
        fonction for change the data of the dict data and update the data variable
        """
        data_prov=self.data
        if param in self.data.keys():
            if len(data) == 1:
                data_prov[param] = data[0]
            else:
                data_prov[param] = data
            self.update_data(data_prov)
    
    def add_category(self, param : str, data : list = []) -> None:
        """
        fonction to add category in data json file
        """
        data_prov=self.data
        data_prov[param] = data
        self.update_data(data_prov)
    
    def __str__(self) : 
        return json.dumps(self.data, indent=4)



if __name__ == "__main__" :
    """
    
    unit test
    
    """
    file="code/db_test.json"
    DB = Data(file)
    print(DB.data["name"])
    print(DB.data["activity"])
    DB.modify_data("name",["pablo",])
    DB.add_data("activity",['5','6'])
    DB.add_category("new")
    print(DB)
    