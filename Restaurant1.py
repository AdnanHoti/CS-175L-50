#CS175L
#Adnan Hoti
#Restaurant

vegetarian=input("Is anyone in your party a vegetarian? ")
vegan=input("Is anyone in your party a vegan? ")
gluten_free=input("Is anyone in your party gluten-free? ")
print("Here are your restaurant choices:")
if vegetarian=="yes" and vegan=="yes" and gluten_free=="yes":
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian=="yes" and vegan=="yes" and gluten_free=="no":
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian=="yes" and vegan=="no" and gluten_free=="yes":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian=="no" and vegan=="yes" and gluten_free=="yes":
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian=="no" and vegan=="no" and gluten_free=="yes":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")
elif vegetarian=="yes" and vegan=="no" and gluten_free=="no":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")
elif vegetarian=="no" and vegan=="yes" and gluten_free=="no":
    print("Corner Cafe")
    print("The Chef's Kitchen")
else:
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")

    

