from tkinter import *

class Application:

    def __init__(self,master=None):
        pass

def atributes_window(root):
    root.geometry("340x600+500+100")
    root.title("Basic Calculator")
    root.resizable(False,False)
    

def main():  
    root = Tk()
    Application(root)
    atributes_window(root)
    root.iconbitmap("images/calculator-icon.ico")
    root.mainloop()

if __name__ == "__main__":
    main()
