# Proyecto-Simulacion
Aeropuerto de barajas(Ejercicio 5) Simulacion

En el Aeropuerto de Barajas, se desea conocer cuánto tiempo se encuentran
vacı́as las pistas de aterrizaje. Se conoce que el aeropuerto cuenta con un máximo
de 5 pistas de aterrizaje dedicadas a aviones de carga y que se considera que
una pista está ocupada cuando hay un avión aterrizando, despegando o cuando
se encuentra cargando o descargando mercancı́a o el abordaje o aterrizaje de
cada pasajero.
Se conoce que el tiempo cada avión que arriba al aeropuerto distribuye,
mediante una función de distribución exponencial con λ = 20 minutos.
Si un avión arriba al aeropuerto y no existen pistas vacı́as, se mantiene
esperando hasta que se vacı́e una de ellas (en caso de que existan varios aviones
en esta situación, pues se establece una suerte de cola para su aterrizaje.
Se conoce además que el tiempo de carga y descarga de un avión distribu-
ye mediante una función de distribución exponencial con λ = 30 minutos. Se
considera además que el tiempo de aterrizaje y despegue de un avión distribuye
normal (N(10,5)) y la probabilidad de que un avión cargue y/o descargue en
cada viaje corresponde a una distribución uniforme.
Además de esto se conoce que los aviones tiene una probabilidad de tener
una rotura de 0.1. Ası́, cuando un avión posee alguna rotura debe ser reparado
en un tiempo que distribuye exponencial con λ = 15 minutos. Las roturas se
identifican justo antes del despegue de cada avión.
Igualmente cada avión, durante el tiempo que está en la pista debe recargar
combustible y se conoce que el tiempo de recarga de combustible distribuye
expoencial λ = 30 minutos y se comienza justamente cuando el avión aterriza.
Se asume además que los aviones pueden aterrizar en cada pista sin ninguna
preferencia o requerimiento.
Simule el comportamiento del aeropuerto por una semana para estimar el
tiempo total en que se encuentran vacı́a cada una de las pistas del aeropuerto.
