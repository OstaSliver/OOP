# ให้เขียนโปรแกรมเพื่อรับ string 1 ตัว
# ให้ส่งคืนเฉพาะตัวอักษรที่เป็นภาษาอังกฤษ โดยใช้ List comprehension
# ให้เขียนในฟังก์ชัน only_english(string1) แล้ว return เป็นคําตอบเป็น string

def only_english(string1):
    return ''.join([i for i in string1 if i.isalpha() and i.isascii()])

string1 = input()
print(only_english(string1))