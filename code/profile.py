from data import Data

class Profile : 
    def __init__(self, profile_name : str):
        self.file_profile = "code/profile_test.json"
        self.profile_elements = [["surname",""],
                                 ["name",""],
                                 ["address",""],
                                 ["phone",""],
                                 ["email",""],
                                 ["github",""],
                                 ["experience",[["title",""],["company",""],["position",""],["dates",""]]],
                                 ["education",[["institution",""],["dates",""]]],
                                 ["awards",[]],
                                 ["skills",[]],
                                 ["hobbies",[]]]
        self.data=Data(self.file_profile)
        self.profile = self.set_profile(profile_name)
    
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
    
    def make_profile(self,profile_elements : list) -> dict:
        data={}
        for element in profile_elements:
            if element[1] == "" :
                data[element[0]] = input(f'{element[0]} : ')
            elif type(element[1]) == list:
                data[element[0]] = self.add_list_element(element)
        
        return data
    
    def add_list_element(self, element : list) -> list:
        res = []
        stop = False

        if element[1] == []:
            while not stop:
                new = input(f'element to add to {element[0]} (q for stop) : ')
                if new == "q":
                    stop = True
                else:
                    res.append(new)

        else :
            while not stop:
                stop = input(f'add new element to {element[0]} (q for stop other to continue) : ')=='q'
                if not stop :
                    new= self.make_profile(element[1])
                    res.append(new)
        return res


if __name__ == '__main__' :
    profile=Profile("profile1")
    print(profile.data)
