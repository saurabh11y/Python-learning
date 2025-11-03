class Father:
    def f_show(self):
        print("Father class")

class Mother:
    def m_show(self):
        print("Mother class")

class Child(Father, Mother):
    def c_show(self):
        print("Child class")

obj = Child()
obj.f_show()
obj.m_show()
obj.c_show()
