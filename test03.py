#คุณสมบัติ OOP : Excapsulation
class MytestA :
    __datal = 10
    Data2 = 20

    def __init__(self, data3) :
        self.__data3 = data3

    def showData(self) :
        print(f'__data1 มีค่า {self.__datal}')
        print(f'data2 มีค่า {self.data2}')
        print(f'__data3 มีค่า {self.__data3}')
        print('----------------------------')

ob1 = MytestA
ob1.showData()
ob1.Data2 = 200
ob1.__datal= 100
ob1.showData()