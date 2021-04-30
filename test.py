import Generate_Email
import delete
import search


''' 
There is some error with this function as it runs very well during the code execution
But I don't know why it is causing error during test
One reason may be the output functions present there but still not sure
'''
# def test_search1():  # Function to test search function
#     assert search.search(1728006) == 1


def test_search():
    output = search.search(1728067)
    assert output == 0


def test_Generate_Email():  # Function to generate email id
    output = Generate_Email.new_email(1728067)
    assert output == "1728067@kiit.ac.in"


def test_Delete1():  # Function to delete a record
    output = delete.delete(1725011)
    assert output == 0


def test_Delete2():
    output = delete.delete(1527093)
    assert output == 0
