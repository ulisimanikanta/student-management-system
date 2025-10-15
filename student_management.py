

import os


DATA_FILE = "students.txt"


def load_students():
    students = {}
    if not os.path.exists(DATA_FILE):
        return students
    with open(DATA_FILE, "r") as f:
        for line in f:
            roll, name, marks = line.strip().split("|")
            students[roll] = {"name": name, "marks": marks}
    return students

# Function to save students to file
def save_students(students):
    with open(DATA_FILE, "w") as f:
        for roll, info in students.items():
            f.write(f"{roll}|{info['name']}|{info['marks']}\n")

# Add new student
def add_student(students):
    roll = input("Enter Roll Number: ").strip()
    if roll in students:
        print(" Roll number already exists!")
        return
    name = input("Enter Student Name: ").strip()
    marks = input("Enter Marks: ").strip()
    students[roll] = {"name": name, "marks": marks}
    save_students(students)
    print("✅ Student added successfully!")

# View all students
def view_students(students):
    if not students:
        print(" No student records found.")
        return
    print("\n--- Student Records ---")
    print(f"{'Roll No.':<10}{'Name':<20}{'Marks'}")
    print("-" * 40)
    for roll, info in students.items():
        print(f"{roll:<10}{info['name']:<20}{info['marks']}")
    print("-" * 40)

# Search student by roll or name
def search_student(students):
    keyword = input("Enter Roll No. or Name to Search: ").strip().lower()
    found = False
    for roll, info in students.items():
        if keyword == roll.lower() or keyword in info['name'].lower():
            print(f" Found: Roll={roll}, Name={info['name']}, Marks={info['marks']}")
            found = True
    if not found:
        print(" No matching student found.")

def update_student(students):
    roll = input("Enter Roll Number to Update: ").strip()
    if roll not in students:
        print(" Student not found!")
        return
    print(f"Current Name: {students[roll]['name']}")
    new_name = input("Enter New Name (leave blank to keep current): ").strip()
    print(f"Current Marks: {students[roll]['marks']}")
    new_marks = input("Enter New Marks (leave blank to keep current): ").strip()
    if new_name:
        students[roll]['name'] = new_name
    if new_marks:
        students[roll]['marks'] = new_marks
    save_students(students)
    print("✅ Student updated successfully!")

def delete_student(students):
    roll = input("Enter Roll Number to Delete: ").strip()
    if roll not in students:
        print("❌ Student not found!")
        return
    confirm = input(f"Are you sure you want to delete {students[roll]['name']}? (y/n): ").strip().lower()
    if confirm == 'y':
        del students[roll]
        save_students(students)
        print("🗑️ Student deleted successfully!")
    else:
        print("❌ Deletion cancelled.")

def menu():
    students = load_students()
    while True:
        print("\n📚 Student Management System")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-6.")

# Run the program
if __name__ == "__main__":
    menu()
