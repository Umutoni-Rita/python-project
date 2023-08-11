import sqlite3

conn = sqlite3.connect('Students.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS students(
            stId INTEGER PRIMARY KEY autoincrement, 
            fname VARCHAR(100), lname VARCHAR(100),
            school VARCHAR(100), grade VARCHAR(10))''')

print("Welcome to Student Management System!! Choose your option to continue")
def gradeStudent(grade_v):
    if (grade_v <= 100 and grade_v >= 90):
        grade = 'A'
    elif(grade_v <= 89 and grade_v >= 75):
        grade = 'B'
    elif(grade_v <= 74 and grade_v >= 60):
        grade = 'C'
    elif(grade_v <= 59 and grade_v >= 50):
        grade = 'D'
    elif(grade_v <= 49 and grade_v >= 35):
        grade = 'F'
    else:
        grade = 'F--'
    return grade

def createStudent(): 
    fname = input("Enter your first name: ")
    lname = input("Enter your last name: ")
    school = input("Enter your school: ")
    grade_value = int(input("Enter your marks: "))

    grade = gradeStudent(grade_value)

    cur.execute('''INSERT INTO students 
                (fname, lname, school, grade) 
                VALUES
                (?, ?, ?, ?)''', (fname, lname, school, grade))
    print("Your grade is ", grade)

    conn.commit()
    cur.close

def viewStudents():
    data = cur.execute("SELECT * FROM students ORDER BY grade ASC")
    for row in data:
        print(row)

def updateInfo():
    stId = int(input("Enter id of the student to update"))
    grade_value = int(input("Enter new marks: "))
    school = input("Enter new school: ")
    grade = gradeStudent(grade_value)

    cur.execute(''' UPDATE students
                SET grade = ?, school = ?
                WHERE stId = ?''', (grade, school, stId))
    conn.commit()
    print("Student info updated successfully!")

def deleteStudent():
    stId = int(input("Enter id of the student to delete"))
    confirm = input("Confirm record deletion (y/n)")
    if confirm == 'y':
        cur.execute("DELETE FROM students WHERE stId = ?", (stId,))
        conn.commit()
        print("Record deleted successfully!")
    elif confirm == 'n':
        print("Student record was not deleted")
    else:
        print('Invalid input')


while True:
    print("1. Create a student \n2. View list students \n3. Update a student \n4. Delete a student \n5. Exit")
    option = input("Your option: ")

    if option == '1':
        createStudent()
    elif option == '2':
        viewStudents()
    elif option == '3':
        updateInfo()
    elif option == '4':
        deleteStudent()
    elif option == '5':
        break
    else:
        print("Invalid option")

cur.close()




