#execute o programa 5.1 para que os seguintes valores 501, 745, 384, 2, 7 e 1

#Programa 5.1
#    valor = int(input("Digite o valor a pagar: "))
#    cedulas = 0
#    atual = 50
#    apagar = valor

#    while True:
#        if atual <= apagar:
#            apagar -= atual
#            cedulas += 1
#        else:
#            print(f"{cedulas} cedula(s) de R${atual}")
#            if apagar == 0:
#                break
#            if atual == 50:
#                atual = 20
#           elif atual == 20:
#               atual = 10
#            elif atual == 10:
#                atual = 5
#            elif atual == 5:
#                atual = 1
#           cedulas = 0

           
valor = int(input("Digite o valor a pagar: "))
cedulas = 0
atual = 50
apagar = valor

while True:
    if atual <= apagar:
        apagar -= atual
        cedulas += 1
    else:
        print(f"{cedulas} cedula(s) de R${atual}")
        if apagar == 0:
             break
        if atual == 745:
            atual = 501
        elif atual == 501:
            atual = 384
        elif atual == 7:
            atual = 7
        elif atual == 2:
            atual = 1
        cedulas = 0