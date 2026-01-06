class Account:
    def __init__(self,acc_No,acc_Pass):
        self.acc_No = acc_No
        self.__acc_Pass = acc_Pass

    def res_Pass(self):
        print(self.__acc_Pass)

account =Account(123456,"abcdef")

print(account.acc_No)
print(account.res_Pass())
