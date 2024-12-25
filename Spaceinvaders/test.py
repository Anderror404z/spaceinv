from socket import create_server as CreateServer
from socket import create_connection as CreateClient

def HostServer():
	try:
		sock = CreateServer("localhost", backlog=4)
		sock.setblocking(False)
		return sock
	except:
		return False

def ConnectToServer(ip, port):
	try:
		sock = CreateClient((ip, port))
		sock.setblocking(False)
		return sock
	except:
		return False

def main():
	answer = input("Создать сервер? [Y/N]")
	isServerSide = False
	if (answer.upper() == 'Y'):
		global g_pSocket
		g_pSocket = HostServer()
		if (not g_pSocket):
			print("Не удалось создать сервер!")
			return False

		isServerSide = True
	else:
		try:
			global g_pSocket
			g_pSocket = ConnectToServer(input("Введите IP-адрес:"), int(input("Введите порт:")))
			if (not g_pSocket):
				raise
		except:
			print("Не удалось подключиться к данному серверу!")
			return False

	socks = []
	while (True):
		if (isServerSide):
			sock = sock.accept()
			if (sock):
				socks.append(sock)

		for sock in socks:
			# Read and use client data
			pass

		AdvanceFrame()

	return True