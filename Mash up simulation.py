import random
print("Welcome to My Butler\n")

mashupbegin = input("Press enter to start a mush up process")

eventchoosing = input("\nWhat is the occasion or dress up?\n(a) Casual/House wear\n(b) Cooperate/work\n(c) Sports/Relaxation\n(d) Party/Special Occasion\n(e) Traditional Assembly/event\nYour answer: ")

if eventchoosing == "a":
    dresscode = input("\nis there any dress code?\n(a) Yes\n(b) No\nYour answer: ")
    if dresscode == "a":
        whichtopdict = {"a": "Long sleeve(T shirt)", "b": "Short sleeve(T shirt)", "c": "Long sleeve(Shirt)", "d": "Short sleeve(Shirt)", "e": "Short sleeve(Turtle neck)", "f": "Long sleeve(Turtle neck"}
        whichtop = input("\nWhich of these is the top side dress code?\n(a) Long sleeve(T shirt)\n(b) Short sleeve(T shirt)\n(c) Long sleeve(Shirt)\n(d) Short sleeve(Shirt)\n(e) Short sleeve(Turtle neck)\n(f) Long sleeve(Turtle neck)\nYour answer: ")
        topcolour = random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet", "Brown", "White"])

        whichbottomdict = {"a": "Jeans", "b": "Chinos", "c": "Shorts"}
        whichbottom = input("\nWhich of these is the bottom dress code?\n(a) Jeans\n(b) Chinos\n(c) Shorts\nYour answer: ")
        bottomcolour = random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Brown", "White"])

        whichfootweardict = {"a": "Flat shoe", "b": "Designer shoe", "c": "Flashy shoe", "d": "Pair of Boots", "e": "Pair of Sneakers", "f": "Pair of Crocs"}
        whichfootwear = input("\nWhich of these is the foot wear dress code?\n(a) Flat shoe\n(b) Designer shoe\n(c) Flashy shoe\n(d) Pair of Boots\n(e) Pair of Sneakers\n(f) Pair of Crocs\nYour answer: ")
        footwearcolour = random.choice(["Red", "Orange", "Yellow", "Green", "Blue", "Brown", "White"])

        mashuptop = print("\n" + whichtopdict[whichtop] + "=" + topcolour)
        mashupbottom = print("\n" + whichbottomdict[whichbottom] + "=" + bottomcolour)
        mashupfootwear = random.choice(["\n" + whichfootweardict[whichfootwear] + "=" + footwearcolour])