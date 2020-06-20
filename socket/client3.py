#soket modulü import edilir
import socket
import time


def Main(): 
	# local host IP '127.0.0.1' 
	host = '127.0.0.1'

	# baglanmak istegimiz port tanımlanır
	port = 12345

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 

	# local sunucuya bağlanır 
	s.connect((host,port)) 

	# server a gönderilecek mesaj
	print('eger toplama yapmak istiyorsanız sayının başına 0 ekleyiniz') 
	
	message = input("bir sayi giriniz   : ")
	while True: 
        
		# sunucuya mesaj gönderildi 
		s.send(message.encode('utf-8')) 

		# mesaj sunucudan alındı 
		data = s.recv(1024) 

		# alınan mesaj ekrana yazdırılır 
	
		print('Received from the server :',str(data.decode('utf-8'))) 

		time.sleep(20.0)
		# client a devam etmek istemediğini sor 
		ans = input('\nDo you want to continue(y/n) :') 
		if ans == 'y': 
			continue
		else: 
			break
	# bağlantı kapatılır
	s.close() 

if __name__ == '__main__': 
	Main() 


