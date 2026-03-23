#this program uses dictionaries and a function to store the student info and then print out the class average grades
student_grades = {
    'Kayla': 71,
    'Adam': 48,
    'Savannah': 99,
    'Kara': 37,
    }

def calculate_average_grades(student_grades):
    total = 0
    count = 0

    for student, grades in student_grades.items():
        total = total + grades
        count = count + 1 
    average = total / count

    return average

average = calculate_average_grades(student_grades)

print(f'The class average is: {average}')