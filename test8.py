import pytest
import System

# Used to restore data
#import RestoreData

### Tests if the check_ontime from Student.py works as intended
def test_check_ontime(grading_system):
    # Test user and password
    username = 'akend3'
    password =  '123454321'

    # Login as student
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Checks if assignment is ontime
    date = '3/19/22'
    due_date = '4/20/23'
    late_date = '2/18/21'

    # Checks if assignment is on time
    assert grading_system.usr.check_ontime(date, due_date) == True
    # Checks if it is late
    assert grading_system.usr.check_ontime(date, late_date) == False

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem