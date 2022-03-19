import pytest
import System

# Used to restore data
#import RestoreData

### Tests if staff can only create assignments for their own courses
def test_create_assignment_requirements(grading_system):
    # Test user and password
    username = 'goggins'
    password =  'augurrox'

    # Login as prof
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Tries add an assignment to a course the prof doesn't teach
    failed = False
    try:
        assignment = 'assignment_test'
        due_date = '04/12/20'
        course = 'comp_sci'
        
        ### Tests that course is taught by professor
        # if this is raised course is already in usr.courses so this test is pointless
        assert course not in grading_system.usr.courses

        grading_system.usr.create_assignment(assignment, due_date, course)

        ### Tests if assignment is added
        assert grading_system.courses[course]['assignments'][assignment]['due_date'] == due_date  
        
        
    except:
        failed = True
    
    # Checks if Staff couldn't create assignment for a course they are not related to
    # If this is raise, the Staff user successfully created an assignment in a course they don't have.
    assert failed == True

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem