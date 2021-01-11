# 面向对象

# 类封装 飞机 坐标 宽高 移动
class Plane():
    # 必须定义构造方法
    def __init__(self,x,y,width,heigh):
        #super(Plane,self).__init__()  调用父类
        self.x = x
        self.y = y
        self.w = width
        self.h = heigh
    # 功能方法
    def move(self,step):
        self.x = self.x + step

# 对象的使用
p1 = Plane(0,0,100,100)
print(p1.x)
for item in range(10):
    p1.move(10)
    print(p1.x)

# 继承
# 定义 敌机 继承飞机
class Emey(Plane):
    def __init__(self,x,y,width,heigh):
        # 调用父类的构造方法
        super(Emey,self).__init__(x,y,width,heigh)
    
    #发射子弹
    def shoot(self):
        print("射击")

e = Emey(10,10,100,100)
print(e.x)
e.move(1000)
print(e.x)