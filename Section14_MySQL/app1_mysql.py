# Section 14 - Interactive English Dictionary using MySQL

import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)


def get_results(word):
    cursor = con.cursor()
    query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s'" %word)
    return cursor.fetchall()


def get_all():
    cursor = con.cursor()
    query = cursor.execute("SELECT * FROM Dictionary")
    return cursor.fetchall()


def print_results(results):
    for result in results:
        print(result[1])


word = input("Enter a word: ")

all_data = get_all()

all_expressions = [i for i, j in all_data]
close_match = get_close_matches(word, all_expressions, cutoff=0.8)

if results := get_results(word): # := in-line assignment works starting with Python 3.8
    print_results(results)
elif len(close_match) > 0:
        yn = input(f"Did you mean {close_match[0]} instead? (y or n): ")
        if yn == "y":
            results = get_results(close_match[0])
            print_results(results)
        elif yn == "n":
            print("The word doesn't exist. Please double check it.")
        else:
            print("We didn't understand your entry.")
else:
    print("No word found!")
