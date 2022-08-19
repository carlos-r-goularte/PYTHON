from tkinter import *
from operations import *

class Application:

    def __init__(self, master=None):

        #=======================FRAMES===========================#
        self.frameMaster = Frame(master)
        self.frameMaster.pack()

        self.frameMenu = Frame()
        self.frameMenu.pack()

        self.frameOperations = Frame()
        self.frameOperations.pack()

        #=======================BOTÕES OPERAÇÕES ADICIONAIS===========================#
        self.bt_clear = Button(self.frameOperations,text="C")
        self.bt_clear.pack()
        self.bt_clearEntry = Button(self.frameOperations,text="CE")
        self.bt_clearEntry.pack()
        self.bt_back = Button(self.frameOperations,text="<<")
        self.bt_back.pack()
        self.bt_percent = Button(self.frameOperations,text="%")
        self.bt_percent.pack()
        self.bt_inverse = Button(self.frameOperations,text="1/x")
        self.bt_inverse.pack()
        self.bt_pow = Button(self.frameOperations,text="x²")
        self.bt_pow.pack()
        self.bt_sqrt = Button(self.frameOperations,text="√x")
        self.bt_sqrt.pack()
        #=======================BOTÕES OPERAÇÕES BASICAS===========================#
        self.bt_add = Button(self.frameOperations,text="+")
        self.bt_add.pack()
        self.bt_sub = Button(self.frameOperations,text="-")
        self.bt_sub.pack()
        self.bt_div = Button(self.frameOperations,text="÷")
        self.bt_div.pack()
        self.bt_mult = Button(self.frameOperations,text="X")
        self.bt_mult.pack()
        #=======================BOTÃO IGUAL===========================#
        self.bt_equal = Button()
        self.bt_equal.pack()
         #=======================BOTÕES NUMERICOS===========================#
        self.bt_zero = Button()
        self.bt_zero.pack()
        self.bt_one = Button()
        self.bt_one.pack()
        self.bt_two = Button()
        self.bt_two.pack()
        self.bt_three = Button()
        self.bt_three.pack()
        self.bt_four = Button()
        self.bt_four.pack()
        self.bt_five = Button()
        self.bt_five.pack()
        self.bt_six = Button()
        self.bt_six.pack()
        self.bt_seven = Button()
        self.bt_eight = Button()
        self.bt_nine = Button()

        self.bt_sign = Button()
        self.bt_score = Button()



def main():
    root = Tk()
    Application(root)
    root.geometry("340x600+500+100")
    root.title("Basic Calculator")
    root.resizable(False, False)
    root.iconbitmap("images/calculator-icon.ico")
    root.mainloop()

if __name__ == "__main__":
    main()
