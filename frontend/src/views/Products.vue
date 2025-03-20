<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";
import { Modal } from "bootstrap";

interface Product {
  id: number;
  name: string;
  description: string;
  price: number;
  stock: number;
}

// State para armazenar os produtos
const products = ref<Product[]>([]);
const isLoading = ref(true);
const errorMessage = ref("");
const successMessage = ref("");

// Produto em edição
const selectedProduct = ref<Product>({ id: 0, name: "", description: "", price: 0, stock: 0 });
const modalEdit = ref<InstanceType<typeof Modal> | null>(null);
const modalDelete = ref<InstanceType<typeof Modal> | null>(null);

// Buscar produtos
const fetchProducts = async () => {
  try {
    const response = await axios.get<Product[]>("http://localhost:8080/products");
    products.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar produtos:", error);
    errorMessage.value = "Erro ao carregar produtos.";
  } finally {
    isLoading.value = false;
  }
};

const openEditModal = (product: Product) => {
  selectedProduct.value = { ...product }; // Clona os dados do produto
  modalEdit.value?.show();
};


// Salvar edição
const saveEdit = async () => {
  if (!selectedProduct.value) return;

  try {
    await axios.put(`http://localhost:8080/products/${selectedProduct.value.id}`, selectedProduct.value);
    
    // Atualiza a UI sem precisar recarregar
    const index = products.value.findIndex(p => p.id === selectedProduct.value!.id);
    if (index !== -1) products.value[index] = { ...selectedProduct.value };

    successMessage.value = `Produto ${selectedProduct.value.id} atualizado com sucesso!`;
    setTimeout(() => (successMessage.value = ""), 3000);
    modalEdit.value?.hide();
  } catch (error) {
    console.error("Erro ao editar produto:", error);
    errorMessage.value = "Erro ao editar produto.";
  }
};

// Abrir modal de exclusão
const openDeleteModal = (product: Product) => {
  selectedProduct.value = product || { id: 0, name: "", description: "", price: 0, stock: 0 };
  modalDelete.value?.show();
};


// Excluir produto
const deleteProduct = async () => {
  if (!selectedProduct.value) return;

  try {
    await axios.delete(`http://localhost:8080/products/${selectedProduct.value.id}`);
    
    // Remove da lista
    products.value = products.value.filter(p => p.id !== selectedProduct.value!.id);

    successMessage.value = `Produto ${selectedProduct.value.name} excluído com sucesso!`;
    setTimeout(() => (successMessage.value = ""), 3000);
    modalDelete.value?.hide();
  } catch (error) {
    console.error("Erro ao excluir produto:", error);
    errorMessage.value = "Erro ao excluir produto.";
  }
};

const getStockStatus = (stock: number) => {
  if (stock === 0) return { text: "Sem Estoque", class: "bg-danger" };
  if (stock < 10) return { text: "Baixo", class: "bg-warning" };
  if (stock < 50) return { text: "Médio", class: "bg-info" };
  return { text: "Alto", class: "bg-success" };
};


// Configurar os modais após a montagem
onMounted(async () => {
  await fetchProducts();

  modalEdit.value = new Modal(document.getElementById("editModal") as HTMLElement);
  modalDelete.value = new Modal(document.getElementById("deleteModal") as HTMLElement);
});
</script>

<template>
    <div class="container mt-4">
        <h1 class="text-center mb-4">📦 Lista de Produtos</h1>

    <!-- Mensagem de Sucesso -->
    <div v-if="successMessage" class="alert alert-success">
      {{ successMessage }}
    </div>

    <!-- Mensagem de Erro -->
    <div v-if="errorMessage" class="alert alert-danger">
      {{ errorMessage }}
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
            <th>Descrição</th>
            <th>Preço</th>
            <th>Estoque</th>
            <th>Status Estoque</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in products" :key="product.id">
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.description }}</td>
            <td>R$ {{ product.price.toFixed(2) }}</td>
            <td>{{ product.stock }}</td>
            <td>
              <span class="badge" :class="getStockStatus(product.stock).class">
                {{ getStockStatus(product.stock).text }}
              </span>
            </td>
            <td>
              <button class="btn btn-primary btn-sm me-2" @click="openEditModal(product)">✏️ Editar</button>
              <button class="btn btn-danger btn-sm" @click="openDeleteModal(product)">🗑️ Excluir</button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Modal de Edição -->
    <div class="modal fade" id="editModal" tabindex="-1">
    <div class="modal-dialog">
        <div class="modal-content">
        <div class="modal-header">
            <h5 class="modal-title">✏️ Editar Produto</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
        </div>
        <div class="modal-body">
            <label class="form-label">Nome</label>
            <input v-model="selectedProduct!.name" type="text" class="form-control" v-if="selectedProduct">

            <label class="form-label mt-2">Descrição</label>
            <input v-model="selectedProduct!.description" type="text" class="form-control" v-if="selectedProduct">

            <label class="form-label mt-2">Preço</label>
            <input v-model="selectedProduct!.price" type="number" class="form-control" v-if="selectedProduct">

            <label class="form-label mt-2">Estoque</label>
            <input v-model="selectedProduct!.stock" type="number" class="form-control" v-if="selectedProduct">
        </div>
        <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-success" @click="saveEdit">Salvar</button>
        </div>
        </div>
    </div>
    </div>


    <!-- Modal de Exclusão -->
    <div class="modal fade" id="deleteModal" tabindex="-1">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">🗑️ Excluir Produto</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
          </div>
          <div class="modal-body">
            <p v-if="selectedProduct">Tem certeza que deseja excluir o produto <strong>{{ selectedProduct.name }}</strong>?</p>
            <p v-if="selectedProduct"><i>{{ selectedProduct.description }}</i></p>
          </div>
          <div class="modal-footer">
            <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancelar</button>
            <button type="button" class="btn btn-danger" @click="deleteProduct">Excluir</button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>
