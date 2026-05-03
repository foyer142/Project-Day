
class User:
    def __init__(self,name,age,email,is_active):
        self.name = name
        self.age = age
        self.email = email
        self.is_active = is_active

    def is_adult(self) -> bool:
        return self.age >= 18
    
    def can_login(self) ->bool:
        return self.is_active
    
    def get_profile(self) -> str:
        return f"{self.name}, {self.age}, {self.email}"
    
class Task:
    def __init__(self,title,done=False):
        self.title = title
        self.done = done

    def mark_done(self) -> None:
        self.done = True
    
    def is_completed(self) -> bool:
        return self.done
    
    def get_info(self) -> str:
        return f"Task: {self.title}, done: {self.done}"
    
class Product:
    def __init__(self,name,price,in_stock):
        self.name = name
        self.price = price
        self.in_stock = in_stock


    def is_available(self) -> bool:
        return self.in_stock
    
    def apply_discount(self,percent: int) -> None:
        self.price = self.price * (100-percent)/100
    
    def get_info(self) -> str:
        return f"Product: {self.name}, price: {self.price}, in stock: {self.in_stock}"


def main():
    user = User("Bulat", 20, "bulat@mail.com", True)
    print(user.is_adult())
    print(user.can_login())
    print(user.get_profile())

    task = Task("Learn OOP")
    print(task.get_info())
    task.mark_done()
    print(task.is_completed())
    print(task.get_info())

    product = Product("Laptop", 1000, True)
    print(product.is_available())
    product.apply_discount(10)
    print(product.get_info())


if __name__ == '__main__':
    main()