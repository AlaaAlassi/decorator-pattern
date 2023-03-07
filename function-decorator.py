import turtle

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        if 'height' in kwargs:
            kwargs['height'] = kwargs['height'] * 10
        if 'width' in kwargs:
            kwargs['width'] = kwargs['width'] * 10
        return func(*args, **kwargs)
    return wrapper

class Drawing:
    def __init__(self):
        self.canvas = turtle.Screen()
        self.turtle = turtle.Turtle()

    @log_decorator
    def draw_rectangle(self, x, y, width, height):
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.pendown()
        for i in range(2):
            self.turtle.forward(width)
            self.turtle.right(90)
            self.turtle.forward(height)
            self.turtle.right(90)
        self.turtle.penup()

drawing = Drawing()
drawing.draw_rectangle(0, 0, width=50, height=25)
