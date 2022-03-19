import pytest
import System

# Used to restore data
#import RestoreData

### Tests if the view_assignments from Student.py works as intended
def test_view_assignments(grading_system):
    # Test user and password
    username = 'akend3'
    password =  '123454321'

    # Login as student
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Views assignments
    course = 'databases'
    result = grading_system.usr.view_assignments(course)

    # Checks if assignments are correctly returned
    assignments = grading_system.courses[course]['assignments']
    assign_index = 0
    for key in assignments:
        assert key == result[assign_index][0]
        assert assignments[key]['due_date'] == result[assign_index][1]
        assign_index += 1

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem