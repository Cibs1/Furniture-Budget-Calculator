import sqlite3
#from precoMaterial import obter_preco_material

def obter_preco_material(codigo_material):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preço FROM materiais WHERE codigo = ?
    ''', (codigo_material,))
    preco = cursor.fetchone()
    conn.close()
    return preco[0] if preco else None

def obter_preco_ferragens(codigo_ferragem):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preço FROM ferragens WHERE codigo = ?
    ''', (codigo_ferragem,))
    preco = cursor.fetchone()
    conn.close()
    return preco[0] if preco else None

def obter_preco_orla(codigo_orla):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT preço FROM materiais WHERE codigo = ?
    ''', (codigo_orla,))
    preco = cursor.fetchone()
    conn.close()
    return preco[0] if preco else None

def preco_gavetas(codigo_material_gavetas, dimensoes, alturas, gavetas):
    material_gaveta = obter_preco_material(codigo_material_gavetas)
    topo = dimensoes[0] * dimensoes[1]
    preco_gavetas = 0
    for altura in alturas:
        frente = dimensoes[0] * altura
        laterais = dimensoes[1] * altura
        traseira = frente / 2
        preco_gavetas += material_gaveta * (topo + frente + laterais + traseira) / 1000000
    return preco_gavetas * gavetas

def calc_superior(codigo_material ,dimensoes,gavetas,gavetões,portas,prateleiras,codigo_material_orla):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    for i in range(0, len(dimensoes)):
        dimensoes[i] = float(dimensoes[i])/1000
    cursor = conn.cursor()
    preco_m2 = float(obter_preco_material(codigo_material))
    preco_orla=float(obter_preco_orla(codigo_material_orla))
    cursor.execute(f"SELECT tempo FROM moveis WHERE nome = 'coluna'")
    tempo = cursor.fetchone()[0]
    if preco_m2 is None:
        print("Material não encontrado")
    costas=dimensoes[0]*dimensoes[2]
    if portas==0:
        preco_portas=0
    else:
        preco_portas = preco_m2*(dimensoes[0]*dimensoes[2]) +2* float(portas)
    if gavetas==0:
        preco_gavetas=0
    else:
        preco_gavetas= float(gavetas)*55
    if gavetões==0:
        preco_gavetões=0
    else:
        preco_gavetões= float(gavetões)*60
    if prateleiras==0:
        preco_prateleiras=0
    else:
        preco_prateleiras=(preco_m2*(dimensoes[0]*dimensoes[1]))*float(prateleiras) 
        + preco_orla*(dimensoes[0]*2+dimensoes[1]*2)*float(prateleiras)
    topo=dimensoes[0]*dimensoes[1]
    laterais=dimensoes[1]*dimensoes[2]*2
    area=(costas+topo*2+laterais)
    area_orla= (dimensoes[0]*2+dimensoes[1]*2)*2+dimensoes[0]*dimensoes[2]*2+dimensoes[1]*dimensoes[2]*2
    custo_orla=preco_orla*area_orla
    custo_material = float(area) * preco_m2 +preco_portas + preco_gavetas + preco_gavetões + preco_prateleiras + custo_orla
    mao_de_obra = tempo * 15  # exemplo de custo de mão de obra
    custo_total = custo_material + mao_de_obra
    cursor.close()
    return custo_total