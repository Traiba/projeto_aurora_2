prioridades = {
    "Extrema": 5,
    "Alta": 4,
    "Média-Alta": 3,
    "Média": 2,
    "Baixa": 1
}

modulos_missao = [
    {"id": "MOD-01", "nome": "Suporte Médico", "massa": 14200, "criticidade": prioridades["Extrema"], "combustivel": 70},
    {"id": "MOD-02", "nome": "Geração de Energia", "massa": 9800, "criticidade": prioridades["Alta"], "combustivel": 78},
    {"id": "MOD-03", "nome": "Habitação Principal", "massa": 18500, "criticidade": prioridades["Média-Alta"], "combustivel": 55},
    {"id": "MOD-04", "nome": "Laboratório Científico", "massa": 11300, "criticidade": prioridades["Média"], "combustivel": 75},
    {"id": "MOD-05", "nome": "Logística e Suprimentos", "massa": 22700, "criticidade": prioridades["Baixa"], "combustivel": 38}
]

def buscar_por_caracteristica(criterio, valor=None):
    
    if criterio == "menor_combustivel":
        return min(modulos_missao, key=lambda m: m['combustivel'])
    
    elif criterio == "maior_prioridade":
        return max(modulos_missao, key=lambda m: m['criticidade'])
    
    elif criterio == "tipo_carga":
        return [m for m in modulos_missao if valor.lower() in m['nome'].lower()]
    
    return None

