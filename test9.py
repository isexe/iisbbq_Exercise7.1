import pytest
import System

# Used to restore data
#import RestoreData

### Tests if the check_grades from Student.py works as intended
def test_check_grades(grading_system):
    # Test user and password
    username = 'akend3'
    password =  '123454321'

    # Login as student
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Checks grades of student
    grades = grading_system.usr.check_grades('comp_sci')

    # Checks if the results are correct
    assign_index = 0
    assignments = grading_system.users[username]['courses']['comp_sci']
    for assignment in assignments:
        # Checks assignment name
        assert assignment == grades[assign_index][0]
        # Checks assignment grade
        assert assignments[assignment]['grade'] == grades[assign_index][1]
        assign_index += 1

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem