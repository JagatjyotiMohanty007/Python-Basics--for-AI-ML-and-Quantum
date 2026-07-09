class Car:

    def __init__(self, brand):
        self.brand = brand

    def show(self):
        print("Brand:", self.brand)

if __name__ == "__main__":
    c = Car("BMW")
    c.show()