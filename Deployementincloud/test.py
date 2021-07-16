# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:40:42 2020

@author: Adminr
"""
import requests

url = "https://language-translation.p.rapidapi.com/translateLanguage/detect-language"

querystring = {"text":"Привет, мой дорогой друг!"}

headers = {
      'x-rapidapi-key': "53f1f79204msh44f4e55984ec5d7p1126fdjsn451cabf12fbd",
    'x-rapidapi-host': "language-translation.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)








