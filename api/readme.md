# 📌 API  - Documentação e Configuração

Bem-vindo ao projeto ! Esta API foi desenvolvida utilizando **Flask**, **SQLAlchemy** e **Flasgger** para documentação via **Swagger UI**.

## 🛠 Requisitos
Antes de rodar o projeto, certifique-se de ter os seguintes requisitos instalados:

- **Python 3.x** (recomendado 3.8+)
- **pip** (gerenciador de pacotes do Python)
- **virtualenv** (opcional, mas recomendado)

## 🚀 Como Rodar a API

### 1️⃣ Criar e ativar um ambiente virtual (opcional, mas recomendado)
```sh
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### 2️⃣ trabalhando com as dependências
#### removendo todas as existentes:
```sh
pip freeze > packages.txt
pip uninstall -y -r packages.txt
del packages.txt
```

```sh
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

### 3️⃣ Criar o arquivo `.env` com as configurações do projeto
Crie um arquivo **.env** na raiz do projeto e adicione:

```ini
FLASK_APP=main.py
FLASK_DEBUG=True
FLASK_RUN_PORT=8080
FLASK_RUN_HOST=

SECRET_KEY=<sua secretkey>
SQLALCHEMY_DATABASE_URI=sqlite:///debug_database.db
SQLALCHEMY_TRACK_MODIFICATIONS=False
```

### 4️⃣ Rodar a API
```sh
flask run --host=0.0.0.0 --port=8080
```
### 4️⃣ Rodar a API [em caso de erro]
```sh
python main.py
```

A API estará disponível em [`http://localhost:8080`](http://localhost:8080)

## 📖 Documentação da API com Swagger

A documentação interativa está disponível em:
📌 **Swagger UI:** [`http://localhost:8080/apidocs`](http://localhost:8080/apidocs)

Com o Swagger, você pode testar os endpoints diretamente pelo navegador, sem precisar de ferramentas externas como Postman ou cURL.

## 📂 Estrutura do Projeto
```
/api
├── app/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── repositories/
│   ├── services/
│   ├── db.py
│   ├── __init__.py
├── main.py
├── requirements.txt
├── .env (deve ser criado pelo usuário)
├── README.md
```

## 🛠 Tecnologias Utilizadas
- **Flask** - Framework para desenvolvimento web
- **Flask-SQLAlchemy** - ORM para manipulação do banco de dados
- **Flask-Migrate** - Controle de migração do banco
- **Flasgger** - Geração automática da documentação via Swagger
- **SQLite** - Banco de dados padrão (pode ser alterado para PostgreSQL, MySQL, etc.)

## 🛠 Comandos Úteis

### 📌 Criar tabelas no banco de dados
```sh
flask db init
flask db migrate -m "Inicializando banco de dados"
flask db upgrade
```
### 📌 [em caso de erro] Criar tabelas no banco de dados
```sh
python -m flask db init
python -m flask db migrate -m "Inicializando banco de dados"
python -m flask db upgrade
```

### 📌 Rodar a API em modo debug
```sh
python -m flask run --debug
```

## ✨ Contribuição
Sinta-se à vontade para contribuir! Envie um **pull request** com melhorias, correções ou novas funcionalidades.

## ⚡ Licença
Este projeto é de código aberto e está sob a licença **MIT**.

---

Feito por [Flavio Ramos] 

