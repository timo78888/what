import time

def ask(question, a, b, c, d, correct):
    print(question)
    time.sleep(0.5)
    print(a + ' ' + b)
    print(c + ' ' + d)
    time.sleep(0.5)
    answer = input("Your answer (as a, b, c, or d): ").lower()
    while answer.isalpha() == False or len(answer) != 1:
            answer = input("Your answer (as a, b, c, or d), pls follow intructions damnit: ").lower()
    if answer == correct:
        print("good job lol :|")
    else:
        print(":^) haha wrong start over now :^)")
        quit()

print("I hope you fail at this game lol")
time.sleep(0.5)

print("Question 1:")
ask("What's 1+1?", "a: 2", "b: 4", "c: 1+1", "d: -2", "c")
time.sleep(1)

print("Question 2:")
ask("Why are you playing this game?", "a: Because I'm bored", "b: Because I have no life", "c: Because I wanna die", "d: Becuase why not?", "b")
time.sleep(1)

print("Question 3:")
ask("What language is this program written in?", "a: B-sharp", "b: island", "c: D-flat", "d: snek", "d")
time.sleep(1)

ans = []
for i in range(4):
    ans.append(f"{1.9+0.1*i} * 10^30 kg")

print("Question 4:")
ask("If Alice had 3 candies and Bob had 1, what is the mass of the sun?", f"a: {ans[0]}", f"b: {ans[1]}", f"c: {ans[2]}",f"d: {ans[3]}", "b")
time.sleep(1)

print("Question 5:")
ask("Did you look up the answer to the previous question?", "a: yes", "b: no", "c: maybe", "d: how did you know?", "a")
time.sleep(1)

print("Question 6:")
ask("Pick the right one.", "a: 1", "b: 2", "c: 3", "d: the right one", "b")
time.sleep(1)

print("Question 7:")
ask("input(\"Why is there code inside of my code?\")", "a: because", "b: why", "c: not", "d: there\'s a bug", "c")
time.sleep(1)

print("Question 8:")
ask("Is this a question?", "a: yes", "b: no", "c: maybe", "d: we\'re all in a simulation", "c")
time.sleep(1)

print("Question 9:")
ask("If Claire has 5 apples and David has 6, how many apples does Alice have?", "a: wtf", "b: 7", "c: 3", "d: I thought Alice had candies", "b")
time.sleep(1)

print("Question 10:")
ask("int a db = ", "a: ab - int bda", "b: ab - int b da", "c: ababadbasdbabsdbdas", "d: I hate integration by parts", "d")
time.sleep(1)

print("Question 11:")
ask("?", "a: !", "b: .", "c: ?", "d: ;", "c")
time.sleep(1)

print("Question 12:")
ask("string = a3uhf. string.isalpha() = ", "a: true", "b: false", "c: wtf does this mean", "d: this code probably won\'t work", "d")
time.sleep(1)

print("Question 13:")
ask("3.", "a: What is the question?", "b: What is sqrt(9)?", "c: What is sqrt(g)", "d: three?", "d")
time.sleep(1)

print("Question 14:")
ask("i++", "a: i += 1", "b: that won't compile", "c: ;", "d: i++;", "c")
time.sleep(1)

print("Question 15:")
ask("If Elizabeth has 15 candies and Frank has 7, how old is Bob?", "a: 6", "b: 18", "c: 17", "d: 29", "c")
time.sleep(1)

print("Question 16:")
ask("George wants to give 50 candies away. How many candies will Alice have?", "a: the same as Bob", "b: the same as everyone else", "c: communism", "d: 3", "c")
time.sleep(1)

print("Question 17:")
ask("Prelude in", "a: A Major", "c: A-flat Major", "b: D Major", "d: B Major", "b")  # yes, the mistake was on purpose
time.sleep(1)

print("Question 18:")
ask("Did you get pranked by Question 17?", "a: yes", "b: no", "c: maybe", "d: how do you know", "a")
time.sleep(1)

