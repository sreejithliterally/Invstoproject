
# Investo CSV data upload and view

This is simple application built using Python, FastAPI, SQLAlchemy, and PostgreSQL to upload and csv data and view it as a table for the purpose of internship at investo . The app allows users to upload CSV files containing investment data, which is then stored in a PostgreSQL database. Users can also view the stored data in tabular format using a React frontend.

## Features

- Upload CSV: Users can upload CSV files containing investment data using the web interface. The backend processes the uploaded file and stores the data in the database.
![Input](https://github.com/sreejithliterally/Invstoproject/blob/main/screenshots/csvip.png)
![Backend Post req](https://github.com/sreejithliterally/Invstoproject/blob/main/screenshots/backendcsvip.png)
- View Data: Users can view the stored investment data as tables on the web interface. The React frontend fetches the data from the backend API and displays it in an easy-to-read format.
![View data]([http://url/to/img.png](https://github.com/sreejithliterally/Invstoproject/blob/main/screenshots/csvtableop.png))
![View data](https://github.com/sreejithliterally/Invstoproject/blob/main/screenshots/backendget.png)
## Prerequisites

Before running the application, make sure you have the following installed on your system:

- Python 3.7+
- Node.js
- PostgreSQL

## Installation

1. Clone the repository to your local machine.

2. Create a virtual environment and activate it:

```bash
   python3 -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate
```

Install the backend dependencies:
```bash
pip install -r requirements.txt
```
Install the frontend dependencies:
```bash
cd app/frontend
npm install
```

Sure! Here's the README in Markdown format again:

markdown

# Investment Data Management App

This is a web application built using Python, FastAPI, SQLAlchemy, and PostgreSQL to manage investment data. The app allows users to upload CSV files containing investment data, which is then stored in a PostgreSQL database. Users can also view the stored data in tabular format using a React frontend.

## Features

- Upload CSV: Users can upload CSV files containing investment data using the web interface. The backend processes the uploaded file and stores the data in the database.

- View Data: Users can view the stored investment data as tables on the web interface. The React frontend fetches the data from the backend API and displays it in an easy-to-read format.

## Prerequisites

Before running the application, make sure you have the following installed on your system:

- Python 3.7+
- Node.js
- PostgreSQL

## Installation

1. Clone the repository to your local machine.

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows: env\Scripts\activate

    Install the backend dependencies:

    bash

pip install -r requirements.txt

Install the frontend dependencies:

```bash

    cd app/frontend
    npm install
```
Database Configuration

Before running the application, you need to set up the PostgreSQL database and configure the database credentials.

   Create a new PostgreSQL database for the app, or use an existing one.

   In the .env file, set the following environment variables:
```bash
DATABASE_URL=postgresql://your_username:your_password@your_hostname:your_port/your_database_name
```
Replace your_username, your_password, your_hostname, your_port, and your_database_name with your actual PostgreSQL credentials.


## Running the Application

To run the application, follow these steps:

1Activate the virtual environment:
```bash
source env/bin/activate  # For Windows: env\Scripts\activate
```
2.Start the backend server:
```bash
uvicorn main:app --reload
```
The backend server will be running at http://127.0.0.1:8000.

3.Start the frontend development server:
```bash
cd app/frontend
npm start
```
The frontend development server will be running at http://localhost:3000

## Usage

    Access the web application by opening your browser and navigating to http://localhost:3000.

    Upload CSV: On the homepage, click on the "Upload CSV" button to select and upload a CSV file containing investment data. The backend will process the file, and the data will be stored in the database.

    View Data: After uploading the CSV file, you can click on the "View Data" button to see the investment data displayed in tabular format. The data will be fetched from the backend API and displayed on the frontend.

