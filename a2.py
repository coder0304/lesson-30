class flashcards:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        return self.word+'('+self.meaning+')'
flash=[]
print("welcome to flashcard application")
while(True):
      word=input("enter the name you want to add to ur flashcard:")
      meaning=input("enter the meaning of the word:")
      flash.append(flashcards(word,meaning))
      option=int(input("enter 0, if u want to add another flascard otherwise enter 1:"))
      if(option):
       break
print("\n your flashcards")
for i in flash:
    print(">",i)