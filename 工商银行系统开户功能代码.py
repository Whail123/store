print("==============================================")
print("|------------中国工商银行账户管理系统------------|")
print("|------------1、开户              ------------|")
print("|------------2、取钱              ------------|")
print("|------------3、存钱              ------------|")
print("|------------4、转账              ------------|")
print("|------------5、查询              ------------|")
print("|------------6、退出              ------------|")
print("==============================================")
import random
def zidingyihanshu2(zhanghao,xingming,mima,dizhi,kaihuhang,guojia,shengfen,jiedao,menpaihao):
    zidian={}
    zidian_name="工商银行起码路分行"
    if len(zidian)>100:return 3
    if xingming in zidian:return 2
    zidian[xingming]={"zhanghao": zhanghao,"mima": mima,"guojia": guojia,"shengfen": shengfen,"jiedao": jiedao,
        "menpaihao": menpaihao,
        "zidian_name":zidian_name
    }
    print(zidian)
    return 1#返回，送回 1
 def zidingyihanshu1():
      zhanghao=random.randint(11111111,111111111)
      xingming=input("请输入姓名")
     mima=input("请输入密码")
      dizhi=input("请输入地址")
      kaihuhang=input("中国工商银行北京起码路分行")
      guojia=("请输入国家")
     shengfen=("请输入省份")
     jiedao=("请输入街道")
     menpaihao=("请输入门牌号")
 zidingyihanshu2=123(zhanghao,xingming,mima,dizhi,kaihuhang,guojia,shengfen,jiedao,menpaihao)
if zidingyihanshu2 == 1:
    print("恭喜你开户成功下面是你的信息")
    info = '''
                ------------个人信息------------
                用户名:%s
                账号:%s
                密码:*****
                国籍:%s
                省份:%s
                街道:%s
                门牌号:%s
                余额:%s
                开户行:%s
            '''
    print(info % (xingming, zhanghao, mima, guojia, shengfen, menpaihao, zidian[xingming], zidian_name))


 while True:
    a=input("请选择需要办理的业务")
    if a == "1":
        print("1、开户")
        zidingyihanshu1()#调用你在def中创建的函数
    elif  a == "2":
        print("2、取钱")
    elif  a == "3":
        print("3、存钱")
    elif  a == "4":
        print("4、转账")
    elif  a == "5":
        print("5、查询 ")
    elif  a == "6":
        print("6、退出")
        break#跳出整个循环