sair = False

while sair == False:

    print("1 - Analisar resumo")
    print("2 - Sair")
    
    opcao = input("Informe o dígito da opção escolhida:")
    opcao = int(opcao)

    if opcao == 1:
        telefone = input("Informe o seu número de telefone:")
        resumoCurriculo = input("Informe o resumo do seu currículo:")
        resumoCurriculo = resumoCurriculo.upper()
        if "PYTHON" in resumoCurriculo or "JAVA" in resumoCurriculo or "C++" in resumoCurriculo or "C#" in resumoCurriculo:
            print("Palavras chaves encontradas.")
            if "PYTHON" in resumoCurriculo:
                print("Palavra-chave 'Python' encontrada")
            if "JAVA" in resumoCurriculo:
                print("Palavra-chave 'Java' encontrada")
            if "C++" in resumoCurriculo:
                print("Palavra-chave 'C++' encontrada")
            if "C#" in resumoCurriculo:
                print("Palavra-chave 'C#' encontrada")
            print("Candidato recomendado, prosseguindo para agendamento de entrevista.")
        else:
            print("Não foi encontrada nenhuma palavra-chave.")
            print("Candidato não-recomendado.")
        sair == True
    
    if opcao == 2:
        exit()