# Project Overview
The Food Truck Finder project is a Django-based application designed to explore San Francisco's street food scene. The implementation includes a web frontend that allows users to find nearby food trucks based on latitude and longitude. The backend utilizes a Haversine algorithm to calculate proximity, and the project includes a CSV import script for data initialization.

# Implementation
## Backend

### Database Design
The backend utilizes Django models to represent food trucks, providing a clear structure for storing and retrieving data.
Sqlite3 database is employed to persistently store food truck information.
### Data Import
The CSV import script (import_foodtrucks.py) efficiently reads the San Francisco Food Truck dataset, transforming each row into a Django FoodTruck model instance.
Database transactions ensure atomicity during the import process, handling potential errors gracefully.
### Haversine Algorithm
The Haversine algorithm is implemented in the backend to calculate distances between user-specified coordinates and food truck locations, facilitating the identification of nearby options.
### Pagination
The Django Paginator is employed for seamless pagination of food trucks, providing an organized and user-friendly display.

## Frontend
The web frontend, built with HTML, CSS, and JavaScript, provides a visually appealing and intuitive interface.
Users input their latitude and longitude to discover nearby food trucks, and the results are displayed on an interactive map.
A "Read More" popup enhances user experience by offering detailed information about a selected food truck.


   ```bash

# Installation

## Windows

Clone the repository: git clone <https://github.com/Masiza-Fidel/RAKT-innovation.git>

Navigate to the project directory: cd RAKT-innovation/innovate
Create a virtual environment: python -m venv venv
Activate the virtual environment: venv\Scripts\activate
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Run the development server: python manage.py runserver
pip install -r requirements.txt


## macOS
Clone the repository: git clone <https://github.com/Masiza-Fidel/RAKT-innovation.git>
Navigate to the project directory: cd RAKT-innovation/innovate
Create a virtual environment: python3 -m venv venv
Activate the virtual environment: source venv/bin/activate
Install dependencies: pip install -r requirements.txt
Run migrations: python manage.py migrate
Run the development server: python manage.py runserver

   ```

## Future Enhancements

### AI-Powered Conversational Interface

With additional time, a planned enhancement involves implementing an AI-powered conversational interface using the Langchain framework. This feature would allow clients to interact with the CSV data in a natural and conversational manner. Users could ask questions, seek recommendations, or inquire about specific details related to food trucks, enhancing the overall user experience and accessibility of the application.
