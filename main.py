from my_class import MyClass
from my_decorator import my_decorator

# Create an instance of MyClass
obj = MyClass()

# Apply the decorator to the instance of MyClass
obj = my_decorator(obj)

# Call the original method and the new method added by the decorator
obj.my_method()        # This is a new method added by the decorator

