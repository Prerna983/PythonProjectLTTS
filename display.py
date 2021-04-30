# Function to display the list of details of the students present in the file
import pandas as pd
import csv

field = ['name', 'age', 'branch', 'year', 'email', 'roll']
database = 'student.csv'


def show():

    print("\n------------------- Student Details --------------------\n\n")

    file = open("student.csv")
    reader = csv.reader(file)
    lines = len(list(reader))

    df = pd.read_csv("student.csv")
    df1 = df.sort_values(by=["roll"], ignore_index=True)

    print(df1.head(lines))

    file.close()

    input("\nPress any key to continue.....")
    return
