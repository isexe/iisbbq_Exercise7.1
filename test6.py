import pytest
import System

# Used to restore data
#import RestoreData

### Tests if the drop_student from Professor.py works as intended
def test_drop_student(grading_system):
    # Test user and password
    username = 'goggins'
    password =  'augurrox'

    # Login as professor
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Drops student to course
    grading_system.usr.drop_student('akend3', 'databases')

    # Tests if student was dropped from course
    for key in grading_system.users['akend3']['courses']:
        assert key != 'databases'

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem