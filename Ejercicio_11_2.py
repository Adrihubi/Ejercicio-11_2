NUM = int(input("CUANTAS TABLAS: "))
T = 1
while T <= NUM:
    I = 10
    while not I < 1:
        RESUL = T * I
        print(f"{T} * {I} = {RESUL}")
        I = I + 1
    input("Pulse una tecla: ")
    T = T + 1
input("Pulse una tecla: ")
