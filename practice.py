class ParentClass():
    def print_hello(self):
        self.print_child_hello(self)


class ChildClass(ParentClass):
    def print_child_hello(self):
        print("hello")


parentIns = ParentClass()
parentIns.print_hello()
