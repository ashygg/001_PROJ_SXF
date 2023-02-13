intro = """Welcome!
You have been selected to participate in anime trivia!
The anime that you will be quizzed on is...
'SPY x FAMILY' by Tatsuya Endo!
Please enjoy.

Now then, onto the questions!
"""
print(intro)
# End of trivia introduction.
total_score = 0

question_1 = """1) What is Loid Forger's spy codename?
a) Nightfall
b) Twilight
c) Daybreak
"""
print(question_1)
ans1 = str(input("Your Answer: "))
if ans1 == "Twilight":
    total_score += 1
    print("Correct")
elif ans1 == "twilight":
    total_score += 1
    print("Correct")
elif ans1 == "b) Twilight":
    total_score += 1
    print("Correct")
elif ans1 == "b) twilight":
    total_score += 1
    print("Correct")
elif ans1 == "b)Twilight":
    total_score += 1
    print("Correct")
elif ans1 == "b)twilight":
    total_score += 1
    print("Correct")
else:
    print(f"Nice try! Incorrect, but the answer is 'Twilight', not {ans1!r}.")
# This is the end of question 1.

print("Let's move on!" + '\n')

print("2) What is the name of the intelligence agency Twilight works for?")
question_2 = ['a) WISE', 'b) WEST', 'c) WIST']  # list
for x in question_2:
    print(x)
ans2 = str(input("Your Answer: "))
if ans2 == "WISE":
    total_score += 1
    print("Correct")
elif ans2 == "wise":
    total_score += 1
    print("Correct")
elif ans2 == "a) WISE":
    total_score += 1
    print("Correct")
elif ans2 == "a) wise":
    total_score += 1
    print("Correct")
elif ans2 == "a)WISE":
    total_score += 1
    print("Correct")
elif ans2 == "a)wise":
    total_score += 1
    print("Correct")
else:
    print(f"Nice try! Incorrect, but the answer is 'WISE', not {ans2!r}.")
# This is the end of question 2.

print(" ")
question_3 = ('3) What is the name of the mission?', 'a) Operation Strix', 'b) Operation Dawn', 'c) Operation Swift')
# tuple
for x in question_3:
    print(x)
ans3 = str(input("Your Answer: "))
if ans3 == "Operation Strix":
    total_score += 1
    print("Correct")
elif ans3 == "operation strix":
    total_score += 1
    print("Correct")
elif ans3 == "a) Operation Strix":
    total_score += 1
    print("Correct")
elif ans3 == "a) operation strix":
    total_score += 1
    print("Correct")
elif ans3 == "a)Operation Strix":
    total_score += 1
    print("Correct")
elif ans3 == "a)operation strix":
    total_score += 1
    print("Correct")
else:
    print(f"Nice try! Incorrect, but the answer is 'Operation Strix', not {ans3!r}.")
# This is the end of question 3.

print(" ")
print("Great job! Now, the final questions will be short-answer! Are you ready?" + '\n')

final_questions = [
    ("4) How many Stella Stars does a student need to be considered an imperial scholar", "8"),
    ("5) What ability does Anya possess", "Telepathy")
]
for question, correct_answer in final_questions:
    ans45 = input(f"{question}? ")
    if ans45 == correct_answer:
        print("Correct")
    else:
        print(f"The answer is {correct_answer!r}, not {ans45!r}.")

if ans45 == correct_answer:
    total_score += 2

print(" ")
print(f"Your total score for this quiz is... {total_score}! Congrats!")
print("Thanks for playing!")