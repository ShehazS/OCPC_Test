class name:
    
    def __init__(self,name,age,phone,email,password,address):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.password = password
        self.address = address

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
    def get_password(self):
        return self.password
    
    def get_address(self):
        return self.address

    def great(self):
        return f"Hello, my name is {self.name} and i am {self.age}"
    
class __main__:
    obj = name("shehaz",20,91211939,"shehaz.zubair@gmail.com",123456789,"Al Salam Street")
    name = obj.get_name()
    age = obj.get_age()
    phone = obj.get_phone()
    email = obj.get_email()
    password = obj.get_password()
    address = obj.get_address()
    greeting = obj.great()
    print(name,age,phone,email,password,address)
    print(greeting)