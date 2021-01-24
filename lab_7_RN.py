#Referinta: curs7 slide-uri 64-69


import math
import random


# Functia de activare sigmoida--------------------------------------

def activare_sigmoida(x):
    return 1 / (1 + math.exp(-x))


if __name__ == '__main__':

    # Introducerea datelor        --------------------------------------

    numarEpoci = int(input("Numar epoci: "))
    rataInvatare = float(input("Rata de invatare: "))
    vectoriIntrare = []
    iesiriDorite = []
    f = open("input_rn", "r")
    for i in range(4):
        inputLine = f.readline()
        temp = [inputLine[0], inputLine[2]]
        iesiriDorite.append(inputLine[4])
        vectoriIntrare.append(temp)

    # Initializare               ----------------------------------------
    neuroni = []
    for i in range(3):
        neuron = []
        pondereIntrare1 = random.uniform(-1.2, 1.2)
        while pondereIntrare1 == 0:
            pondereIntrare1 = random.uniform(-1.2, 1.2)
        neuron.append(pondereIntrare1)
        pondereIntrare2 = random.uniform(-1.2, 1.2)
        while pondereIntrare2 == 0:
            pondereIntrare2 = random.uniform(-1.2, 1.2)
        neuron.append(pondereIntrare2)
        prag = random.uniform(-1.2, 1.2)
        while prag == 0:
            prag = random.uniform(-1.2, 1.2)
        neuron.append(prag)
        neuroni.append(neuron)
    eroarePatratica = 0
    for j in range(numarEpoci):
        eroarePatratica = 0
        for i in range(len(vectoriIntrare)):
            intrare1 = int(vectoriIntrare[i][0])
            intrare2 = int(vectoriIntrare[i][1])
            iesireDorita = int(iesiriDorite[i])

            # Propagare inainte ---------------------------------
            iesire1 = activare_sigmoida(intrare1 * neuroni[0][0] + intrare2 * neuroni[0][1] - neuroni[0][2])
            iesire2 = activare_sigmoida(intrare1 * neuroni[1][0] + intrare2 * neuroni[1][1] - neuroni[1][2])
            iesireReala = activare_sigmoida(iesire1 * neuroni[2][0] + iesire2 * neuroni[2][1] - neuroni[2][2])
            eroare = iesireDorita - iesireReala
            # Propagare inapoi ----------------------------------
            gradientIesire = iesireReala * (1 - iesireReala) * eroare
            corectiiIesire = []
            corectiiIesire.append(rataInvatare * iesire1 * gradientIesire)
            corectiiIesire.append(rataInvatare * iesire2 * gradientIesire)
            corectiiIesire.append(rataInvatare * -1 * gradientIesire)

            gradientAscuns1 = iesire1 * (1 - iesire1) * gradientIesire * neuroni[2][0]
            gradientAscuns2 = iesire2 * (1 - iesire2) * gradientIesire * neuroni[2][1]
            corectiiAscuns1 = []
            corectiiAscuns1.append(rataInvatare * intrare1 * gradientAscuns1)
            corectiiAscuns1.append(rataInvatare * intrare2 * gradientAscuns1)
            corectiiAscuns1.append(rataInvatare * -1 * gradientAscuns1)
            corectiiAscuns2 = []
            corectiiAscuns2.append(rataInvatare * intrare1 * gradientAscuns2)
            corectiiAscuns2.append(rataInvatare * intrare2 * gradientAscuns2)
            corectiiAscuns2.append(rataInvatare * -1 * gradientAscuns2)
            # Actualizare ponderi si praguri
            for i in range(3):
                neuroni[0][i] = neuroni[0][i] + corectiiAscuns1[i]
                neuroni[1][i] = neuroni[1][i] + corectiiAscuns2[i]
                neuroni[2][i] = neuroni[2][i] + corectiiIesire[i]
            eroarePatratica += eroare * eroare
        eroarePatraticaMedie = eroarePatratica/4
        print(eroarePatraticaMedie)
        if eroarePatraticaMedie < 0.01:
            print(j)
            break
