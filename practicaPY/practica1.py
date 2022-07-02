notas = (5, 6, 9),
for notas in notas:
    suma_de_notas = 0

    for nota in notas:
        suma_de_notas += nota

        print (suma_de_notas)

    mean = sum(notas)/len(notas)
    print (mean)


    if (mean) <= 7:
        print("SUPLETORIO")
    else:
        print("APROBADO")
