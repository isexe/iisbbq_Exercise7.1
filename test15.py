import pytest
import System

# Used to restore data
#import RestoreData

### Tests if professors can only change grades of students in their courses
def test_change_grade_requirements(grading_system):    
    # username and password
    username = 'goggins'
    password =  'augurrox'

    # Login as professor
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password
    
    # Tries to change grade of student in course not taught by prof
    failed = False  #state of test
    try:
        # Info
        student = 'akend3'
        course = 'comp_sci'
        hw = 'assignment1'
        new_grade = 0

        # Since currently change_grade is bugged, save old and compare with new
        old_grade = grading_system.users[student]['courses'][course][hw]['grade']

        #  Change grade of student enrolled in prof's class
        grading_system.usr.change_grade(student, course, hw, new_grade)

        ### Tests the if grade was changed from old_grade
        assert old_grade != grading_system.users[student]['courses'][course][hw]['grade']
    except:
        failed = True
    
    # Check that test failed and prof couldn't change grade of student
    assert failed == True




@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem