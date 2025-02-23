# 📦 Vue 3 + TypeScript + Bootstrap - Frontend para CRUD de Usuários

Este projeto é um frontend desenvolvido em **Vue 3** com **TypeScript** e estilizado com **Bootstrap 5**. Ele permite **cadastrar, editar e excluir usuários, produtos e transações** consumindo uma API REST, tudo para simular um ambiente produtivo.

---

## 🚀 **Setup do Projeto**

### **1️⃣ Clonar o repositório**
```sh
git clone https://github.com/LFBRxD/TestesEAutomacaoParaQAs.git
cd frontend
```

### **2️⃣ Instalar dependências**
```sh
npm install
```

### **3️⃣ Rodar o projeto**
```sh
npm run dev
```
Após rodar o comando, o frontend estará disponível em:
```
http://localhost:5173/
```

Se precisar acessar de outro dispositivo na mesma rede:
```sh
npm run dev -- --host
```

---

## 🛠 **Tecnologias Utilizadas**

- [Vue 3](https://vuejs.org/) (Composition API + Script Setup)
- [TypeScript](https://www.typescriptlang.org/)
- [Bootstrap 5](https://getbootstrap.com/)
- [Vue Router](https://router.vuejs.org/) (Gerenciamento de rotas)
- [Axios](https://axios-http.com/) (Requisições HTTP para o backend)

---

## 🔗 **Conectando com o Backend Flask**
Se você já tem o backend rodando em Flask, **certifique-se de que ele está acessível na URL**:
```
http://localhost:8080/
```

Se precisar rodar o backend Flask:
```sh
cd ../backend
python app.py  # Ou flask run
```

Agora, o frontend estará conectado e pronto para consumir a API REST!

---

## 📜 **Funcionalidades**
✅ **Listagem de Usuários**
- Exibe uma tabela com todos os usuários cadastrados.

✅ **Cadastro de Novo Usuário**
- Formulário em modal para adicionar novos usuários.

✅ **Edição de Usuário**
- Modal de edição para alterar dados do usuário.

✅ **Exclusão de Usuário**
- Confirmação antes de excluir um usuário.

---

## 📄 **Estrutura do Projeto**
```
frontend/
├── src/
│   ├── components/       # Componentes reutilizáveis
│   ├── views/            # Telas do sistema (Users.vue, etc.)
│   ├── router.ts         # Configuração do Vue Router
│   ├── main.ts           # Arquivo principal do Vue
│   ├── App.vue           # Componente raiz
├── public/               # Arquivos estáticos
├── package.json          # Dependências do projeto
└── vite.config.ts        # Configuração do Vite
```

---

## 📌 **Rotas do Sistema**
```
/                  # Tela inicial
/users             # CRUD de Usuários
```

---

## 🎯 **Próximos Passos**
🔹 Melhorar UI/UX com componentes do Bootstrap 5
🔹 Implementar autenticação de usuário (Login/Logout)
🔹 Paginação na listagem de usuários

---

## 👨‍💻 **Desenvolvido por**
[Flavio Ramos](https://github.com/seu-usuario)

Se tiver dúvidas, abre uma **issue** ou manda um **pull request**! 🚀

