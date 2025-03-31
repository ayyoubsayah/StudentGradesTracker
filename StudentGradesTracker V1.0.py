# Dictionary to store student names and their grades
students = {
    "Karim": (85, 90, 78),
    "Ali": (92, 88, 95),
    "Fatima": (70, 80, 65)
}

# Function to print students and their grades
def print_students():
    print("\n📌 Students and their grades:")
    for name, grades in students.items():
        print(f"👉 {name}: {grades}")

# Function to calculate and print average grades
def print_averages():
    print("\n📊 Averages:")
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        print(f"📌 {name}: {avg:.2f}")

# Function to add a new student
def add_student():
    name = input("\n✏️ Enter student name: ")
    grades = tuple(map(int, input("📚 Enter three grades separated by spaces (e.g. 85 90 78): ").split()))
    students[name] = grades
    print(f"✅ {name} added successfully!")

# Main program
print("🎓 Welcome to the Student Grades Tracker!\n")

while True:
    print_students()
    print_averages()

    add_student()  # Allow the user to add a student

    # Ask if they want to continue
    cont = input("\n🔄 Do you want to add another student? (yes/no): ").strip().lower()
    if cont != "yes":
        # 🛠 FIX: Print the final updated student list before exiting
        print_students()
        print_averages()
        print("\n👋 Exiting program. Have a great day!")
        break
