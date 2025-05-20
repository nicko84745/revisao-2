# 🤖 Classificador de Inteligência Artificial

# Solicita o nome do sistema de IA
nome_ia = input("Informe o nome do sistema de IA: ")

# Solicita a pontuação de performance
try:
    pontuacao = float(input("Informe a pontuação de performance (0 a 100): "))

    print(f"\nSistema: {nome_ia}")
    print(f"Pontuação: {pontuacao:.1f}")

    # Classificação baseada na pontuação
    if pontuacao < 0:
        print("Classificação: Erro: Pontuação inválida! ❌")
    elif pontuacao <= 39.9:
        print("Classificação: IA em Treinamento 🍼")
        print("🔁 Continue alimentando os dados para melhorar a performance.")
    elif pontuacao <= 69.9:
        print("Classificação: IA Intermediária 🧠")
    elif pontuacao <= 89.9:
        print("Classificação: IA Otimizada 🚀")
    elif pontuacao <= 100:
        print("Classificação: Inteligência Artificial Avançada 🤯")
        print("⚡ Iniciando protocolo de expansão neural...")
    else:
        print("Classificação: Erro: IA fora da escala! ⚠️")
except ValueError:
    print("Erro: Entrada inválida! Por favor, insira um número para a pontuação.")