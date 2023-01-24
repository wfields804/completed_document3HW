

def square_footage():
    length_2 = []
    width_2 = []
    

    #How to multiply the list in "area"
    length = int(input("What is the length ? "))
    if length :
        length_2.append(length)
    
    width = int(input("What is the width ? "))
    if width :
        width_2.append(width)
    area = length_2[0] * width_2[0]
    print(area)

square_footage()






def circumference():
    radius_2 = []
    pi = 3.14

    radius = int(input("Whats is the radius ? "))
    if radius:
        radius_2.append(radius)
    
    circumfrance_2 = radius_2[0] * pi
    print(circumfrance_2)

circumference()

    


    
