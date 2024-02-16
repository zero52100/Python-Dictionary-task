def student(student_name, Parents_detail):
    student_combined = student_name.copy()
    student_combined.update(Parents_detail)
    return student_combined
Student_detail= {'student_name': "John", 'Class': 6}
Parents_detail= {'father_name': 'Ali','Mother_name':'Fathima' ,'Contact_no': '911234512345'}
result = student(Student_detail, Parents_detail)
print("Student detail:", result)
