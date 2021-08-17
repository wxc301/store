import random

# 准备数据

bank = {} # 空的数据库
bank_name = "中国工商银行昌平回龙观支行ICBC-568-01502"

def bank_addUser(account,username,password,country,province,street,door,many):
    # 是否已满
    if len(bank) > 100:
        return 3
    # 是否存在
    if account in bank:
        return 2
    # 正常开户




    bank[account] = {
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":many,
        "bank_name":bank_name

    }

    return 1

# 用户的开户操作
def addUser():
    username = input("请输入姓名：")
    password = input("请输入密码：")
    print("请输入您的个人详细地址：")
    country = input("\t\t国籍:")
    province = input("\t\t省份:")
    street = input("\t\t街道:")
    door = input("\t\t门牌号:")
    many = int(input("请输入你的初始金额："))
    # 10000000~99999999
    account = random.randint(10000000,99999999)
    status = bank_addUser(account,username,password,country,province,street,door,many)
    if status == 3:
        print("对不起，该银行用户已满，请携带证件到其他银行办理!")
    elif status == 2:
        print("对不起，该用户已开户，请不要重复开户！别瞎弄！")
    elif status == 1:
        print("恭喜正常开户！以下是您的个人信息：")
        info = '''
            ------------个人信息------------
            账号:%s
            姓名：%s
            密码：*****
            国籍：%s
            省份：%s
            街道：%s
            门牌号：%s
            余额：%s
            开户行名称：%s
        '''
        print(info % (account,username,country,province,street,door,many,bank_name))




#存钱
def saveMoney():
    account = int(input("请输入用户账号"))
    if account  in bank:
        money = int(input("请输入存款金额："))

        bank[account ]["money"] += money
    else:

        return False
#提款
def drawMoney():
    account  = int(input("请输入用户账号"))
    if account  in bank:
        password = input("请输入用户密码")
        if password == bank[account ]["password"]:
            money = int(input("请输入取款金额"))
            if money <= bank[account ]["money"]:
                bank[account ]["money"] -= money
            else:
                return 3
        else:
            return 2
    else:
        return 1
#转账
def transferAccounts():
    enter_account  = int( input("请输入转帐用户账号"))
    exit_account  = int(input("请输入你的用户账号"))
    if enter_account in bank and exit_account  in bank:
        password = input("请输入你的密码")
        if password == bank[exit_account ]["password"]:
            money = int(input("请输入转账金额"))
            if money <= bank[exit_account ]["money"]:
                bank[enter_account ]["money"] += money
                bank[exit_account ]["money"] -= money
            else:
                return 3
        else:
            return 2
    else:
        return 1
#查询
def inquire():
    account  = int(input("请输入用户账号"))
    if account  in bank:
        password = input("请输入用户密码")
        if password == bank[account]["password"]:
            print("以下是您的个人信息：")
            info = '''
                       ------------个人信息------------
                       账号：%s
                       密码：*****
                       余额：%s
                       国际：%s
                       省份：%s
                       街道：%s
                       门牌号：%s
                       当前账户的开户行：%s
                   '''
            print(info % (account, bank[account]["money"],bank[account]["country"],bank[account]["province"] , bank[account]["street"], bank[account]["door"], bank_name))

        else:
            return None
    else:
        return 1
def welcome():
    print("----------------------------------------")
    print("-        中国工商银行账户管理系统V1.0    -")
    print("----------------------------------------")
    print("- 1.开户                               -")
    print("- 2.存钱                              -")
    print("- 3.取钱                               -")
    print("- 4.转账                               -")
    print("- 5.查询                               -")
    print("- 6.Bye!                               -")
    print("-------------------------------------- -")

# 入口程序
while True:
    welcome()
    # 输入用户的业务逻辑
    chose = input("请输入您的业务：")
    if chose == "1":
        addUser()
    elif chose == "2":
        status =  saveMoney()
        if status == False:
            print("对不起，用户不存在")

    elif chose == "3":
        status = drawMoney()
        if status == 3:
            print("对不起，该用户余额不够")
        elif status == 2:
            print("对不起，该用户密码不正确")
        elif status == 1:
            print("用户不存在")
    elif chose == "4":
        status = transferAccounts()
        if status == 3:
            print("对不起，该用户余额不够")
        elif status == 2:
            print("对不起，该用户密码不正确")
        elif status == 1:
            print("用户不存在")
    elif chose == "5":
        status = inquire()
        if status == 1:
            print("对不起，不存在该用户")
        elif status == None:
            print("对不起，该用户密码错误")
    elif chose == "6":
        break
    else:
        print("对不起，别瞎弄！再弄三次锁定！")







































