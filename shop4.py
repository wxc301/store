'''
    商城：
        1.初始化钱包余额
        2.推个空的购物车
        3.正常购物：
            输入商品的编号
            看是否有这个商品
                有：
                    看钱是否足够
                        够：
                            添加到购物车里
                            余额减去相对应的钱
                        不够：
                            温馨：穷鬼，别瞎弄！请买个其他商品
                没有：
                    买个其他商品，别瞎弄！
        4.打印购物小条
    任务：
        1.购物小条的商品重复打印问题
        2.  10张联想电脑 0.5，  20老干妈优惠券 0.1 ， 15 华为优惠券 0.6
            随机抽取一张优惠券，在结算的时候进行打折，进行结算。
'''
import random
shop = [
    ["lenovo PC",5000],
    ["Mac pc",12000],
    ["HUAWEI  WATCH PRO 20",2000],
    ["机械革命",15000],
    ["老干妈",7.5],
    ["卫龙辣条",3],
    ["西瓜",2]
]
# 1.空的购物车
mycart = []

#  2.初始化您的余额
money = input("请输入您本月工资：")
money = int(money)
#  2.1 10张联想电脑 0.5/1，  20老干妈优惠券 0.1/2 ， 15 华为优惠券 0.6/3
#             随机抽取一张优惠券，在结算的时候进行打折，进行结算。

note = random.randint(0,90)
if note in [1,2,3,4,5,6,0,7,8,9,10]:
    print("你抽到联想电脑优惠券")

elif note in [11,12,13,14,15,16,17,18,19,20,31,32,34,33,35,36,37,38,39,40]:
    print("你抽到老干妈优惠券")

elif note in [61,62,63,64,65,66,67,68,69,70,84,85,86,87,88]:
    print("你抽到华为优惠券")

else:
    print("你没有抽到优惠券")


# 3.正常购物
i = 1
while i <= 20:
    # 展示商品
    for key, value in enumerate(shop):
        print(key, value)
    chose = input("请输入您想要的商品：")
    if chose.isdigit():
        chose = int(chose)
        if chose > len(shop): # len
            print("没有改号商品！请重新输入！")
        else:
            # 钱够不够
            if money > shop[chose][1]:
                if chose == 0 :
                    money = money - shop[0][1]*0.5
                elif chose == 4:
                    money = money - shop[4][1]*0.1
                elif chose == 2:
                    money = money - shop[2][1]*0.6
                else:
                    money = money - shop[chose][1] # 减去价格
                mycart.append(shop[chose])

                print("恭喜，添加成功！您的余额还剩",money)
            else:
                print("穷鬼，钱不够了，别瞎弄！买其他商品吧！")
    elif chose == "q" or chose == "Q":
        print("欢迎下次光临！")
        break  # 跳出循环
    else:
        print("对不起，您输入错误，别瞎弄！")
    i = i + 1
print("以下是您的购物小条，请拿好！")
print("---------------------------------------")
print('商品   数量    单价   打折前总价')
for i in range(len(shop)):
    j = mycart.count(shop[i])
    if j > 0:
        print(shop[i][0], '\t', j, '\t', shop[i][1], '\t', j * shop[i][1])
print("---------------------------------------")
print("您的余额还剩：￥",money)


































