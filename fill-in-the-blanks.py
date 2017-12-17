# IPND Stage 2 Final Project.ver4. Alan Lloyd 20th January 2017.

initialGameText="\nPlease select a game difficulty by typing it in. Possible inputs are easy, medium, or hard."

#'initialGame' texts separate from main 'GameTexts', to make text display easier
easyGameText1="\nYou\'ve chosen easy!  The current paragraph reads:"

easyGameText="""
A common first thing to do in a language is display \'Hello __1__ !\'  In __2__ this is particularly easy; all you have to do
is type in: __3__ \"Hello __1__ !\".  Of course, that isn\'t a very useful thing to do.
However, it is an example of how to output to the user using the __3__ command, and produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that can be done even more easily with an __4__ file in a browser, but it\'s
a step in learning __2__ syntax, and that\'s really its purpose."""

mediumGameText1="\nYou\'ve chosen medium! The current paragraph reads:"

mediumGameText="""
A __1__ is created with the def keyword.  You specify the inputs a __1__ takes by adding __2__ separated by commas between the parentheses.
__1__ s by default returns __3__ if you don\'t specify the value to return. __2__ can be standard data types such as string, integer, dictionary, tuple,
and __4__ or can be more complicated such as objects and lambda functions.
"""
hardGameText1="\nYou\'ve chosen hard! The current paragraph reads:"

hardGameText="""
When you create a __1__ , certain __2__ s are automatically generated for you if you don\'t make them manually. These contain multiple underscores before and
after the word defining them.  When you write a __1__ , you almost always include at least the __3__ __2__ , defining variables for when __4__ s of the __1__
get made.  Additionally, you generally want to create a __5__ __2__ , which will allow a string representation of the method to be viewed by other developers.

You can also create binary operators, like __6__ and __7__ , which allow + and - to be used by __4__ s of the __1__ .  Similarly, __8__ , __9__ , and __10__
allow __4__ s of the __1__ to be compared (with <, >, and ==).
"""

answerSpaces=['__1__','__2__','__3__','__4__','__5__','__6__','__7__','__8__','__9__','__10__']
 
easyAnswers=['world','python','print','HTML']
mediumAnswers=['function','arguments','None','list']
hardAnswers=['class','method','__init__','instance','__repr__','__add__','__sub__','__lt__','__gt__','__eq__']


#function to handle user selection of game. It also then calls play_game()
user_input1=""
def initial_game_choice():
        user_input1=str(raw_input(initialGameText))
        if user_input1 == "easy":
            play_game(easyGameText1, easyGameText, easyAnswers, answerSpaces)

        elif user_input1 == "medium":
            play_game(mediumGameText1, mediumGameText, mediumAnswers, answerSpaces)

        elif user_input1 == "hard":
            play_game(hardGameText1, hardGameText, hardAnswers, answerSpaces)


#runs game, checks answers for correctness, prints progress and final results.
def play_game(quizIntroTxt, quiz, answers, answerSpaces):
    index=0
    print quiz, '\npossible answers are: ' , answers
    while (index < len(quiz)):
       while (index < len(answers)):
            user_answer_example=raw_input("Please select answer for: " + answerSpaces[index])
            if user_answer_example in answers[index]:
                quiz= quiz.replace(answerSpaces[index], user_answer_example)
                print quiz, '\npossible answers are: ' , answers 
                index=index+1 
            else:
                print "wrong, try again"
            quiz="".join(quiz)
            if index == len(answers):
                print "\ncongratulations, you've answered all the questions"
 
initial_game_choice()
