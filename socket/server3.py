# soket kütüphanesi import edilir 
import socket 
import math
# thread modulü import edilir 
from _thread import *
import threading 

print_lock = threading.Lock() 

# thread fonksiyonu
def threaded(c): 
	while True: 
		
		# veri client 'dan alınır 
		data = c.recv(1024)
		#eger alınan verinin ilk elemanı '0' ise toplama yap
		if data[0] =='0':
				total = 0
				sayi =int(data)
				while sayi>=10 :
					 bas = sayi % 10
					 total = total + bas
					 sayi = sayi // 10
				print('Sum the digits of number=',total+sayi)

				#topla
				#c.send(str(data).encode('utf-8'))  gönder
				 
		#eger alınan verinin ilk elemanı '0 değil ise faktöriyelini al
		data = (math.factorial( int(data)))

			# veriyi tekrar client a gönderir
		c.send(str(data).encode('utf-8')) 

	# bağlantı kapatılır
	c.close() 


def Main(): 
	host = "" 
 
	
	# port belirlenir
	port = 12345
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
	s.bind((host, port)) 
	print("Socket binded to port: ", port) 

	# soket dinleme moduna alınır 
	s.listen(5) 
	print("Socket is listening...") 

	# istemci çıkmak isteyene kadar döngü devam eder
	while True: 

		# client ile bağlantı kurulur
		c, addr = s.accept() 

		# client tarafından alınan kilit 
		print_lock.acquire() 
		print('Connected to :', addr[0], ':', addr[1]) 

		# Yeni bir thread başlatır ve tanımlayıcısını döndürür 
		start_new_thread(threaded, (c,))

	s.close() 


				
		
		

if __name__ == '__main__': 
	Main()
	
