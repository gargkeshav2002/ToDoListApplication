from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter import filedialog
root = Tk()
root.geometry("1000x700")
root.title("Planner")
# img = PhotoImage(file="C:\\Users\\HP\\Downloads\\planner.png")
# root.iconphoto(False,img)

def add():
    work = en1.get()
    if work != "":
        lsb.insert(END, work)
        en1.delete(0,END)
    else:
        tmsg.showwarning("NULL", "Please enter some task")

def clear():
    en1.delete(0, END)
def delete():
    lsb.delete(0, END)

def add_G():
    gr = G_en.get()
    G_lsb.insert(END, gr)
def Del_G():
    G_lsb.delete(0, END)

def Exit():
    tmsg.showwarning("Thank you", "Hope your day was productive")
    root.destroy()

def save():
    file = filedialog.asksaveasfile(defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*"),
                                    ])
    if file is None:
        return
    filetext = str(Y_text.get(1.0,END))
    file.write(f"productivity={slider.get()}\n")
    file.write(filetext)
    file.close()



def crossof():
    lsb.itemconfig(lsb.curselection(), fg="red")
    lsb.selection_clear(0,END)
def uncross():
    lsb.itemconfig(lsb.curselection(), fg="black")
    lsb.selection_clear(0, END)

# 1st fame starts here
f1 = Frame(root, bg="#800080")
f1.place(relwidth=0.5, relheight=1)

D_text = Text(f1, bg="white")
D_text.place(relx=0.8, relwidth=0.8, relheight=0.04, anchor='n')

l1 = Label(f1, text="Day & Date:", font="Helvetica 16 underline", bg="orange") # import day and time
l1.place(relx=0.2,relwidth=0.4, relheight=0.04, anchor='n')

l2 = Label(f1, text="Plan your day", font="Cursive 28 bold underline", bg="#800080", fg="white")
l2.place(relx=0.5,rely=0.06,relwidth=0.8, relheight=0.06, anchor='n')

l3 = Label(f1, text="I am gratitude for:", font="Courier 12 bold underline", bg="orange")
l3.place(relx=0.35,rely=0.16,relwidth=0.4, relheight=0.04, anchor='n')

G_lsb = Listbox(f1, bg="white", font="18")
G_lsb.place(relx=0.5,rely=0.2, relwidth=0.7, relheight=0.3, anchor='n')
G_en = Entry(f1,width=89,bg="white")
G_en.place(rely=0.52, relx=0.15)
b_g = Button(f1, text="Add Gratitude", width=10, command=add_G,relief=SUNKEN, borderwidth=3, bg="orange", fg="black").place(rely=0.55, relx=0.14)
b_gD = Button(f1, text="Delete", width=10, command=Del_G,relief=SUNKEN, borderwidth=3,bg="orange", fg="black").place(rely=0.55, relx=0.74)

l4 = Label(f1, text="*Goals-Daily/Weekly/Monthly/Yearly",font="Courier 11 bold underline", bg="orange")
l4.place(relx=0.5, rely=0.59, relwidth=0.5, relheight=0.05, anchor='n')
Y_l = Label(f1, text="Enter in the below space:", bg="orange")
Y_l.place(relx=0.282, rely=0.66, relwidth=0.3, relheight=0.03, anchor='n')

Y_text = Text(root, bg="white")
Y_text.place(relx=0.24,rely=0.99, relwidth=0.35, relheight=0.3, anchor='s')
Button(text="save", command=save, relief=SUNKEN).place(relx=0.45,rely=0.98, relwidth=0.06, relheight=0.05, anchor='s')
# 1st frame ends here
#mainMenu = Menu(root)
#m1 = Menu(mainMenu, tearoff=0)
#m1.add_command(label="save", command=save)
#mainMenu.add_cascade(label="save", menu=m1)
#root.config(menu=mainMenu)
# Second frame starts here
f2 = Frame(root, bg="orange")
f2.place(relx=1, rely=1, relwidth=0.5, relheight=2, anchor='e')

P_l = Label(f2,text="My Top 3 priorities", font="Roman 16 bold underline", bg="#800080", fg="white")
P_l.place(relx=0.5,relwidth=0.4, relheight=0.02, anchor='n')

p1_text = Text(f2, bg="white") # align in center
p1_text.place(relx=0.16,rely=0.03, relwidth=0.2, relheight=0.05, anchor='n')
var = StringVar()
#radio = Radiobutton(f2, text="Tick", variable=var, value="tick", padx=11).place(rely=0.5, relx=0.5, anchor="nw")

p2_text = Text(f2, bg="white")
p2_text.place(relx=0.5,rely=0.03, relwidth=0.2, relheight=0.05, anchor='n')

p3_text = Text(f2, bg="white")
p3_text.place(relx=0.8,rely=0.03, relwidth=0.2, relheight=0.05, anchor='n')

l5 = Label(f2, text="Today's Plan->",font="Roman 16 bold underline", bg="#800080", fg="white")
l5.place(relx=0.28, rely=0.11, relwidth=0.4, relheight=0.02, anchor='n')

# Now I will create a list box with entry
lsb = Listbox(f2, height=20, width=90, activestyle="none", selectbackground="#800080")
lsb.place(rely=0.13, relx=0.08)
en1 = Entry(f2,width=90,bg="white")
en1.place(rely=0.35, relx=0.08)
en_l = Label(f2, text="Enter your task:",bg="#800080",fg="white")
en_l.place(rely=0.3365, relx=0.08)

b1 = Button(f2, text="Add Task", width=76, command=add, relief=SUNKEN, borderwidth=3,bg="#800080", fg="white").place(rely=0.37, relx=0.08)
b2 = Button(f2, text="Clear", width=76, command=clear, relief=SUNKEN, borderwidth=3,bg="#800080", fg="white").place(rely=0.39, relx=0.08)
b3 = Button(f2,text="Delete All Tasks", width=76, command=delete, relief=SUNKEN, borderwidth=3,bg="#800080", fg="white").place(rely=0.45, relx=0.08)
b5 = Button(f2, text="Cross off",width=76, command=crossof, relief=SUNKEN, borderwidth=3, bg="#800080", fg="white").place(rely=0.41, relx=0.08)
b6 = Button(f2, text="Uncross",width=76, command=uncross, relief=SUNKEN, borderwidth=3, bg="#800080", fg="white").place(rely=0.43, relx=0.08)
b4 = Button(f2, text="Exit",width=20, command=Exit, relief=SUNKEN, borderwidth=3, bg="#800080", fg="white").place(rely=0.48, relx=0.59)


slider = Scale(f2,from_=0, to=10, bg="#800080",fg="white")
slider.place(rely=0.13, relx=0.8, relwidth=0.06,relheight=0.2, anchor="nw")

#V_l = Label(f2, text="Rate| your| productivity!")
#V_l.place(rely=0.13, relx=0.1, relwidth=0.06,relheight=0.2, anchor="nw",orientation=)
Label(f2, text="Rate-Your-Productivity", wraplength=1, bg="#800080",  font="bold", fg="white").place(rely=0.09, relx=0.9, relwidth=0.06,relheight=0.4, anchor="nw")

root.mainloop()