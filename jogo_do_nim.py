def campeonato():
    cont = 0
    while cont < 3:
        partida()
        cont+=1


def partida():
    
    n = int(input("Dê o número de peças da partida:"))
    m = int(input("Forneça o número máximo de peças que podem ser retirados:"))
    if n<=m:
        partida()
        
    if n%(m+1) == 0:
        print("O usuário começa!")
        c = usuario_escolhe_jogada(n, m)
        print("Você tirou %d peças"%(c))
        print("Restaram %d peças no tabuleiro"%(n-c))
        n=n-c
        if n == 0:
            print("O usuário venceu !")
        else:
            while n!=0:
                d = computador_escolhe_jogada(n, m)
                print("O computador tirou %d peças"%(d))
                print("Restaram %d peças no tabuleiro"%(n-d))
                n = n-d
                if n == 0:
                    print("O computador venceu !")
                else:
                    c = usuario_escolhe_jogada(n, m)
                    print("Você tirou %d peças"%(c))
                    print("Restaram %d peças no tabuleiro"%(n-c))
                    n = n-c
                    if n == 0:
                        print(" O usuário venceu !")
            
    else:
        print("O computador começa!")
        d=  computador_escolhe_jogada(n, m)
        print("O computador tirou %d peças"%(d))
        print("Restaram %d peças no tabuleiro"%(n-d))
        n = n-d
        if n == 0:
            print("O computador venceu !")
        else:
            while n!=0:
                c = usuario_escolhe_jogada(n, m)
                n = t
                print("Você tirou %d peças"%(c))
                print("Restaram %d peças no tabuleiro"%(n-c))
                n = n-c
                if n == 0:
                    print("O usuário venceu !")
                else:
                    d =  computador_escolhe_jogada(n, m)
                    print("O computador tirou %d peças"%(d))
                    print("Restaram %d peças no tabuleiro"%(n-d))
                    n = n-d
                    if n == 0:
                        print("O computador venceu !")

def  computador_escolhe_jogada(n, m):
    cont = 0
    if n > m:
        while n%(m+1)!=0 and m<=n:
            cont+=1
            n = n-1
            return(cont)
    else:
        while n!=0:
            n = n-1
            cont+=1
        return(cont)


def usuario_escolhe_jogada(n, m):
    c = int(input("Digite o número de peças a serem retiradas do tabuleiro: "))
    if c<=m and c<=n:
        n = n - c
        return(c)
    else:
        while c>m or c> n:
            print("Jogada inválida")
            c = int(input("Digite o número de peças a serem retiradas do tabuleiro: "))
        n = n -c
        return (c)
#---------------------------------------------------------------------------------------------------------------------------------------------------
print("Bem-vindo ao jogo do nim")
k = int(input(" 1 - para partida ou 2 - para campeonato: "))
if k == 1:
    partida()
elif k == 2:
    campeonato()

            

        
        
                
        
            
