# Plano Detalhado para o App de Gestão de Estoque

Este plano descreve a criação de um aplicativo web em Python usando Flask e SQLite para gerenciar os equipamentos internos da empresa. O design segue uma estética inspirada no site da Tesla – moderno, minimalista e com tipografia e espaçamentos bem definidos. Todas as funcionalidades foram planejadas para incluir os seguintes campos:  
- Nº DO BEM  
- CATEGORIA  
- OBJETO  
- MODELO  
- DATA AQUISIÇÃO  
- NOTA FISCAL  
- VALOR  
- ESTADO DE CONSERVAÇÃO  
- SETOR ALOCADO  
- RESPONSÁVEL / OPERADOR  
- DATA ENTREGA  
- MANUTENÇÃO DADA  
- SERVIÇO REALIZADO  

A seguir, o plano com os arquivos dependentes, alterações e melhores práticas.

---

## Estrutura de Pastas e Arquivos

```
/python_inventory/

├── app.py
├── models.py
├── forms.py
├── requirements.txt
├── db_setup.py           # (opcional) para inicializar o banco de dados
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── layout.html
    ├── index.html
    ├── add_equipment.html
    └── edit_equipment.html
```

---

## 1. requirements.txt

Liste as dependências necessárias:
```plaintext
Flask
Flask-WTF
Flask-SQLAlchemy
```

---

## 2. app.py

Configure o aplicativo Flask, integração com o banco de dados e as rotas principais.  
- Configure a aplicação para usar SQLite (por exemplo, 'sqlite:///inventory.db').  
- Implemente as rotas:  
  - `/` – Lista o inventário (index).  
  - `/add` – Página para adicionar novo equipamento.  
  - `/edit/<int:id>` – Página para editar equipamento existente.  
  - `/delete/<int:id>` – Endpoint para remoção com tratamento de erros.  
- Adicione handlers para erros 404 e 500 com feedback amigável.  
- Utilize sessões e mensagens Flash para feedback de sucesso/erro.  
- Exemplo trecho de código:
```python
from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Equipment
from forms import EquipmentForm
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SECRET_KEY'] = 'sua_chave_secreta'
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    equipments = Equipment.query.all()
    return render_template('index.html', equipments=equipments)

@app.route('/add', methods=['GET', 'POST'])
def add_equipment():
    form = EquipmentForm()
    if form.validate_on_submit():
        try:
            equip = Equipment(
                num_bem=form.num_bem.data,
                categoria=form.categoria.data,
                objeto=form.objeto.data,
                modelo=form.modelo.data,
                data_aquisicao=form.data_aquisicao.data,
                nota_fiscal=form.nota_fiscal.data,
                valor=form.valor.data,
                estado_conservacao=form.estado_conservacao.data,
                setor_alocado=form.setor_alocado.data,
                responsavel_operador=form.responsavel_operador.data,
                data_entrega=form.data_entrega.data,
                manutencao_dada=form.manutencao_dada.data,
                servico_realizado=form.servico_realizado.data
            )
            db.session.add(equip)
            db.session.commit()
            flash('Equipamento adicionado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao adicionar: {str(e)}', 'danger')
    return render_template('add_equipment.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_equipment(id):
    equip = Equipment.query.get_or_404(id)
    form = EquipmentForm(obj=equip)
    if form.validate_on_submit():
        try:
            form.populate_obj(equip)
            db.session.commit()
            flash('Equipamento atualizado com sucesso!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash(f'Erro ao atualizar: {str(e)}', 'danger')
    return render_template('edit_equipment.html', form=form)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_equipment(id):
    equip = Equipment.query.get_or_404(id)
    try:
        db.session.delete(equip)
        db.session.commit()
        flash('Equipamento removido!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao remover: {str(e)}', 'danger')
    return redirect(url_for('index'))

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
```

---

## 3. models.py

Defina o modelo de dados usando SQLAlchemy.  
- Crie o modelo "Equipment" com os campos requeridos, definindo tipos apropriados (String, Float, Date, Text).  
- Exemplo:
```python
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Equipment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_bem = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(50), nullable=False)
    objeto = db.Column(db.String(100), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    data_aquisicao = db.Column(db.Date, nullable=False)
    nota_fiscal = db.Column(db.String(50), nullable=False)
    valor = db.Column(db.Float, nullable=False)
    estado_conservacao = db.Column(db.String(50), nullable=False)
    setor_alocado = db.Column(db.String(50), nullable=False)
    responsavel_operador = db.Column(db.String(50), nullable=False)
    data_entrega = db.Column(db.Date, nullable=True)
    manutencao_dada = db.Column(db.String(50), nullable=True)
    servico_realizado = db.Column(db.Text, nullable=True)
```

---

## 4. forms.py

