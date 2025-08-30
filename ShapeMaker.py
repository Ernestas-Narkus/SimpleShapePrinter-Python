from enum import Enum
# shape maker: square, triangle, circle

class Shape(Enum):
    SQUARE = 1
    TRIANGLE = 2 
    CIRCLE = 3

def get_answer(mode, message):
    answered = False
    while not answered:
        try:
            answer = int(input(message))
            if mode == "Shape":
                if answer == Shape.SQUARE.value or answer == Shape.TRIANGLE.value or answer == Shape.CIRCLE.value:
                    answered = True
                else:
                    print("Pick one of the options")
            elif mode == "Size":
                answered = True
            else:
                print("Weird")
        except ValueError:
            print("Please use an integer")
    return answer
    
def get_shape():
    shape = get_answer("Shape", "Which shape do you want to draw? Square(1), Triangle(2), Circle(3) ")
    return shape
        
def get_size():
    size = get_answer("Size", "How big is the shape? (height) ")
    return size
    
def make_square(size):
    for i in range(size):
        for j in range(size):
            print("x", end=" ")
        print()
        
def make_triangle(size):
    for i in range(size):
        for j in range(size - i - 1):
            print(" ", end="")
        for k in range((i*2)+1):
            print("x", end="")
        print()
            
            
        
def draw(shape, size):
    if shape == Shape.SQUARE.value:
        make_square(size)
    elif shape == Shape.TRIANGLE.value:
        make_triangle(size)
    else:
        print("Work in progress")
    
def main():
    shape = get_shape()
    size = get_size() 
    draw(shape, size)
    
main()