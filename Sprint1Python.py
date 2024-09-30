"""
G4-TECH
Membros:
Augusto Douglas Nogueira de Mendonça - RM558371
Gabriel Vasquez Queiroz da Silva - RM557056
Guilherme Araujo de Carvalho - RM558926
Gustavo Oliveira Ribeiro - RM559163
"""

from typing import List, Tuple, Optional

# Função de boas-vindas
def boas_vindas() -> bool:
    print('\n----------------------------------------------------------')
    print('BEM VINDO AO G4-TECH - ANALISADOR DE VOLTAS')
    print('----------------------------------------------------------\n')
    while True:
        print("Escolha uma opção:")
        print("1. Iniciar programa")
        print("2. Encerrar programa")
        opcao = input("Digite o número da opção desejada: ")
        if opcao == "1":
            return True
        elif opcao == "2":
            print('\n---------------------------------------------------------')
            print("ENCERRANDO O PROGRAMA. OBRIGADO POR UTILIZAR!")
            print('---------------------------------------------------------\n')
            return False
        else:
            print("\nOpção inválida. Por favor, escolha uma opção válida.\n")

# Função para voltar ao menu
def voltar_ao_menu() -> bool:
    while True:
        retorno = input("\nDeseja voltar ao menu? (s/n): ").strip().lower()
        if retorno == 's':
            return True
        elif retorno == 'n':
            print('\n---------------------------------------------------------')
            print("ENCERRANDO O PROGRAMA. OBRIGADO POR UTILIZAR!")
            print('---------------------------------------------------------\n')
            return False
        else:
            print("Entrada inválida. Por favor, responda com 's' para sim ou 'n' para não.")

# Função para converter o tempo em segundos para minuto:segundo:milissegundo
def converter_tempo(tempo: float) -> str:
    """Converte o tempo em segundos para o formato MM:SS:MMM."""
    minutos = int(tempo // 60)
    segundos = int(tempo % 60)
    milissegundos = int((tempo - int(tempo)) * 1000)
    return f"{minutos:02}:{segundos:02}:{milissegundos:03}"

# Função para encontrar o melhor e pior tempo e suas respectivas voltas
def encontrar_melhor_pior_tempo(tempos: List[float]) -> Tuple[float, float, int, int]:
    """Encontra o melhor e o pior tempo, assim como suas respectivas voltas."""
    melhor_tempo = tempos[0]
    pior_tempo = tempos[0]
    volta_melhor_tempo = 1
    volta_pior_tempo = 1

    for i in range(1, len(tempos)):
        if tempos[i] < melhor_tempo:
            melhor_tempo = tempos[i]
            volta_melhor_tempo = i + 1
        if tempos[i] > pior_tempo:
            pior_tempo = tempos[i]
            volta_pior_tempo = i + 1

    return melhor_tempo, pior_tempo, volta_melhor_tempo, volta_pior_tempo

# Função para atualizar a lista de melhores voltas
def atualizar_melhores_voltas(melhores_voltas: List[dict], nome: str, tempo: float, volta: int) -> None:
    """Atualiza a lista de melhores voltas com o novo tempo."""
    melhores_voltas.append({"nome": nome, "tempo": tempo, "volta": volta})
    melhores_voltas.sort(key=lambda x: x["tempo"])  # Ordena pela melhor volta (menor tempo) 
    
# Função para atualizar a lista de voltas
def atualizar_voltas(todas_voltas: List[dict], nome: str, tempos_voltas: List[float]) -> None:
    """Atualiza a lista de voltas com todas as voltas de um piloto."""
    for i, tempo in enumerate(tempos_voltas):
        todas_voltas.append({"nome": nome, "tempo": tempo, "volta": i + 1})
    
# Função para exibir a melhor volta registrada
def exibir_melhor_volta(melhores_voltas: List[dict]) -> Tuple[Optional[str], Optional[str], Optional[int]]:
    """Exibe a melhor volta registrada na lista."""
    if melhores_voltas:
        melhor_volta = melhores_voltas[0]
        return melhor_volta["nome"], converter_tempo(melhor_volta["tempo"]), melhor_volta["volta"]
    else:
        return None, None, None

# Função para calcular a média dos tempos das voltas
def calcular_media_tempos(tempos: List[float]) -> float:
    """Calcula a média dos tempos das voltas."""
    if not tempos:
        return 0
    return sum(tempos) / len(tempos)

# Função para exibir todas as melhores voltas registradas
def exibir_todas_melhores_voltas(melhores_voltas: List[dict]) -> None:
    """Exibe todas as melhores voltas registradas."""
    if melhores_voltas:
        print("\nMelhores voltas registradas:")
        for volta in melhores_voltas:
            print(f"Piloto: {volta['nome']} - Tempo: {converter_tempo(volta['tempo'])} (Volta {volta['volta']})")
    else:
        print("Ainda não há melhores voltas registradas.")

# Função para visualizar tempos de um piloto específico
def visualizar_tempo_piloto(todas_voltas: List[dict], nome_piloto: str = "") -> None:
    """Exibe os tempos de um piloto específico e calcula a média de suas voltas."""
    if not nome_piloto:
        nome_piloto = input("Digite o nome do piloto: ").strip()

    tempos = [volta for volta in todas_voltas if volta["nome"].lower() == nome_piloto.lower()]
    if tempos:
        print(f"\nTempos registrados para {nome_piloto}:")
        for volta in tempos:
            print(f"Tempo: {converter_tempo(volta['tempo'])} (Volta {volta['volta']})")
        
        # Calcular a média dos tempos
        media = calcular_media_tempos([volta["tempo"] for volta in tempos])
        print(f"\nMédia dos tempos de {nome_piloto}: {converter_tempo(media)}")
    else:
        print(f"Nenhum tempo registrado para o piloto {nome_piloto}.")

# Função para salvar os melhores tempos em um arquivo
def salvar_melhores_tempos(melhores_voltas: List[dict], filename: str = "melhores_tempos.txt") -> None:
    """Salva os melhores tempos registrados em um arquivo de texto."""
    with open(filename, "w") as file:
        file.write("Melhores Tempos Registrados\n")
        file.write("=" * 40 + "\n")
        for volta in melhores_voltas:
            file.write(f"Piloto: {volta['nome']}\n")
            file.write(f"Tempo: {converter_tempo(volta['tempo'])} (Volta {volta['volta']})\n")
            file.write("-" * 40 + "\n")
    print(f"Melhores tempos salvos em '{filename}' com sucesso!")

# Função para garantir que a entrada seja um número inteiro
def entrada_numero_inteiro(mensagem: str) -> int:
    while True:
        try:
            valor = int(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

# Função para garantir que a entrada seja um número decimal
def entrada_numero_float(mensagem: str) -> float:
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número decimal válido.")

# Lista para armazenar os melhores tempos
melhores_voltas = []

# Lista para armazenar todos os tempos
todas_voltas = []

# Loop principal do programa
if boas_vindas():
    while True:
        print('\n----------------------------------------------------------')
        print('MENU PRINCIPAL')
        print('----------------------------------------------------------\n')

        print("Escolha uma opção:")
        print("1. Registrar voltas")
        print("2. Exibir melhor volta registrada")
        print("3. Calcular média dos tempos das voltas")
        print("4. Exibir todas as melhores voltas registradas")
        print("5. Visualizar tempos de um piloto específico")
        print("6. Salvar melhores tempos em arquivo")
        print("7. Sair")

        opcao = input("Digite o número da opção desejada: ")
        
        match opcao:
            case "1":
                # Exibir a melhor volta registrada
                melhor_nome, melhor_tempo_registrado, melhor_volta = exibir_melhor_volta(melhores_voltas)
                if melhor_nome:
                    print(f"\nMelhor volta registrada: {melhor_tempo_registrado} (Volta {melhor_volta}) por {melhor_nome}")
                else:
                    print("\nAinda não há voltas registradas.")

                # Coletar o nome do piloto
                nome_piloto = input("Digite o nome do piloto: ").strip()
                if not nome_piloto:
                    print("Nome do piloto não pode estar em branco. Tente novamente.")
                    continue

                # Coletar o número de voltas e os tempos de cada volta
                voltas = entrada_numero_inteiro("Digite o número de voltas: ")

                tempos_voltas = []
                for i in range(voltas):
                    tempo = entrada_numero_float(f"Digite o tempo da volta {i + 1} em segundos: ")
                    tempos_voltas.append(tempo)

                # Encontrar o melhor e pior tempo e suas respectivas voltas
                melhor_tempo, pior_tempo, volta_melhor_tempo, volta_pior_tempo = encontrar_melhor_pior_tempo(tempos_voltas)

                # Atualizar a lista de melhores voltas
                atualizar_melhores_voltas(melhores_voltas, nome_piloto, melhor_tempo, volta_melhor_tempo)
                
                # Atualizar a lista de voltas com todas as voltas
                atualizar_voltas(todas_voltas, nome_piloto, tempos_voltas)

                # Exibir os resultados
                print("\nTempos das voltas:")
                for i, tempo in enumerate(tempos_voltas):
                    print(f"Volta {i + 1}: {converter_tempo(tempo)}")

                print(f"\nMelhor tempo: {converter_tempo(melhor_tempo)} (Volta {volta_melhor_tempo})")
                print(f"Pior tempo: {converter_tempo(pior_tempo)} (Volta {volta_pior_tempo})")

            case "2":
                melhor_nome, melhor_tempo_registrado, melhor_volta = exibir_melhor_volta(melhores_voltas)
                if melhor_nome:
                    print(f"\nMelhor volta registrada: {melhor_tempo_registrado} (Volta {melhor_volta}) por {melhor_nome}")
                else:
                    print("\nAinda não há voltas registradas.")

            case "3":
                if todas_voltas:
                    tempos = [volta["tempo"] for volta in todas_voltas]
                    media = calcular_media_tempos(tempos)
                    print(f"\nA média dos tempos de todas as voltas é: {converter_tempo(media)}")
                else:
                    print("\nAinda não há tempos registrados para calcular a média.")

            case "4":
                exibir_todas_melhores_voltas(melhores_voltas)

            case "5":
                visualizar_tempo_piloto(todas_voltas)

            case "6":
                salvar_melhores_tempos(melhores_voltas)

            case "7":
                print('\n---------------------------------------------------------')
                print("ENCERRANDO O PROGRAMA. OBRIGADO POR UTILIZAR!")
                print('---------------------------------------------------------\n')
                break

            case _:
                print("Opção inválida. Por favor, escolha uma opção válida.")

        # Voltar ao menu ou encerrar o programa
        if not voltar_ao_menu():
            break