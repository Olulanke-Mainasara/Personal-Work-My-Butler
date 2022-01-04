import random


# This is the function for the colour randomising.
def colourcombo():
    if whichcolour == "a":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Mustard yellow", "Pink", "Silver", "Camel", " Light Blue", "Army Green", "Grey", "White", "Tawny-Orange", "Black", "Dark Blue", "Beige"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "b":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Mustard yellow", "Pink", "Silver", "Camel", " Light Blue", "Army Green", "Grey", "White", "Tawny-Orange", "Black", "Dark Blue", "Beige"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "c":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Dark Blue", "White", "Black", "Beige", "Green"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "d":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Orange", "Light Blue", "White", "Purple", "Black", "Yellow"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "e":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Pink", "Red", "Orange", "White", "Black", "Dark Blue", "Purple"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "f":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Red", "Light Blue", "Pink", "Purple", "White", "Black", "Grey", "Yellow"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "g":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Red", "Light Blue", "Pink", "Purple", "White", "Black", "Grey", "Yellow", "Dark Blue", "Wine", "Brown", "Beige", "Green", "Orange"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "h":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Red", "Light Blue", "Pink", "Purple", "White", "Black", "Grey", "Yellow", "Dark Blue", "Wine", "Brown", "Beige", "Green", "Orange"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "i":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Red", "Light Blue", "White", "Black", "Grey", "Dark Blue", "Wine", "Beige"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "j":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Light Blue", "White", "Black", "Grey", "Dark Blue", "Green", "Orange"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "k":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Purple", "White", "Black", "Yellow", "Dark Blue", "Brown", "Orange"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "l":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["White", "Black", "Beige", "Orange"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "m":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Red", "Pink", "Purple", "White", "Black", "Dark Blue"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

    elif whichcolour == "n":
        topcolour = whichcolourdict[whichcolour]
        bottomcolour = random.choice(["Red", "White", "Black", "Grey", " Warm Brown"])
        shoecolour = whichcolourdict[whichcolour]

        topclothing = random.choice(["Long sleeve(T shirt)", "Short sleeve(T shirt)", "Long sleeve(Shirt)", "Short sleeve(Shirt)", "Short sleeve(Turtle neck)", "Long sleeve(Turtle neck"])
        bottomclothing = random.choice(["Jeans", "Chinos", "Shorts"])
        if bottomclothing == "Shorts":
            footwear = random.choice(["Pair of slippers", "Pair of Sneakers", "Pair of Crocs", "Pair of sandals"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")
        else:
            footwear = random.choice(["Designer shoes", "Pair of Boots", "Pair of Sneakers", "Pair of Crocs"])
            print("\nYour matchup is: ")
            print("\n" + topclothing + " " + "=" + " " + topcolour)
            print("\n" + bottomclothing + " " + "=" + " " + bottomcolour)
            print("\n" + footwear + " " + "=" + " " + shoecolour + ", with a touch of = " + bottomcolour + "(optional)")

        return topcolour, bottomcolour, shoecolour

# The main Program
print("Welcome to My Butler\n")

mashupbegin = input("Press enter to start a mush up process")

eventchoosing = input("\nWhat is the occasion or dress up?\n(a) Casual/House wear\n(b) Cooperate/work\n(c) Sports/Relaxation\n(d) Party/Special Occasion\n(e) Traditional Assembly/event\nYour answer: ")

if eventchoosing == "a":
    colourcode = input("\nIs there any colour code?\n(a) Yes\n(b) No\nYour answer: ")
    if colourcode == "a":
        schemechoice = input("Which matchup scheme do you want?\n(a) Completely random\n(b) Specific\nYour answer: ")
        if schemechoice == "a":
            whichcolourdict = {"a": "Red", "b": "Orange", "c": "Yellow", "d": "Green", "e": "Light Blue", "f": "Dark Blue", "g": "Black", "h": "White", "i": "Pink", "j": "Purple", "k": "Beige", "l": "Brown", "m": "Grey", "n": "Wine"}
            whichcolour = input("\nWhich colour has been given?\n(a) Red\n(b) Orange\n(c) Yellow\n(d) Green\n(e) Light Blue\n(f) Dark Blue\n(g) Black\n(h) White\n(i) Pink\n(j) Purple\n(k) Beige\n(l) Brown\n(m) Grey\n(n) Wine\nYour answer: ")
            notsatisfied = "b"
            while notsatisfied == "b":
                colourcombo()
                notsatisfied = input("\nAre you satisfied with the match up given?\n(a) Yes\n(b) No\nYour answer: ")

            print("You have selected a match up, nice choice.")

        elif schemechoice == "b":
            whichcolourdict = {"a": "Red", "b": "Orange", "c": "Yellow", "d": "Green", "e": "Light Blue", "f": "Dark Blue", "g": "Black", "h": "White", "i": "Pink", "j": "Purple", "k": "Beige", "l": "Brown", "m": "Grey", "n": "Wine"}
            whichcolour = input("\nWhich colour has been given?\n(a) Red\n(b) Orange\n(c) Yellow\n(d) Green\n(e) Light Blue\n(f) Dark Blue\n(g) Black\n(h) White\n(i) Pink\n(j) Purple\n(k) Beige\n(l) Brown\n(m) Grey\n(n) Wine\nYour answer: ")

            whichtopdict = {"a": "Long sleeve(T shirt)", "b": "Short sleeve(T shirt)", "c": "Long sleeve(Shirt)", "d": "Short sleeve(Shirt)", "e": "Short sleeve(Turtle neck)", "f": "Long sleeve(Turtle neck"}
            whichtop = input("\nWhich top do you plan on going with?\n(a) Long sleeve(T shirt)\n(b) Short sleeve(T shirt)\n(c) Long sleeve(Shirt)\n(d) Short sleeve(Shirt)\n(e) Short sleeve(Turtle neck)\n(f) Long sleeve(Turtle neck)\nYour answer: ")

            whichbottomdict = {"a": "Jeans", "b": "Chinos", "c": "Shorts"}
            whichbottom = input("\nWhich bottom do you plan on going with?\n(a) Jeans\n(b) Chinos\n(c) Shorts\nYour answer: ")

            whichfootweardict = {"a": "Flat shoe", "b": "Designer shoe", "c": "Flashy shoe", "d": "Pair of Boots", "e": "Pair of Sneakers", "f": "Pair of Crocs"}
            whichfootwear = input("\nWhich foot wear do you plan on going with?\n(a) Flat shoe\n(b) Designer shoe\n(c) Flashy shoe\n(d) Pair of Boots\n(e) Pair of Sneakers\n(f) Pair of Crocs\nYour answer: ")

            print("\n" + whichtopdict[whichtop] + "=")
            print("\n" + whichbottomdict[whichbottom] + "=")
            print("\n" + whichfootweardict[whichfootwear] + "=")
    '''
    elif colourcode == "b":
        toprancolour = random.choice(["Red", "Light Blue", "Pink", "Purple", "White", "Black", "Grey", "Yellow", "Dark Blue", "Wine", "Brown", "Beige", "Green", "Orange"])
        colourdict = {"a": "Red", "b": "Orange", "c": "Yellow", "d": "Green", "e": "Light Blue", "f": "Dark Blue", "g": "Black", "h": "White", "i": "Pink", "j": "Purple", "k": "Beige", "l": "Brown", "m": "Grey", "n": "Wine"}
    '''