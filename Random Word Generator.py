from tkinter import *
import random

root=Tk()
root.title("Random Number Generator")
root.geometry("400x400")
root.configure(background="blue")

title=Label(root,text="Random Word Generator")

def NG():
    alpha_list=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    N1_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18,19,20,21,22,23,24,25,26]
    N2_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18,19,20,21,22,23,24,25,26]
    N3_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18,19,20,21,22,23,24,25,26]
    N4_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18,19,20,21,22,23,24,25,26]
    N5_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,27,18,19,20,21,22,23,24,25,26]
    N1_list=random.randint(1,26)
    N2_list=random.randint(1,26)
    N3_list=random.randint(1,26)
    N4_list=random.randint(1,26)
    N5_list=random.randint(1,26)
    N1=alpha_list[N1_list]
    N2=alpha_list[N2_list]
    N3=alpha_list[N3_list]
    N4=alpha_list[N4_list]
    N5=alpha_list[N5_list]
    text["text"]=str(N1)+str(N2)+str(N3)+str(N4)+str(N5)
    
button1=Button(root,text="Generate",command=NG)
text=Label(root)
title.place(relx=0.5, rely=0.4, anchor=CENTER)
button1.place(relx=0.5, rely=0.5, anchor=CENTER)
text.place(relx=0.5, rely=0.6, anchor=CENTER)

root.mainloop()