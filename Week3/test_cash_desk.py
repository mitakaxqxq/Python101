import unittest

from cash_desk import Bill,BatchBill,CashDesk

class TestBillClass(unittest.TestCase):
    def test_bill_with_negative_amount(self):

        exc = None
        try:
            Bill(-12)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'The amount can not be negative number')

    def test_bill_when_amount_is_not_int(self):
        
        exc = None
        try:
            Bill(2.2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'The type of ammount has to be int')

    def test_str_method(self):

        a = Bill(10)
        result = str(a)
        self.assertEqual(result,'A 10$ bill')

    def test_add_method(self):

        a = Bill(10)
        b = Bill(20)
        result = a + b
        self.assertEqual(result,Bill(30))

    def test_int_method(self):

        a = Bill(10)
        result = int(a)
        self.assertEqual(result,10)

    def test_when_two_bills_are_equal(self):

        a = Bill(10)
        b = Bill(10)
        self.assertTrue(a == b, 'The bills are equal')

    def test_when_two_bills_are_different(self):

        a = Bill(10)
        b = Bill(5)
        self.assertFalse(a == b, 'The bills are different')

    def test_when_a_bill_is_added_to_a_dictionary(self):

        a = Bill(10)
        b = Bill(10)

        myDict = {}

        myDict[a]=1

        if b in myDict:
            myDict[b] += 1

        self.assertEqual(myDict[b],2)

class TestBatchBill(unittest.TestCase):
    def test_batchbill_with_wrong_type_of_bills(self):
        
        exc = None
        try:
            BatchBill((1,2,3,4))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Argument of batch bill must be list')


    def test_get_the_length_of_bills_in_batchbill(self):

        values = [5,10,20,20,50,50,100]

        bills = [Bill(value) for value in values]
        batchbill1 = BatchBill(bills)

        result = 7
        self.assertEqual(result,len(batchbill1))

    def test_batchbill_getitem_method(self):

        values = [10,20,50,100]

        bills = [Bill(value) for value in values]
        batchbill1 = BatchBill(bills)

        result = Bill(50)

        self.assertEqual(result,batchbill1[2])
    
    def test_get_amount_of_all_bills_in_a_batchbill(self):
        values = [10,20,50,100]

        bills = [Bill(value) for value in values]
        batchbill1 = BatchBill(bills)
        
        self.assertEqual(batchbill1.total(),180)

class TestCashDesk(unittest.TestCase):

    def test_take_money_when_parameter_is_of_wrong_type(self):

        desk = CashDesk()
        exc = None
        try:
            desk.take_money([1,3,2])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'The parameter has to be of type Bill or BatchBill')


    def test_take_money_when_adding_a_single_bill(self):

        desk = CashDesk()

        expectedDict = {Bill(10):1}

        self.assertEqual(expectedDict,desk.take_money(Bill(10)))

    def test_take_moeny_when_adding_a_batch_bill(self):

        expectedDict = {Bill(10):1,Bill(20):1,Bill(50):1,Bill(100):3}

        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]

        batch = BatchBill(bills)

        desk = CashDesk()

        self.assertEqual(expectedDict,desk.take_money(batch))

    
    def test_find_total_amount_of_money_in_the_bank(self):

        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]

        batch = BatchBill(bills)

        desk = CashDesk()

        desk.take_money(batch)
        desk.take_money(Bill(10))
        print(desk.inspect())

        self.assertEqual(desk.total(),390)

    def test_check_if_inspect_function_prints_in_the_correct_order_cash_desk(self):

        values = [10, 20, 50, 100, 100, 100]
        bills = [Bill(value) for value in values]

        batch = BatchBill(bills)

        desk = CashDesk()

        desk.take_money(batch)
        desk.take_money(Bill(10))

        expectedString = 'We have a total of 390$ in the desk\nWe have the following count of bills, sorted in ascending order:\n10$ bills - 2\n20$ bills - 1\n50$ bills - 1\n100$ bills - 3\n'
        result = desk.inspect()

        self.assertEqual(expectedString,result)

if __name__ == '__main__':
    unittest.main()