import pytest
import System

### Tests if the add_student from Professor.py works as intended
def test_add_student(grading_system):
    # Test user and password
    username = 'goggins'
    password =  'augurrox'

    # Login as professor
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Adds student to course
    grading_system.usr.add_student('akend3', 'software_engineering')

    # Tests if student was added to course
    assert grading_system.users['akend3']['courses']['software_engineering']

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem