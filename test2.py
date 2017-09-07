class Base1:
    def foo1(self):
        print(1)

class Base2:
    def foo2(self):
        print("2")

class C(Base1,Base2):
    pass

c=Base1()
c.foo1()
