
students = []

def add_student():
    name= input("Enter student name: ")
    age= int(input("Enter student age: "))

    math= float(input("Enter marks in Math: "))
    english= float(input("Enter marks in English:"))     
    science= float(input("Enter marks in Science: "))

    student={
        "name": name,
        "age": age,
        "math": math,
        "english": english,
        "science": science
    } 

    students.append(student)

    print(f"Student {name} added successfully!")

def view_students():
    if len(students)== 0:
        print("No students found.")
        return
    print("List of Students:")

    for i, student in enumerate(students, start =1):
        print(
            i,
            student["name"],
            "| Age:", student["age"],
            "| Math:", student["math"],
            "| English:", student["english"],
            "| Science:", student["science"]
        )   

def search_student():
     name= input("Enter student name to search: ")
     found= False
     for student in students: 
         if student["name"].lower() == name.lower():
             print("Student found:")
             print("\nName:", student["name"])
             print("Age:", student["age"])
             print("Math:", student["math"])
             print("English:", student["english"])
             print("Science:", student["science"])

             found= True
             break
     if not found:
        print("Student not found.")

def calculate_average():
   name= input("Enter student name to calculate average: ")
    
   for student in students:
        if student["name"].lower() == name.lower():

             total=student["math"]+ student["english"]+ student["science"]

             average = total / 3
             print("Average marks for", student["name"], "is:", average)

             if average >= 90:
                print("Grade: A")
             elif average >= 80:
                print("Grade: B")
             elif average >= 70:
                print("Grade: C")
             elif average >= 60:
                 print("Grade: D")
             elif average < 60:
                 print("Grade: F")
             else:
                 print("Grade E. ")

def highest_scorer():
    if len(students)==0:
        print("No students found.")
        return
    highest_student= students[0]

    for student in students:
        current_total = (
            student["math"]
            + student["english"]
            + student["science"]
        )

        highest_total= (
            highest_student["math"]
            + highest_student["english"]
            + highest_student["science"]
        )

        if current_total > highest_total:
            highest_student= student

    print("Highest Scorer:")
    print("Name:", highest_student["name"])

    total = (
        highest_student["math"]
       + highest_student["english"]
        + highest_student["science"]
    )

    print("Total Marks:", total)            
    print("Math:", highest_student["math"])

        
while True:
    print("Student Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate average and Grade")
    print("5. Find Highest scorer")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice== "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        calculate_average()
    
    elif choice == "5": 
        highest_scorer()
    
    elif choice == "6":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

