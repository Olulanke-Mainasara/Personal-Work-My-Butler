# Program for the prototype of the MY BUTLER app
print("Welcome to My Butler")
print("Lets get started ˆ_ˆ")
print("\n")


# Getting personal details from the user
userdetails = []
name = input("What is your name: ")
userdetails.append("Your name is " + name)
print("Hello", name, "\n")
age = input("How old are you: ")
userdetails.append("You are " + age + " " + "Years old")
print("\n")
compdict = {"a": "Extremely Light", "b": "Light", "c": "Tanned", "d": "Olive", "e": "Brown", "f": "Dark"}
complexion = input("What is your complexion?\n(a) Extremely Light\n(b) Light\n(c) Tanned\n(d) Olive\n(e) Brown\n(f) Dark\nI am: ")
userdetails.append("You have a" + " " + compdict[complexion] + " " + "skin")
print("\n")
gendict = {"a": "Male", "b": "Female"}
gender = input("What is your gender?\n(a) Male\n(b) Female\nI am: ")
userdetails.append("You're a" + " " + gendict[gender])
print("These are your details: ", userdetails)
print("\n")

if gender == "a":
    print("Cool, nice to meet you", name)
    print("\n")
    print("Ok! Lets get started on your outlook")
    print("\n")
    personlist = []
    persdict = {"a": "Flashy", "b": "Quiet", "c": "Conservative", "d": "Casual", "e": "Cooperate"}
    perschoose = input("what kind of person are you i.e your personality?\n(a) Flashy\n(b) Quiet\n(c) Conservative\n(d) Casual\n(e) Cooperate\nYour answer: ")
    personlist.append(persdict[perschoose])
    andp = input("\nAny other personality? y = Yes, n = No: ")
    if andp == "y":
        perschoosen = input("\nwhat other kind of person are you e.g your personality?\n(a) Flashy\n(b) Quiet\n(c) Conservative\n(d) Casual\n(e) Cooperate\nYour answer: ")
        personlist.append(persdict[perschoosen])
        print("\n")
        print("Ok then, You're a", personlist[0], "and a", personlist[1], "person, No problem")
    else:
        print("Ok then, You're a" + " ", personlist, "person, No problem")


    # Available owned clothes
    print("\nLets go through what you have shall we")
    print("\n")
    groups = []
    groupchoosing = input("Which type of cloths should we start with?\n(a) Casual/House wear\n(b) Cooperate/work\n(c) Sports/Relaxation\n(d) Party/Special Occasion\n(e) Traditional Attire\nYour answer: ")
    if groupchoosing == "a":
        casual = []

        print("\nCasual/Hat Category")
        hatslist = []
        morechoicehats = "y"
        while morechoicehats == "y":
            hatsdict = {"a": "Baseball hat", "b": "Bucket hat", "c": "Cowboy hat", "d": "Sunblock", "e": "Camo hat"}
            hats = input("what type of hats do you have?\n(a) Baseball hat\n(b) Bucket hat\n(c) Cowboy hat\n(d) Sunblock\n(e) Camo hat\nYour answer: ")
            hatslist.append("You have a: " + hatsdict[hats])
            casual.append(hatslist)
            print("")
            morechoicehats = input("Do you have any other type of hat from the list? y = Yes, n = No: ")
        print(hatslist)

        print("")
        print("\nCasual/Shirt Category")
        shirtslist = []
        morechoiceshirts = "y"
        while morechoiceshirts == "y":
            shirtsdict = {"a": "Long sleeve(T shirt)", "b": "Short sleeve(T shirt)", "c": "Long sleeve(Shirt)", "d": "Short sleeve(Shirt)", "e": "Short sleeve(Turtle neck)", "f": "Long sleeve(Turtle neck"}
            shirts = input("what type of shirts do you have?\n(a) Long sleeve(T shirt)\n(b) Short sleeve(T shirt)\n(c) Long sleeve(Shirt)\n(d) Short sleeve(Shirt)\n(e) Short sleeve(Turtle neck)\n(f) Long sleeve(Turtle neck)\nYour answer: ")
            shirtslist.append("You have a: " + shirtsdict[shirts])
            casual.append(shirtslist)
            print("")
            morechoiceshirts = input("Do you have any other type of shirt from the list? y = Yes, n = No: ")
        print(shirtslist)

        print("")
        print("\nCasual/Jacket Category")
        jacketslist = []
        morechoicejackets = "y"
        while morechoicejackets == "y":
            jacketsdict = {"a": "Blazer", "b": "Fur Jacket", "c": "Jean Jacket", "d": "Rain coat", "e": "Plain Jacket"}
            jackets = input("Which of these do u have do you  have?\n(a) Blazer\n(b) Fur Jacket\n(c) Jean Jacket\n(d) Rain coat\n(e) Plain Jacket\nYour answer: ")
            jacketslist.append("You have a: " + jacketsdict[jackets])
            casual.append(jacketslist)
            print("")
            morechoicejackets = input("Do you have any other type of jacket from the list? y = Yes, n = No: ")
        print(jacketslist)

        print("\nCasual/Belt Category")
        beltslist = []
        morechoicebelts = "y"
        while morechoicebelts == "y":
            beltsdict = {"a": "Plain belt(with Buckle mouth)", "b": "Woven Belt", "c": "Plain Belt(with button mouths)"}
            belts = input("What type of belts do you have?\n(a) Plain belt(with Buckle mouth)\n(b) Woven Belt\n(c) Plain Belt(with button mouths)\nYour answer: ")
            beltslist.append("You have a: " + beltsdict[belts])
            casual.append(beltslist)
            print("")
            morechoicebelts = input("Do you have any other type of belt from the list? y = Yes, n = No")
        print(beltslist)

        print("\nCasual/Watch Category")
        watchlist = []
        morechoicewatches = "y"
        while morechoicewatches == "y":
            watchesdict = {"a": "Smart watch", "b": "Simple watch", "c": "Element endowed watch", "d": "Fancy/Trending watch"}
            watches = input("What type of watches do you have?\n(a) Smart watch\n(b) simple watch\n(c) Element endowed watch\n(d) Fancy/Trending watches\nYour answer: ")
            watchlist.append("You have a: " + watchesdict[watches])
            casual.append(watchlist)
            print("")
            morechoicewatches = input("Do you have any other type of watch from the list? y = Yes, n = No")
        print(watchlist)

        print("\nCasual/Shoe Category")
        shoelist = []
        morechoiceshoes = "y"
        while morechoiceshoes == "y":
            shoesdict = {"a": "pointy shoe", "b": "Flat shoe", "c": "Designer shoe", "d": "Flashy shoe", "e": "Pair of Boots", "f": "Pair of Sneakers", "g": "Pair ofCrocs"}
            shoes = input("What style of shoe do you have?\n(a) Pointy shoe\n(b) Flat shoe\n(c) Designer shoe\n(d) Flashy shoe\n(e) Pair of Boots\n(f) Pair of Sneakers\n(g) Pair of Crocs\nYour answer: ")
            shoelist.append("You have a: " + shoesdict[shoes])
            casual.append(shoelist)
            print("")
            morechoiceshoes = input("Do you have any other type of shoe from the list? y = Yes, n = No")
        print(shoelist)

        groups.append("These are the items you have for the casual category: ")
        groups.append(casual)
        print(groups)


    elif groupchoosing == "b":
        cooperate = []

        print("\nCooperate/Shirts Category")
        coshirtslist = []
        morechoicecoshirts = "y"
        while morechoicecoshirts == "y":
            coshirtsdict = {"a": "Long sleeve(T shirt)", "b": "Short sleeve(T shirt)", "c": "Long sleeve(Shirt)", "d": "Short sleeve(Shirt)"}
            coshirts = input("what type of shirts do you have?\n(a) Long sleeve(T shirt)\n(b) Short sleeve(T shirt)\n(c) Long sleeve(Shirt)\n(d) Short sleeve(Shirt)\nYour answer: ")
            coshirtslist.append("You have a: " + coshirtsdict[coshirts])
            cooperate.append(coshirtslist)
            print("")
            morechoicecoshirts = input("Do you have any other type of cooperate shirt from the list? y = Yes, n = No")
        print(coshirtslist)

        print("\nCooperate/Ties Category")
        cotieslist = []
        morechoicecoties = "y"
        while morechoicecoties == "y":
            cotiesdict = {"a": "Woven ties", "b": "Plain ties", "c": "Patterned ties", "d": "Vintage ties", "e": "Bow ties"}
            coties = input("What type of ties do you have?\n(a) Woven ties\n(b) Plain ties\n(c) patterned ties\n(d) Vintage ties\n(e) Bow ties\nYour answer: ")
            cotieslist.append("You have a: " + cotiesdict[coties])
            cooperate.append(cotieslist)
            print("")
            morechoicecoties = input("Do you have any other type of cooperate tie from the list? y = Yes, n = No")
        print(cotieslist)