print("Question 19:")
ask("Claire wants to exchange her apples for candies. Name a fair exchange rate.", "a: 1a = 1c", "b: 1a = 5c", "c: 1a = 20c", "d: 1a = 50c", "b")
time.sleep(1)

print("Question 20:")
ask("How many apples will David have once he exchanges his apples for candies?", "a: 25", "b: 30", "c: 35", "d: 40", "e")
# make sure you read the question!!!
time.sleep(1)

print("Question 21:")
ask("void", "a: int main", "b: what", "c: I want to go there", "d: N U L L", "c")
time.sleep(1)

print("Question 22:")
ask("Select the wrong one", "a: 1", "b: 2", "c: 3", "d: the right one", "c")
time.sleep(1)

print("Question 23:")
ask("printf(\"Question 23:\");", "a: This is not C", "b: This is not Python", "c: This is confusing", "d: Why even bother", "d")
time.sleep(1)

print("Question 24:")
ask("Do you want a new file?", "a: Yes", "b: Yes pls", "c: No", "d: Why would I want that?", "d")
time.sleep(1)

print("Question 25:")
for i in range(50):
    new_file = open(f"file_{i}.txt","w+")
    new_file.write("haha lol")
    new_file.close()
ask("", "a: Why?!?!?", "b: Well that sucks", "c: Why would you do that?", "d: Alice is 15 years old", "a")
time.sleep(1)

print("Question 26:")
ask("If you get this wrong, what happens?", "a: I start over", "b: I die", "c: Nothing", "d: yes", "a")
time.sleep(1)

print("Question 27:")
ask("219471374+98127346923 = ", "a: 98346818397", "b: 98356818297", "c: 98346718297", "d: 98346818297", "d")
time.sleep(1)

print("Question 28:")
ask("You used a calulator for the previous question right?", "a: yes", "b: no", "c: maybe", "d: how do you know", "a")
time.sleep(1)

print("Question 29:")
ask("How many candies do Alice and Bob have together?", "a: 3", "b: 4", "c: 5", "d: 26", "b")
time.sleep(1)

print("Question 30:")
ask("Do you agree?", "a: yes", "b: no", "c: maybe", "d: nope", "a")
time.sleep(1)

print("Question 31:")
ask("If a = b, then what's the just intonation ratio for a minor 3rd?", "a: 8/7", "b: 7/6", "c: 6/5", "d: 5/4", "c")
time.sleep(1)

print("Question 32:")
ask("a = ", "a: 432", "b: 435", "c: 440", "d: 442", 'a')
time.sleep(1)

print("Question 33:")
ask("lingling...?", "a: 40 hours", "b: 40hours", "c: 40hrs", "d: 40hr", "c")
time.sleep(1)

print("Question 34:")
ask("Think outside the box!", "a: Huh", "b: What", "c: Why", "d: This is a wrong answer", "x")
time.sleep(1)

print("Question 35:")
ask("Pick c", "a: C", "b: C.", "c: c~", "d: c", "d")
time.sleep(1)

print("Question 36:")
ask("Which of these is true?", "a: Alice is 15 years old", "b: Bob is 18 years old", "c: David has 0 candies", "d: Claire has 6 apples", "a")
time.sleep(1)

print("Question 37:")
ask("If Alice gets 1 banana, and Bob gets 2, how many will Frank get?", "a: 6", "b: 16", "c: 32", "d: 63", "c")
time.sleep(1)

print("Question 38:")
print("haha lol")
ask("What question does the above text refer to?", "a. #24", "b: #25", "c: #26", "d: #27", "b")
time.sleep(1)

print("Question 39:")
ask("If Annie has 2 cookies and Bob has 3, how many does David have?", "a: 4", "b: 5", "c: what does this even mean", "d: who the hell is Annie", "d")
time.sleep(1)

