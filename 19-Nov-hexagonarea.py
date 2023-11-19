def hexagon_area(side):
    area= (3/2)*(side**2)*(3**0.5)
    return area

s=int(input("Enter length of hexagon edge in cms: "))
area=hexagon_area(s)
print("Area of hexagon of side ",s,"is", area)
