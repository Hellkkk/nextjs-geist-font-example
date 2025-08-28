from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, DateField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, NumberRange

class EquipmentForm(FlaskForm):
    num_bem = StringField('Nº DO BEM', validators=[DataRequired()], render_kw={"placeholder": "Ex: BEM001"})
    categoria = SelectField('CATEGORIA', validators=[DataRequired()], choices=[
        ('', 'Selecione uma categoria'),
        ('Informática', 'Informática'),
        ('Móveis', 'Móveis'),
        ('Equipamentos', 'Equipamentos'),
        ('Veículos', 'Veículos'),
        ('Ferramentas', 'Ferramentas'),
        ('Outros', 'Outros')
    ])
    objeto = StringField('OBJETO', validators=[DataRequired()], render_kw={"placeholder": "Ex: Notebook Dell"})
    modelo = StringField('MODELO', validators=[DataRequired()], render_kw={"placeholder": "Ex: Inspiron 15"})
    data_aquisicao = DateField('DATA AQUISIÇÃO', validators=[DataRequired()])
    nota_fiscal = StringField('NOTA FISCAL', validators=[DataRequired()], render_kw={"placeholder": "Ex: NF123456"})
    valor = FloatField('VALOR (R$)', validators=[DataRequired(), NumberRange(min=0)], render_kw={"placeholder": "Ex: 2500.00"})
    estado_conservacao = SelectField('ESTADO DE CONSERVAÇÃO', validators=[DataRequired()], choices=[
        ('', 'Selecione o estado'),
        ('Novo', 'Novo'),
        ('Bom', 'Bom'),
        ('Regular', 'Regular'),
        ('Ruim', 'Ruim'),
        ('Péssimo', 'Péssimo')
    ])
    setor_alocado = StringField('SETOR ALOCADO', validators=[DataRequired()], render_kw={"placeholder": "Ex: TI, RH, Financeiro"})
    responsavel_operador = StringField('RESPONSÁVEL / OPERADOR', validators=[DataRequired()], render_kw={"placeholder": "Nome do responsável"})
    data_entrega = DateField('DATA ENTREGA')
    manutencao_dada = StringField('MANUTENÇÃO DADA', render_kw={"placeholder": "Ex: Preventiva, Corretiva"})
    servico_realizado = TextAreaField('SERVIÇO REALIZADO', render_kw={"placeholder": "Descreva os serviços realizados...", "rows": 3})
    submit = SubmitField('Salvar Equipamento')