Implemente os formulários utilizando Flask-WTF para facilitar a entrada dos dados.  
- Crie um formulário "EquipmentForm" com todos os campos e validações obrigatórias.  
- Exemplo:
```python
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class EquipmentForm(FlaskForm):
    num_bem = StringField('Nº DO BEM', validators=[DataRequired()])
    categoria = StringField('CATEGORIA', validators=[DataRequired()])
    objeto = StringField('OBJETO', validators=[DataRequired()])
    modelo = StringField('MODELO', validators=[DataRequired()])
    data_aquisicao = DateField('DATA AQUISIÇÃO', format='%Y-%m-%d', validators=[DataRequired()])
    nota_fiscal = StringField('NOTA FISCAL', validators=[DataRequired()])
    valor = FloatField('VALOR', validators=[DataRequired()])
    estado_conservacao = StringField('ESTADO DE CONSERVAÇÃO', validators=[DataRequired()])
    setor_alocado = StringField('SETOR ALOCADO', validators=[DataRequired()])
    responsavel_operador = StringField('RESPONSÁVEL / OPERADOR', validators=[DataRequired()])
    data_entrega = DateField('DATA ENTREGA', format='%Y-%m-%d', validators=[])
    manutencao_dada = StringField('MANUTENÇÃO DADA')
    servico_realizado = TextAreaField('SERVIÇO REALIZADO')
    submit = SubmitField('Salvar')
```

---

## 5. Templates HTML

