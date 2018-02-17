#REPRESENTAÇÃO EM FRAÇÕES CONTÍNUAS
def main():
    a = int(input("Digite um numero inteiro : "))
    b = int(input("Digite um número inteiro : "))
    q = a//b
    r = a - q*b
    fr = []
    div = False
    while not div:
        fr.append(q)
        a = b
        b = r
        q = a//b
        r = a - q*b
        if a%b == 0:
            div = True
    fr.append(q)
    print(fr)
#--------------------------------------------------------------------------------
main()
        
