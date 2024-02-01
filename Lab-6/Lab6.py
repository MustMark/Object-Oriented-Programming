class Bank:
    def __init__(self, name):
        self.__name = name
        self.__user_list = []
        self.__account_list = []
        self.__card_list = []
        self.__atm_list = []
    
    def add_user_list(self,user):
        self.__user_list.extend(user)

    def add_account_list(self,account):
        self.__account_list.extend(account)

    def add_card_list(self,card):
        self.__card_list.extend(card)

    def add_atm_list(self,atm):
        self.__atm_list.extend(atm)

class User:
    def __init__(self, id_number, name):
        self.__id_number = id_number
        self.__name = name
        self.__account_list = []

    def add_account_list(self, account):
        self.__account_list.append(account)

class Account:
    def __init__(self, owner, id_account, balance):
        self.__owner = owner
        self.__id_account = id_account
        self.__balance = balance
        self.__limit_per_day = 40000
        self.__transaction_list = []
        self.__card = None

    @property
    def balance(self):
        return self.__balance
    
    @property
    def limit_per_day(self):
        return self.__limit_per_day
    
    @property
    def transaction_list(self):
        return self.__transaction_list
    
    @property
    def card(self):
        return self.__card
    
    @card.setter
    def card(self, input_card):
        self.__card = input_card

    def deposit(self, input_money, id_atm):
        self.__balance += input_money
        self.__transaction_list.append(Transaction("D", input_money, "date", id_atm, self.balance, None))

    def withdraw(self, input_money, id_atm):
        self.__balance -= input_money
        self.__limit_per_day -= input_money
        self.__transaction_list.append(Transaction("W", input_money, "date", id_atm, self.balance, None))

    def transfer(self, to_account, input_money, id_atm):
        self.__balance -= input_money
        to_account.__balance += input_money
        self.__limit_per_day -= input_money
        self.__transaction_list.append(Transaction("T", input_money, "date", id_atm, self.balance, to_account))
        to_account.__transaction_list.append(Transaction("T", f"+{input_money}", "date", id_atm, to_account.__balance, None))

class Card:
    def __init__(self, owner, card_no, pin_number):
        self.__owner = owner
        self.__card_no = card_no
        self.__pin_number = pin_number

    @property
    def owner(self):
        return self.__owner
    
    @property
    def pin_number(self):
        return self.__pin_number
    
    def card_free(self):
        self.__owner.balance -= 150

class ATM:
    def __init__(self, id_atm, balance):
        self.__id_atm = id_atm
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, money):
        self.__balance = money
    
    @property
    def id_atm(self):
        return self.__id_atm
    
    def insert_card(self, input_bank, input_card, input_pin):
        if input_bank == MBANK and input_card in card_list and input_pin == input_card.pin_number:
            return input_card.owner
        return None
    
    def deposit(self, input_account, input_money):
        if input_money <= 0 or not isinstance(input_account, Account):
            return "error"
        else:
            input_account.deposit(input_money, self.id_atm)
            self.__balance += input_money
            return "success"

    def withdraw(self, input_account, input_money):
        if input_money <= 0 or input_money > input_account.balance or input_money > self.__balance or not isinstance(input_account, Account) or input_money > input_account.limit_per_day:
            return "error"
        else:
            input_account.withdraw(input_money, self.id_atm)
            self.__balance -= input_money
            return "success"
        
    def transfer(self, from_account, to_account, input_money):
        if input_money <= 0 or input_money > from_account.balance or not isinstance(from_account, Account) or not isinstance(to_account, Account) or input_money > from_account.limit_per_day:
            return "error"
        else:
            from_account.transfer(to_account, input_money, self.id_atm)
            return "success"

class Transaction:
    def __init__(self, transaction_type, amount, date, atm, total_balance, to_id_account):
        self.__transaction_type = transaction_type
        self.__amount = amount
        self.__date = date
        self.__atm = atm
        self.__total_balance = total_balance
        self.__to_id_account = to_id_account
    
    def __str__(self):
        return f"{self.__transaction_type}-ATM:{self.__atm}-{self.__amount}-{self.__total_balance}"

def create_instance():
    bank = Bank("MBANK")
    user_list.append(User(id_list[0], user[id_list[0]][0]))
    user_list.append(User(id_list[1], user[id_list[1]][0]))
    account_list.append(Account(user_list[0], user[id_list[0]][1], user[id_list[0]][2]))
    account_list.append(Account(user_list[1], user[id_list[1]][1], user[id_list[1]][2]))
    user_list[0].add_account_list(account_list[0])
    user_list[1].add_account_list(account_list[1])
    card_list.append(Card(account_list[0], user[id_list[0]][3], "1234"))
    card_list.append(Card(account_list[1], user[id_list[1]][3], "1234"))
    account_list[0].card = card_list[0]
    account_list[1].card = card_list[1]
    atm_list.append(ATM(atm_id_list[0], atm[atm_id_list[0]]))
    atm_list.append(ATM(atm_id_list[1], atm[atm_id_list[1]]))
    bank.add_user_list(user_list)
    bank.add_account_list(account_list)
    bank.add_card_list(card_list)
    bank.add_atm_list(atm_list)
    return bank

