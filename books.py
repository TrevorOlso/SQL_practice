#importing necessary tools
import pandas as pd
import csv
import sqlite3

#Set up files needed and variables needed
books_db = "books.db"
connection = sqlite3.connect("books.db")
books_df = pd.read_csv("books.csv")
curs = connection.cursor()

#creating the table"
curs.execute( '''
     CREATE TABLE IF NOT EXISTS books(
           title TEXT,
           author TEXT,
           genre TEXT,
           height REAL,
           publisher TEXT)''')
connection.commit()
print("table created succesfully")

#filling table with data
insert_records = "INSERT INTO books (title , author, genre, height, publisher) values(?, ?, ?, ?, ?)"

data_to_insert = books_df[['Title', 'Author', 'Genre', 'Height', 'Publisher']].values.tolist()

curs.executemany(insert_records, data_to_insert)

connection.commit()

print("Sucessfuly loaded table data")

#-----basic queries-----#
print("Basic Queries")

curs.execute("Select DISTINCT genre from books")
unique_genres = curs.fetchall()
print("Unique genres: ", [row[0] for row in unique_genres])


curs.execute("SELECT genre, COUNT(*) FROM books GROUP by genre")
genre_counts = curs.fetchall()
print("Books per genre: ")
for genre, count in genre_counts:
    print(f"{genre} , {count}")
    
