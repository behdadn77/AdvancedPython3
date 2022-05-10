import threading

def zoe():
	while True:
		print("Zoe")

def zelda():
	while True:
		print("Zelda")

t1= threading.Thread(target=zoe)
t1.start()

threading.Thread(target=zelda).start()