# กำหนดรูปแบบของ user ดังนี้ {รหัสประชาชน : [ชื่อ, หมายเลขบัญชี, จำนวนเงิน, หมายเลข ATM]}
# *** Dictionary นี้ ใช้สำหรับสร้าง user และ atm instance เท่านั้น
user = {'1-1101-12345-12-0':['Harry Potter','1234567890', 20000, '12345'],
       '1-1101-12345-13-0':['Hermione Jean Granger','0987654321', 1000 ,'12346']}

atm = {'1001' : 1000000, '1002' : 200000}

id_list = [id for id in user]
atm_id_list = [atm_id for atm_id in atm]
user_list = []
account_list = []
card_list = []
atm_list = []
MBANK = create_instance()

# Test case #1 : ทดสอบ การ insert บัตร ที่เครื่อง atm เครื่องที่ 1 โดยใช้บัตร atm ของ harry
# และ Pin ที่รับมา เรียกใช้ function หรือ method จากเครื่อง ATM 
# ผลที่คาดหวัง : พิมพ์ หมายเลขบัตร ATM อย่างถูกต้อง และ หมายเลข account ของ harry อย่างถูกต้อง
# Ans : 12345, 1234567890, Success
print("Test case #1")
print(atm_list[0].insert_card(MBANK, card_list[0], "1234"))

# Test case #2 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 1000 บาท
# ให้เรียกใช้ method ที่ทำการฝากเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนฝาก หลังฝาก และ แสดง transaction
# Hermione account before test : 1000
# Hermione account after test : 2000
print("Test case #2")
print("Hermione account before test :", account_list[1].balance)
print(atm_list[1].deposit(atm_list[1].insert_card(MBANK, card_list[1], "1234"), 1000))
print("Hermione account after test :", account_list[1].balance)

# Test case #3 : ทดสอบฝากเงินเข้าในบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน -1 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #3")
print(atm_list[1].deposit(atm_list[1].insert_card(MBANK, card_list[1], "1234"), -1))

# Test case #4 : ทดสอบการถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 500 บาท
# ให้เรียกใช้ method ที่ทำการถอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน และ แสดง transaction
# Hermione account before test : 2000
# Hermione account after test : 1500
print("Test case #4")
print("Hermione account before test :", account_list[1].balance)
print(atm_list[1].withdraw(atm_list[1].insert_card(MBANK, card_list[1], "1234"), 500))
print("Hermione account after test :", account_list[1].balance)

# Test case #5 : ทดสอบถอนเงินจากบัญชีของ Hermione ในเครื่อง atm เครื่องที่ 2 เป็นจำนวน 2000 บาท
# ผลที่คาดหวัง : แสดง Error
print("Test case #5")
print(atm_list[1].withdraw(atm_list[1].insert_card(MBANK, card_list[1], "1234"), 2000))

# Test case #6 : ทดสอบการโอนเงินจากบัญชีของ Harry ไปยัง Hermione จำนวน 10000 บาท ในเครื่อง atm เครื่องที่ 2
# ให้เรียกใช้ method ที่ทำการโอนเงิน
# ผลที่คาดหวัง : แสดงจำนวนเงินในบัญชีของ Harry ก่อนถอน หลังถอน และ แสดงจำนวนเงินในบัญชีของ Hermione ก่อนถอน หลังถอน แสดง transaction
# Harry account before test : 20000
# Harry account after test : 10000
# Hermione account before test : 1500
# Hermione account after test : 11500
print("Test case #6")
print("Harry account before test :", account_list[0].balance)
print("Hermione account before test :", account_list[1].balance)
print(atm_list[1].transfer(atm_list[1].insert_card(MBANK, card_list[0], "1234"),account_list[1] , 10000))
print("Harry account after test :", account_list[0].balance)
print("Hermione account after test :", account_list[1].balance)

# Test case #7 : แสดง transaction ของ Hermione ทั้งหมด 
# กำหนดให้เรียกใช้ method __str__() เพื่อใช้คำสั่งพิมพ์ข้อมูลจาก transaction ได้
# ผลที่คาดหวัง
# Hermione transaction : D-ATM:1002-1000-2000
# Hermione transaction : W-ATM:1002-500-1500
# Hermione transaction : T-ATM:1002-+10000-11500
print("Test case #7")
for transaction in account_list[1].transaction_list:
    print(transaction)