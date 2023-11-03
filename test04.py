#คุณสมบัติเด่น oop : Interitanc สืบทอด
#คือ คลาสหนึ่งสืบทอดอีกคลาสหนึ่ง (มีแม่ super/มีลูก sub)
#พอเป็นแม่ลูกกัน แม่มีอะไรลูกมีด้วย
class TestA :
    data1 = 10
    data2 = 20

    def showSAU() :
        print('Hi......SAU')

class TestB(TestA) :
    data3 = 30

    def showWow() :
        print('Wow wow wow')

class TestC(TestA) :
    data4 = 40

class TestD(TestB) :
    data5 = 50

ob1 = TestA()
ob2 = TestB()
ob3 = TestD()

class TestZ(TestA) :
    data6 = 60

    def showSAU():
        print('Hello..........SAU')

ob4 = TestZ