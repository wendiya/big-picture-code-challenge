#Prerequisites

Before running the application, ensure you have all the necessary requirements installed. 
You can install them using requirements.txt.


## Getting started
To start the server and create the database automatically, run:
```
python3 main.py
```

## Running Tests

To run the tests, use the following command:
```
python3 tests/run_route_test.py
```

The testing script covers three possible scenarios:\
    1. Scenario 1: Returns all books from the library using the "/books" route.\
    2. Scenario 2: Adds three test books using their ISBN numbers using the "/books" route.\
    3. Scenario 3: Returns book information by its ISBN number using the "/isbn/<isbn>" route.