import pytest
import System

# Used to restore data
#import RestoreData

### Tests if the submit_assignment from Student.py works as intended
def test_submit_assignment(grading_system):
    # Test user and password
    username = 'akend3'
    password =  '123454321'

    # Login as student
    grading_system.login(username,password)

    ### Tests correct user login
    assert grading_system.usr.name == username
    assert grading_system.usr.password == password

    # Submits an assignment as a student
    course = 'databases'
    assignment = 'assignment1'
    submission = 'asdf'
    date = '3/19/22'
    grading_system.usr.submit_assignment(course, assignment, submission, date)

    # Tests if the assignment submission was changed for the student
    assignment_info = grading_system.users[username]['courses'][course][assignment]
    due_date = grading_system.courses[course]['assignments'][assignment]['due_date']
    assert assignment_info['submission_date'] == date
    assert assignment_info['submission'] == submission
    assert assignment_info['ontime'] == grading_system.usr.check_ontime(date, due_date)
    

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem