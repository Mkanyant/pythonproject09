class IoTThailand :
    #data
    wow = 100
    wea = ''
 
    # construtor ไม่ใช่ nimber แต่จะทำงานทุกครั้งที่มีการสร้าง object
    def __init__(self, woo, wee, wea):
        self.woo = woo
        self.wee = wee
        self.wea = wea
 
    #method
    def showData(salf) :
        print(salf.wow * 20)

    #dest
    def __del__(self):
        print('Good morning Teacher...')

 
 
ob1 = IoTThailand(10, 20, 10)
ob2 = IoTThailand(10, 20, 30)
ob3 = IoTThailand(5, 20, 10)
ob4 = IoTThailand(10, 20, 10)
 
print(ob1.wea + ob2.wea)
print(ob3.showData())
