# Python SQLite and Pandas Project

## Overview

This project demonstrates how to use Python, the `sqlite3` module, and the `pandas` library to manage data. It specifically focuses on:

1.  **Reading data from a CSV file:** Using pandas to efficiently read and process data.
2.  **Storing data in a SQLite database:** Creating a database and table, and inserting data from the CSV file.
3.  **Executing SQL queries:** Performing various SQL operations (SELECT, INSERT, etc.) using Python's `sqlite3` module.

This project provides a foundation for working with structured data in Python, combining the flexibility of pandas for data manipulation with the robustness of SQLite for data storage.

## Features

-   Reads data from a CSV file (`books.csv`).
-   Creates a SQLite database (`books.db`) and a table named `books`.
-   Inserts the data from the CSV file into the `books` table.
-   Demonstrates basic SQL queries using Python's `sqlite3` module.

## Prerequisites

Before running this project, ensure you have the following installed:

-   **Python:** (Version 3.6 or later is recommended)
-   **pandas:** Install using pip:
    ```bash
    pip install pandas
    ```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/TrevorOlso/SQL_practice]
  
2.  **Place the `books.csv` file:** Make sure the `books.csv` file is in the same directory as the `books.py` script.

## Usage

1.  **Run the Python script:**
    ```bash
    python books.py
    ```

The script will:

-   Create the `books.db` database (if it doesn't exist).
-   Create the `books` table within the database.
-   Read the data from `books.csv`.
-   Insert the data into the `books` table.
-   Execute and print the results of a few basic SQL queries.
