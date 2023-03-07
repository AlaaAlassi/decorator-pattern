def custom_method_decorator(cls):
    def my_method(self):
        print("This is a custom method added by the decorator")
    cls.my_method = my_method
    return cls

@custom_method_decorator
class MyClass:
    def my_method(self):
        print("This is the original method")
    def print_stuff(self):
        self.my_method()

# Create an instance of MyClass
obj = MyClass()

# Call the original method
obj.my_method()  # Output: "This is the original method"

# Call the custom method added by the decorator
obj.my_method()  # Output: "This is a custom method added by the decorator"


obj.print_stuff()