from child_class import Child


class GrandChildClass(Child):
    def __init__(self, name, age, address):
        Child.__init__(self, name, age)
        self.address = address

    def get_address(self):
        return self.address


obj = GrandChildClass('Ivan Ivanov', 50, 'Sofia')
print(obj.get_name(), obj.get_age(), obj.get_address())
