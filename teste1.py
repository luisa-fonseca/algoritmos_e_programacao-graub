import numpy as np

sair = False

while sair == False:

    print("1 - Calcular a média de um(a) aluno(a)")
    print("2 - Sair")
    
    opcao = input("Informe o dígito da opção escolhida:")
    opcao = int(opcao)

    if opcao == 1:
            numeroMatricula = input("Digite o número da sua matrícula:")
            nomeDisciplina = input("Informe o nome da disciplina:")
            notas = np.array([0, 0, 0])
            for i in range (3):
                notas[i] = input("Digite suas três notas nessa disciplina:")
                notas[i] = int(notas[i])
            if (numeroMatricula.isdigit() == False) or (nomeDisciplina.isalpha() == False) or ((notas[0] < 0 or notas[0] > 10) or (notas[1] < 0 or notas[1] > 10) or (notas[2] < 0 or notas[2] > 10)):
                print("Erro. Alguns dos requisitos não foram atendidos.")
                sair == True
            else:
                print("Número de matrícula:", numeroMatricula)
                print("Nome da disciplina:", nomeDisciplina)
                print("Três notas:", notas)
                mediaSimples = (notas[0] + notas[1] + notas[2])/3
                print("Média simples:", mediaSimples)
    elif opcao == 2:
        exit()
