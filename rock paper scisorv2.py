from tkinter import *
from tkinter.messagebox import *
import random
from PIL import Image,ImageTk

class App(Tk):
    def __init__(self):
        super().__init__()
        image = Image.open("0828951849d7535bca24acce112995ef.jpg")
        resized_image = image.resize((150, 180))
        self.robot = ImageTk.PhotoImage(resized_image)
        self.label = Label(self,image=self.robot).pack(padx=150)
        self.iconphoto(True,self.robot)
        self.title("Robert")
        self.resizable(False,False)
        ############################################################
        self.frame = Frame()
        self.frame.pack()
        ############################################################
        image2 = Image.open("Background (21).png")
        resized_image2 = image2.resize((120, 120))
        self.imagescissor = ImageTk.PhotoImage(resized_image2)
        self.buttonscissor = Button(self.frame,image=self.imagescissor,borderwidth=1,relief="solid",command=lambda:self.calculation(3))
        self.buttonscissor.grid(column=2,row=0,pady=12)
        ############################################################
        image3 = Image.open("Background (22).png")
        resized_image3 = image3.resize((120, 120))
        self.imagesrock = ImageTk.PhotoImage(resized_image3)
        self.buttonrock = Button(self.frame,image=self.imagesrock,borderwidth=1,relief="solid",command=lambda:self.calculation(1))
        self.buttonrock.grid(column=0,row=0,pady=12,padx=5)
        ############################################################
        image1 = Image.open("Background (23).png")
        resizenimage1 = image1.resize((120, 120))
        self.imagepaper = ImageTk.PhotoImage(resizenimage1)
        self.buttonpaper = Button(self.frame,image=self.imagepaper,borderwidth=1,relief="solid",command=lambda:self.calculation(2))
        self.buttonpaper.grid(column=1,row=0,pady=12,padx=5)

    def calculation(self,valeur):
        computer_choice = random.randint(1,3)
        # 1 is rock, 2 is paper, 3 is scisors
        if valeur == computer_choice:
            showinfo("Tie", "Its a tie.")
        elif valeur == 1: # rock
            if computer_choice == 2: #paper
                showerror("You lost","Robert wins")
            else:
                showinfo("Win","You won")
        elif valeur == 2: #rock
            if computer_choice == 3: #scissors
                showinfo("Win", "You won")
            else:
                showerror("You lost","Robert wins")
        elif valeur == 3:#paper
            if computer_choice == 1:#scissor
                showerror("You lost","Robert wins")
            else:
                showinfo("Win", "You won")
if __name__ == "__main__":
    app = App()
    app.mainloop()