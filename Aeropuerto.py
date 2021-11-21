import numpy as np
import sys

def gen_VA_N(mi, sigma2):
    arrayU = [np.random.uniform(0,1) for x in range(12)]
    X = mi + np.sqrt(sigma2)*(np.sum(arrayU)-6)
    return X


def gen_VA_exp(lambd):
    U = np.random.uniform(0,1)
    X = -lambd*np.log(U)
    return X

class Aeropuerto:
    def __init__(self):
        self.t_pista = [sys.maxsize,sys.maxsize,sys.maxsize,sys.maxsize,sys.maxsize]
        #0 aterrizando
        #1 despegando
        #2 carga , descarga , combustible
        #3 reparacion
        #6 vacio
        self.Total = [0,0,0,0,0]
        self.ultima_ocupacion = [0,0,0,0,0]
        
        self.pista = [6,6,6,6,6]
        self.t = 0
        self.T_MAX = 24*7*60
        self.t_arribo = sys.maxsize
        self.Cola = 0

    def Simulacion(self):
        self.t = self.t_arribo = self.t + gen_VA_exp(20)
        while(self.t<self.T_MAX):
            if(self.t==self.t_arribo):
                print("Arribo un avion con tiempo "+ str(self.t))
                self.Arribo()
                            
            elif(self.t == min(self.t_pista)):
                index = self.t_pista.index(self.t)
                action = self.pista[index]
                if action == 0:
                    print("Aterrizo un avion en la pista "+ str(index) +" con tiempo "+ str(self.t))
                    self.Aterrizo(index)
                    
                elif action == 2:
                    print("Se cargo el avion de la pista "+ str(index) +" con tiempo "+ str(self.t))
                    self.Cargo(index)
                    
                elif action == 3:
                    print("Se reparo el avion de la pista "+ str(index) +" con tiempo "+ str(self.t))
                    self.Reparo(index)
                    
                elif action == 1:
                    print("Despego el avion de la pista "+ str(index) +" con tiempo "+ str(self.t))
                    self.Despego(index)
            self.t = min(self.t_arribo,min(self.t_pista))
                
        for x in range(5):
            if(self.pista[x] == 6):
                self.Total[x] += (self.T_MAX - self.ultima_ocupacion[x])
            print("Tiempo total de la pista {} vacia es : {} minutos".format(x+1,self.Total[x]))
                    
    def Despego(self,index):
        if self.Cola:
            self.t_pista[index] = self.t + gen_VA_N(10,5)
            self.pista[index] = 0
            self.Cola -= 1
            print("Va a aterrizar un avion en la pista "+ str(index) + " , aviones en cola: "+ str(self.Cola) )
        else:
            self.t_pista[index] = sys.maxsize
            self.pista[index] = 6
            self.ultima_ocupacion[index] = self.t
            print("Pista " + str(index) + " libre")

    def Reparo(self,index):
        print("Va a despegar el avion de la pista "+ str(index))
        self.t_pista[index] = self.t + gen_VA_N(10,5)
        self.pista[index] = 1

    def Cargo(self,index):
        rotura = True if np.random.randint(0,101) < 10 else False
        if rotura:
            print("Se rompio el avion de la pista "+ str(index))
            self.t_pista[index] = self.t + gen_VA_exp(15)
            self.pista[index] = 3
        else:
            print("Va a despegar el avien de la pista "+ str(index))
            self.t_pista[index] = self.t + gen_VA_N(10,5)
            self.pista[index] = 1


    def Aterrizo(self,index):
        #Probabilidad uniforme de carga y descarga
        carga = gen_VA_exp(30) if np.random.uniform(0,1) < 0.5 else 0
        combustible = gen_VA_exp(30)
        self.t_pista[index] = self.t + max(carga,combustible)
        if(carga>combustible):
            print("Esta cargando o descargando el avion de la pista "+ str(index))
        else:
            print("Esta cargando combustible el avion de la pista "+ str(index))
        
        self.pista[index] = 2


    def Arribo(self):
        try:
            index = self.pista.index(6)
            self.t_pista[index] = self.t + gen_VA_N(10,5)
            self.pista[index] = 0
            print("Va a aterrizar un avion el la pista "+ str(index))
            self.Total[index] = self.Total[index] + self.t - self.ultima_ocupacion[index]
        except:
            self.Cola += 1
            print("Pistas llenas, "+ str(self.Cola) +" aviones en cola")

        
        self.t_arribo = self.t + gen_VA_exp(20)

Aeropuerto().Simulacion()