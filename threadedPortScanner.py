import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'pythonprogramming.net'

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port,'is open!!')

        con.close()

    except:
        #pass
        print('port',port,'is closed')

def threader():
    while True:
        #get worker from queue
        worker = q.get()
        #ports as workers
        portscan(worker)
        #empty out queue
        q.task_done()

q = Queue()

#30 workers in thread
for x in range(30):
    t = threading.Thread(target=threader)
    #daemon dies when main thread dies
    t.daemon = True
    t.start()

#assign amount of jobs/ports
#100 ports
for worker in range(1,26):
    #put worker to work
    q.put(worker)
    #wait until thread terminates 722
    q.join()
    
