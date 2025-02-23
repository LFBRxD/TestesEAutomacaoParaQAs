<script setup lang="ts">
import { ref, onMounted } from "vue";
import axios from "axios";

interface Transaction {
  id: number;
  product_id: number;
  user_id: number;
  quantity: number;
  total: number;
  status: string;
}

interface Product {
  id: number;
  name: string;
}

interface User {
  id: number;
  name: string;
}

const transactions = ref<Transaction[]>([]);
const users = ref<Record<number, string>>({});
const products = ref<Record<number, string>>({});
const isLoading = ref(true);
const errorMessage = ref("");

const fetchUsers = async () => {
  try {
    const response = await axios.get<User[]>("http://localhost:8080/users");
    users.value = response.data.reduce((acc, user) => {
      acc[user.id] = user.name;
      return acc;
    }, {} as Record<number, string>);
  } catch (error) {
    console.error("Erro ao buscar usuários:", error);
    errorMessage.value = "Erro ao carregar usuários";
  }
};

const fetchProducts = async () => {
  try {
    const response = await axios.get<Product[]>("http://localhost:8080/products");
    products.value = response.data.reduce((acc, product) => {
      acc[product.id] = product.name;
      return acc;
    }, {} as Record<number, string>);
  } catch (error) {
    console.error("Erro ao buscar produtos:", error);
    errorMessage.value = "Erro ao carregar produtos";
  }
};

const fetchTransactions = async () => {
  try {
    const response = await axios.get<Transaction[]>("http://localhost:8080/transactions");
    transactions.value = response.data;
  } catch (error) {
    console.error("Erro ao buscar transações:", error);
    errorMessage.value = "Erro ao carregar transações";
  } finally {
    isLoading.value = false;
  }
};

onMounted(async () => {
  await Promise.all([fetchUsers(), fetchProducts(), fetchTransactions()]);
});
</script>

<template>
  <div class="container mt-4">
    <h1 class="text-center mb-4">📜 Lista de Transações</h1>

    <div v-if="isLoading" class="text-center">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Carregando...</span>
      </div>
    </div>

    <div v-else>
      <div v-if="errorMessage" class="alert alert-danger">
        {{ errorMessage }}
      </div>

      <table class="table table-striped table-bordered">
        <thead class="table-dark">
          <tr>
            <th>ID</th>
            <th>Usuário</th>
            <th>Produto</th>
            <th>Quantidade</th>
            <th>Valor Total</th>
            <th>Status</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="transaction in transactions" :key="transaction.id">
            <td>{{ transaction.id }}</td>
            <td>{{ users[transaction.user_id] || "Desconhecido" }}</td>
            <td>{{ products[transaction.product_id] || "Desconhecido" }}</td>
            <td>{{ transaction.quantity }}</td>
            <td>R$ {{ transaction.total.toFixed(2) }}</td>
            <td>
              <span
                class="badge"
                :class="{
                  'bg-success': transaction.status === 'completed',
                  'bg-warning': transaction.status === 'pending',
                  'bg-danger': transaction.status === 'failed'
                }"
              >
                {{ transaction.status }}
              </span>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

