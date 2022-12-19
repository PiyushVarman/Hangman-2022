print('''Welcome to the Hangman Game!
You have 5 lives to start this game. 
I will give you a word but hide all the letters of it.
You must enter a single letter at a time.
Do you think you have it in you to beat me? Let's go!\n''')
import random
from words import words
word=random.choice(words) #word picker
chk=[]  #What the player must see without typing in anything
p1=''
print("This is a",len(word),"letter word.")
for i in range(len(word)):
    if word[i]=='-':
        chk.append('-')
    else:
        chk.append('_')

def chkpt():
    global p1 
    for i in range(len(chk)):
        p1+=chk[i]
        print(chk[i],end='')
    print()
chkpt()  #Checkpoint(abbreviation)

play=[] #All the letters that the player has chosen
life=5 #Number of lives
st=0  #This will check for the modifications made
while life>0:
    p1=''
    a=input("\nEnter a single letter for this word.").lower()
    a=a.strip()
    if len(a)==1 and a not in play:
        play.append(a)
        
        for i in range(len(word)):
            if word[i]==a:
                chk[i]=a
                st+=1
        chkpt()
        if st==0:  #(No changes are made; hence, it was an incorrect guess)
            life-=1
            print("Uhoh! That's incorrect! You are now down to",life,"lives!")
            if life==0:
                print("\nYou lost the game! The word was '",word,"'.",sep='')
                break
        print("The letters you have used are:",sorted(play))
        st=0 #Resetting the modifcation counter.

        if p1==word:
            print("\nThat's Right, the word was, indeed",p1,"!\nYou WIN!!")
            break
    elif len(a)!=1:
        print("You can only enter a single letter at a time! Try again.!")
    # elif a in play:
        print("You have already used the letter",a,"!\nTry Again!")
        
        
    
