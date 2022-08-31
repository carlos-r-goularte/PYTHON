from string import whitespace
from tkinter import *
from turtle import st
from operations import Operations

class Application:


    def __init__(self, master=None,resultOperation=None):

        resultOperation = StringVar()
        resultOperation.set(Operations.adiction(10,4))

        #=======================FRAMES===========================#
        self.frameMaster = Frame(master)
        self.frameMaster.pack()

        self.frameResult = Frame()
        self.frameResult.pack()

        self.frameOperations = Frame()
        self.frameOperations.pack()

        self.lb_result = Label(self.frameResult,fg='white',bg="#2c302d",font=('Arial 35 bold'),padx=5,pady=5,width=10,height=3,anchor=E,textvariable=resultOperation)
        
        #=======================BOTÕES OPERAÇÕES ADICIONAIS===========================#
        self.bt_clear = Button(self.frameOperations,text="C",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        self.bt_clearEntry = Button(self.frameOperations,text="CE",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        self.bt_back = Button(self.frameOperations,text="<<",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        self.bt_percent = Button(self.frameOperations,text="%",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)    
        self.bt_inverse = Button(self.frameOperations,text="1/x",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        self.bt_pow = Button(self.frameOperations,text="x²",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)       
        self.bt_sqrt = Button(self.frameOperations,text="√x",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        
        #=======================BOTÕES OPERAÇÕES BASICAS===========================#
        self.bt_add = Button(self.frameOperations,text="+",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_sub = Button(self.frameOperations,text="-",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)       
        self.bt_div = Button(self.frameOperations,text="÷",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)       
        self.bt_mult = Button(self.frameOperations,text="X",font=('Arial 14'),bg='#2c302d',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        
        #=======================BOTÃO IGUAL===========================#
        self.bt_equal = Button(self.frameOperations,text="=",font=('Arial 14'),bg='#87601e',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)

        #=======================BOTÕES NUMERICOS===========================#
        self.bt_zero = Button(self.frameOperations,text="0",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)     
        self.bt_one = Button(self.frameOperations,text="1",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_two = Button(self.frameOperations,text="2",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_three = Button(self.frameOperations,text="3",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_four = Button(self.frameOperations,text="4",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_five = Button(self.frameOperations,text="5",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_six = Button(self.frameOperations,text="6",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_seven = Button(self.frameOperations,text="7",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_eight = Button(self.frameOperations,text="8",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_nine = Button(self.frameOperations,text="9",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_sign = Button(self.frameOperations,text="±",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_score = Button(self.frameOperations,text=",",font=('Arial 14'),bg='#111211',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)

        #=========================================================================================================================================#

        self.bt_percent.grid(row=0, column=0)
        self.bt_clearEntry.grid(row=0,column=1)
        self.bt_clear.grid(row=0,column=2)
        self.bt_back.grid(row=0,column=3)

        self.bt_inverse.grid(row=1, column=0)
        self.bt_pow.grid(row=1, column=1)
        self.bt_sqrt.grid(row=1, column=2)
        self.bt_div.grid(row=1, column=3)

        self.bt_seven.grid(row=2, column=0)
        self.bt_eight.grid(row=2, column=1)
        self.bt_nine.grid(row=2, column=2)
        self.bt_mult.grid(row=2, column=3)

        self.bt_four.grid(row=3, column=0)
        self.bt_five.grid(row=3, column=1)
        self.bt_six.grid(row=3, column=2)
        self.bt_sub.grid(row=3, column=3)

        self.bt_one.grid(row=4, column=0)
        self.bt_two.grid(row=4, column=1)
        self.bt_three.grid(row=4, column=2)
        self.bt_add.grid(row=4, column=3)

        self.bt_sign.grid(row=5, column=0)
        self.bt_zero.grid(row=5, column=1)
        self.bt_score.grid(row=5, column=2)
        self.bt_equal.grid(row=5, column=3)

        self.lb_result.grid(columnspan=2,sticky='we')


def main():
    root = Tk()
    Application(root)
    
    #resolução do app
    root.geometry("320x580")
    root.title("Basic Calculator")
    root.resizable(False, False)

    #icones e imagens
    root.iconbitmap("images/calculator-icon.ico")

    root.mainloop()
    
    
if __name__ == "__main__":
    main()
