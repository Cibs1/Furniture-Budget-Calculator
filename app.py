import sqlite3
from flask import Flask, request, jsonify, send_from_directory, redirect, url_for,render_template
from flask_cors import CORS

from inserir2 import insert_row
from atualizar import update_row
from apagar_linha import delete_row

from calcularOrc import calc_orcamento
from moveis.armario import calc_armario
from moveis.piso import calc_piso
from moveis.tampo import calc_tampo
from moveis.independente import calc_independente
from moveis.coluna import calc_coluna


app = Flask(__name__, static_folder='static')
CORS(app)  # Habilita CORS para todas as rotas

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/atualizar.html')
def atualizar_page():
    return send_from_directory('static', 'atualizar.html')

@app.route('/Contact.html')
def contact_page():
    return send_from_directory('static', 'Contact.html')

@app.route('/about.html')
def about_page():
    return send_from_directory('static', 'about.html')

@app.route('/atualizar', methods=['POST'])
def atualizar():
    action = request.form['action']
    table = request.form['table']
    database = 'orcamentos_cozinha.db'
    
    if action == 'update':
        row_id = request.form['id']
        attribute = request.form['attribute']
        new_value = request.form['value']
        update_row(database, table, row_id, attribute, new_value)
    
    elif action == 'insert':
        columns = request.form['columns'].split(',')
        values = request.form.getlist('values')
        insert_row(database, table, columns, values)
    
    elif action == 'delete':
        row_id = request.form['id']
        delete_row(database, table, row_id)
    
    return redirect(url_for('atualizar_page'))

@app.route('/atualizar/delete', methods=['DELETE'])
def delete():
    data = request.get_json()
    table = data['table']
    row_id = data['id']
    database = 'orcamentos_cozinha.db'
    delete_row(database, table, row_id)
    return jsonify({'status': 'success'})

@app.route('/list_tables', methods=['GET'])
def list_tables():
    database = 'orcamentos_cozinha.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    conn.close()
    return jsonify(tables)

@app.route('/show_table/<table_name>', methods=['GET'])
def show_table(table_name):
    database = 'orcamentos_cozinha.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    columns = [description[0] for description in cursor.description]
    conn.close()
    result = [dict(zip(columns, row)) for row in rows]
    return jsonify(result)

@app.route('/get_columns/<table_name>', methods=['GET'])
def get_columns(table_name):
    database = 'orcamentos_cozinha.db'
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = [info[1] for info in cursor.fetchall()]
    conn.close()
    return jsonify(columns)

@app.route('/calcular_orcamento', methods=['POST'])
def calcular_orcamento():
    try:
        data = request.json
        moveis = data.get('moveis', [])
        preco_total = 0

        for movel in moveis:
            tipo = movel.get('tipo')
            codigo_material = movel.get('codigo')
            dimensoes = movel.get('dimensoes', [])
            
            if tipo in ['coluna', 'inferior', 'superior']:
                codigo_material_orla = movel.get('codigo_orla', '')
                portas = movel.get('portas', 0)
                gavetas = movel.get('gavetas', 0)
                gavetoes = movel.get('gavetoes', 0)
                prateleiras = movel.get('prateleiras', 0)
                preco_total += calc_coluna(codigo_material, dimensoes, gavetas, gavetoes, portas, prateleiras, codigo_material_orla)
            elif tipo == 'piso':
                nome_material = movel.get('nome_material', '')
                preco_total += calc_piso(dimensoes, nome_material)
            elif tipo == 'tampo':
                nome_material = movel.get('nome_material', '')
                preco_total += calc_tampo(nome_material, dimensoes)
            elif tipo in ['remate', 'placa', 'painel']:
                nome_material = movel.get('nome_material', '')
                preco_total += calc_independente(nome_material, dimensoes)
            else:
                return jsonify({'success': False, 'message': 'Tipo de móvel inválido'}), 400

        return jsonify({'success': True, 'custo_total': preco_total})

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 500


# Página das Tabelas
@app.route('/tabelas')
def tabelas():
    return render_template('tabelas.html')

# Exibir tabela específica
@app.route('/tabela/<nome_tabela>')
def mostrar_tabela(nome_tabela):
    conn = sqlite3.connect('orcamentos_cozinha.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {nome_tabela}")
    colunas = [desc[0] for desc in cursor.description]
    linhas = cursor.fetchall()
    conn.close()
    return render_template('tabela.html', nome_tabela=nome_tabela, colunas=colunas, linhas=linhas)

if __name__ == '__main__':
    app.run(debug=True)




