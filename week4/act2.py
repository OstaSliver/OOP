# 4.2 : Student
# • โดยใช้กลุ่มเดิม ใช้ระบบ Pair Programmer คือ คนที่ 1 บอก Code ให้คนที่ 2 เขียนตามคําบอก
# โดยหากไม่เห็นด้วย สามารถทักท้วงได้
# • ให้เขียนโปรแกรม เพื่อสร้างคลาสต่อไปนี้
# – นักศึกษา (Student) โดยมี attribute : student_id, student_name
# – รายวิชา (Subject) โดยมี attribute : subject_id, subject_name, section, credit
# – ผู้สอน (Teacher) โดยมี attribute : teacher_id, teacher_name
# – สามารถเพิ่ม attribute อื่นๆ ได้
# • ให้สร้าง Instance ของทุกคลาส และ สร้างความสัมพันธ์ (สามารถเพิ่ม attribute ได้)
# – ให้สร้าง instance ของนักศึกษา 5 คนขึ้นไป
# – ให้สร้าง instance ของอาจารย์ 2 คน
# – ให้สร้าง instance ของวิชา object oriented programming 2 instance 2 section โดยแต่ละ
# section มีผู้สอนคนละคน และแต่ละ section มีคนเรียนอย่างน้อย 2 คน
# – ข้อมูลใน Instance ให้เป็นข้อมูลที่จริงจังสักหน่อย
# • ให้เขียนฟังก์ชัน #1 โดยเมื่อใส่ รหัสผู้สอน แล้วสามารถบอกได้ว่ามี นศ. คนไหนบ้างที่เรียนกับผู้สอนนี้
# โดยให้บอกเป็นชื่อนักศึกษา
# • ให้เขียนฟังก์ชัน #2 โดยเมื่อใส่ รหัส นศ. แล้วบอกว่าเรียนวิชาอะไรบ้าง โดยให้บอกเป็นชื่อวิชา
# • ข้อมูลทั้งหมดต้องอยู่ในคลาสเท่านั้น ยกเว้น List ที่เก็บ นศ. ทั้งหมด วิชาทั้งหมด อาจารย์ทั้งหมด ให้
# อยู่ข้างนอกได้ และห้ามใช้ dictionary ในการเก็บข้อมูล

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

class Subject:
    def __init__(self, subject_id, subject_name, section, credit):
        self.subject_id = subject_id
        self.subject_name = subject_name
        self.section = section
        self.credit = credit

class Teacher:
    def __init__(self, teacher_id, teacher_name):
        self.teacher_id = teacher_id
        self.teacher_name = teacher_name

def main():
    student1 = Student(66010840, "oat")
    student2 = Student(66011428, "ice")
    student3 = Student(66010843, "nat")
    student4 = Student(66011464, "tart")
    student5 = Student(66010437, "tur")

    subject1 = Subject(01076106, "OOP-16", "16", 3)
    subject2 = Subject(01076106, "OOP-17", "17", 3)

    teacher1 = Teacher(990001, "tana")
    teacher2 = Teacher(990002, "teacher2")

    subject1.student = [student1, student2]
    subject2.student = [student1, student3, student4, student5]

    subject1.teacher = teacher1
    subject2.teacher = teacher2

    def get_student(teacher_id):
        for subject in [subject1, subject2]:
            if subject.teacher.teacher_id == teacher_id:
                return [student.student_name for student in subject.student]
    
    def get_subject(student_id):
        subject_list = []
        for subject in [subject1, subject2]:
            if student_id in [student.student_id for student in subject.student]:
                subject_list.append(subject.subject_name)
        return subject_list
    
    print(subject1.teacher.teacher_name)
    print(get_student(990001))
    print(get_subject(6600001))

main()