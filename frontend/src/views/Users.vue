<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import { Modal } from "bootstrap";

interface User {
  id: number;
  name: string;
  email: string;
  document: string;
}

const users = ref<User[]>([]);
const isLoading = ref(true);
const errorMessage = ref("");
const successMessage = ref("");

// Controle dos modais
const modalNewUser = ref<InstanceType<typeof Modal> | null>(null);
const modalEditUser = ref<InstanceType<typeof Modal> | null>(null);
const modalDeleteUser = ref<InstanceType<typeof Modal> | null>(null);

// Estados para criação, edição e exclusão
const newUser = ref<User>({ id: 0, name: "", email: "", document: "" });
const selectedUser = ref<User | null>(null);

const fetchUsers = async () => {
  try {
    const response = await axios.get<User[]>("http://localhost:8080/users");
    users.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar usuários:", error);
    errorMessage.value = "Erro ao carregar usuários.";
  } finally {
    isLoading.value = false;
  }
};

// Abrir modal de cadastro
const openNewUserModal = () => {
  newUser.value = { id: 0, name: "", email: "", document: "" };
  modalNewUser.value?.show();
};

// Cadastrar usuário
const createUser = async () => {
  try {
    const response = await axios.post<User>("http://localhost:8080/user", newUser.value);
    users.value.push(response.data);
    successMessage.value = "Usuário cadastrado com sucesso!";
    setTimeout(() => (successMessage.value = ""), 3000);
    modalNewUser.value?.hide();
  } catch (error) {
    console.error("Erro ao cadastrar usuário:", error);
    errorMessage.value = "Erro ao cadastrar usuário.";
  }
};

// Abrir modal de edição
const openEditUserModal = (user: User) => {
  selectedUser.value = { ...user };
  modalEditUser.value?.show();
};

// Salvar edição
const saveEditUser = async () => {
  if (!selectedUser.value) return;

  try {
    await axios.put(`http://localhost:8080/users/${selectedUser.value.id}`, selectedUser.value);
    
    // Atualiza a UI sem precisar recarregar
    const index = users.value.findIndex(u => u.id === selectedUser.value!.id);
    if (index !== -1) users.value[index] = { ...selectedUser.value };

    successMessage.value = `Usuário ${selectedUser.value.id} atualizado com sucesso!`;
    setTimeout(() => (successMessage.value = ""), 3000);
    modalEditUser.value?.hide();
  } catch (error) {
    console.error("Erro ao editar usuário:", error);
    errorMessage.value = "Erro ao editar usuário.";
  }
};

// Abrir modal de exclusão
const openDeleteUserModal = (user: User) => {
  selectedUser.value = user;
  modalDeleteUser.value?.show();
};

// Excluir usuário
const deleteUser = async () => {
  if (!selectedUser.value) return;

  try {
    await axios.delete(`http://localhost:8080/users/${selectedUser.value.id}`);
    
    // Remove da lista
    users.value = users.value.filter(u => u.id !== selectedUser.value!.id);

    successMessage.value = `Usuário ${selectedUser.value.name} excluído com sucesso!`;
    setTimeout(() => (successMessage.value = ""), 3000);
    modalDeleteUser.value?.hide();
  } catch (error) {
    console.error("Erro ao excluir usuário:", error);
    errorMessage.value = "Erro ao excluir usuário.";
  }
};

onMounted(async () => {
  await fetchUsers();

  setTimeout(() => {
    const newUserModalEl = document.getElementById("newUserModal");
    const editUserModalEl = document.getElementById("editUserModal");
    const deleteUserModalEl = document.getElementById("deleteUserModal");

    if (newUserModalEl) modalNewUser.value = new Modal(newUserModalEl);
    if (editUserModalEl) modalEditUser.value = new Modal(editUserModalEl);
    if (deleteUserModalEl) modalDeleteUser.value = new Modal(deleteUserModalEl);
  }, 100);
});

</script>

<template>
  <div class="container mt-4">
    <h1 class="text-center mb-4">👤 Lista de Usuários</h1>

    <!-- Mensagem de Sucesso -->
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <!-- Mensagem de Erro -->
    <div v-if="errorMessage" class="alert alert-danger">
      {{ errorMessage }}
    </div>

    <div class="d-flex justify-content-end mb-3">
      <button class="btn btn-success" @click="openNewUserModal">➕ Adicionar Usuário</button>
    </div>

    <!-- Loading -->
    <div v-if="isLoading" class="text-center">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Carregando...</span>
      </div>
    </div>

    <div v-else>
      <table class="table table-striped table-bordered">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Nome</th>
            <th>Email</th>
            <th>Documento</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users" :key="user.id">
            <td>{{ user.id }}</td>
            <td>{{ user.name }}</td>
            <td>{{ user.email }}</td>
            <td>{{ user.document }}</td>
            <td>
              <button class="btn btn-primary btn-sm me-2" @click="openEditUserModal(user)">✏️ Editar</button>
              <button class="btn btn-danger btn-sm" @click="openDeleteUserModal(user)">🗑️ Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- Modal de Cadastro -->
    <div class="modal fade" id="newUserModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">➕ Cadastrar Usuário</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <label class="form-label">Nome</label>
            <input v-model="newUser.name" type="text" class="form-control">

            <label class="form-label mt-2">Email</label>
            <input v-model="newUser.email" type="email" class="form-control">

            <label class="form-label mt-2">Documento</label>
            <input v-model="newUser.document" type="text" class="form-control">
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-success" @click="createUser">Salvar</button>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal de Edição -->
  <div class="modal fade" id="editUserModal" tabindex="-1">
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">✏️ Editar Usuário</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
          <label class="form-label">Nome</label>
          <input v-model="selectedUser!.name" type="text" class="form-control" v-if="selectedUser">

          <label class="form-label mt-2">Email</label>
          <input v-model="selectedUser!.email" type="email" class="form-control" v-if="selectedUser">

          <label class="form-label mt-2">Documento</label>
          <input v-model="selectedUser!.document" type="text" class="form-control" v-if="selectedUser">
        </div>
        <div class="modal-footer">
          <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
          <button type="button" class="btn btn-success" @click="saveEditUser">Salvar</button>
        </div>
      </div>
    </div>
  </div>

    <!-- Modal de Exclusão -->
    <div class="modal fade" id="deleteUserModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">🗑️ Excluir Usuário</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <p>Tem certeza que deseja excluir o usuário <strong>{{ selectedUser?.name }}</strong>?</p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="deleteUser">Excluir</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
