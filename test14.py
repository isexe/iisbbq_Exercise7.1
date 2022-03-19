import pytest
import System

# Used to restore data
#import RestoreData

### Tests if professors can only check grades of students in their courses
def test_check_grades_requirements(grading_system):    
    # username and password
    username = 'goggins'
    password =  'augurrox'

    # Login as professor
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password
    
    # Tries to check grades of student in course not taught by prof
    failed = False  #state of test
    try:
        

        # Checks grades of student
        student = 'akend3'
        course = 'comp_sci'
        grades = grading_system.usr.check_grades(student, course)

        # Checks if the results are correct
        assign_index = 0
        assignments = grading_system.users[student]['courses'][course]
        for key in assignments:
            # Checks assignmnet name
            assert key == grades[assign_index][0]
            # Checks assignment grade
            assert assignments[key]['grade'] == grades[assign_index][1]
            assign_index += 1
        
        assert course != grading_system.usr.courses
    except:
        failed = True
    
    # Check that test failed an prof couldn't view grades of student
    assert failed == True




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem