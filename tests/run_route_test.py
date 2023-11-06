"""Contains testing scenarios for website

The testing script covers three possible scenarios:
    1. Scenario 1: Returns all books from the library using the "/books" route.
    2. Scenario 2: Adds three test books using their ISBN numbers using the "/books" route.
    3. Scenario 3: Returns book information by its ISBN number using the "/isbn/<isbn>" route.
"""

import requests

localhost = 'http://localhost:5000/{}'

SCENARIO = 2 # You can change it to 3 different options: 1, 2, 3 (watch description above)


####### First test
if SCENARIO == 1:
     url = localhost.format("books")
     response = requests.get(url)
     if response.status_code == 200:
         print("Request was successful!")
         print("Response content: ", response.text)
     else:
         print(f"Request failed with status code {response.status_code}")

####### Second test
if SCENARIO == 2:
    data = [{"isbn": "0451524934"},
            {"isbn": "9780451524935"},
            {"isbn": "0061120081"}]
    url = localhost.format("books")
    for isbn in data:
        response = requests.post(url, json=isbn)
        if response.status_code == 200:
            print("Request was successful!")
            print("Response content: ", response.text)
        else:
            print(f"Request failed with status code {response.status_code}")

####### Third test
if SCENARIO == 3:
    data = ["0451524934", "9780451524935", "0061120081"]
    for isbn in data:
        sub_url = f"isbn/{isbn}"
        url = localhost.format(sub_url)
        response = requests.get(url)
        if response.status_code == 200:
            print("Request was successful!")
            print("Response content: ", response.text)
        else:
            print(f"Request failed with status code {response.status_code}")