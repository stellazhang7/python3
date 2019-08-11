def judge_student(student_name, student):
    if student_name in student:
        print(student_name, 'is in the set')
    else:
        print(student_name, 'is not in the set')

student = {'tom', 'jim', 'tom', 'jack', 'rose'}
student_name = "stella"
judge_student(student_name, student)


