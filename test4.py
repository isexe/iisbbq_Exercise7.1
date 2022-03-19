import pytest
import System

### Tests if the create_assignment from Staff.py works as intended
def test_create_assignment(grading_system):
    # Test user and password
    username = 'goggins'
    password =  'augurrox'

    # Login as professor
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Create a new assignment
    grading_system.usr.create_assignment('assignment3', '04/01/20', 'cloud_computing')

    ### Tests if the course was added and if the due date is right
    # Throws KeyError if assignment not added
    # Throws AssertionError if date wrong
    assert grading_system.courses['cloud_computing']['assignments']['assignment3']['due_date'] == '04/01/20'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem