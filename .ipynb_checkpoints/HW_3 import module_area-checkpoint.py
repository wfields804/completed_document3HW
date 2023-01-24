

def square_footage():
    length_2 = []
    width_2 = []
    area = length_2 * width_2

    #How to multiply the list in "area"
    length = input("What is the length ? ")
    if length :
        length_2.append(length)
    while True:
        width = input("What is the width ? ")
        if width :
            width_2.append(width)
        break   
    print(area)

square_footage()



    
