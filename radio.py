import threading
import time

import time
# Criar um objeto Lock
mutex = threading.Lock()
THREADS = 300
radio_zero = 0
priority = 0

first_priority=[0,3]
secound_priority=[3,8]
tirdy_priority =[8,10]
end_priority = [10,THREADS-1]

class machine_radio():
    def __init__(self, radio_zero):
        self.milisieverts = radio_zero
        self.red = 80
        self.orange = 1
        self.green = 0.5
        self.blue = 0.001

    def worker_with_lock(self):
        with mutex:
            self.work_radio()     
    
    def worker_lockless(self):
        self.work_radio()
    
    def work_radio(self):
        global priority
        if priority >=first_priority[0] and priority <= first_priority[1]:
            self.milisieverts+= self.red
        elif priority > secound_priority[0] and priority <=secound_priority[1]:
            self.milisieverts+= self.orange
        elif priority > tirdy_priority[0] and priority < tirdy_priority[1]:
            self.milisieverts += self.green
        elif end_priority[0] <= priority < end_priority[1]:
            self.milisieverts += self.blue
        elif priority == end_priority[1]:
            if int(self.milisieverts) >= 500:
                # pass
                self.milisieverts = 0
        self.recalibrando_dosagem()
        priority +=1


    def recalibrando_dosagem(self):
        time.sleep(0.02) # tempo para maquina não superaquecer

    def main(self,security):
        global THREADS
        threads = []
        
        for i in range(THREADS):
            if x == 1:
                thread = threading.Thread(target=self.worker_with_lock)
            else:
                thread = threading.Thread(target=self.worker_lockless)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        print(f'carregando: {self.milisieverts:.2f} mSV')
        [(time.sleep(1),print(f'awaiting in : {i}')) for i in range(3,-1,-1)]

if __name__ == "__main__":
    run = machine_radio(radio_zero)
    x = int(input("Deseja fazer radio usando operação segura do Mutex?\n sim - digite: 1\n nao - digite: 2\n -> : "))
    print('\n')
    run.main(x)
    print("\nAplicando a segunda dosagem\n")
    run.main(x)
    print("RADIOTERAPIA encerrada!")