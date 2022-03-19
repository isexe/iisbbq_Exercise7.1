import pytest
import System

# Used to restore data
#import RestoreData

### Tests security of system by trying to find Prof credentials
def test_login_security(grading_system):
    #task state
    failed = False

    # Empty username and password
    username = ''
    password =  ''

    try:
        # Try to access db information
        users = grading_system.users
        for key in users:
            if users[key]['role'] == 'professor':
                username = key
                password = users[key]['password']

        # Login as professor
        grading_system.login(username,password)

        ### Tests correct user login
        assert grading_system.usr.name == username
        assert grading_system.usr.password == password
    except:
        failed = True

    # Tests if user couldn't log in with database information
    assert failed == True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem