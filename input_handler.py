def escolha_usuario_inicio():
    print("""Bem vindo! Escolha uma das opções
      [1] - Baixar todos os capítulos de um mangá
      [2] - Baixar capítulos específicos de um mangá (para intervalo use x-x)
      [3] - Alterar idioma (padrão pt-BR)
      [4] - Sair""")
    
    opcao = int(input("Digite a opção: "))
    return(opcao)

def encontrar_nome_manga():
    return input("Escreva o nome do mangá: ")

def selecao_mangas():
    return int(input("Selecione o mangá que deseja escolher:"))

def manga_language():
    return int(input("Selecione o idioma desejado: "))

def choose_chapters():
    user_input = input("Escreva os capítulos que deseja baixar. Vazio para todos, com espaço para capítulos específicos e x-x para intervalo (Ex. 1, 5-10): ")
    final_list = []
    parts = user_input.replace(',',' ').split()

    for part in parts:
        if '-' in parts:
            start, end = part.split('-')
            for i in range(int(start), int(end) + 1):
                final_list.append(int(i))
        else:
            final_list.append(int(part))
    return final_list
                



