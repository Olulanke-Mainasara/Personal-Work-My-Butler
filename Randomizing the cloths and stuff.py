import random
'''
food = random.choice(["beans", "bread", "egg", "amala", "krokro"])
toppings = random.choice(["chicken", "fish", "gizzard", "snail"])
drink = random.choice(["fanta", "water", "sprite", "wine", "tea"])
print(food + " " + toppings + " " + drink)


float = [12, 23, 24, 45, 34, 67]
flozz = random.shuffle(float)
print(float)
'''

whichcolourdict = {"a": "Red", "b": "Orange", "c": "Yellow", "d": "Green", "e": "Light Blue", "f": "Dark Blue", "g": "Black", "h": "White", "i": "Pink", "j": "Purple", "k": "Beige", "l": "Brown", "m": "Grey", "n": "Wine"}
whichcolour = input("\nWhich colour has been given?\n(a) Red\n(b) Orange\n(c) Yellow\n(d) Green\n(e) Light Blue\n(f) Dark Blue\n(g) Black\n(h) White\n(i) Pink\n(j) Purple\n(k) Beige\n(l) Brown\n(m) Grey\n(n) Wine\nYour answer: ")

if whichcolour == "a":
    topcolour = whichcolourdict[whichcolour]
    bottomcolour = random.choice(["Mustard yellow", "Pink", "Silver", "Camel", " Light Blue", "Army Green", "Grey", "White", "Tawny-Orange", "Black", "Dark Blue", "Beige"])
    shoecolour = whichcolourdict[whichcolour]

    topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
    bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
    footwear = random.choice(["Flat shoe", "Designer shoe", "Flashy shoe", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])

    print("\nYour matchup is: ")
    print("\n" + topclothing + " " + "=" + " " + topcolour)
    print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
    print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour)