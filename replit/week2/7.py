# ให้เขียน function ชื่อ day_of_year(day, month ,year)
# โดยมีการคืนค่า คือ day_of_years เป็นวันที่ลําดับที่เท่าใดของปีคริสตศักราช year
# – ปีที่เป็น Leap Year เดือนกุมภาพันธ์จะมี 29 วัน
# – ให้สร้างฟังก์ชัน is_leap เพื่อตรวจสอบ leap year แยกออกมา และให้ฟังก์ชัน day_of_year
# เรียกใช้ is_leap อีกที

day_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
    return sum(day_in_month[:month]) + day + (1 if is_leap(year) and month > 2 else 0)
    
day, month, year = map(int, input().split())
print(day_of_year(day, month, year))