def my_decorator(obj):
    class NewClass(type(obj)):
        def my_new_method(self):
            self.old_my_method() # Call the original method using self parameter
            print("This is a new method added by the decorator")

    # Create a new method with a different name
    setattr(NewClass, 'new_my_method', NewClass.my_new_method)

    # Set the original method to be an alias for the new method
    setattr(NewClass, 'my_method', NewClass.new_my_method)
    
    # Save a reference to the old my_method
    setattr(NewClass, 'old_my_method', obj.my_method)

    obj.__class__ = NewClass
    return obj