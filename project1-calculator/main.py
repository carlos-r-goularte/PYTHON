from tkinter import *
from math import sqrt,pow

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
        
        self.bt_percent = Button(frameOperations,text="%",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="percent": self._display(m))    
        self.bt_inverse = Button(frameOperations,text="1/x",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="inverse": self._display(m))
        self.bt_pow = Button(frameOperations,text="x²",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="pow": self._display(m))       
        self.bt_sqrt = Button(frameOperations,text="√x",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="sqrt": self._display(m))
        
        #=======================BOTÕES OPERAÇÕES BASICAS===========================#
        self.bt_add = Button(frameOperations,text="+",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="add": self._display(m))        
        self.bt_sub = Button(frameOperations,text="-",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="sub": self._display(m))       
        self.bt_div = Button(frameOperations,text="÷",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="div": self._display(m))       
        self.bt_mult = Button(frameOperations,text="x",font=('Arial 14'),bg='#131313',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="mult": self._display(m))
        
        #=======================BOTÃO IGUAL===========================#
        self.bt_equal = Button(frameOperations,text="=",font=('Arial 14'),bg='#794a12',fg='white',relief=FLAT,width=6,height=2,anchor=CENTER,command=lambda m="equal": self._display(m))

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
        
        self.lb_wait = Label(frameOperations,fg='#9c9c9c',bg="#1f1f1f",font=('Helvetica 14'),pady=30,anchor='e')
        self.lb_wait.grid(row=0,columnspan=4,sticky='news')

        self.lb_result = Label(frameOperations,fg='white',bg="#1f1f1f",font=('Helvetica 20'),anchor='e',height=3)
        self.lb_result.grid(row=1,columnspan=4,sticky='news')

        self.bt_percent.grid(row=2, column=0)
        self.bt_clearEntry.grid(row=2,column=1)
        self.bt_clear.grid(row=2,column=2)
        self.bt_back.grid(row=2,column=3)

        self.bt_inverse.grid(row=3, column=0)
        self.bt_pow.grid(row=3, column=1)
        self.bt_sqrt.grid(row=3, column=2)
        self.bt_div.grid(row=3, column=3)

        self.bt_seven.grid(row=4, column=0)
        self.bt_eight.grid(row=4, column=1)
        self.bt_nine.grid(row=4, column=2)
        self.bt_mult.grid(row=4, column=3)

        self.bt_four.grid(row=5, column=0)
        self.bt_five.grid(row=5, column=1)
        self.bt_six.grid(row=5, column=2)
        self.bt_sub.grid(row=5, column=3)

        self.bt_one.grid(row=6, column=0)
        self.bt_two.grid(row=6, column=1)
        self.bt_three.grid(row=6, column=2)
        self.bt_add.grid(row=6, column=3)

        self.bt_sign.grid(row=7, column=0)
        self.bt_zero.grid(row=7, column=1)
        self.bt_score.grid(row=7, column=2)
        self.bt_equal.grid(row=7, column=3)


    def _display(self, value):
        
        nums = ('0','1','2','3','4','5','6','7','8','9')

        if value in nums and len(self.display) < 17:
            self.display.append(value)
            strValue = "".join(self.display)
            self.lb_result['text'] = strValue
                   
        if value == '.' and self.score == False:
            self.display.append(value)
            strValue = "".join(self.display)
            self.lb_result['text'] = strValue
            self.score = True

        if value == 'clear':
            self.lb_result['text'] = '0'
            self.lb_wait['text'] = ''
            self.display = []
            self.score = False

        if value == 'clearEntry':
            self.lb_result['text'] = '0'
            self.display = []
            self.score = False

        if value == 'back':
            try:  
                if self.display.pop() == '.':
                    self.display.pop()
                    self.score = False

                strValue = "".join(self.display)
                if len(self.display) == 0:
                    self.lb_result['text'] = '0'
                    self.display = []
                else:
                    self.lb_result['text'] = strValue
            except:
                self.lb_result['text'] = '0'
    


        if value == 'add':
            self.lb_wait['text'] = self.lb_result['text']
            self.lb_result['text'] = '0'
            self.display = []
            self.score = False

        if value == 'sub':
            pass

        if value == 'div':
            pass

        if value == 'mult':
            pass

        if value == 'percent':
            pass

        if value == 'inverse':
            pass

        if value == 'pow':
            pass

        if value == 'sqrt':
            pass

        if value == 'equal':
            pass

           


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
