import paramiko
import socket
import pickle
import os

class Server():
    def __init__(self, name, you):
        try:
            IP = (([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2]
            if not ip.startswith("127.")] or [[(s.connect(("8.8.8.8", 53)),
            s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET,
            socket.SOCK_DGRAM)]][0][1]]) + ["no IP found"])[0]
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect('46.254.20.230', username='root', password='25453Zrjd')
            self.ftp = self.ssh.open_sftp()
            self.get_str = ''
            self.put_str = ''
            self.gamer = name
            if you == 'first':
                self.ssh.exec_command('mkdir '+str(name))
            else:
                pass
        except:
            print("Oops! У вас траблы с инетом.")


    def GET(self, get_str):
        self.ftp.get(str(self.gamer)+'/'+get_str, get_str)
        with open(get_str, 'rb') as Input:
            var = pickle.load(Input)
            os.remove(get_str)
            return var

    def PUT(self, put, put_str):
        with open(put_str+'i', 'wb') as output:
            pickle.dump(put, output)
        self.ftp.put(put_str+'i', str(self.gamer)+'/'+put_str)
        os.remove(put_str+'i')

    def LIST(self, folder = ''):
        if folder != '':
            return self.ftp.listdir(folder)
        else:
            return self.ftp.listdir()

    def end(self):
        self.ssh.exec_command('rm -r '+str(self.gamer))
        self.ssh.close()
        self.ftp.close()

server = Server('Jacob', 'first')

print(server.LIST('Jacob'))
list = 'kjzfgbksdgnljkbndlfkx;nbdljkgf,nb nsx,nƒ lvbjmx,jcgnvg vkx.db,nfcg'
server.PUT(list, 'list')
print(server.LIST('Jacob'))
print(server.GET('list'))
print(server.LIST())

server.end()


