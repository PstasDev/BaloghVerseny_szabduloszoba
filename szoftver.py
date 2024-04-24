import tkinter as tk
import time
import datetime

key = 827
starttime = time.perf_counter()
stopped = True
tocount = 20
maxerrors = 3
def callnumber(number):
	pass

def starttimer(event=''):
	global tocount
	global starttime
	global stopped
	if stopped == True:
		starttime = int(time.perf_counter()) + tocount + 1
		stopped = False
		print(starttime, stopped)
		errordisplay.configure(text="")

def startcustom(event=''):
	global tocount
	global starttime
	global stopped
	if stopped == True:
		toadd = input('Egyedi idő(másodperc): ')
		time.sleep(1)
		starttime = int(time.perf_counter()) + int(toadd) + 1
		stopped = False
		print(starttime, stopped)
		errordisplay.configure(text="")

def validate():
	global window
	global key
	global maxerrors
	global stopped
	code = enterfield.get()
	if isinstance(int(code), int):
		print(int(code), key)
		if int(code) == key:
			stopped = True
			countdownlabel.configure(fg="lime")
			enterfield.delete(0,tk.END)
		else:
			errordisplay.configure(text=errordisplay.cget('text')+"x")
	else:
		pass
	if "x"*maxerrors == errordisplay.cget('text'):
		stopped = True
		countdownlabel.configure(fg="orange")
		enterfield.delete(0,tk.END)

def update():
	global starttime
	global window
	global stopped

	if stopped == True:
		enterfield.configure(state='disabled')
		validatebutton.configure(state='disabled')
	else:
		countdownlabel.configure(fg="red")
		enterfield.configure(state='normal')
		validatebutton.configure(state='normal')
		print('count')
		now = time.perf_counter()
		conversion = datetime.timedelta(seconds=int(starttime-now))
		if str(conversion) == '0:00:00':
			stopped = True
			enterfield.delete(0,tk.END)
		countdownlabel.configure(text=str(conversion))
	window.after(200, update)

def revealkey():
	print("megoldás:", key)

def fullscreen(event=''):
	window.attributes('-fullscreen', True)

window = tk.Tk()
window.configure(bg="black")

countdownframe = tk.Frame(window)
countdownlabel = tk.Label(countdownframe, bg='black', fg='red', font=('MS Sans Serif', 250), text="0:00:00")
countdownlabel.pack()
countdownframe.pack()
inputframe = tk.Frame(window)
enterfield = tk.Entry(inputframe)
enterfield.pack(side=tk.LEFT,fill=tk.Y)
validatebutton = tk.Button(inputframe, bg='green', fg='white', command=validate, text='Ellenőrzés')
validatebutton.pack(side=tk.RIGHT)
inputframe.pack()
errorsframe = tk.Frame(window)
errordisplay = tk.Label(errorsframe, bg="black", fg='red', font=('MS Sans Serif', 80), text='')
errordisplay.pack()
errorsframe.pack()

window.after(0, update)
window.bind('f', fullscreen)
window.bind('o', starttimer)
window.bind('p', startcustom)
window.mainloop()