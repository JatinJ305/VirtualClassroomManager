class VirtualClassroomManager:
    def __init__(self):
        self.classrooms={}  # Creating a dictionary for classrooms and their students

    def add_classroom(self,class_name):
        if class_name not in self.classrooms:
            self.classrooms[class_name]=[]  # We create a new classroom if it doesn't exist
            print(f"Classroom {class_name} has been created.")
        else:
            print(f"Classroom {class_name} already exists.")


    def list_classrooms(self):
        return list(self.classrooms.keys())  # Displays all the classrooms available

    def remove_classroom(self,class_name):
        if class_name in self.classrooms:
            del self.classrooms[class_name]  # Removes the specified classroom
            print(f"Classroom {class_name} has been removed.")
        else:
            print(f"Classroom {class_name} does not exist.")


    def add_student_to_class(self,student_id,class_name):
        if class_name in self.classrooms:
            if student_id not in self.classrooms[class_name]:
                self.classrooms[class_name].append(student_id)  # Adds students into the classroom
                print(f"Student {student_id} has been enrolled in {class_name}.")
            else:
                print(f"Student {student_id} is already enrolled in {class_name}.")
        else:
            print(f"Classroom {class_name} does not exist.")

    def list_students_in_class(self,class_name):
        if class_name in self.classrooms:
            return self.classrooms[class_name]  # Returns all students that are enrolled in a particular classroom
        else:
            return []  # Returns empty list if classroom doesn't exist

    def schedule_assignment(self, class_name,assignment_details):
        if class_name in self.classrooms:  # Schedule an assignment for a particular classroom
            print(f"Assignment for {class_name} has been scheduled: {assignment_details}")
        else:
            print(f"Classroom {class_name} does not exist.")

    def submit_assignment(self, student_id, class_name, assignment_details):
        if class_name in self.classrooms and student_id in self.classrooms[class_name]:
            # Assignment submissions by particular student of particular class
            print(f"Assignment submitted by Student {student_id} in {class_name}: {assignment_details}")
        else:
            print(f"Student {student_id} or Classroom {class_name} does not exist or the student is not enrolled in the class.")


if __name__=="__main__":

    manager=VirtualClassroomManager()

    while True:
        user_input=input("Enter command: ").split()
        if user_input[0] == "add_classroom":
            manager.add_classroom(user_input[1])
        elif user_input[0] == "list_classrooms":
            print("Available Classrooms:",manager.list_classrooms())
        elif user_input[0] == "remove_classroom":
            manager.remove_classroom(user_input[1])
        elif user_input[0] == "add_student":
            manager.add_student_to_class(user_input[1],user_input[2])
        elif user_input[0] == "list_students":
            students = manager.list_students_in_class(user_input[1])
            if students:
                print(f"Students in {user_input[1]}:",students)
            else:
                print(f"No students found in {user_input[1]}.")
        elif user_input[0] == "schedule_assignment":
            assignment_details = ' '.join(user_input[2:])
            manager.schedule_assignment(user_input[1],assignment_details)
        elif user_input[0] == "submit_assignment":
            assignment_details = ' '.join(user_input[3:])
            manager.submit_assignment(user_input[1],user_input[2],assignment_details)

        elif user_input[0] == "exit":
            break
        else:
            print("Invalid command.")
