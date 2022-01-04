from QuestionC import Question

# Program for the prototype of the MY BUTLER app
print("Welcome to My Butler")
print("Lets get started ˆ_ˆ")
print("\n")


# Getting personal details from the user
def acqdet():
    userdetails = []
    name = input("What is your name: ")
    userdetails.append("Your name is " + name)
    print("Hi", name, "\n")
    age = input("How old are you: ")
    userdetails.append("You are " + age + " " + "Years old")
    print("\n")
    compdict = {"a": "Extremely Light", "b": "Light", "c": "Tanned", "d": "Olive", "e": "Brown", "f": "Dark"}
    complexion = input("What is your complexion?\n(a) Extremely Light\n(b) Light\n(c) Tanned\n(d) Olive\n(e) Brown\n(f) Dark\nI am: ")
    userdetails.append("You are" + " " + compdict[complexion] + " " + "in colour")
    gender = input("What is your gender: ")
    userdetails.append("You are a" + " " + gender)
    print("These are your details: ", userdetails)
    print("\n")

acqdet()
detchange = input("Would you like to change anything?, type y for Yes and n for No: ")
print("\n")
while detchange == "y":
    print("Ok then, lets go over your details again shall we.")
    acqdet()
else:
    print("\n")

if gender == "male":
    print("Cool, nice to meet you", name)
    print("\n")
    print("Ok! Lets get started on your outlook")
    print("\n")

    # Program to determine cloth mashup

    question_prompts = [
        "what kind of person are you e.g your personality?\n(a) Flashy\n(b) Quiet\n(c) Conservative\n(d) Casual\n(e) Cooperate\n\n",
        "what type of cloths would you like to use for mashups in the future?\n(a) Traditional\n(b) Cooperate\n(c) Casual\n(d) Party cloths\n(e) Event\n\n",
        "what type of hats do you have?\n(a) Baseball hats\n(b) Bucket hats\n(c) Cowboy hats\n(d) Sunblocks\n(e) Army hats\n\n",
        "what type of shirts do you have?\n(a) Polo\n(b) Hoodies\n(c) Jackets\n(d) T Shirts\n(e) Long sleeves\n\n",
        "What type of ties do you have?\n(a) Coloured ties\n(b) Plain ties\n(c) patterned ties\n(d) Vintage ties\n(e) Bow ties\n\n",
        "Which one(s) do you  have?\n(a) Blazers\n(b) Plain Jackets\n(c) Jean Jackets\n\n",
        "Do you like suits?,If yes then which type?\n(a) Yes(3 piece suits)\n(b) Yes(2 piece suits)\n(c) No\n\n",
        "How do u see belts?\n(a) Necessary\n(b) To be used occasionally\n(c) Not really important\n(d) I don't lik them\n\n",
        "What type of watches do u like wearing?\n(a) Tech\n(b) simple\n(c) Element endowed\n(d) Fancy/Trending\n\n",
        "What style of shoes do you like?\n(a) Pointy\n(b) Flat\n(c) Designer\n(d) Flashy\n(e) Boots\n\n",
        "What colours do you have?\n(a) Red\n(b) Yellow\n(c) Blue\n(d) Green\n(e) Black\n\n",
    ]

    questions = [
        Question(question_prompts[0], "a", "b", "c", "d", "e"),
        Question(question_prompts[1], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[2], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[3], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[4], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[5], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[6], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[7], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[8], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[9], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
    ]

    clothdet = []
    def run_test(questions):
        for question in questions:
            answer = input(question.prompt)
            clothdet.append(answer)
        print(clothdet)
        print("Ok!, now lets begin mashups")


    run_test(questions)

elif gender == "female":
    print("Cool, nice to meet you", name)
    print("\n")
    print("Ok! Lets get started on your outlook")
    print("\n")

    # Program to determine cloth mashup

    question_prompts = [
        "what kind of person are you e.g your personality?\n(a) Flashy\n(b) Quiet\n(c) Conservative\n(d) Casual\n(e) Cooperate\n\n",
        "what type of cloths would you like to use for mashups in the future?\n(a) Traditional\n(b) Cooperate\n(c) Casual\n(d) Party cloths\n(e) Event\n\n",
        "what type of hats do you have/do u like wearing?\n(a) Customized hats\n(b) Bucket hats\n(c) Cowboy hats\n(d) Sunblocks\n(e) Berets\n\n",
        "what type of shirts do you have/think look good on you?\n(a) Polo\n(b) Hoodies\n(c) Crop tops\n(d) T Shirts\n(e) Long sleeves\n\n",
        "What type of body accessories do you have/prefer?\n(a) Earrings\n(b) Necklaces\n(c) Bangles/Bracelets\n(d) Brooches/Pins\n(e) Neckties\n\n",
        "Which one(s) do you have?\n(a) Blazers\n(b) Plain Jackets\n(c) Jean Jackets\n\n",
        "Do you like suits?,If yes then which type?\n(a) Yes(3 piece suits)\n(b) Yes(2 piece suits)\n(c) No\n\n",
        "How do u see bags?\n(a) Necessary\n(b) To be used occasionally\n(c) Not really important\n(d) I don't lik them\n\n",
        "What type of watches do u like wearing?\n(a) Tech\n(b) simple\n(c) Element endowed\n(d) Fancy/Trending\n\n",
        "What style of shoes do you like?\n(a) High heeled\n(b) Flat\n(c) Designer\n(d) Flashy\n(e) Boots\n\n",
        "What colours do you have type do u have?\n(a) Red\n(b) Yellow\n(c) Blue\n(d) Green\n(e) Black\n\n",
    ]

    questions = [
        Question(question_prompts[0], "a", "b", "c", "d", "e"),
        Question(question_prompts[1], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[2], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[3], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[4], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[5], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[6], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[7], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[8], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
        Question(question_prompts[9], "a", "b", "c", "d", "e"),
        Question(question_prompts[10], "a", "b", "c", "d", "e"),
    ]


    def run_test(questions):
        for question in questions:
            answer = input(question.prompt)
        print("Ok!, now lets begin mashups")


        run_test(questions)
        input("How do you want would you like to look today?")

else:
    print("Invalid choice, please choose a gender.")