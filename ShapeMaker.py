from enum import Enum
# shape maker: square, triangle, circle

class Shape(Enum)
    SQUARE = 1
    TRIANGLE = 2 
    CIRCLE = 3

def get_answer(mode, message):
    answered = False
    while not answered:
        try:
            answer = int(input(message))
            if mode == "Shape":
                if answer == Shape.SQUARE or answer == Shape.TRIANGLE or answer == Shape.CIRCLE:
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
    size = get_answer("Size", "How big is the shape? (x*x) ")
    return size
    
def make_square(size):
    for i in range(size):
        for j in range(size):
            print("x", end=" ")
        print()
        
def draw(shape, size):
    if shape == Shape.SQUARE:
        make_square(size)
    else:
        print("Work in progress")
    
def main():
    shape = get_shape()
    size = get_size() 
    draw(shape, size)
    
main()