# PROJETO DE TEORIA DA COMPUTAÇÃO - 6968 - 8101 - 8127


#importação bibliotecas e arquivos

from main_func import *
from turing import *
import os
from graphviz import Digraph
import sys

## Main.py

#variaveis de controle e essenciais 
new_AFD_AFN = True 
stop_program = False
estados = []
alfabeto = []
func_transicao = {}
estado_inicial = ""
estados_finais = []
idAutomato = 0


## Loop do programa
while(stop_program == False):

    desicao = input("Deseja criar uma maquina de turing[Sim/Não]: ")
    if desicao == "Sim":

        fita = list(input("Informe a fita: "))
        simbolo_vazio = input("Informe o simbolo vazio: ")
        alfabeto = input("Informe o alfabeto de Entrada: ").split()
        estados = input("Informe os estados: ").split()
        estado_inicial = input("Informe o estado Inicial: ")
        estados_finais = input("Informe os estados finais: ").split()
        func_transicao = define_func_transition_Turing(estados, alfabeto)

        newTuring = Turing(
            fita,
            simbolo_vazio, 
            estado_inicial, 
            estados_finais, 
            func_transicao
        )

        newTuring.turing()

        input("Pressione Enter para continuar...")        

        #Caso queira um novo automato, cria novamente
    if(new_AFD_AFN):
        idAutomato += 1
            #definição da estrutura do automato

        AFN_or_AFD = input("AFD ou AFN ? [AFN/AFD]: ").lower()
        estados = input("Informe o conjunto de estados: ").split()
        alfabeto = input("Informe o alfabeto: ").split()
        estado_inicial = input("Informe o estado inicial: ")
        estados_finais = input("Informe os estados finais: ").split()

            #definição das funções de transição
        func_transicao = define_func_transition(estados, alfabeto)

            #checagem para saber se é um afn ou afd
        afd = True
        afn = False
        for (estado, simbolo), destinos in func_transicao.items():
            if len(destinos) > 1:
                afd = False
                afn = True
                break

            #criacao de AFN ou AFD 
        if(AFN_or_AFD == "afn" and afn == True):
            automato = AFN(estados, alfabeto, func_transicao, estado_inicial, estados_finais)

        elif(AFN_or_AFD == "afn" and afn == False):
            print("Criação de AFN impossivel!!")
            os.system("pause")
            sys.exit(0)

        elif(AFN_or_AFD == "afd" and afd == True):
            func_transicao = {key: next(iter(value)) if value else None for key, value in func_transicao.items()}
            automato = AFD(estados, alfabeto, func_transicao, estado_inicial, estados_finais)

        elif(AFN_or_AFD == "afd" and afd == False):
            print("Criação de AFD impossivel!!")
            os.system("pause")
            sys.exit(0)

        else:
            print("Nenhuma opção valida digitada!!")
            os.system("pause")
            sys.exit(0)
            
            #Criação de um novo diretorio, caso não exista para o armazenamento do automato
        new_directory = 'Automatos_'
        if(afd == True):
            new_directory = new_directory + "AFD"
        elif(afn == True):
            new_directory = new_directory + 'AFN'

        create_directory(new_directory)

            #instanciação grafica do automato
        imgAutomato = create_img(automato)
            
        strIDAutomato =  str(idAutomato)
            #salvando a imagem
        
        if(afd == True):
            save_img(imgAutomato, new_directory, strIDAutomato, afd=afd)
        elif(afn == True):
            save_img(imgAutomato, new_directory, strIDAutomato, afn=afn)

            #variavel de controle para criação de novos automatos set False
        new_AFD_AFN = False
    ##-----------------------------------------------------------------------------------------------------------------##

    ##------------------------------------------TESTE DE CADEIA PARA O AFD OU AFN CRIADO------------------------------------------------##

    entrada = input("Informe a cadeia de entrada: ")

        ##------------------------entrada para o AFD------------------------------##
    if isinstance(automato, AFD):
        reconheceuOUnao = automato.reconhecer_cadeiaAFD( entrada)
        if(reconheceuOUnao):
            print("Cadeia reconhecida pelo AFD!!")
        else:
            print("Cadeia não reconhecida pelo AFD!!")

        ##---------------------------------------entrada para o AFN-----------------------------##
    elif isinstance(automato, AFN):
        reconheceuOUnao = automato.reconhecer_cadeiaAFN( entrada)
        if(reconheceuOUnao):
            print("Cadeia reconhecida pelo AFN!!")
        else:
            print("Cadeia não reconhecida pelo AFN!!")

    os.system("pause")
    os.system("cls")
        
        # -----------------------Conversão de AFN para AFD se for um AFN----------------------------------------------------##]
    Conversao=""
    if(afn):
        Conversao = input("Deseja realizar a conversão de AFN para AFD(Yes/No) ? ").lower()

        if(Conversao == "yes"):
            AFD_posConversao = automato.convertendoAFNparaAFD(alfabeto, strIDAutomato)
            afn = False
            afd = True 
            os.system("pause")
            os.system("cls")

        ## ----------------------- TESTE DE CADEIA DO AFD CONVERTIDO -----------------------------##
        reconheceuOUnao = AFD_posConversao.reconhecer_cadeiaAFD(entrada)
        if(reconheceuOUnao):
            print("Cadeia anterior reconhecida pelo AFD convertido!!")
        else:
            print("Cadeia anterior não reconhecida pelo AFD convertido!!")

        #### --------------------------------Fim da Conversão ----------------------------####

    input("Pressione enter para Continuar")
    os.system('cls')

        #----------------------------- MINIMIZACAO---------------------------------------##

    if(Conversao == "yes"):
        minimizacao = input("Deseja fazer a minimizacao ? (Yes/No)").lower()
        if(minimizacao == "yes"): 
            afd_minimizado = AFD_posConversao.minimize()
            create_directory("Automatos_Minimizados")
            img_afd_minimizado = create_img(afd_minimizado)
            save_img(img_afd_minimizado,"Automatos_Minimizados", strIDAutomato, afd=afd)
            print("AFD minimizado criado com sucesso!!", end='\n')
            print("Vizualize na imagem gerada!!")
            os.system("pause")
            os.system("cls")
        
        ##----------------------------------------------------------------------------------##

        ## ----------------------------- TESTE DE EQUIVALENCIA ENTRE UM AFN E AFD ------------------------ ####
    if(isinstance(automato, AFN) and Conversao == "yes"):
        max_cadeias = 10
        max_tamanho = random.randint(1, 100)
        cadeias_para_teste = gerador_cadeias(alfabeto, max_cadeias, max_tamanho)

        print("Cadeias para o teste de Equivalencia: ", end='\n')
        for i in range(max_cadeias):
            print(cadeias_para_teste[i], end='\n')

        os.system("pause")
        os.system("cls")

        for i in range(max_cadeias):
            reconheceuOUnaoAFD = AFD_posConversao.reconhecer_cadeiaAFD(cadeias_para_teste[i])
            reconheceuOUnaoAFN = automato.reconhecer_cadeiaAFN(cadeias_para_teste[i])

            if(reconheceuOUnaoAFD == True and reconheceuOUnaoAFN == True or reconheceuOUnaoAFD == False and reconheceuOUnaoAFN == False):
                equivalentes = True
            else:
                equivalentes = False
                break; 
            
        if(equivalentes == True):
            print("AFN e AFD convertido são equivalentes!!")
        else:
            print("AN e AFN não são equivalentes!!")
            
        os.system("pause")
        os.system("cls")
        ## ----------------------------------------------------------------------------------------------- ####

    continue_or_not = input("Deseja testar mais automatos ? [Yes/No] ").lower()
    print(" ")
    if continue_or_not == "no":
        stop_program = True
    else:
        novo_afd_afn = input("Deseja criar um novo automato ? [Yes/No] ").lower()
        if novo_afd_afn == 'yes':
            new_AFD_AFN = True
            
    os.system("cls")

