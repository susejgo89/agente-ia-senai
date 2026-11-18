import ollama



def perguntar_agente(instrucao, mensagem):
    resposta = ollama.chat(model='qwen2.5:3b', messages=[
        {'role': 'system', 'content': instrucao},
        {'role': 'user', 'content': mensagem}
    ])
    return resposta['message']['content']

def gerar_roteiro(tema, prompt_base):
    mensagem = f"Tema: {tema}\n\nInstruções do roteiro:\n{prompt_base}"
    return perguntar_agente(instrucao, mensagem)

instrucao = "Você é um roteirista especialista em criar roteiros claros, envolventes e bem estruturados para vídeos."

prompt_base = "Crie um roteiro curto de 1 minuto com: gancho inicial, explicação simples e chamada para ação no final."

print('Agente roteirista pronto! Digite "sair" para encerrar.')

while True:
    tema = input("\nDigite o tema do roteiro: ")
    if tema == "sair":
        break

    print(f"\n--- Gerando roteiro para: {tema} ---")
    roteiro = gerar_roteiro(tema, prompt_base)
    print(roteiro)



    