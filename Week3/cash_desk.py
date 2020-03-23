class Bill:
    def __init__(self,amount):
        if amount < 0:
            raise ValueError('The amount can not be negative number')
        if not isinstance(amount,int):
            raise TypeError('The type of ammount has to be int')
        self.amount = amount
    
    def __str__(self):
        return f'A {self.amount}$ bill'

    def __repr__(self):
        return f'A {self.amount}$ bill'

    def __int__(self):
        return int(self.amount)

    def __eq__(self,other):
        return self.amount == other.amount

    def __add__(self,other):
        return Bill(self.amount+other.amount)

    def __lt__(self,other):
        return self.amount<other.amount

    def __hash__(self):
        return hash(self.amount)

class BatchBill:
    def __init__(self,bills):
        if not isinstance(bills,list):
            raise TypeError('Argument of batch bill must be list')
        self.bills=bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self,index):
        return self.bills[index]

    def total(self):
        s = 0
        for bill in self.bills:
            s += bill.amount
        return s

class CashDesk:
    def __init__(self):
        self.totalAmount={}

    def take_money(self,money):
        if not (isinstance(money,Bill) or isinstance(money,BatchBill)):
            raise TypeError('The parameter has to be of type Bill or BatchBill')
        if isinstance(money,Bill):
            if money in self.totalAmount.keys():
                self.totalAmount[money] += 1
            else:
                self.totalAmount[money] = 1
        if isinstance(money,BatchBill):
            for bill in money:  
                if bill in self.totalAmount.keys():
                    self.totalAmount[bill] += 1
                else:
                    self.totalAmount[bill] = 1
        return self.totalAmount

    def total(self):
        finalSum = 0
        for bill in self.totalAmount.keys():
            finalSum += bill.amount * self.totalAmount[bill]
        return finalSum

    def inspect(self):
        myStr = 'We have a total of ' + str(self.total()) + '$ in the desk\n' + 'We have the following count of bills, sorted in ascending order:\n'
        for i in sorted(self.totalAmount.keys()):
            myStr += str(i.amount)
            myStr += '$ bills - '
            myStr += str(self.totalAmount.get(i))
            myStr += '\n'
        return myStr