# Sistema de Gestão de Estoque

Um sistema web moderno para gerenciamento de equipamentos internos da empresa, desenvolvido em Python com Flask e inspirado no design minimalista da Tesla.

## 🚀 Características

- **Interface moderna e limpa** inspirada no design da Tesla
- **Gestão completa de equipamentos** com todos os campos necessários
- **Busca e filtros** para localizar equipamentos rapidamente
- **Responsivo** - funciona perfeitamente em desktop e mobile
- **Validação de dados** com feedback em tempo real
- **Base de dados SQLite** - sem necessidade de configuração externa

## 📋 Campos de Equipamento

O sistema gerencia os seguintes dados para cada equipamento:

- **Nº DO BEM** - Identificador único do equipamento
- **CATEGORIA** - Tipo de equipamento (Informática, Móveis, etc.)
- **OBJETO** - Descrição do equipamento
- **MODELO** - Modelo específico do equipamento
- **DATA AQUISIÇÃO** - Data de compra/aquisição
- **NOTA FISCAL** - Número da nota fiscal
- **VALOR** - Valor de aquisição em reais
- **ESTADO DE CONSERVAÇÃO** - Condição atual (Novo, Bom, Regular, Ruim, Péssimo)
- **SETOR ALOCADO** - Departamento responsável
- **RESPONSÁVEL / OPERADOR** - Pessoa responsável pelo equipamento
- **DATA ENTREGA** - Data de entrega (opcional)
- **MANUTENÇÃO DADA** - Tipo de manutenção realizada (opcional)
- **SERVIÇO REALIZADO** - Descrição detalhada dos serviços (opcional)

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+**
- **Flask** - Framework web
- **Flask-SQLAlchemy** - ORM para banco de dados
- **Flask-WTF** - Formulários e validação
- **SQLite** - Banco de dados
- **HTML5 + CSS3** - Interface responsiva
- **Google Fonts** - Tipografia moderna

## 📦 Instalação

### Pré-requisitos

- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Passos de Instalação

1. **Clone ou baixe o projeto**
   ```bash
   cd python_inventory
   ```

2. **Instale as dependências**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute a aplicação**
   ```bash
   python app.py
   ```

4. **Acesse o sistema**
   - Abra seu navegador
   - Vá para: `http://localhost:8000`

## 🎯 Como Usar

### Adicionar Equipamento
1. Clique em "Adicionar" na barra de navegação
2. Preencha os campos obrigatórios (marcados com *)
3. Clique em "Salvar Equipamento"

### Visualizar Equipamentos
- A página inicial mostra todos os equipamentos em uma tabela
- Use a barra de busca para filtrar por objeto, categoria, setor ou responsável

### Editar Equipamento
1. Na lista de equipamentos, clique em "Editar"
2. Modifique os campos necessários
3. Clique em "Salvar Equipamento"

### Ver Detalhes
- Clique em "Ver" para visualizar todos os detalhes de um equipamento
- Nesta página você também pode editar ou excluir o equipamento

### Excluir Equipamento
- Clique em "Excluir" na lista ou na página de detalhes
- Confirme a exclusão (ação irreversível)

## 🎨 Design

O sistema foi desenvolvido com uma estética inspirada no site da Tesla:

- **Tipografia limpa** com fonte Inter
- **Cores neutras** (preto, branco, cinzas)
- **Espaçamentos generosos** para melhor legibilidade
- **Animações suaves** nas interações
- **Layout responsivo** para todos os dispositivos
- **Sem ícones ou imagens externas** - foco na funcionalidade

## 📱 Responsividade

O sistema é totalmente responsivo e se adapta a:
- **Desktop** (1200px+)
- **Tablet** (768px - 1199px)
- **Mobile** (até 767px)

## 🔧 Estrutura do Projeto

```
python_inventory/
├── app.py                 # Aplicação principal Flask
├── models.py              # Modelos de dados (SQLAlchemy)
├── forms.py               # Formulários (Flask-WTF)
├── requirements.txt       # Dependências Python
├── static/
│   └── css/
│       └── style.css      # Estilos CSS
├── templates/
│   ├── layout.html        # Template base
│   ├── index.html         # Lista de equipamentos
│   ├── add_equipment.html # Adicionar equipamento
│   ├── edit_equipment.html# Editar equipamento
│   ├── view_equipment.html# Visualizar equipamento
│   ├── 404.html          # Página não encontrada
│   └── 500.html          # Erro interno
└── inventory.db          # Banco de dados SQLite (criado automaticamente)
```

## 🚨 Tratamento de Erros

O sistema inclui tratamento robusto de erros:
- **Validação de formulários** com mensagens claras
- **Páginas de erro personalizadas** (404, 500)
- **Mensagens flash** para feedback do usuário
- **Confirmação de exclusão** para prevenir perdas acidentais

## 🔒 Segurança

- **Validação server-side** de todos os dados
- **Proteção CSRF** nos formulários
- **Sanitização de entrada** para prevenir injeções
- **Tratamento seguro de exceções**

## 📈 Funcionalidades Futuras

Possíveis melhorias para versões futuras:
- Relatórios em PDF/Excel
- Sistema de usuários e permissões
- Histórico de alterações
- Notificações de manutenção
- API REST para integração
- Backup automático
- Dashboard com gráficos

## 🐛 Solução de Problemas

### Erro ao instalar dependências
```bash
# Atualize o pip
pip install --upgrade pip

# Instale novamente
pip install -r requirements.txt
```

### Porta 8000 já em uso
```bash
# No app.py, altere a porta:
app.run(debug=True, port=8001)
```

### Banco de dados corrompido
```bash
# Delete o arquivo inventory.db
# Execute novamente: python app.py
```

## 📞 Suporte

Para dúvidas ou problemas:
1. Verifique se todas as dependências estão instaladas
2. Confirme que está usando Python 3.8+
3. Verifique se a porta 8000 está disponível

## 📄 Licença

Este projeto foi desenvolvido para uso interno da empresa.

---

**Desenvolvido com ❤️ usando Python e Flask**
