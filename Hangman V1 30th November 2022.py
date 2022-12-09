import random
from words import words
word=random.choice(words) #word picker
chk=[]  #What the player must see without typing in anything
yolo=''
for i in range(len(word)):
    if word[i]=='-':
        chk.append('-')
    else:
        chk.append('_')

def chkpt():
    global yolo 
    for i in range(len(chk)):
        yolo+=chk[i]
        print(chk[i],end='')
    print()
chkpt()  #Checkpoint(abbreviation)

play=[] #All the letters that the player has chosen
life=5 #Number of lives
st=0  #This will check for the modifications made
while life>0:
    yolo=''
    a=input("\nEnter a single letter for this "+str(len(word))+" letter word.").lower()
    if len(a)==1:
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

        if yolo==word:
            print("\nYou WIN!!")
            break
    else:
        print("You can only enter a single letter at a time! Try again.!")
        
        
    
