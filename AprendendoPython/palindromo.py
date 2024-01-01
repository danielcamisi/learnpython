x = 0
y = 0   #variáveis em zero para executar a equação
pol = 0
while x <= 9999:    #abrindo o loop e definindo a quantidade de dígitos
    y = x
    while y <= 9999:
        time = str(x * y)
        timeinv = time[::-1]     #definindo as possibilidades inversas
        if time == timeinv:
            poltime = int(time)  
            if poltime > pol:
                pol = poltime 
        y += 1                         #atribuindo o resultado a variável pol
    x += 1
print(pol)