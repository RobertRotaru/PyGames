import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.iconbitmap(r'C:/Users/User/Desktop/Projects/Calculator Desktop App/calculator_icon.ico')
root.resizable = True

output = "0"
t1 = 0
t2 = 0
operand = ""
_output = ""
ok = False

def onTap(c):
	global output
	global t1
	global t2
	global operand
	global _output
	global ok
	if c == "AC":
		output = "0"
		_output = "0"
		t1 = 0
		t2 = 0
		operand = ""
		ok = False
		entry.delete(0, 'end')

	elif c == "DEL":
		_output = _output[0:len(_output)-1]
		entry.delete(0, 'end')

	elif c == "+" or c == "-" or c == "X" or c == "/" or c == "^":
		t1 = float(output)
		entry.delete(0, 'end')
		operand = c
		_output = "0"
		ok = False

	elif c == ".":
		entry.delete(0, 'end')
		if "." not in _output:
			_output = _output + "."

	elif c == "+-":
		entry.delete(0, 'end')
		if "-" in _output:
			_output = _output[1:]
		else: 
			_output = "-" + _output

	elif c == "=":
		t2 = float(output)
		entry.delete(0, 'end')
		if operand == "+":
			intRes = int(t1 + t2)
			floatRes = float(t1 + t2)
			if float(intRes) != floatRes:
				_output = str(floatRes)
			else: _output = str(intRes)
		elif operand == "-":
			intRes = int(t1 - t2)
			floatRes = float(t1 - t2)
			if float(intRes) != floatRes:
				_output = str(floatRes)
			else: _output = str(intRes)
		elif operand == "X":
			intRes = int(t1 * t2)
			floatRes = float(t1 * t2)
			if float(intRes) != floatRes:
				_output = str(floatRes)
			else: _output = str(intRes)
		elif operand == '/':
			try:
				intRes = int(t1 / t2)
				floatRes = float(t1 / t2)
				if float(intRes) != floatRes:
					_output = str(floatRes)
				else: _output = str(intRes)
			except:
				_output = "Error"
		elif operand == "^":
			try:
				intRes = int(t1 ** t2)
				floatRes = float(t1 ** t2)
				if float(intRes) != floatRes:
					_output = str(floatRes)
				else: _output = str(intRes)
			except:
				_output = "Error"
		t1 = 0.0
		t2 = 0.0
		operand = ""
		ok = False
	
	else:
		entry.delete(0, 'end')
		if ok == False: 
			_output = ""
		_output = _output + c
		ok = True
	
	output = _output
	entry.insert(0, output)
	

def makeButton(c, i, j, nrPadx, nrPady):
	button = tk.Button(root, text = c, padx = nrPadx, pady = nrPady, command =lambda: onTap(c))
	button.grid(row = i, column = j, sticky='EWNS')
	return button

entry = tk.Entry(root, width = 46)
entry.grid(row = 0, columnspan = 5, padx = 10, pady = 10)
entry.insert(0, output)

b7 = makeButton("7", 1, 0, 20, 20)
b8 = makeButton("8", 1, 1, 20, 20)
b9 = makeButton("9", 1, 2, 20, 20)
bd = makeButton("DEL", 1, 3, 20, 20)
bc = makeButton("AC", 1, 4, 20, 20)

b4 = makeButton("4", 2, 0, 20, 20)
b20 = makeButton("5", 2, 1, 20, 20)
b6 = makeButton("6", 2, 2, 20, 20)
bx = makeButton("X", 2, 3, 20, 20)
bdiv = makeButton("/", 2, 4, 20, 20)

b1 = makeButton("1", 3, 0, 20, 20)
b2 = makeButton("2", 3, 1, 20, 20)
b3 = makeButton("3", 3, 2, 20, 20)
bp = makeButton("+", 3, 3, 20, 20)
bm = makeButton("-", 3, 4, 20, 20)

b0 = makeButton("0", 4, 0, 20, 20)
bdot = makeButton(".", 4, 1, 20, 20)
bpm = makeButton("+-", 4, 2, 20, 20)
bpow = makeButton("^", 4, 3, 20, 20)
b = makeButton("=", 4, 4, 20, 20)

root.mainloop()
