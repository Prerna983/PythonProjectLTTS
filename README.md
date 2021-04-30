# KIIT Management System

## Introduction

- This project is mainly based on the the 'KIIT UNIVERISTY' system where the registered students are given roll numbers and email ids during the time of joining.
- So basically when a student is registering for the college he/she is getting a roll number based on the branch and year in which they are joining.
- Also, the email is generated based on the roll number and the domain is kept common for all.
- So, this project mainly demonstrates an example of how it is being done in the college.

## File Structure

Files               | description
------------------- | ----------------------------------------------
`main.py`           | Main menu to run the program
`menu.py`           | To display the main menu of the program
`add.py`            | To add new entries and details. After entry it generates roll no. and email id 
`search.py`         | To search if the given roll number is present or not
`delete.py`         | To delete an entry
`display.py`        | To display list of students present in the record in increasing order of roll number
`Generate_Email.py` | To generate email id based on the roll no.
`Generate_Roll.py`  | To generate roll number from the branch and year of joining
`test.py`           | To test the files and functions used in the program
`student.csv`       | A csv file to store all the details of the student

## Working

1) A main menu is displayed that asks for user input for their choice.
2) As per the choice the program runs.
3) If the user input is '1' i.e. add, it asks the user for the details. After entering the details, it generates roll no. and email id and asks the user to keep a note of it for further use.
4) The flow then returns back to the main menu
5) If the user input is '2' i.e. search or 'confirm your entry' here, the computer asks the user for his roll no. so that it can confirm if his name is registered or not.
6) If the user input is '3' i.e. 'display the list', the computer displays the existing record entry in increasing roll number.
7) If the user input is '4' i.e. delete or 'leave the college' here, the computer deletes his entry from the list.
8) If the user input is '5', it exits from the program

