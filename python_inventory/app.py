from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Equipment
from forms import EquipmentForm
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'tesla_inspired_inventory_management_2024'

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    search = request.args.get('search', '')
    if search:
        equipments = Equipment.query.filter(
            Equipment.objeto.contains(search) |
            Equipment.categoria.contains(search) |
            Equipment.setor_alocado.contains(search) |
            Equipment.responsavel_operador.contains(search)
        ).all()
    else:
        equipments = Equipment.query.all()
    
    return render_template('index.html', equipments=equipments, search=search)

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
            flash(f'Erro ao adicionar equipamento: {str(e)}', 'danger')
    
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
            flash(f'Erro ao atualizar equipamento: {str(e)}', 'danger')
    
    return render_template('edit_equipment.html', form=form, equipment=equip)

@app.route('/delete/<int:id>', methods=['POST'])
def delete_equipment(id):
    equip = Equipment.query.get_or_404(id)
    try:
        db.session.delete(equip)
        db.session.commit()
        flash('Equipamento removido com sucesso!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Erro ao remover equipamento: {str(e)}', 'danger')
    
    return redirect(url_for('index'))

@app.route('/view/<int:id>')
def view_equipment(id):
    equip = Equipment.query.get_or_404(id)
    return render_template('view_equipment.html', equipment=equip)

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
