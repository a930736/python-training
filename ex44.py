class Parent(object):
    def implicit(self):
        print("PARENT")

    def override(self):
        print("PARENT override()")

    def altered(self):
        print("PARENT ALTERED")



class Child(Parent):
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, before PARENET altered")
        super(Child,self).altered()
        print("CHILD, after")
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
