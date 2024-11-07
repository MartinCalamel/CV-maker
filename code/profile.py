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
        pass
        
