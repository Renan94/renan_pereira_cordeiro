import math
import random
'''AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO-PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS DESSE
  PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A SUA DISTRIBUIÇÃO.
  ESTOU CIENTE QUE OS CASOS DE PLÁGIO E DESONESTIDADE ACADÊMICA
  SERÃO SEVERAMENTE PUNIDOS.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E, AINDA
  ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome:Renan Pereira Cordeiro
  Número USP:9794510
  Curso:lic. em matemática
  Disciplina: MAC0110 Introdução à Computação    Turma: LM - 47
  Exercício-Programa 03

  Este programa foi feito no windows 10, utilizando idle do python versão 3.6.1
  '''
print("\nEste programa executa a aproximação do número pi através dos métodos dos trapézios ou através do método de Monte Carlo.\n")
print("\nMétodo dos trapézios:    't'\n")
print("\nMétodo de Monte Carlo:   'm'\n")
print("\nPara encerrar o programa:'-'\n")
def main():
    print("================================================================================")
    esc = str(input("\nDigite o código de uma tarefa (`t' ou `m' ou `-'): "))
    if esc == 't':
        a = 0.0
        b = 1.0
        k = int(input("\nDigite o número de trapézios: "))
        aproximacao_trapezios = metodo_trapezios(a, b, k)
        print("\nTarefa : Valor aproximado de PI pelo método dos trapézios\n")
        print("\nNúmero de trapézios =",k)
        print("\nDeltax =",(b-a)/k)
        print("\nPi =",aproximacao_trapezios*4)
        main()

    elif esc == 'm':
        a = 0.0
        b = 1.0
        M = 1.0
        h = int(input("\nDigite uma semente para o gerador de números pseudo-aleatórios: "))
        random.seed(h)
        repeticoes = int(input("\nDigite o número de repetições para o cálculo da área:"))
        n = int(input("\nDigite o número de pontos a serem gerados: "))
        i = 1
        soma = 0
        while i <= repeticoes:
            monte_carlo = metodo_monte_carlo(a, b, M, n)
            soma = soma + monte_carlo
            i = i+1
        soma = (soma/repeticoes)*4
        print("\nTarefa : Valor aproximado de PI pelo método de Monte Carlo")
        print("\nSemente =", h)
        print("\nNumero de repetições =",repeticoes)
        print("\nNúmero de pontos =",n)
        print("\nPi =", (soma))
        main()
        
    elif esc == '-':
        print("\n====================================================================================")


def metodo_monte_carlo(a, b, M, n):
    i = 1
    soma = 0
    while i <= n:
        funciona =  gera_coordenadas_ponto(a, b, M) 
        soma += funciona
        i+=1
            
    return ((soma/n)*(b-a)*M)

def gera_coordenadas_ponto(a, b, M):
    interno = 0
    externo = 0
    d = random.uniform(a,b)
    e = math.sqrt(1.0 - (d**2))
    y = random.uniform(0.0, M)
    if y <= e:
        return 1
    else:
        return 0
   
    
def metodo_trapezios(a, b, k):
    deltax = (b-a)/k
    i = 1
    soma = f(a) 
    while i < k:
        a =(i*deltax)
        r = 2*f(a)
        soma = soma + r
        i = i+1
    i = k
    a =(i*deltax)
    soma = soma + f(a)
    soma = (soma)*(deltax/2)
    return (soma)
        



def f(x):
    
    if (1.0 - (x**2))> 0:
        raiz = math.sqrt(1.0 - (x**2))
    else:
        raiz = 0
    return raiz
        
#-------------------------------------------------------------------------------------------
main()
        

       
    
    
