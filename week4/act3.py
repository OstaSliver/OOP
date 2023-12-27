# 4.3 : พี่รหัส
# • ให้แก้ไขคลาส student โดยเพิ่มข้อมูล พี่รหัส (student_menter) หมายถึงนักศึกษาที่เป็นพี่รหัสขึ้นไป 1
# ชั้นปีเท่านั้น
# • ให้สร้าง instance ของ นศ. 4 คนขึ้นไป เช่น a เป็นปี 1, b เป็นปี 2 และเป็นพี่รหัสของ a
# c เป็นปี 3 และเป็นพี่รหัสของ b ส่วน d เป็นปี 4 และเป็นพี่รหัสของ c การสร้าง Instance ให้ใช้รหัส
# นักศึกษา 8 หลัก และเลข 2 ตัวแรกตามชั้นปีจริง
# – ให้เขียนฟังก์ชัน #3 โดยเมื่อป้อนรหัสนักศึกษา x แล้วตอบว่ามีพี่รหัส เป็นใครบ้าง โดยให้
# ตอบให้ครบ เช่น ถ้าป้อน a ให้ตอบ b, c, d ถ้าป้อน b ให้ตอบ c, d โดยให้แสดงทั้งรหัส
# นักศึกษาและชื่อ ในการแสดงให้แสดงกรณีไม่มีพี่รหัสด้วย
# – ให้เขียนฟังก์ชัน #4 โดยเมื่อป้อนรหัสนักศึกษา Student x และ student y ให้ตรวจสอบว่าเป็น
# สายรหัสกันหรือไม่ ให้ตอบเป็น True และ False

class Student:
    def __init__(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_menter = None

    def set_student_menter(self, student_menter):
        self.student_menter = student_menter

    def get_student_menter(self):
        return self.student_menter

def recursive(student, ans):
    if student.get_student_menter() is not None:
        ans.append(student.get_student_menter())
        recursive(student.get_student_menter(), ans)
    return ans

def get_list_student_menter(student, ans):
    recursive(student, ans)
    if ans == []:
        return "No student menter"
    return [student.student_name +" "+ student.student_id for student in ans]

def is_same_menter(student1, student2):
    student_mentors1 = recursive(student1, [])
    student_mentors2 = recursive(student2, [])
    if student2 in student_mentors1 or student1 in student_mentors2:
        return True
    else:
        return False

def main():
    a = Student('01-66010840', "oat")
    b = Student('02-66011428', "Ice")
    c = Student('03-66010843', "Nat")
    d = Student('04-66011464', "tart")

    a.set_student_menter(b)
    b.set_student_menter(c)
    c.set_student_menter(d)

    print(get_list_student_menter(b, []))
    print(get_list_student_menter(d ,[]))
    print(is_same_menter(a, b))
    print(is_same_menter(c, a))
main()
