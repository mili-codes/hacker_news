class Cordinate:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:

    def __init__(self, c1, c2):
        '''creating the rectangle based on the two diagonal corners coordinates 
        C1 and C2(corners)'''

        self.right_edge = max(c1.x, c2.x)
        self.left_edge = min(c1.x, c2.x)
        self.top_edge = max(c1.y, c2.y)
        self.bottom_edge = min(c1.y, c2.y)  


def test_overlap(rectangle1, rectangle2):
    '''determins if the given rectangles overlap'''

    horizontal_overlap = True
    verticle_overlap = True
    if (rectangle1.right_edge <= rectangle2.left_edge) or (rectangle1.left_edge >= rectangle2.right_edge):
        horizontal_overlap = False
    if (rectangle1.top_edge <= rectangle2.bottom_edge) or (rectangle1.bottom_edge >= rectangle2.top_edge):
        verticle_overlap = False
    
    if horizontal_overlap and verticle_overlap :
        print("Rectangles overlap")
    else:
        print("Rectanges do not overlap")


c1 = Cordinate(1,1)
c2 = Cordinate(4,4)
rectangle1 = Rectangle(c1,c2)
c3 = Cordinate(2,3)
c4 = Cordinate(3,4)
rectangle2 = Rectangle(c3,c4)

test_overlap(rectangle1,rectangle2)

test_overlap(rectangle2, rectangle1)
    
c5 = Cordinate(3,3)
c6 = Cordinate(6,7)
rectangle3 = Rectangle(c5, c6)

test_overlap(rectangle2, rectangle3)
test_overlap(rectangle1, rectangle3)

var = (1,2,4,5).to_set
