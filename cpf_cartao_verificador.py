"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
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
  Curso:Licenciatura em matemática
  Disciplina: MAC0110 Introdução à Computação    Turma: LM - 47
  Exercício-Programa 02
"""
def main():
    
    print("Qual documento deseja escolher?\n")
    print("Para escolher CPF tecle 1, para cartão de crédito tecle 2 e para finalizar tecle 0!\n")
    n=int(input("Escolha uma das opções fornecidas:"))

 #Leitor de CPF   
    
    if n == 1:
        k=9
        soma_digitos1 = 0
        soma_digitos2 = 0
        cpf=int(input("Digite o número do cpf sem pontos e sem o traço:"))
        cpf1=cpf//100
        cpf2=cpf//10

        while k!=0:
            soma_digitos1= soma_digitos1 + ((cpf1%10)*k)
            cpf1=cpf1//10
            k = k-1
        print("O primeiro dígito verificador é", (soma_digitos1 % 11))
        k = 9

        while k>=0:
            soma_digitos2 = soma_digitos2 +((cpf2%10)*k)
            cpf2=cpf2//10
            k = k-1
        print("O Segundo dígito verificador é",(soma_digitos2 % 11))

        if ((soma_digitos1 % 11)*10 + soma_digitos2 % 11) == cpf % 100:
            print("Os dois dígitos verificadores do CPF %03d.%03d.%03d-%02d estão corretos.\n"%(cpf//10**8,cpf//10**5-((cpf//10**8)*1000),cpf//10**2-(cpf//10**5)*1000,cpf%100))

        else:
            print("Os dois dígitos verificadores do CPF %03d.%03d.%03d-%02d não estão corretos.\n"%(cpf//10**8,cpf//10**5-((cpf//10**8)*1000),cpf//10**2-(cpf//10**5)*1000,cpf%100))

       
        main()
        
  #Leitor de cartões de crédito          
            
    elif n==2:
        cartao_de_credito=int(input("Digite o número do cartão de crédito:"))
        c = cartao_de_credito
        k = 1
        cart_cred = cartao_de_credito//10
        soma_cart_credito = 0
        
        
        while cart_cred != 0:
            if k==2:
                k=1
                verif_maior_nove = ((cart_cred % 10)*k)
                if verif_maior_nove > 9:
                    verif_maior_nove = verif_maior_nove - 9
                    soma_cart_credito = soma_cart_credito+((verif_maior_nove))
                    cart_cred= cart_cred//10
                    

                else:
                    soma_cart_credito = soma_cart_credito+((verif_maior_nove))
                    cart_cred= cart_cred//10
                    
                

            elif k==1:
                k = 2
                verif_maior_nove = ((cart_cred % 10)*k)
                if verif_maior_nove > 9:
                    verif_maior_nove = (verif_maior_nove) - 9
                    soma_cart_credito = soma_cart_credito+((verif_maior_nove))
                    cart_cred= cart_cred//10
                    
                else:
                    soma_cart_credito = soma_cart_credito+((verif_maior_nove))
                    cart_cred= cart_cred//10
                    
                    

        print("O dígito verificador deve ser:",(10 -(soma_cart_credito%10)))

        if (cartao_de_credito%10) == (10 -(soma_cart_credito%10)):
            print("O dígito verificador do cartão de crédito %04d %04d %04d %04d está correto\n"%(c//10**12, c//10**8-(c//10**12)*10000,(c//10**4)-(c//10**8)*10000,c%10000))
                                                                               


        else:
            print("O dígito verificador do cartão de crédito %04d %04d %04d %04d não está correto\n"%(c//10**12, c//10**8-(c//10**12)*10000,(c//10**4)-(c//10**8)*10000,c%10000))



        main()
            
#Fim do programa
    elif n == 0:
        print("=======================================================")
#Usuário digitou um número diferente dos pré-determinados

    else:
        print("Você não digitou um número válido")
      
        main()

#--------------------------------------------------------------------------------
main()
