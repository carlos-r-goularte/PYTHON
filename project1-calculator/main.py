from tkinter import *

class Application:

    def __init__(self, master):

        #=======================FRAMES===========================#
        self.widget = Frame(master)
        frameOperations = self.widget
        frameOperations.pack()

        self.display = []
        self.score = False
        #=======================BOTÕES OPERAÇÕES ADICIONAIS===========================#
        self.bt_clear = Button(frameOperations,text="C",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="clear": self._display(m))
        self.bt_clearEntry = Button(frameOperations,text="CE",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="clearEntry": self._display(m))
        self.bt_back = Button(frameOperations,text="<<",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="back": self._display(m))
        self.bt_percent = Button(frameOperations,text="%",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)    
        self.bt_inverse = Button(frameOperations,text="1/x",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        self.bt_pow = Button(frameOperations,text="x²",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)       
        self.bt_sqrt = Button(frameOperations,text="√x",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        
        #=======================BOTÕES OPERAÇÕES BASICAS===========================#
        self.bt_add = Button(frameOperations,text="+",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)        
        self.bt_sub = Button(frameOperations,text="—",font=('Arial 12'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)       
        self.bt_div = Button(frameOperations,text="÷",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)       
        self.bt_mult = Button(frameOperations,text="x",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)
        
        #=======================BOTÃO IGUAL===========================#
        self.bt_equal = Button(frameOperations,text="=",font=('Arial 14'),bg='#794a12',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER)

        #=======================BOTÕES NUMERICOS===========================#
        self.bt_zero = Button(frameOperations,text="0",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="0": self._display(m))
        self.bt_one = Button(frameOperations,text="1",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="1": self._display(m))        
        self.bt_two = Button(frameOperations,text="2",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="2": self._display(m))        
        self.bt_three = Button(frameOperations,text="3",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="3": self._display(m))        
        self.bt_four = Button(frameOperations,text="4",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="4": self._display(m))        
        self.bt_five = Button(frameOperations,text="5",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="5": self._display(m))        
        self.bt_six = Button(frameOperations,text="6",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="6": self._display(m))        
        self.bt_seven = Button(frameOperations,text="7",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="7": self._display(m))        
        self.bt_eight = Button(frameOperations,text="8",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="8": self._display(m))        
        self.bt_nine = Button(frameOperations,text="9",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="9": self._display(m))        
        self.bt_sign = Button(frameOperations,text="±",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="sign": self._display(m))        
        self.bt_score = Button(frameOperations,text=",",font=('Arial 14'),bg='#060606',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m=".": self._display(m))

        #=========================================================================================================================================#
        
        self.lb_result = Label(frameOperations,fg='white',bg="#1f1f1f",font=('Arial 20 bold'),anchor='e',height=5)
        self.lb_result.grid(row=0,columnspan=4,sticky='wens')
        self.lb_result.propagate(0)


        self.bt_percent.grid(row=1, column=0)
        self.bt_clearEntry.grid(row=1,column=1)
        self.bt_clear.grid(row=1,column=2)
        self.bt_back.grid(row=1,column=3)

        self.bt_inverse.grid(row=2, column=0)
        self.bt_pow.grid(row=2, column=1)
        self.bt_sqrt.grid(row=2, column=2)
        self.bt_div.grid(row=2, column=3)

        self.bt_seven.grid(row=3, column=0)
        self.bt_eight.grid(row=3, column=1)
        self.bt_nine.grid(row=3, column=2)
        self.bt_mult.grid(row=3, column=3)

        self.bt_four.grid(row=4, column=0)
        self.bt_five.grid(row=4, column=1)
        self.bt_six.grid(row=4, column=2)
        self.bt_sub.grid(row=4, column=3,sticky='wens')

        self.bt_one.grid(row=5, column=0)
        self.bt_two.grid(row=5, column=1)
        self.bt_three.grid(row=5, column=2)
        self.bt_add.grid(row=5, column=3)

        self.bt_sign.grid(row=6, column=0)
        self.bt_zero.grid(row=6, column=1)
        self.bt_score.grid(row=6, column=2)
        self.bt_equal.grid(row=6, column=3)

    def _display(self, value):
        
        nums = ('0','1','2','3','4','5','6','7','8','9')

        if value in nums and len(self.display) < 12:
                self.display.append(value)
                self.lb_result['text'] = self.display
        
        if value == '.' and self.score == False:
            self.display.append(value)
            self.lb_result['text'] = self.display
            self.score = True

        if value == 'clear':
            self.display = ['0']
            self.lb_result['text'] = self.display
            self.display = []

        if value == 'back':
            try:
                self.display.pop()
                if len(self.display) == 0:
                    self.display = ['0']
                    self.lb_result['text'] = self.display
                    self.display = []
                else:
                    self.lb_result['text'] = self.display
            except:
                self.display = ['0']
                self.lb_result['text'] = self.display

def main():
    root = Tk()
    Application(root)

    #resolução do app
    root.geometry("310x550")
    root.title("Basic Calculator")
    root.resizable(False, False)
    root.configure(bg='#1f1f1f')

    #icones e imagens
    root.iconbitmap("images/calculator-icon.ico")

    root.mainloop()

if __name__ == "__main__":
    main()
