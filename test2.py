import pytest
import System

### Tests if the check_password from System.py only accepts correct passwords
def test_check_password(grading_system):
    # Test User with correct password
    user = 'cmhbf5'
    password =  'bestTA'

    # Incorrect Passwords
    password1 =  'bestta'
    password2 =  'BestTA'
    password3 =  'best TA'
    password4 =  'bestTA.'
    password5 =  ''

    ### Tests passwords
    # Base Case
    assert grading_system.check_password(user, password)   == True

    # Incorrect variants
    assert grading_system.check_password(user, password1)   == False
    assert grading_system.check_password(user, password2)   == False
    assert grading_system.check_password(user, password3)   == False
    assert grading_system.check_password(user, password4)   == False
    assert grading_system.check_password(user, password5)   == False


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem