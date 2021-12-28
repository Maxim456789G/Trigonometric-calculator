a = 350
b = 400

import tkinter as tk
from PIL import Image
from PIL import ImageTk



window = tk.Tk()
window1 = tk.Tk()

frame = tk.Frame(window)
frame.grid()


window1.geometry(f'{a}x{b}+725+200')
window1.resizable(False, False)
window1.title('Trigonometric Сalculator - B&')
window1.config(bg = 'white')

window.geometry(f'{a}x{b}+350+200')
window.resizable(False, False)
window.title('Trigonometric Сalculator - A&')
window.config(bg = 'white')


#F-n tr windows
def get_entrys_cos():
	val_cos_ac = int(enter_ac.get())
	val_cos_ab = int(enter_ab.get())
	if val_cos_ac and val_cos_ab:
		print(val_cos_ac/val_cos_ab)
	else:
		print("Error")
	answer_cos = tk.Label(window, text = val_cos_ac/val_cos_ab,
						bg = 'white')
	answer_cos.grid(row = 6, column = 1)

def get_entrys_sin():
	val_sin_bc = int(enter_bc.get())
	val_sin_ab = int(enter_ab.get())
	if val_sin_bc and val_sin_ab:
		print(val_sin_bc/val_sin_ab)
	else:
		print("Error")
	answer_sin = tk.Label(window, text = val_sin_bc/val_sin_ab,
							bg = 'white')
	answer_sin.grid(row = 6, column = 1)

def get_entrys_tg():
	val_tg_bc = int(enter_bc.get())
	val_tg_ac = int(enter_ac.get())
	if val_tg_ac and val_tg_bc:
		print(val_tg_bc/val_tg_ac)
	else:
		print("Error")
	answer_tg = tk.Label(window, text = val_tg_bc/val_tg_ac,
    						bg = 'white')
	answer_tg.grid(row = 6, column = 1)

def get_entrys_cAtg():
	val_cAtg_ac = int(enter_ac.get())
	val_cAtg_bc = int(enter_bc.get())
	if val_cAtg_ac and val_cAtg_bc:
		print(val_cAtg_ac/val_cAtg_bc)
	else:
		print("Error")
	answer_cAtg = tk.Label(window, text = val_cAtg_ac/val_cAtg_bc,
    						bg = 'white')

	answer_cAtg.grid(row = 6, column = 1)


#F-n tr windows1
def get_entrys_cos1():
	val_cos_bc = int(enter_bc1.get())
	val_cos_ab = int(enter_ab1.get())
	if val_cos_bc and val_cos_ab:
		print(val_cos_bc/val_cos_ab)
	else:
		print("Error")
	answer_cos = tk.Label(window1, text = val_cos_bc/val_cos_ab,
						bg = 'white')
	answer_cos.grid(row = 6, column = 1)

def get_entrys_sin1():
	val_sin_ac = int(enter_ac1.get())
	val_sin_ab = int(enter_ab1.get())
	if val_sin_ac and val_sin_ab:
		print(val_sin_ac/val_sin_ab)
	else:
		print("Error")
	answer_sin = tk.Label(window1, text = val_sin_ac/val_sin_ab,
							bg = 'white')
	answer_sin.grid(row = 6, column = 1)

def get_entrys_tg1():
	val_tg_ac = int(enter_ac1.get())
	val_tg_bc = int(enter_bc1.get())
	if val_tg_ac and val_tg_bc:
		print(val_tg_ac/val_tg_bc)
	else:
		print("Error")
	answer_tg = tk.Label(window1, text = val_tg_ac/val_tg_bc,
    						bg = 'white')
	answer_tg.grid(row = 6, column = 1)

def get_entrys_cAtg1():
	val_cAtg_bc = int(enter_bc1.get())
	val_cAtg_ac = int(enter_ac1.get())
	if val_cAtg_bc and val_cAtg_ac:
		print(val_cAtg_bc/val_cAtg_ac)
	else:
		print("Error")
	answer_cAtg = tk.Label(window1, text = val_cAtg_bc/val_cAtg_ac,
    						bg = 'white')

	answer_cAtg.grid(row = 6, column = 1)


#strings window
enter_ab = tk.Entry(window)
enter_bc = tk.Entry(window)
enter_ac = tk.Entry(window)

#etring window1
enter_ab1 = tk.Entry(window1)
enter_bc1 = tk.Entry(window1)
enter_ac1 = tk.Entry(window1)

#texts window

action = tk.Label(window, text = 'Action A:',
					bg = 'white',
					width = 50)

text_ab = tk.Label(window, text = "AB:",
					bg = "white")
text_bc = tk.Label(window, text = "BC:",
					bg = "white")
text_ac = tk.Label(window, text = "AC:",
					bg = "white")
answer = tk.Label(window, text = "Answer:",
					bg = 'white')

#texts window1
formuls = tk.Label(window1, text = 'cos A = AC/AB\nsin A = BC/AB\ntg A = BC/AC\ncAtg A = AC/BC\n\ncos B = BC/AB\nsin B = AC/AB\ntg B = AC/BC\ncAtg B = BC/AC',
					bg = 'white',
					font = 'bold')

action1 = tk.Label(window1, text = 'Action B:',
					bg = 'white',
					width = 50)

answer1 = tk.Label(window1, text = "Answer:",
					bg = 'white')

text_ab1 = tk.Label(window1, text = "AB:",
					bg = "white")
text_bc1 = tk.Label(window1, text = "BC:",
					bg = "white")
text_ac1 = tk.Label(window1, text = "AC:",
					bg = "white")
answer1 = tk.Label(window1, text = "Answer:",
					bg = 'white')

#buttons window
btn_cos = tk.Button(window, text = 'cos',
					command = get_entrys_cos,
					bg = 'white',
					padx = 70,
					pady = 5,
					highlightcolor = 'grey')

btn_sin = tk.Button(window, text = 'sin',
					command = get_entrys_sin,
					bg = 'white',
					padx = 70,
					pady = 5,
					highlightcolor = 'grey')

btn_tg = tk.Button(window, text = 'tg',
					command = get_entrys_tg,
					bg = 'white',
					padx = 73.4,
					pady = 5,
					highlightcolor = 'grey')

btn_cAtg = tk.Button(window, text = 'cAtg',
					command = get_entrys_cAtg,
					bg = 'white',
					padx = 65,
					pady = 5,
					highlightcolor = 'grey')

#buttons window1
btn_cos1 = tk.Button(window1, text = 'cos',
					command = get_entrys_cos1,
					bg = 'white',
					padx = 70,
					pady = 5,
					highlightcolor = 'grey')

btn_sin1 = tk.Button(window1, text = 'sin',
					command = get_entrys_sin1,
					bg = 'white',
					padx = 70,
					pady = 5,
					highlightcolor = 'grey')

btn_tg1 = tk.Button(window1, text = 'tg',
					command = get_entrys_tg1,
					bg = 'white',
					padx = 73.4,
					pady = 5,
					highlightcolor = 'grey')

btn_cAtg1 = tk.Button(window1, text = 'cAtg',
					command = get_entrys_cAtg1,
					bg = 'white',
					padx = 65,
					pady = 5,
					highlightcolor = 'grey')

#AB
text_ab.grid(row = 3, column = 0)
enter_ab.grid(row = 3, column = 0, columnspan = 30)

#BC
text_bc.grid(row = 4, column = 0)
enter_bc.grid(row = 4, column = 0, columnspan = 30)

#AC
text_ac.grid(row = 5, column = 0)
enter_ac.grid(row = 5, column = 0, columnspan = 30)

#...
action.grid(row = 0, column = 0, columnspan = 2, stick = 'we')

answer.grid(row = 6, column = 0)

btn_cos.grid(row = 1, column = 0)
btn_sin.grid(row = 1, column = 1)
btn_tg.grid(row = 2, column = 0)
btn_cAtg.grid(row = 2, column = 1)

#AB1
text_ab1.grid(row = 3, column = 0)
enter_ab1.grid(row = 3, column = 0, columnspan = 30)

#BC1
text_bc1.grid(row = 4, column = 0)
enter_bc1.grid(row = 4, column = 0, columnspan = 30)

#AC1
text_ac1.grid(row = 5, column = 0)
enter_ac1.grid(row = 5, column = 0, columnspan = 30)

#... 1
action1.grid(row = 0, column = 0, columnspan = 2, stick = 'we')

answer1.grid(row = 6, column = 0)

btn_cos1.grid(row = 1, column = 0)
btn_sin1.grid(row = 1, column = 1)
btn_tg1.grid(row = 2, column = 0)
btn_cAtg1.grid(row = 2, column = 1)

formuls.place(x = 100, y = 200)

#.....
imageee = Image.open('c:\Users\DOM\Desktop\Trigonometric calculator\img\paanglee.png')

canvas = tk.Canvas(window, height=200, width=350)
img = Image.open("c:\Users\DOM\Desktop\Trigonometric calculator\img\paanglee.png")
photo = ImageTk.PhotoImage(img)
image = canvas.create_image(0, 0, anchor='nw',image=photo)
canvas.place(x = 0, y = 180)


window.mainloop()
window1.mainloop()