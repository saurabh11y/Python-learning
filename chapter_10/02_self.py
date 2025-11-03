class employee:
    language = "python"  # this is a class attribute
    salary = 1790000
    
    def getinfo(self):
        print(f"the language is {self.language},the salary is{self.salary } ")


shaurya = employee()
# shaurya.name = "shaurya"  # this is an object attribute
shaurya.getinfo()
# print(shaurya.salary,shaurya.language)