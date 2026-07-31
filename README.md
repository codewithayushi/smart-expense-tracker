# Smart Expense Tracker API

A simple REST API built with FastAPI to manage personal expenses. Data is stored in a local JSON file.

## Features
- Add an expense
- View all expenses (with optional category filtering)
- Calculate total expenses (overall and category-wise)
- Delete an expense by ID

## Installation & Setup

1. Clone the repository and navigate to the folder.
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   venv\Scripts\activate

## Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t expense-tracker .

## Docker Support 
To run the application using Docker:
```bash
docker build -t smart-expense-tracker .
docker run -p 8000:8000 smart-expense-tracker

## Project Screenshot
![Expense Tracker Preview](screenshot/output.png)
