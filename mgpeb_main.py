from collections import deque

# Mapeamento de nível de criticidade para valor numérico usado na ordenação
prioridades = {
    "Extrema": 5,
    "Alta": 4,
    "Média-Alta": 3,
    "Média": 2,
    "Baixa": 1
}

# Módulos da missão com seus dados operacionais
modulos_missao = [
    {"id": "MOD-01", "nome": "Suporte Médico", "massa": 14200, "criticidade": prioridades["Extrema"], "combustivel": 70, "status": "OK"},
    {"id": "MOD-02", "nome": "Geração de Energia", "massa": 9800, "criticidade": prioridades["Alta"], "combustivel": 78, "status": "OK"},
    {"id": "MOD-03", "nome": "Habitação Principal", "massa": 18500, "criticidade": prioridades["Média-Alta"], "combustivel": 55, "status": "OK"},
    {"id": "MOD-04", "nome": "Laboratório Científico", "massa": 11300, "criticidade": prioridades["Média"], "combustivel": 75, "status": "OK"},
    {"id": "MOD-05", "nome": "Logística e Suprimentos", "massa": 22700, "criticidade": prioridades["Baixa"], "combustivel": 38, "status": "OK"}
]

def buscar_por_caracteristica(criterio, valor=None):
    # Retorna módulo(s) com base no critério informado
    if criterio == "menor_combustivel":
        return min(modulos_missao, key=lambda m: m['combustivel'])

    elif criterio == "maior_prioridade":
        return max(modulos_missao, key=lambda m: m['criticidade'])

    elif criterio == "tipo_carga":
        # Filtra por substring no nome do módulo
        return [m for m in modulos_missao if valor.lower() in m['nome'].lower()]

    return None

def reorganizar_fila_pouso(criterio, decrescente=True):
    # Reordena a fila global de pouso pelo campo informado
    global fila_pouso

    ordenados = sorted(list(fila_pouso), key=lambda x: x[criterio], reverse=decrescente)

    fila_pouso = deque(ordenados)
    print(f"Fila reorganizada por: {criterio}")

def avaliar_autorizacao_pouso(modulo, vento_kmh, visibilidade_km):
    # Verifica condições mínimas de segurança antes de autorizar o pouso
    if modulo['combustivel'] < 35.0:
        return "BLOQUEADO: Combustível insuficiente."

    elif vento_kmh >= 50.0:
        return "BLOQUEADO: Rajadas de vento fora do limite operacional."

    elif visibilidade_km <= 10.0:
        return "BLOQUEADO: Visibilidade insuficiente para navegação LIDAR."

    elif modulo.get('status') == "ALERTA":
        return "BLOQUEADO: Módulo com falha reportada."

    else:
        return f"AUTORIZADO: {modulo['nome']} pronto para descida."


# Fila de pouso inicializada com todos os módulos da missão
fila_pouso = deque(modulos_missao)

print("--- MGPEB: Início da Sequência de Pouso ---")

# Ordena por criticidade decrescente: módulos mais críticos pousam primeiro
reorganizar_fila_pouso("criticidade", decrescente=True)

vento_atual = 15.0
visibilidade_atual = 12.0

# Processa cada módulo da fila até esgotá-la
while fila_pouso:

    modulo_atual = fila_pouso.popleft()

    resultado = avaliar_autorizacao_pouso(modulo_atual, vento_atual, visibilidade_atual)

    print(f"\nVerificando {modulo_atual['nome']}:")
    print(f"Status do MGPEB: {resultado}")

print("\n--- Fila de pouso processada com sucesso ---")

# Pilha de histórico de missão (LIFO)
historico_missao = []

print("\n--- Registrando módulos no histórico da missão ---")
for modulo in modulos_missao:
    historico_missao.append(modulo["nome"])
    print(f"  Empilhado: {modulo['nome']}")

print("\n--- Revisando histórico (último processado primeiro) ---")
while historico_missao:
    print(f"  Desempilhado: {historico_missao.pop()}")
