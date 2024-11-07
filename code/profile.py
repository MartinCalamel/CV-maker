from data import Data

class Profile : 
    def __init__(self, profile_name : str):
        self.file_profile = "profile.json"
        self.profile_elements = [["surname",""],
                                 ["name",""],
                                 ["address",""],
                                 ["phone",""],
                                 ["email",""],
                                 ["github",""],
                                 ["experience",["title","company","position","dates"]],
                                 ["education",["institution","dates"]],
                                 ["awards",[]],
                                 ["skills",[]],
                                 ["hobbies",[]]]
        self.data=Data(self.file_profile)
    
    def set_profile(self, profile_name : str) -> dict:
        """
        fonction for get profile info from the profile.json file

        """
        profile_data = self.data.read()
        if profile_name in profile_data.keys():
            return profile_data[profile_name]
        return self.add_profile(profile_name)
    
    def add_profile(self, profile_name : str) -> dict:
        """
        fonction for add a profile in the file profile.json and return the data of the profile
        """
        data = self.make_profile(self.profile_elements)
        self.data.add_category(profile_name,data)
        return data
    
    def make_profile(self,profile_elements : list):
        data={}
        for element in profile_elements:
            if element[1] == "" :
                data[element[0]] = input(f'{element[0]} : ')
            elif element[1] == []:
                data[element[0]] = self.add_list_element(element[0])
            elif type(element[1]) == list:
                for i in element[1]:
                    self.make_profile()
    
    def add_list_element(self, element_name : str) -> list:
        res = []
        stop = False
        while not stop:
            new = input(f'element to add to {element_name} (q for stop) : ')
            if new == "q":
                stop = True
            else:
                res.append(new)
        return new
