# Patrick Reed
import turtle
tom = turtle.Turtle()

# Graphing Functions
def nooseandhead(t):
    tom.seth(90)
    tom.forward(100)
    tom.left(180)
    tom.forward(200)
    tom.left(180)
    tom.forward(100)
    tom.seth(0)
    tom.forward(275)
    tom.left(90)
    tom.forward(75)
    tom.left(90)
    tom.forward(25)
    turtle.speed(10)
    tom.seth(270)
    for i in range(360):
        tom.left(1)
        tom.forward(.35)

def body(t):
    tom.seth(180)
    tom.penup()
    tom.forward(40)
    tom.pendown()
    tom.forward(100)

def leftbicep(t):
    tom.seth(0)
    tom.penup()
    tom.forward(75)
    tom.pendown()
    tom.seth(210)
    tom.forward(35)

def leftforearm(t):
    tom.seth(180)
    tom.forward(35)
    tom.penup()
    tom.seth(0)
    tom.forward(35)
    tom.seth(30)
    tom.forward(35)
    tom.seth(0)

def rightbicep(t):
    tom.seth(60)
    tom.forward(50)
    tom.penup()
    tom.seth(240)
    tom.forward(50)
    tom.seth(0)

def rightbicep(t):
    tom.pendown()
    tom.seth(150)
    tom.forward(35)

def rightforearm(t):
    tom.seth(180)
    tom.forward(35)
    tom.penup()
    tom.seth(0)
    tom.forward(35)
    tom.seth(330)
    tom.forward(35)
    tom.seth(0)

def leftthigh(t):
    tom.seth(180)
    tom.forward(75)
    tom.pendown()
    tom.seth(210)
    tom.forward(50)
    
def leftcalf(t):
    tom.seth(180)
    tom.forward(50)
    tom.penup()
    tom.seth(0)
    tom.forward(50)
    tom.seth(30)
    tom.forward(50)
    tom.seth(0)

def rightthigh(t):
    tom.seth(150)
    tom.pendown()
    tom.forward(50)
    
def rightcalf(t):
    tom.seth(180)
    tom.forward(50)
    tom.penup()
    tom.seth(0)
    tom.forward(50)
    tom.seth(330)
    tom.forward(50)
    tom.seth(0)
    
graphiclist = [nooseandhead, body, leftbicep, leftforearm,
               rightbicep, rightforearm, leftthigh, leftcalf, 
               rightthigh, rightcalf]

# Dictionary Function
def readInDict(dictfile):
    dictionary = {}
    myfile = open(dictfile, 'r', encoding = 'utf-8')
    for word in myfile:
        word = word.strip()
        word = word.lower()
        if word.endswith("'s"):
            word = word[:-2]
        if not word in dictionary:
            lword = len(word)
            dictionary[word] = lword
            c = dictionary.get(lword, [])
            c.append(word)
            dictionary[lword] = c
    myfile.close()
    return dictionary

# Initializing variables
letter = ['abcdefghijklmnopqrstuvwxyz']
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j','k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
dictionary = readInDict('american-english')

newdictionary = []
for word in dictionary:
    newdictionary.append(str(word))

# Hangman Component Functions
def pickOne(l, Length):
    length = int(Length)
    pwords = []
    from random import randint
    for word in l:
        if len(word) == length:
            pwords.append(word)
    index = randint(0, len(pwords)-1)
    return pwords[index]
    
def displayWord(word, rl):
    s = ' '
    for letter in word:
        if letter in rl:
            s += letter
        else:
            s += '_'
    return s

def humanGuess(Graphic, Length):
    yes = 0
    no = 0
    word = pickOne(newdictionary, Length)
    print('Number of Letters is:', len(word))
    rl = []
    wl = []
    #wl is wrong letters
    for i in range(len(word) + 10):
        letter = input('Give me a letter: ').lower()
        if letter in word and len(letter) == 1:
            yes += 1
            rl.append(letter)
            print('correct tries: ', yes, 'good choice!',
                  displayWord(word, rl))
        elif no == 10:
            print('You lose! The word was ', word)
            wn.exitonclick()
            break
        elif not '_' in displayWord(word, rl):
            print('You win!', 'word =', word)
            break
        else:
            no += 1
            if Graphic == True:
                wn = turtle.Screen()
                wn.mode('logo')
                tom = turtle.Turtle()
                for i in range(no):
                    graphiclist[i](tom)
            if not letter in wl:
                wl.append(letter)
            print('Wrong!', no, 'try again!', wl)

def computerGuess(Graphic, Length):
    from random import randint
    yes = 0
    no = 0
    rl = []
    wl = []
    answerword = []
    for i in range(Length):
        answerword.append('_')
    #wl is wrong letters
    for i in range(Length + 10):
        random = randint(0, len(alphabet) - 1)
        guessedletter = alphabet[random]
        print('Is there a(n)', guessedletter, '?')
        answer = input('Y/N: ')
        if answer == 'Y' and len(guessedletter) == 1:
            yes += 1
            alphabet.pop(random)
            rl.append(guessedletter)
            position = int(input('Where? '))
            for i in range(len(answerword)):
                if i == position:
                    answerword.pop(position)
                    answerword.insert(position, guessedletter)
                elif i != position:
                    answerword
            if not '_' in answerword:
                finalword = ''.join(answerword)
                print('You win!', 'word =', finalword)
                break
        elif 'N' and no == 10:
            print('You lose! You got', answerword)
            break
        elif answer == 'N' and no != 10:
            no += 1
            if Graphic == True:
                wn = turtle.Screen()
                wn.mode('logo')
                tom = turtle.Turtle()
                for i in range(no):
                    graphiclist[i](tom)
            if not guessedletter in wl:
                alphabet.pop(random)
                wl.append(guessedletter)
            print('Wrong!', no, 'try again!', wl)
        
# Final Hangman Function 
def hangman(Computer, Graphic, Length):
    '''
    This function starts a game where the computer is choosing a word
    if Computer is True and you choose the word if Computer is False.
    The words will be of length Length.
    Graphics is either True or False and indicates whether the man is drawn.
    It returns True if the Computer wins and False if the Computer loses.
    '''
    if Computer == True:
        humanGuess(Graphic, Length)
    if Computer == False:
        computerGuess(Graphic, Length)
        
        