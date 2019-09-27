# Multiple objects
# Inheritence
# Operator overloading
# self  - instance variable , scope object level. to identify the object


class Account1:
    def adduser(self, n):
        self.name = n

    def viewuser(self):
        return self.name

    bank = 'ICICI'  # class variable

    @classmethod
    def bankrules(cls, area):
        return 'Brules:' + area

    @staticmethod
    def bankinfo():
        return 'bank info'

    def __init__(self):
        print('sb login here')


cust1 = Account1()
cust2 = Account1()
cust1.adduser('c1')  # adduser(cust1,'c1')
cust2.adduser('c2')


# print(cust1.viewuser(), cust2.viewuser(), cust1.name, cust2.name, Account1.bank, cust1.bank,
#       Account1.bankrules('banglore'), Account1.bankinfo(), sep='\n')


class Account2(Account1):
    def addadhar(self, a):
        self.adhar = a

    def viewadhar(self):
        return self.adhar

    def viewuser(self):
        return 'Welcome ' + self.name

    def __init__(self):
        super().__init__()
        print('CA logic here')
        Account1.__init__(self)


cust3 = Account2()
cust3.adduser('c3')
# print(cust3.viewuser(), Account2.bank, Account2.bankrules('PUNE'), Account2.bankinfo(), sep='\n')
cust3.addadhar('A1')


# print(cust3.viewadhar())


class RBI:
    def viewrules(self):
        return 'RBI rules'


class Account3(Account2, RBI):
    pass


cust4 = Account3()


# print(cust4.viewrules())


class Govt:
    def viewrules(self):
        return 'Govt rules'


class Account4(Govt, Account3):
    pass


cust5 = Account4()


# print(cust5.viewrules())
# print(Govt.viewrules(cust5))


class Accout5(Account3):
    def __init__(self):
        self.gov = Govt()


cust6 = Accout5()


# print(cust6.viewrules())
# print(cust6.gov.viewrules())
#

class Account6():
    def __init__(self, a):
        self.name = a

    def __add__(self, x):
        return 'Hello' + self.name + x.name

    def __str__(self):
        return self.name

    def __len__(self):
        return len(self.name)

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        c = self.count
        if c < len(self.name):
            self.count += 1
            return self.name[c]
        else:
            raise StopIteration


cust7 = Account6('c7')
cust8 = Account6('c8')
result = cust7 + cust8
# print('result=', result)
#
# print('cust7=', cust7)
# print('len of  cust7=', len(cust7))

# for i in cust7:
# print('i=', i)

from abc import ABC, abstractmethod


class Account(ABC):
    def adduser(self, a):
        self.name = a

    @abstractmethod
    def viewuser(self):
        pass

class MyAccount(Account):
    def viewuser(self):
        return 'Hello ' + self.name

b=MyAccount()
b.adduser('XYZ')
print(b.viewuser())
# a = Account()
