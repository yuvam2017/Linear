from tkinter import *
root = Tk()
root.title('LINEAR EQUATION SOLVER')
root.configure(bg='orange')


########## Functions #####################
def solve(a1,b1,c1,a2,b2,c2):
     txt.delete('1.0',END)
     if a1 ==0 or b1==0 or c1==0 or a2==0 or b2 ==0 or c2==0:
          if a2 ==0 or b2==0 or c2==0:
               a1,a2=a2,a1
               b1,b2=b2,b1
               c1,c2=c2,c1
               
     if a1/a2 == b1/b2 == c1/c2:
          txt.insert(END,'The Two Lines equation entered is concident \n')
          txt.insert(END,'As we know for concident line\n')
          txt.insert(END,'a\u2081/a\u2082 = b\u2081/b\u2082 = c\u2081/c\u2082\n')
          txt.insert(END,f'Here a\u2081={a1} b\u2081={b1} c\u2081={c1}\n')
          txt.insert(END,f'a\u2082={a2} b\u2082={b2} c\u2082={c2}\n')
          txt.insert(END,f'So the condition is satisfied by the equation\n')
          txt.insert(END,f'a\u2081/a\u2082 = {a1}/{a2} = {a1/a2}\n')
          txt.insert(END,f'b\u2081/b\u2082 = {b1}/{b2} = {b1/b2}\n')
          txt.insert(END,f'c\u2081/c\u2082 = {c1}/{c2} = {c1/c2}\n')
          txt.insert(END,f'Infinite solution of the equation\n As the lines are concident\n ')
     elif a1/a2 == b1/b2 != c1/c2:
          txt.insert(END,f'The Two lines are parallel to each other\n')
          txt.insert(END,f'As we know for the parallel lines\n')
          txt.insert(END,f'a\u2081/a\u2082 = b\u2081/b\u2082 \n')
          txt.insert(END,f'Here a\u2081={a1} b\u2081={b1} \n')
          txt.insert(END,f'Here a\u2082={a2} b\u2082={b2} \n')
          txt.insert(END,f'So a\u2081/a\u2082 = {a1}/{a2} = {a1/a2}\n')
          txt.insert(END,f'and b\u2081/b\u2082 = {b1}/{b2} = {b1/b2}\n')
          txt.insert(END,f'No solution of the equation\n As the lines are parallel\n')
     elif a1/a2 != b1/b2 != c1/c2:
          txt.insert(END,f'The pair of line is intersecting\n And has a unique solution\n')
          txt.insert(END,f'Here a\u2081={a1} b\u2081={b1} c\u2081={c1}\n')
          txt.insert(END,f' a\u2082={a2} b\u2082={b2} c\u2082={c2}\n')
          txt.insert(END,'x=(b1*c2 - b2*c1)/(a1*b2-a2*b1)\n\n\n')
          #x = (b1*c2 - b2*c1)/(a1*b2-a2*b1)
          #y = (c1*a2-c2*a1)/(a1*b2-a2*b1)
          num1 = (b1*c2-b2*c1)
          num2 = (c1*a2-c2*a1)
          den  = (a1*b2-a2*b1)
          if (num1//den)*den == num1:
               txt.insert(END,f'x = ({b1}*{c2} - {b2}*{c1})/({a1}*{b2} - {a2}*{b1})\n')
               txt.insert(END,f'x = ({b1*c2} - {b2*c1})/({a1*b2} - {a2*b1})\n')
               txt.insert(END,f'x = ({(b1*c2) - (b2*c1)})/({(a1*b2) - (a2*b1)})\n')
               txt.insert(END,f'x = {(b1*c2 - b2*c1)//(a1*b2-a2*b1)}\n\n\n')
               txt.insert(END,'y = (c1*a2-c2*a1)/(a1*b2-a2*b1)\n')
               if (num2//den)*den == num2:
                    txt.insert(END,f'y = ({c1}*{a2} - {c2}*{a1})/({a1}*{b2} - {a2}*{b1})\n')
                    txt.insert(END,f'y = ({c1*a2} - {c2*a1})/({a1*b2} - {a2*b1})\n')
                    txt.insert(END,f'y = ({(c1*a2) - (c2*a1)})/({(a1*b2) - (a2*b1)})\n')
                    txt.insert(END,f'y = {(c1*a2 - c2*a1)//(a1*b2-a2*b1)}\n')
               else:
                    txt.insert(END,f'y = ({c1}*{a2} - {c2}*{a1})/({a1}*{b2} - {a2}*{b1})\n')
                    txt.insert(END,f'y = ({c1*a2} - {c2*a1})/({a1*b2} - {a2*b1})\n')
                    txt.insert(END,f'y = ({(c1*a2) - (c2*a1)})/({(a1*b2) - (a2*b1)})\n')
                    txt.insert(END,f'y = {(c1*a2 - c2*a1)}/{(a1*b2-a2*b1)}\n')
                    
          else:
               txt.insert(END,f'x = ({b1}*{c2} - {b2}*{c1})/({a1}*{b2} - {a2}*{b1})\n')
               txt.insert(END,f'x = ({b1*c2} - {b2*c1})/({a1*b2} - {a2*b1})\n')
               txt.insert(END,f'x = ({(b1*c2) - (b2*c1)})/({(a1*b2) - (a2*b1)})\n')
               txt.insert(END,f'x = {(b1*c2 - b2*c1)}/{(a1*b2-a2*b1)}\n\n\n')
               txt.insert(END,'y = (c1*a2-c2*a1)/(a1*b2-a2*b1)\n')
               if (num2//den)*den == num2:
                    txt.insert(END,f'y = ({c1}*{a2} - {c2}*{a1})/({a1}*{b2} - {a2}*{b1})\n')
                    txt.insert(END,f'y = ({c1*a2} - {c2*a1})/({a1*b2} - {a2*b1})\n')
                    txt.insert(END,f'y = ({(c1*a2) - (c2*a1)})/({(a1*b2) - (a2*b1)})\n')
                    txt.insert(END,f'y = {(c1*a2 - c2*a1)//(a1*b2-a2*b1)}\n')
               else:
                    txt.insert(END,f'y = ({c1}*{a2} - {c2}*{a1})/({a1}*{b2} - {a2}*{b1})\n')
                    txt.insert(END,f'y = ({c1*a2} - {c2*a1})/({a1*b2} - {a2*b1})\n')
                    txt.insert(END,f'y = ({(c1*a2) - (c2*a1)})/({(a1*b2) - (a2*b1)})\n')
                    txt.insert(END,f'y = {(c1*a2 - c2*a1)}/{(a1*b2-a2*b1)}\n')
               
               
               
def reset():
     
     entry_a1.delete(0,END)
     entry_b1.delete(0,END)
     entry_c1.delete(0,END)
     entry_a2.delete(0,END)
     entry_b2.delete(0,END)
     entry_c2.delete(0,END)
     txt.delete('1.0',END)
def dark():
     txt.configure(bg='black',fg='white')
     root.configure(bg='black')
     label_head.configure(bg='black',fg='white')
     frame_head.configure(bg='black')
     frame_eq.configure(bg='black')
     frame_sol.configure(bg='black')
     label1.configure(bg='black',fg='white')
     label2.configure(bg='black',fg='white')
     label3.configure(bg='black',fg='white')
     label4.configure(bg='black',fg='white')
     label5.configure(bg='black',fg='white')
     label6.configure(bg='black',fg='white')
     label_first.configure(bg='black',fg='white')
     label_sec.configure(bg='black',fg='white')
     label_x1.configure(bg='black',fg='white')
     label_y1.configure(bg='black',fg='white')
     label_x2.configure(bg='black',fg='white')
     label_y2.configure(bg='black',fg='white')
     label_7.configure(bg='black',fg='white')
     label_9.configure(bg='black',fg='white')
     label_11.configure(bg='black',fg='white')
     label_12.configure(bg='black',fg='white')
def light():
     txt.configure(bg='white',fg='blue')
     root.configure(bg='white')
     label_head.configure(bg='white',fg='black')
     frame_head.configure(bg='white')
     frame_eq.configure(bg='white')
     frame_sol.configure(bg='white')
     label1.configure(fg='black',bg='white')
     label2.configure(fg='black',bg='white')
     label3.configure(fg='black',bg='white')
     label4.configure(fg='black',bg='white')
     label5.configure(fg='black',bg='white')
     label6.configure(fg='black',bg='white')
     label_first.configure(fg='black',bg='white')
     label_sec.configure(fg='black',bg='white')
     label_x1.configure(fg='black',bg='white')
     label_y1.configure(fg='black',bg='white')
     label_x2.configure(fg='black',bg='white')
     label_y2.configure(fg='black',bg='white')
     label_7.configure(fg='black',bg='white')
     label_9.configure(fg='black',bg='white')
     label_11.configure(fg='black',bg='white')
     label_12.configure(fg='black',bg='white')
def normal():
     txt.configure(bg='white',fg='blue')
     root.configure(bg='orange')
     label_head.configure(bg='orange',fg='white')
     frame_head.configure(bg='orange')
     frame_eq.configure(bg='orange')
     frame_sol.configure(bg='orange')
     label1.configure(bg='orange',fg='white')
     label2.configure(bg='orange',fg='white')
     label3.configure(bg='orange',fg='white')
     label4.configure(bg='orange',fg='white')
     label5.configure(bg='orange',fg='white')
     label6.configure(bg='orange',fg='white')
     label_first.configure(bg='orange',fg='white')
     label_sec.configure(bg='orange',fg='white')
     label_x1.configure(bg='orange',fg='black')
     label_y1.configure(bg='orange',fg='black')
     label_x2.configure(bg='orange',fg='black')
     label_y2.configure(bg='orange',fg='black')
     label_7.configure(bg='orange',fg='white')
     label_9.configure(bg='orange',fg='white')
     label_11.configure(bg='orange',fg='white')
     label_12.configure(bg='orange',fg='white')





# frame for LINEAR EQUATION SOLVER Heading
frame_head = Frame(root,bd=15,bg='orange',relief=RAISED)
label_head = Label(frame_head,text="LINEAR EQUATION SOLVER",fg='white',font='comicsansms 60 bold',bg='orange',pady=50)
label_head.pack(anchor="center")

#frame for equation

frame_eq = Frame(root,bd=15,bg='orange',relief=RAISED)
label1 = Label(frame_eq,text=' ',bg='orange',fg='orange')
label1.grid(row=0,column=0)
label2 = Label(frame_eq,text=' ',bg='orange',fg='orange')
label2.grid(row=1,column=0)
label3 = Label(frame_eq,text=' ',bg='orange',fg='orange')
label3.grid(row=2,column=0)
label4 = Label(frame_eq,text=' ',bg='orange',fg='orange')
label4.grid(row=3,column=0)
label5 = Label(frame_eq,text=' ',bg='orange',fg='orange')
label5.grid(row=4,column=0)
label6 = Label(frame_eq,text=' ',bg='orange',fg='orange')
label6.grid(row=5,column=0)

label_first = Label(frame_eq,text="First equation: ",fg="white",font="comicsansms 24 bold",bg="orange")
label_first.grid(row=6,column=0)#col=0
entry_a1 = Entry(frame_eq,bd=2,bg="white",width=8,fg="black") #col =1
entry_a1.grid(row=6,column=1)
label_x1 = Label(frame_eq,text=" x + ",fg="black",font="comicsansms 15",bg="orange")
label_x1.grid(row=6,column=2)#col = 2
entry_b1 = Entry(frame_eq,bd=2,bg="white",width=8,fg="black")#col = 3
entry_b1.grid(row=6,column=3)
label_y1 = Label(frame_eq,text=" y + ",fg="black",font="comicsansms 15",bg="orange")
label_y1.grid(row=6,column=4)# col =4
entry_c1 = Entry(frame_eq,bd=2,bg="white",width=8,fg="black")#col =5
entry_c1.grid(row=6,column=5,padx=5)
label_7 = Label(frame_eq,text=' ',bg='orange')
label_7.grid(row=7,column=0)


label_sec = Label(frame_eq,text="Second equation: ",fg="white",font="comicsansms 20 bold",bg="orange")
label_sec.grid(row=8,column=0)#col=0
entry_a2 = Entry(frame_eq,bd=2,bg="white",width=8,fg="black") #col =1
entry_a2.grid(row=8,column=1)
label_x2 = Label(frame_eq,text=" x + ",fg="black",font="comicsansms 15",bg="orange")#col = 2
label_x2.grid(row=8,column=2)
entry_b2 = Entry(frame_eq,bd=2,bg="white",width=8,fg="black")#col = 3
entry_b2.grid(row=8,column=3)
label_y2 = Label(frame_eq,text=" y + ",fg="black",font="comicsansms 15",bg="orange")# col =4
label_y2.grid(row=8,column=4)
entry_c2 = Entry(frame_eq,bd=2,bg="white",width=8,fg="black")#col =5
entry_c2.grid(row=8,column=5,padx=5)
label_9 = Label(frame_eq,text=' ',bg='orange')
label_9.grid(row=9,column=0)

btn_submit = Button(frame_eq,text="Submit",font='comicsansms 20 bold',fg="black",bg='white',width=10,bd=5,command=lambda: solve(int(entry_a1.get()),int(entry_b1.get()),int(entry_c1.get()),int(entry_a2.get()),int(entry_b2.get()),int(entry_c2.get())))
btn_submit.grid(row=10,column=0,columnspan=6,sticky='news')

label_11 = Label(frame_eq,text=' ',bg='orange')
label_11.grid(row=11,column=0)
label_12 = Label(frame_eq,text=' ',bg='orange')
label_12.grid(row=12,column=0)

btn_light = Button(frame_eq,text='Light theme',font='Courier 15 bold',fg='black',bg='white',bd=2,
                   command= lambda: light()).grid(row=13,column=0,sticky='news')
btn_normal = Button(frame_eq,text="Normal",font='Courier 15 bold',fg='black',bg='white',bd=2,
                   command= lambda: normal()).grid(row=13,column=1,sticky='news')
btn_dark = Button(frame_eq,text="Dark Theme",font='Courier 15 bold',fg='black',bg='white',bd=2,
                  command =lambda: dark()).grid(row=13,column=2,columnspan=4,sticky='news')

# Frame for  Notes, heading and solution
frame_sol = Frame(root,bd=15,bg='orange',relief=RAISED)
txt = Text(frame_sol,height=17,width=42,font ='comicsansms 15',bg='white',fg='blue')
txt.grid(row=0,column=0,columnspan=2)
btn_reset = Button(frame_sol,text='Reset',bg='white',fg='black',font='Courier 15 bold',bd=2,
                   command= reset,width=10)

btn_reset.grid(row=1,column=0)

btn_quit = Button(frame_sol,text='Quit',bg='white',fg='black',font='Courier 15 bold',bd=2,
                  command=root.destroy,width=10)

btn_quit.grid(row=1,column=1)



#putting on the screen
frame_head.pack(fill=BOTH,side=TOP)
frame_eq.pack(side=LEFT,fill='y',anchor=CENTER,ipadx=50)
frame_sol.pack(side=RIGHT,fill='both')


root.mainloop()