print("Question 40:")
ask("Hi", "a: ik", "b: jk", "c: jl", "d: mo", "b")
time.sleep(1)

print("Question 41:")
ask("\n", "a: huh", "b: huh", "c: huh", "d: huh", "b")
time.sleep(1)

print("Question 42:")
ask("Press F to pay respects", "a: E-sharp", "b: G-double-flat", "c: f", "d: huh these are all f", "f")
time.sleep(1)

print("Question 43:")
i = 1
while i < (2**64):
    print(i)
    i *= 2
    time.sleep(0.125)
ask("Now, tell me. How many cookies does David have?", "a: 4", "b: 5", "c: what how", "d: idk ask David", "d")
time.sleep(1)

print("Question 44:")
ask("Which of these numbers appeared in the long list?","a: 144115188075855872", "b: 70368744277664", "c: 135217728", "d: 36029787018963968", "a")
time.sleep(1)

print("Question 45:")
ask("Choose the wrong answer!", "a: The right answer", "b: The wrong answer", "c: c", "d: D", "a")
time.sleep(1)

print("ok final 5 questions are free-response, don\'t die now :P")
time.sleep(0.5)

print("Question 46:")
ans_46 = input("Alice, Bob, Claire, David, Elizabeth, Frank, and George took an exam. Who has an A? ").lower()
if ans_46 == "bob" or ans_46 == "george":
    print(":^) haha wrong start over now :^)")
    print("Death at 90% oof")
    quit()
else:
    print("Continue on.")

time.sleep(1)
print("Question 47:")
ans_47 = input("If Alice has 3 candies and Bob has 4, then (2n+1)(2n-1) = ")
if ans_47 == "4n^2-1" or ans_47 == "4n**2-1" or ans_47 == "4n^2 - 1" or ans_47 == "4n**2 - 1":
    print("Continue on.")
else:
    print(":^) haha wrong start over now :^)")
    time.sleep(0.25)
    print("It would be a shame if you formatted your answer wrong, but I don\'t care haha")
    time.sleep(0.25)
    print("Death at 92% oof")
    quit()

for i in range(100):
    print(i)
    i += 1

print("Question 48:")
ans_48 = input("How many candies could you get for trading in one apple? ").lower()
if ans_48 == '5' or ans_48 == "five":
    print("Continue on.")
else:
    print(":^) haha wrong start over now :^)")
    print("Death at 94% big oof")
    quit()

for i in range(1000):
    print(i)
    i += 1
    time.sleep(0.1)

print("Question 49:")
ans_49 = input("Type something: ").lower()
if ans_49 == "something":
    print("Continue to the final question, don\'t fail there!")
else:
    print(":^) haha wrong start over now :^)")
    print("Death at 96% big oof")
    quit()

time.sleep(2)

print("Question 50:")
ans_50 = input("Add up Alice\'s and Bob\'s ages, plus the number of apples both Claire and David had initially, plus the number of files this game generated!\n")
if ans_50 == "93" or ans_50 == "ninety-three" or ans_50 == "ninety three":
    sure = input("Are you sure?\n a: yes\n b: no\n").lower()
    while sure.isalpha() == False or len(sure) != 1:
        sure = input("Are you sure?\n a: yes\n b: no\n").lower()
    if sure == "a":
        print("WOWOWOWOWOWOW you win lol :D")
        print("you get bragging rights and that\'s pretty much it")
        win = open("you_win.txt", "w+")
        win.write("gg :) " * 100)
        win.close()
    else:
        print("OOF YOU SHOULD HAVE BEEN SURE")
        print("Now start over :^)")
        print("Death at 99%, such unfortunate adklfjhslkdfjahdlfkjahdlsfkjhasdklfjhasdkfljhasdlkjh")
        quit()
else:
    print(":^) haha wrong start over now :^)")
    print("Death at 98% wdslfkjasflkjadfkjshfkj")