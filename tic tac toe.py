from tkinter import *
from tkinter import messagebox

player1 = 'Гравець 1'
player2 = 'Гравець 2'
button_arr = [[],[],[]]
isActivePlayer1 = True

tk = Tk()
playerLbl = Label(tk, text=player1, font= ('Calibri', 30, 'bold'))
playerLbl.grid(row=0, column=0, columnspan=3)

class T_F:
    x00 = False
    x01 = False
    x02 = False
    x10 = False
    x11 = False
    x12 = False
    x20 = False
    x21 = False
    x22 = False
    
    o00 = False
    o01 = False
    o02 = False
    o10 = False
    o11 = False
    o12 = False
    o20 = False
    o21 = False
    o22 = False
    
    def __init__(self, x00, x01, x02, x10, x11, x12, x20, x21, x22, o00, o01, o02, o10, o11, o12, o20, o21, o22):
        self.x00 = x00
        self.x01 = x01
        self.x02 = x02
        self.x10 = x10
        self.x11 = x11
        self.x12 = x12
        self.x20 = x20
        self.x21 = x21
        self.x22 = x22
        
        self.o00 = o00
        self.o01 = o01
        self.o02 = o02
        self.o10 = o10
        self.o11 = o11
        self.o12 = o12
        self.o20 = o20
        self.o21 = o21
        self.o22 = o22
    
    
def oxT():
    x00 = button_arr[0][0]['text'] == 'X'
    x01 = button_arr[0][1]['text'] == 'X'
    x02 = button_arr[0][2]['text'] == 'X'
    x10 = button_arr[1][0]['text'] == 'X'
    x11 = button_arr[1][1]['text'] == 'X'
    x12 = button_arr[1][2]['text'] == 'X'
    x20 = button_arr[2][0]['text'] == 'X'
    x21 = button_arr[2][1]['text'] == 'X'
    x22 = button_arr[2][2]['text'] == 'X'
    
    o00 = button_arr[0][0]['text'] == 'O'
    o01 = button_arr[0][1]['text'] == 'O'
    o02 = button_arr[0][2]['text'] == 'O'
    o10 = button_arr[1][0]['text'] == 'O'
    o11 = button_arr[1][1]['text'] == 'O'
    o12 = button_arr[1][2]['text'] == 'O'
    o20 = button_arr[2][0]['text'] == 'O'
    o21 = button_arr[2][1]['text'] == 'O'
    o22 = button_arr[2][2]['text'] == 'O'
    
    T_F.__init__(T_F, x00, x01, x02, x10, x11, x12, x20, x21, x22, o00, o01, o02, o10, o11, o12, o20, o21, o22)


def Victori(g):
    if g == 1:
        messagebox.showinfo("Перемога", "Перший гравець переміг!")
    if g == 2:
        messagebox.showinfo("Перемога", "Другий гравець переміг!")

def checkWinCombination():
    oxT()
    
    if T_F.x00 and T_F.x01 and T_F.x02:
        Victori(1)
    if T_F.x10 and T_F.x11 and T_F.x12:
        Victori(1)
    if T_F.x20 and T_F.x21 and T_F.x22:
        Victori(1)
    if T_F.x00 and T_F.x11 and T_F.x22:
        Victori(1)
    if T_F.x02 and T_F.x11 and T_F.x20:
        Victori(1)
    if T_F.x00 and T_F.x10 and T_F.x20:
        Victori(1)
    if T_F.x01 and T_F.x11 and T_F.x21:
        Victori(1)
    if T_F.x02 and T_F.x12 and T_F.x22:
        Victori(1)
        
        
    if T_F.o00 and T_F.o01 and T_F.o02:
        Victori(2)
    if T_F.o10 and T_F.o11 and T_F.o12:
        Victori(2)
    if T_F.o20 and T_F.o21 and T_F.o22:
        Victori(2)
    if T_F.o00 and T_F.o11 and T_F.o22:
        Victori(2)
    if T_F.o02 and T_F.o11 and T_F.o20:
        Victori(2)
    if T_F.o00 and T_F.o10 and T_F.o20:
        Victori(2)
    if T_F.o01 and T_F.o11 and T_F.o21:
        Victori(2)
    if T_F.o02 and T_F.o12 and T_F.o22:
        Victori(2)
        

def button_click(row, column):
    global button_arr
    global isActivePlayer1
    
    if button_arr[row][column]['text'] =='':
        if isActivePlayer1:
            button_arr[row][column].config(text = "X")
            playerLbl.config(text=player2)
        else:
            button_arr[row][column].config(text = "O")
            playerLbl.config(text=player1)
        checkWinCombination()
        isActivePlayer1 = not isActivePlayer1

    
for i in range(3):
    for j in range(3):
        button_arr[i].append(
            Button(
                tk,
                text='',
                font = ('Calibri', 20, 'bold'),
                width = 6,
                height = 2,
                bg = 'lightblue'
                )
            )
        button_arr[i][j].grid(row = i + 1, column = j, padx = 2, pady = 2)
        button_arr[i][j].config(command = lambda r = i, c = j: button_click(r, c))

tk.mainloop()