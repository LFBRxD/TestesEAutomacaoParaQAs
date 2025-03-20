<script setup>
import { RouterView, RouterLink } from "vue-router";
</script>

<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-dark">
      <div class="container">
        <RouterLink class="navbar-brand" to="/">🚀 Meu Sistema</RouterLink>

        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>

        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav ms-auto">
            <li class="nav-item">
              <RouterLink class="nav-link" to="/">🏠 Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/users">👤 Usuários</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/products">📦 Produtos</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/transactions">💰 Transações</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>
  </header>

  <main class="container mt-4">
    <RouterView />
  </main>
</template>
