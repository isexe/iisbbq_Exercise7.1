import pytest
import System

### Tests if the change_grade from Staff.py can changes grades
def test_change_grade(grading_system):
    # Test user and password
    username = 'goggins'
    password =  'augurrox'

    # Login as professor
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    new_grade = 100

    #  Change grade of student enrolled in prof's class
    grading_system.usr.change_grade('yted91', 'software_engineering', 'assignment1', new_grade)

    ### Tests the if grade was changed to new grade
    assert grading_system.users['yted91']['courses']['software_engineering']['assignment1']['grade'] == new_grade

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem