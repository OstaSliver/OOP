# Class Code

# class diagram
# bank
# 	-User_list
# 	-ATM_list
# 	+add_User()
# 	+get_User()
# 	+add_ATM()
# 	+get_ATM()

# User
# 	-Citizen Id
# 	-Name
# 	-Account_list
# 	+add_account()
# 	+get_account()

# ATM
# 	-ATM ID
# 	-balance
# 	+insent_card()
# 	+deposit()
# 	+withdraw()
# 	+transfer()

# Account
# 	-User[obj]
# 	-Account_id
# 	-balance
# 	-transaction_list
# 	-ATM_Card

# ATM_Card
# 	-Account_id
# 	-Pin Number

# Transaction
# 	-balance
# 	-timestamp
# 	-ATM_id
# 	-transfer_account
# 	-amount


# bank<>--User
# bank<>--ATM

# Account--User
# Account-->ATM_Card
# Account-->Transaction

##################################################################################

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, หมายเลข ATM, จำนวนเงิน ]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น
user ={'1-1101-12345-12-0':['Harry Potter','1234567890','12345',20000],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321','12346',1000]}

atm ={'1001':1000000,'1002':200000}

class Bank:
       def __init__(self):
              self.__user_list = []
              self.__atm_list = []
              
       def add_user(self,user):
              self.__user_list.append(user)
       
       def add_atm(self,atm):
              self.__atm_list.append(atm)
              
       def get_user(self):
              return self.__user_list
              
       def get_atm(self):
              return self.__atm_list
       
class User:
       def __init__(self,citizen_id,name):
              self.__citizen_id = citizen_id
              self.__name = name
              self.__account_list = []
              
       def add_account(self,account):
              self.__account_list.append(account)
              
       def get_account(self):
              return self.__account_list
       
class ATM:
       def __init__(self,atm_id,balance):
              self.__atm_id = atm_id
              self.__balance = balance

       def insert_card(self,bank,atm_card,pin):
              for user in bank.get_user():
                     for account in user.get_account():
                            if account.get_atm_card().account_id == atm_card.account_id and account.get_atm_card().pin == pin:
                                   return account
              return None
                            
       def deposit(self,account,amount):
              if amount > 0:
                     account.balance += amount
                     account.transaction_list.append(Transaction('D',account.balance,self.__atm_id,amount))
                     return 'Success'
              else:
                     return 'Error'
       def withdraw(self,account,amount):
              if amount > 0 and amount <= account.balance:
                     account.balance -= amount
                     account.transaction_list.append(Transaction('W',account.balance,self.__atm_id,-amount))
                     return 'Success'
              else:
                     return 'Error'
              
       def transfer(self,account,transfer_account,amount):
              if amount > 0 and amount <= account.balance:
                     account.balance -= amount
                     account.transaction_list.append(Transaction('T',account.balance,self.__atm_id,-amount,transfer_account))
                     transfer_account.balance += amount
                     transfer_account.transaction_list.append(Transaction('TT',transfer_account.balance,self.__atm_id,amount,account))
                     return 'Success'
              else:
                     return 'Error'
class Account:
       def __init__(self,user,account_id,balance):
              self.__user = user
              self.__account_id = account_id
              self.__balance = balance
              self.__atm_card = None
              self.__transaction_list = []
              
       def add_atm_card(self,atm_card):
              self.__atm_card = atm_card
              
       def get_atm_card(self):
              return self.__atm_card
       
       def __str__(self):
              return f'{self.__account_id} {self.__balance}'
       
class ATM_Card:
       def __init__(self,account_id,pin):
              self.__account_id = account_id
              self.__pin = pin


class Transaction:
       def __init__(self,type_tran,balance,atm_id,amount,transfer_account = None):
              self.__type_tran
              self.__balance = balance
              self.__atm_id = atm_id
              self.__amount = amount
              self.__transfer_account
              
       def __str__(self):
              
              if self.type_tran == 'D':
                     return f'D-ATM:{self.__atm_id}-{self.__amount}-{self.__balance}'
              elif self.type_tran == 'W':
                     return f'W-ATM:{self.__atm_id}{self.__amount}-{self.__balance}'
              elif self.type_tran == 'T':
                     return f'T-ATM:{self.__atm_id}-{self.__amount}-{self.__balance}'
              elif self.type_tran == 'TT':
                     return f'T-ATM:{self.__atm_id}-+{self.__amount}-{self.__balance}'
# TODO 1 : จากข้อมูลใน user ให้สร้าง instance จากข้อมูล Dictionary
# TODO :   key:value โดย key เป็นรหัสบัตรประชาชน และ value เป็นข้อมูลของคนนั้น ประกอบด้วย
# TODO :   [ชื่อ, หมายเลขบัญชี, หมายเลขบัตร ATM, จำนวนเงินในบัญชี]
# TODO :   return เป็น instance ของธนาคาร
# TODO :   และสร้าง instance ของเครื่อง ATM จำนวน 2 เครื่อง

def add_data(user,atm):
       bank_temp = Bank()
       for key,value in user.items():
              user_temp = User(key,value[0])
              account_temp = Account(user_temp,value[1],value[3])
              atm_card_temp = ATM_Card(value[2],value[2])
              account_temp.add_atm_card(atm_card_temp)
              user_temp.add_account(account_temp)
              bank_temp.add_user(user_temp)

       for key,value in atm.items():
              atm_temp = ATM(key,value)
              bank_temp.add_atm(atm_temp)

       return bank_temp

bank = add_data(user,atm)

# TODO 2 : เขียน method ที่ทำหน้าที่สอดบัตรเข้าเครื่อง ATM มี parameter 3 ตัว ได้แก่ 1) instance ของธนาคาร
# TODO     2) instance ของ atm_card 3) entered Pin ที่ user input ให้เครื่อง ATM
# TODO     return ถ้าบัตร และ Pin ถูกต้องจะได้ instance ของ account คืนมา ถ้าไม่ถูกต้องได้เป็น None
# TODO     ควรเป็น method ของเครื่อง ATM



# TODO 3 : เขียน method ที่ทำหน้าที่ฝากเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้เพิ่มจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0


#TODO 4 : เขียน method ที่ทำหน้าที่ถอนเงิน โดยรับ parameter 2 ตัว คือ 
# TODO     1) instance ของ account 2) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชี และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


#TODO 5 : เขียน method ที่ทำหน้าที่โอนเงิน โดยรับ parameter 3 ตัว คือ 
# TODO     1) instance ของ account ตนเอง 2) instance ของ account ที่โอนไป 3) จำนวนเงิน
# TODO     การทำงาน ให้ลดจำนวนเงินในบัญชีตนเอง และ เพิ่มเงินในบัญชีคนที่โอนไป และ สร้าง transaction ลงในบัญชี
# TODO     return หากการทำรายการเรียบร้อยให้ return success ถ้าไม่เรียบร้อยให้ return error
# TODO     ต้อง validate การทำงาน เช่น ตัวเลขต้องมากกว่า 0 และ ไม่ถอนมากกว่าเงินที่มี


# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success

print('\nTest case #1 :')
atm_1 = bank.get_atm()[0]
account = atm_1.insert_card(bank,ATM_Card('12345','12345'),'12345')
if account != None:
       print(account.get_atm_card().account_id,account.account_id,'Success')
else:
       print('Fail')

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000

print('\nTest case #2 :')
atm_2 = bank.get_atm()[1]
account = atm_2.insert_card(bank,ATM_Card('12346','12346'),'12346')
print('Hermione account before test :',account.balance)
atm_2.deposit(account,1000)
print('Hermione account after test :',account.balance)

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error

print('\nTest case #3 :')
atm_2 = bank.get_atm()[1]
account = atm_2.insert_card(bank,ATM_Card('12346','12346'),'12346')
print('Hermione account before test :',account.balance)
print(atm_2.deposit(account,-1))
print('Hermione account after test :',account.balance)

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500

print('\nTest case #4 :')
atm_2 = bank.get_atm()[1]
account = atm_2.insert_card(bank,ATM_Card('12346','12346'),'12346')
print('Hermione account before test :',account.balance)
atm_2.withdraw(account,500)
print('Hermione account after test :',account.balance)

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error

print('\nTest case #5 :')
atm_2 = bank.get_atm()[1]
account = atm_2.insert_card(bank,ATM_Card('12346','12346'),'12346')
print('Hermione account before test :',account.balance)
print(atm_2.withdraw(account,2000))
print('Hermione account after test :',account.balance)


# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500

print('\nTest case #6 :')
atm_2 = bank.get_atm()[1]
account = atm_2.insert_card(bank,ATM_Card('12345','12345'),'12345')
print('Harry account before test :',account.balance)
account_hermione = atm_2.insert_card(bank,ATM_Card('12346','12346'),'12346')
print('Hermione account before test :',account_hermione.balance)
atm_2.transfer(account,account_hermione,10000)
print('Harry account after test :',account.balance)
print('Hermione account after test :',account_hermione.balance)



# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print('\nTest case #7 :')

for transaction in account_hermione.transaction_list:
       print('Hermione transaction :',transaction)