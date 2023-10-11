from school import School,Classroom,Subject
from Persons import Student,Teacher
def main():
    school = School('adamjee','uttara')

    eight = Classroom('eight')
    school.add_classroom(eight)
    nine=Classroom('nine')
    school.add_classroom(nine)
    ten=Classroom('ten')
    school.add_classroom(ten)

    abul = Student('Abul',eight)
    school.student_admission(abul)
    Babul = Student('Babul',eight)
    school.student_admission(Babul)
    kabul = Student('kabul',eight)
    school.student_admission(kabul)


  
    physics_teacher = Teacher('Shahjahan Tapan')
    physics= Subject('physics',physics_teacher)
    eight .add_subject(physics)

    chemistry_teacher = Teacher('haradon nag')
    chemistry= Subject('chemistry',chemistry_teacher)
    eight .add_subject(chemistry)

    biology_teacher = Teacher('amal hasan')
    biology= Subject('biology',biology_teacher)
    eight .add_subject(biology)

    eight.take_semester_final()

    print(school)


if __name__=='__main__':
    main()