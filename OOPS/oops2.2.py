class car:
 wheels =5 # class variable or static variable
 def __init__(self):
    self.mil =10 # instance variable
    self.com ='BMW' # insance variable
c1 = car()
c2 = car()
c1.wheels =6

print(c1.com, c1.mil)
print(c2.com, c2.mil)
print(c1.wheels,c1.com,c1.mil)