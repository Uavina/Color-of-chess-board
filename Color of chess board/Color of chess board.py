try:
    Cont="Yes"
    class Chess:
        def __init__(self,Coins):
            self.Coins=Coins
        def Details(self):
            alpha=['a' , 'b' , 'c', ' d' , 'e' , 'f' , ' g' , ' h']
            for i in range(len(alpha)):
                for j in range(1,9):
                    if alpha[i]+str(j)==Coins:
                        if (i+j)%2==0:
                            return "White Colour !!!!!!"
            return "Black Color!!!!"
    while Cont=="Yes":
        print("Enter the Correct Values!")
        Coins=input("Enter the Color Value")
        point=Chess(Coins)
        print("The colour is ",point.Details())
        Cont=input("Do you want to continue this program [Yes/No] :")
except ValueError:
    print("Plz Give Correct Input (or) Do Give Any Space")
except:
    print("Something went wrong")
