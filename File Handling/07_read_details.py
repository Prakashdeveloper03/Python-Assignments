import json


def read_data():
    try:
        with open("files/faculty.json", "r") as file:
            return json.load(file)
    except Exception:
        return []


def write_data(data):
    with open("files/faculty.json", "w") as file:
        json.dump(data, file)


def add_faculty(faculty_id, name, department, designation):
    data = read_data()
    faculty = {
        "faculty_id": faculty_id,
        "name": name,
        "department": department,
        "designation": designation,
    }
    data.append(faculty)
    write_data(data)
    print("Faculty added successfully\n")


def delete_faculty(faculty_id):
    data = read_data()
    for i, faculty in enumerate(data):
        if faculty["faculty_id"] == faculty_id:
            del data[i]
            write_data(data)
            print("Faculty deleted successfully\n")
            return
    print("Faculty not found\n")


def update_faculty(faculty_id, name, department, designation):
    data = read_data()
    for i, faculty in enumerate(data):
        if faculty["faculty_id"] == faculty_id:
            data[i]["name"] = name
            data[i]["department"] = department
            data[i]["designation"] = designation
            write_data(data)
            print("Faculty updated successfully\n")
            return
    print("Faculty not found\n")


def display_faculty(faculty_id=None):
    data = read_data()
    if faculty_id:
        for faculty in data:
            if faculty["faculty_id"] == faculty_id:
                print(faculty)
                return
        print("Faculty not found\n")
    else:
        for faculty in data:
            print(faculty)
        print()


def menu():
    while True:
        print("1. Add faculty")
        print("2. Delete faculty")
        print("3. Update faculty")
        print("4. Display faculty")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            faculty_id = input("Enter faculty id: ")
            name = input("Enter name: ")
            department = input("Enter department: ")
            designation = input("Enter designation: ")
            add_faculty(faculty_id, name, department, designation)
        elif choice == 2:
            faculty_id = input("Enter faculty id: ")
            delete_faculty(faculty_id)
        elif choice == 3:
            faculty_id = input("Enter faculty id: ")
            name = input("Enter name: ")
            department = input("Enter department: ")
            designation = input("Enter designation: ")
            update_faculty(faculty_id, name, department, designation)
        elif choice == 4:
            faculty_id = input("Enter faculty id (leave blank to display all): ")
            display_faculty(faculty_id)
        elif choice == 5:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    menu()
