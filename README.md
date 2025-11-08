teste1: instruções

1. Crie um programa que ofereça as as seguintes opções:

    1. Calcular a média de um(a) aluno(a)

    2. Sair

Na opção 1, o programa deve ler do teclado o número da matrícula, o nome da disciplina e as três notas dele(a) nessa disciplina. A matrícula e o nome da disciplina devem ficar armazenados em strings e as notas devem ficar armazenadas em um array. 

APÓS receber TODAS as informações, o programa deve verificar se os dados preenchem os seguintes requisitos: 

- a matrícula só pode conter dígitos
- o nome da disciplina só pode conter letras
- todas as notas precisam estar entre 0 e 10

Se TODOS os requisitos forem atendidos, o programa deve mostrar na tela o número de matrícula, o nome da disciplina, todas as notas e a média simples do(a) aluno(a).

Se ALGUM dos requisitos acima NÃO for atendido, o programa deve mostrar uma mensagem de erro na tela e deve retornar ao menu inicial.

Na opção 2 o programa deve encerrar a execução.

teste2: instruções

2. Construa um programa que simule a análise de currículos para vagas de programador(a). O programa será usado no setor de RH de uma empresa. 

Devem ser mostradas as opções:

    1. Analisar resumo

    2. Sair

Na opção 1 o programa deve solicitar a) o telefone do candidato e b) o resumo do currículo. O programa deve transformar todas as letras em maiúsculas e deve analisar o texto buscando pelas seguintes palavras-chave:  "PYTHON", "JAVA", "C++", "C#".

O programa deve exibir todas as palavras-chave encontradas no resumo. Caso não seja encontrada nenhuma palavra-chave, deve ser exibida a mensagem "Não foi encontrada nenhuma palavra-chave.".

Se for encontrada pelo menos uma palavra-chave, deve ser impressa na tela a mensagem: "Candidato recomendado, prosseguindo para agendamento de entrevista." Considere que o sistema enviará automaticamente uma mensagem para o(a) candidato(a), isto é, sem a necessidade de qualquer ação do RH.

Do contrário, deve ser mostrada na tela a mensagem: "Candidato não-recomendado".

Após a análise o programa volta ao menu inicial.

Na opção 2 o programa encerra a execução.

Use somente strings para armazenar os dados do candidato.