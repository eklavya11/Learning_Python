print("Enter number of students:")
N = int(input())
students_grade = []
for i in range(N):
    print("Enter student name:")
    student = input()
    print("Enter student grade:")
    grade = float(input())
    students_grade.append([student,grade]) 

min_grade = students_grade[0][1]

student_len = len(students_grade)
min_student = []

for i in range(student_len):
    if students_grade[i][1]<=min_grade:
        min_student = students_grade[i]
        
students_grade.remove(min_student)     

second_min_grade = students_grade[0][1]
second_min_student = []

for i in range(len(students_grade)):
    if students_grade[i][1]<=second_min_grade:
        second_min_student =students_grade[i]
        
second_lowest_students = [second_min_student]


for i in range(len(students_grade)):
    if ((students_grade[i][1] == second_lowest_students[0][1])
       & (students_grade[i][0] != second_lowest_students[0][0])):
        second_lowest_students.append(students_grade[i])
        
second_lowest_students.sort()

for students in second_lowest_students:
    print(students[0])
        
       
    
        
