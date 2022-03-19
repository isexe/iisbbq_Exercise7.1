import pytest
import System

# Used to restore data
#import RestoreData

### Tests if instructor can only drop_students from their own courses
def test_drop_student_requirements(grading_system):
    # Test user and password
    username = 'goggins'
    password =  'augurrox'

    # Login as professor
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Tries to remove student from course that prof doesn't teach
    failed = False
    try:
        student = 'akend3'
        course = 'comp_sci'
        
        ### Tests that course is not taught by professor
        assert course not in grading_system.usr.courses
        
        grading_system.usr.drop_student(student, course)

        ### Tests if student is removed
        for key in grading_system.users[student]['courses']:
            assert key != course
    except:
        failed = True
    
    # Checks if prof was able to removed student from course they do not instruct
    # If this raises then the activity was completed when it shouldn't have
    assert failed == True
        
        

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem