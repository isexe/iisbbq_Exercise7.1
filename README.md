# Exercise 07.1 - Construction and Testing
## CMP_SC 4320 Software Engineering
###Isaac Sexe - iisbbq

All of these tests are ran with pytest.  Make sure that all of the tests are in the same directory as the systems files such as: System.py, User.py, Student.py, Staff.py, TA.py, Professor.py, RestoreData.py, and the Data folder with the database json files inside them.  While running the tests, please be sure to run RestoreData.py every so often as some of the test may cause conflict with each other if they alter the database.  The original [README.md](./ExerciseInfo/README_Exercise.md) and various other informational files can be found in the folder [ExerciseInfo](./ExerciseInfo/) if you have any questions on set-up or other aspects of the exercise.

### Test 1: login - [System.py](./System.py)

Pass
    The funciton login() logs in the specified user.  User logged in matches the provided username and password.

### Test 2: check_password - [System.py](./System.py)

Pass
    The function check_password() accepts the password of the user.  Only the one predefined password can authenticate the user, no alternatives work.

### Test 3: change_grade - [Staff.py](./Staff.py)

Fail - AssertionError
    The function change_grade() failed to correctly chang the grade of the student.  The new grade in the function is hard coded as 0 so any attempt to change the grade of an assignment will always result in the new grade being 0

### Test 4: create_assignment - [Staff.py](./Staff.py)

Pass - ?
    The function create_assignment() creates an assignment in the courses database.  The assignment was correctly added to the courses database with the correct due_date.  Side note, currently the students don't have access to the newly created assignments.  Because of this it may be considered failed, but with the verification requirements listed I've decided it passed.

### Test 5: add_student - [Professor.py](./Professor.py)

Fail - KeyError
    The function add_student() failed to added a new student to a course.  The function would try to add the course to the staff user's courses rather than the student user.

### Test 6: drop_student - [Professor.py](./Professor.py)

Pass
    The function drop_student() drops a student from a specified course.  This function correctly drops a student from the course specified by the Professor user

### Test 7: submit_assignment - [Student.py](./Student.py)

Fail - ?
    The function submit_assignment() tries to submit an assignment for a student user.  The function almost works properly but has the due_date set to a due_date from an assignment in 'comp_sci'.  Since this is hard coded in the due_date for calculating ontime is wrong.  Although this function failed, no error is raised since check_ontime() doesn't work as intended.

### Test 8: check_ontime - [Student.py](./Student.py)

Fail - AssertionError
    The function check_ontime() fails to see if a submission date is ontime by comparing it to the due date.  This function literally does nothing and always returns true.  It should be abundantly clear why this function fails to operate correctly.

### Test 9: check_grades - [Student.py](./Student.py)

Pass
    The function check_grades() checks the grades of a specified course for a student user.  These grades are returned in a 2d list that for each element has the assignment name in index 0 and the grade in index 1.  These assignments are correctly organized and have their cooresponding grades returned to the correct user.

### Test 10: view_assignments - [Student.py](./Student.py)

Fail - AssertionError
    The function view_assignments() fails to returned the correct assignments the student user asked for.  This function always returns the 'comp_sci' assignments for the student user instead of the given course.  Because the course is hard coded this function fails to return the correct assignments to the user.

### Test 11: drop_student - [Professor.py](./Professor.py)

Fail - AssertionError
    This test checks if the professor can only drop a student from courses they instruct.  This test fails because the professor can drop any student from any specified course whether they instruct it or not.

### Test 12: created_assignment - [Staff.py](./Staff.py)

Fail - AssertionError
    This test checks if the Staff user can only create assignments for courses they instruct.  This test fails because the Staff user successfully created a new assignment for a course they do not have.

### Test 13: login - [System.py](./System.py)

Fail - AssertionError
    This test checks if the database can't be access by a user until they've logged in.  This is for security reasons as they will have access to usernames and passwords the system if the database can be access directly before logging in.  This test fails because the user was able to access the database, look for an Professor user, and then log in with their credentials.

### Test 14: check_grades - [Staff.py](./Staff.py)

Fail - AssertionError
    This test checks if a Staff user can only check the grades of a Student user in their courses.  This test fails because the Staff user can input any Student user and any course and the function returns the grades of them.

### Test 15: change_grade - [Staff.py](./Staff.py)

Fail - AssertionError
    This test checks if a Staff user can only change the grades of Students in their courses.  This test fails because the Staff user can change the grades of any studented for any course.
