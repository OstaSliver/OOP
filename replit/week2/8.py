# จากโปรแกรมในข้อ 7 ให้เขียนฟังก์ชัน เพิ่มเติมเป็น date_diff
# – รับข้อมูลในรูปแบบ “dd-mm-yyyy” เช่น
# date_diff(“1-1-2018”, “1-1-2020”) จะได้ 731 วัน
# date_diff(“25-12-1999”, “9-3-2000”) จะได้ 76 วัน
# – ให้เขียนฟังก์ชัน day_in_year โดยจะส่งค่าจํานวนวันของปี (365 หรือ 366) โดยรับข้อมูลเป็น ปี
# – ส่งคืนข้อมูลเป็นจํานวนวันตั้งแต่วันที่แรก จนถึงวันที่สอง โดยรวมทั้ง 2 วันนั้นเข้าไปด้วย
# – ให้สมมติว่าวันแรก จะต้องมาก่อนวันที่สองเสมอ ดังนั้นไม่ต้องตรวจสอบ


day_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def day_of_year(day, month, year):
    return sum(day_in_month[:month]) + day + (1 if is_leap(year) and month > 2 else 0)

def day_in_year(year):
    return 366 if is_leap(year) else 365

def date_diff(date_1, date_2):
  date_1 = list(map(int, date_1.split("-")))
  date_2 = list(map(int, date_2.split("-")))

  diff_date = 0
  diff_date += day_in_year(date_1[2]) - day_of_year(date_1.split("-")) + 1

  for year in range(date_1[2]+1, date_2[2]):
    diff_date += day_in_year(year)

  diff_date += day_of_year(date_2.split("-"))

  return diff_date

print(date_diff("1-1-2018", "1-1-2020"))
print(date_diff("25-12-1999", "9-3-2000"))  # 76