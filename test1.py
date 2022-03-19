import pytest
import System

### Tests if the login from System.py can login username
def test_login(grading_system):
    # Test user and password
    username = 'cmhbf5'
    password =  'bestTA'

    # Attempt to login
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem