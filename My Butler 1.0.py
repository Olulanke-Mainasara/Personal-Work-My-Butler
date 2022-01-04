from QuestionC import Question

# Program for app prototype
print("Welcome to My Butler")
print("Lets get started ˆ_ˆ")
print("\n")

# Getting personal details from the user
Name = input("What is your name: ")
print("Hi", Name, "\n")
Age = input("How old are you: ")
print("\n")
Complexion = input("What is your complexion: ")
print("\n")

while True:
    Gender = input("What is your gender: ")
    print("\n")
    if Gender == "male" or Gender == "female" or Gender == "other":
        print("Cool, nice to meet you", Name)
        print("\n")
        print("Ok! Lets get started on your outlook")
        print("\n")
        break
    else:
        print("Invalid choice, please choose a gender.")
        continue

# Program to get cloth information from the user

question_prompts = [
    "what kind of person are you e.g your personality?\n(a) Flashy\n(b) Quiet\n(c) Conservative\n(d) Casual\n(e) Cooperate\n\n",
    "what type of cloths would you like to use for mashups in the future?\n(a) Traditional\n(b) Cooperate\n(c) Casual\n(d) Party cloths\n(e) Event\n\n",
    "what type of hats do you have/do u like wearing?\n(a) Baseball hats\n(b) Bucket hats\n(c) Cowboy hats\n(d) Sunblocks\n(e) Army hats\n\n",
    "what type of shirts do you have/think look good on you?\n(a) Polo\n(b) Hoodies\n(c) Jackets\n(d) T Shirts\n(e) Long sleeves\n\n",
    "What type of ties do you have prefer?\n(a) Checked ties\n(b) Plain ties\n(c) patterned ties\n(d) Vintage ties\n(e) Bow ties\n\n",
    "Which one do you  have?\n(a) Blazers\n(b) Jackets\n(c) Both\n\n",
    "Do you like suits?,If yes then which type?\n(a) Yes(3 piece suits)\n(b) Yes(2 piece suits)\n(c) No\n\n",
    "How do u see belts?\n(a) Necessary\n(b) To be used occasionally\n(c) Not really important\n(d) I dont lik them\n\n",
    "What type of watches do u like wearing?\n(a) Techy\n(b) simple\n(c) Element made\n(d) Fancy/Trending\n\n",
    "What style of shoes do you like?\n(a) Pointy\n(b) Flat\n(c) Designed\n(d) Shiny\n(e) Techy\n\n",
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
