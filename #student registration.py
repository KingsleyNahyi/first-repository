#student registration 
class Student():
  def register(self):   
    student_credentials = input("Put in your student name and Id: ")
    split = student_credentials.split(",")
    with open("students.csv","a") as file: 
      file.write(student_credentials+ "\n")

  def enroll(self):
    enroll_course = input("Put in your id and select course")
    cred = enroll_course.split(",")
    with open("courses.csv," "r") as file:
      courses = [line.strip().split(",")[0] for line in file]
    if cred[1] in courses:
      with open("enrollments.csv","a") as file: 
        file.write(f"{cred[0]},{cred[1]}\n")
  
  def drop(self):
    drop_course = input("Put in your id and select the course you want to drop")
    cred = drop_course.split(",")
    with open("enrollments.csv","r") as file: 
      enrollments = [line for line in file]
    updated_enrollments = [enrollment for enrollment in enrollments if enrollment!= f"{cred[0]},{cred[1]}"]


  def display(self):
    student_id = input("Put in your ID to view your schedule: ")
  
    # Load enrollments
    with open("enrollments.csv", "r") as file:
      enrollments = [line.strip().split(",") for line in file if line.strip()]
  
    # Load course details
    with open("courses.csv", "r") as file:
      course_details = {line.strip().split(",")[0]: line.strip().split(",")[1] for line in file if line.strip()}
  
    # Find and display courses for the student
    print(f"\nSchedule for student ID {student_id}:")
    found = False
    for enrollment in enrollments:
      if enrollment[0] == student_id:
        course_code = enrollment[1]
        course_name = course_details.get(course_code, "Unknown Course")
        print(f"- {course_code}: {course_name}")
        found = True
  
    if not found:
      print("No courses found for this student.")
    


class Admin():
  def add_course(self):
    add_course = input("Put in the course code, course name, max capacity")
    split = add_course.split(",")
    course = {split[0]:[split[1],int(split[2])]}
    with open("courses.csv","w") as file:
      if add_course not in file: 
        file.write(add_course)

while True:
  student_course = {}
  print("What would you like to do today\n")
  print("Type in 1 for student registration\n")
  print("Type in 2 for course management\n")
  print("Type in 3 for course enrollment\n")
  print("Type in 4 to view student schedule\n")
  print("Type in 5 to drop a course\n")
  print("Type in 6 to exit the app\n")
  master_interaction = input()
  if master_interaction=="6": 
    break 
  elif master_interaction =="1": 
    instance = Student().register()
  elif master_interaction =="2": 
    instance2 = Admin().add_course()
  elif master_interaction =="3": 
    instance3 = Student().enroll()
  elif master_interaction=="4": 
    instance4= Student().display()


