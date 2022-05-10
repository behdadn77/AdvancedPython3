import threading

tname= threading.current_thread().name
print(tname)
if tname==threading.main_thread():
	print("main thread")

threading.current_thread().name="foobar"
print(threading.current_thread().name)
		