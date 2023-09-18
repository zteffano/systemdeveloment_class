"""
REST API CLASS

ROUTES:
    /register - POST
    /login - POST
    /users - GETi
    /quotes - GET
    /quote/:qid - GET
    /quote - POST
    /quote/:qid - PUT
    /qoute/:qid - DELETE

"""
import requests
import json
from time import sleep
API_URL = "https://rocky-gorge-77460-611a79604e3d.herokuapp.com"


class MyAPI:

    def __init__(self, API_URL, uid, pwd, auth_token=""):
        self.api_url = API_URL
        self.uid = uid
        self.pwd = pwd
        self.auth_token = ""
        self.quotes = {}
        self.users = {}
        self.my_quotes_id = []
        self.register() #opretter bruger, hvis ikke der kan logges ind med de oplysninger der er givet
    def register(self):
    
            payload = {
                "uid": self.uid, 
                "pwd": self.pwd
                }
            response = requests.post(f"{self.api_url}/register", json=payload)
            if response.status_code == 201:
                print(f"Welcome {self.uid} - New User created Succesfully")
            elif response.status_code == 500 and "duplicate key" in response.content.decode("utf-8"):
                print(f"User {self.uid} already exists")
            else:
                print("Something went wrong")
            return response


    def login(self):
        # Test login
        payload = {
            "uid": self.uid, 
            "pwd": self.pwd
            }

        response = requests.post(f"{self.api_url}/login", json=payload)
        self.auth_token = response.content.decode("utf-8").strip('"')
        print("My auth token: ", self.auth_token)
        return response
        

    def get_users(self):
        response = requests.get(f"{self.api_url}/users")
        self.users = response.json()
        return response


    def get_quotes(self):
        response = requests.get(f"{self.api_url}/quotes")
        self.quotes = response.json()
        return response

    def get_quote(self,qid):
        response = requests.get(f"{self.api_url}/quote/{qid}")
        return response

    def post_quote(self, quote, attribution):
        payload = {
            "quote": quote, 
            "attribution": attribution
        }
        auth =  {"Authorization":self.auth_token}
        response = requests.post(f"{self.api_url}/quote", headers=auth, json=payload)
        return response


    def change_quote(self,qid, quote, attribution):
        payload = {
            "quote": quote, 
            "attribution": attribution
        }
        auth =  {"Authorization":self.auth_token}
        response = requests.put(f"{self.api_url}/quote/{qid}", headers=auth, json=payload)
        return response

    def delete_quote(self,qid):
        auth = {"Authorization":self.auth_token}
        response = requests.delete(f"{self.api_url}/quote/{qid}", headers=auth)
        return response
    
    def print_users(self):
        print(json.dumps(self.users,indent=2))
    
    def print_quotes(self):
        print(json.dumps(self.quotes,indent=2))

    def get_my_quotes(self):
        self.get_quotes()
        my_quotes = []
        for key in self.quotes.values():
            for v in key:
                if v["uid"] == self.uid:
                    my_quotes.append(v["qid"])
        self.my_quotes_id = my_quotes
        return self.my_quotes_id
   
      

 


api = MyAPI(API_URL, "steffan", "1234")
