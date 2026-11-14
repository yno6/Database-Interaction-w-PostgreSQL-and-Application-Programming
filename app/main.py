#psycopg2 is the library that lets Python talk to PostgreSQL.
import psycopg2

#connection settings for PostgreSQL setup
DB_CONFIG = {
    "dbname": "database_name",      #the name of the database you created in pgAdmin (for me it's A3_Q1)
    "user": "postgres",             #the PostgreSQL username (postgres is the default)
    "password": "your_password",    #the password set when installing PostgreSQL
    "host": "localhost",            #"localhost" means the database is on this same computer
    "port": "5432",                 #the port PostgreSQL listens on (5432 is the default)
}

def get_connection():
    #Opens and returns a connection to the PostgreSQL database
    return psycopg2.connect(**DB_CONFIG)

#READ - fetches every row from the students table and prints it
def getAllStudents():
    conn = get_connection()         #open the connection to the database
    cur = conn.cursor()             #the cursor is the tool that sends SQL commands and gets results back
    cur.execute("SELECT * FROM students ORDER BY student_id;") #ask for all students, sorted by ID
    for row in cur.fetchall():      #fetchall() returns every row we asked for
        print(row)                  #printing one student per line
    cur.close()                     #put the cursor away when finished
    conn.close()                    #close the connection to the database

#CREATE - inserts a new student
def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_connection()         #open the connection
    cur = conn.cursor()             #make a cursor to send the command and get back results
    # The %s are placeholders, Python fills them in safely with the values in the brackets below, in the same order. 
    # This protects against SQL injection (someone sneaking harmful SQL into the input)
    # We don't give student_id cause the database creates it automatically
    cur.execute(
        "INSERT INTO students (first_name, last_name, email, enrollment_date) "
        "VALUES (%s, %s, %s, %s);",
        (first_name, last_name, email, enrollment_date),
    )
    conn.commit()                   #saves the change permanently, without commit, the change will NOT be saved
    cur.close()                     #put the cursor away
    conn.close()                    #close the connection to the database

#UPDATE - changes the email of the student with the given ID
def updateStudentEmail(student_id, new_email):
    conn = get_connection()          
    cur = conn.cursor()          
    #SET changes the email. WHERE makes sure only the student with this ID is changed
    #Without WHERE, every student would get the same email
    cur.execute(
        "UPDATE students SET email = %s WHERE student_id = %s;",
        (new_email, student_id),
    )
    conn.commit()                   
    cur.close()                 
    conn.close()                    

#DELETE - removes the student with the given ID
def deleteStudent(student_id):
    conn = get_connection()
    cur = conn.cursor()
    #WHERE makes sure only this one student (with the speficied student_id) is deleted
    #The comma in (student_id,) is needed because Python wants a tuple here, even when there is only one value
    cur.execute("DELETE FROM students WHERE student_id = %s;", (student_id,))
    conn.commit()
    cur.close()
    conn.close()

#This block only runs when we run this program using python main.py
#For demo purposes
if __name__ == "__main__":
    #show the starting data (the 3 students from schema.sql)
    print("All students:");            
    getAllStudents()

     #ADD a new student, then print again to see them appear
    addStudent("Alice", "New", "alice.new@gmail.com", "2026-11-11")
    print("After adding Alice:");      
    getAllStudents()

    #UPDATE/change the email of the student with ID 1 (John), then print again to check if it worked
    updateStudentEmail(1, "john.new@gmail.com")
    print("After updating email:");    
    getAllStudents()

    #DELETE the student with ID 3 (Jim) from the database, then print again to check if it worked
    deleteStudent(3)
    print("After deleting student 3:"); 
    getAllStudents()
