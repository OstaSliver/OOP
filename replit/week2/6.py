# กําหนดให้ list x และ y เป็น list ของจํานวนเต็ม โดยมีขนาดเท่ากัน
# ให้ return list ที่เป็นผลบวกของ list x และ y โดยใช้ list comprehension
# ให้เขียนในฟังก์ชัน function ชื่อ add2list(lst1,lst2)

def add2list(lst1,lst2):
    return [lst1[i]+ lst2[i] for i in range(len(lst1))]