### 5.1 layout.html
- Arquivo base que define o cabeçalho, rodapé e inclui o CSS.  
- Inclua uma barra de navegação com links para "Início" e "Adicionar Equipamento".  
- Exemplo:
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Gestão de Estoque</title>
  <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
  <header>
    <h1>Gestão de Estoque</h1>
    <nav>
      <a href="{{ url_for('index') }}">Início</a>
      <a href="{{ url_for('add_equipment') }}">Adicionar Equipamento</a>
    </nav>
  </header>
  <main>
    {% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        <div class="flash-messages">
          {% for category, message in messages %}
            <div class="flash {{ category }}">{{ message }}</div>
          {% endfor %}
        </div>
      {% endif %}
    {% endwith %}
    {% block content %}{% endblock %}
  </main>
  <footer>
    <p>&copy; Empresa Interna</p>
  </footer>
</body>
</html>
```

### 5.2 index.html
- Exibe uma tabela com todos os equipamentos, seguindo uma estética limpa e moderna.  
- Utilize tipografia espaçada e cores suaves para linhas e cabeçalho inspirados na Tesla.
```html
{% extends "layout.html" %}
{% block content %}
  <h2>Lista de Equipamentos</h2>
  <table>
    <thead>
      <tr>
        <th>Nº DO BEM</th>
        <th>CATEGORIA</th>
        <th>OBJETO</th>
        <th>MODELO</th>
        <th>DATA AQUISIÇÃO</th>
        <th>NOTA FISCAL</th>
        <th>VALOR</th>
        <th>ESTADO</th>
        <th>SETOR</th>
        <th>RESPONSÁVEL</th>
        <th>DATA ENTREGA</th>
        <th>MANUTENÇÃO</th>
        <th>SERVIÇO</th>
        <th>Ações</th>
      </tr>
    </thead>
    <tbody>
      {% for equip in equipments %}
      <tr>
        <td>{{ equip.num_bem }}</td>
        <td>{{ equip.categoria }}</td>
        <td>{{ equip.objeto }}</td>
        <td>{{ equip.modelo }}</td>
        <td>{{ equip.data_aquisicao.strftime('%d/%m/%Y') if equip.data_aquisicao else '' }}</td>
        <td>{{ equip.nota_fiscal }}</td>
        <td>{{ equip.valor }}</td>
        <td>{{ equip.estado_conservacao }}</td>
        <td>{{ equip.setor_alocado }}</td>
        <td>{{ equip.responsavel_operador }}</td>
        <td>{{ equip.data_entrega.strftime('%d/%m/%Y') if equip.data_entrega else '' }}</td>
        <td>{{ equip.manutencao_dada }}</td>
        <td>{{ equip.servico_realizado }}</td>
        <td>
          <a href="{{ url_for('edit_equipment', id=equip.id) }}">Editar</a>
          <form action="{{ url_for('delete_equipment', id=equip.id) }}" method="post" onsubmit="return confirm('Confirma exclusão?');">
            <button type="submit">Excluir</button>
          </form>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

### 5.3 add_equipment.html e edit_equipment.html
- Use formulários simples e modernos com labels claros e campos com espaçamento adequado.
```html
{% extends "layout.html" %}
{% block content %}
  <h2>{{ 'Editar' if form.num_bem.data else 'Adicionar' }} Equipamento</h2>
  <form method="POST">
    {{ form.hidden_tag() }}
    <div class="form-group">
      {{ form.num_bem.label }}<br>
      {{ form.num_bem(size=32) }}
    </div>
    <div class="form-group">
      {{ form.categoria.label }}<br>
      {{ form.categoria(size=32) }}
    </div>
    <div class="form-group">
      {{ form.objeto.label }}<br>
      {{ form.objeto(size=32) }}
    </div>
    <div class="form-group">
      {{ form.modelo.label }}<br>
      {{ form.modelo(size=32) }}
    </div>
    <div class="form-group">
      {{ form.data_aquisicao.label }}<br>
      {{ form.data_aquisicao() }}
    </div>
    <div class="form-group">
      {{ form.nota_fiscal.label }}<br>
      {{ form.nota_fiscal(size=32) }}
    </div>
    <div class="form-group">
      {{ form.valor.label }}<br>
      {{ form.valor() }}
    </div>
    <div class="form-group">
      {{ form.estado_conservacao.label }}<br>
      {{ form.estado_conservacao(size=32) }}
    </div>
    <div class="form-group">
      {{ form.setor_alocado.label }}<br>
      {{ form.setor_alocado(size=32) }}
    </div>
    <div class="form-group">
      {{ form.responsavel_operador.label }}<br>
      {{ form.responsavel_operador(size=32) }}
    </div>
    <div class="form-group">
      {{ form.data_entrega.label }}<br>
      {{ form.data_entrega() }}
    </div>
    <div class="form-group">
      {{ form.manutencao_dada.label }}<br>
      {{ form.manutencao_dada(size=32) }}
    </div>
    <div class="form-group">
      {{ form.servico_realizado.label }}<br>
      {{ form.servico_realizado(rows=3, cols=40) }}
    </div>
    <div class="form-group">
      {{ form.submit() }}
    </div>
  </form>
{% endblock %}
```

---

## 6. static/css/style.css

Crie um CSS minimalista e moderno, inspirado na estética da Tesla.  
- Utilize fontes sans-serif, cores neutras (ex.: fundo branco, textos em cinza escuro) e espaçamentos amplos.  
- Exemplo:
```css
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  background-color: #ffffff;
  color: #333333;
  margin: 0;
  padding: 0;
}
header {
  background-color: #f8f8f8;
  padding: 20px;
  text-align: center;
  border-bottom: 1px solid #e0e0e0;
}
header h1 {
  margin: 0;
  font-size: 2rem;
}
nav a {
  margin: 0 15px;
  text-decoration: none;
  color: #333;
  font-weight: bold;
}
main {
  max-width: 1200px;
  margin: 30px auto;
  padding: 0 20px;
}
.flash-messages {
  margin-bottom: 20px;
}
.flash {
  padding: 10px;
  margin: 5px 0;
  border-radius: 4px;
}
.flash.success { background-color: #d4edda; color: #155724; }
.flash.danger { background-color: #f8d7da; color: #721c24; }
table {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 30px;
}
table th, table td {
  border: 1px solid #e0e0e0;
  padding: 10px;
  text-align: left;
}
table th {
  background-color: #f5f5f5;
  font-weight: bold;
}
.form-group {
  margin-bottom: 15px;
}
.form-group input,
.form-group textarea {
  width: 100%;
  padding: 8px;
  border: 1px solid #cccccc;
  border-radius: 4px;
}
button {
  padding: 8px 16px;
  border: none;
  background-color: #333;
  color: #fff;
  cursor: pointer;
  border-radius: 4px;
}
button:hover {
  background-color: #555;
}
footer {
  background-color: #f8f8f8;
  text-align: center;
  padding: 15px;
  border-top: 1px solid #e0e0e0;
}
```

---

## 7. db_setup.py (Opcional)

Se preferir isolar a criação do banco de dados:
```python
from app import app, db
with app.app_context():
    db.create_all()
    print("Banco de dados iniciado.")
```

---

## Considerações Finais de UI/UX e Funcionalidade

- A interface utiliza uma tipografia limpa e espaçamentos generosos para promover um design moderno.  
- As tabelas e formulários são responsivos com mensagens de feedback via flash e confirmação de ações críticas.  
- Cada rota e formulário inclui tratamento de exceções para garantir confiabilidade e segurança.  
- O layout base e o CSS garantem uma aparência alinhada à estética Tesla sem o uso de imagens externas ou ícones.

---

## Resumo

- Criamos uma aplicação Flask com integração a SQLite e Flask-WTF para validação dos formulários.  
- Modelos e formulários foram definidos para os campos de estoque conforme especificado.  
- Templates HTML utilizam um layout base moderno e minimalista, inspirando-se na Tesla.  
- Arquivos CSS fornecem um design limpo com tipografia, cores e espaçamentos apropriados.  
- Tratamentos de erro e mensagens flash garantem uma boa experiência do usuário.  
- A estrutura modular facilita futuras alterações e expansões do sistema.

