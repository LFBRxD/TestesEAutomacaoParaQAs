import { createRouter, createWebHistory } from "vue-router";
import Home from "@/views/Hom.vue";
import Users from "@/views/Users.vue";
import Products from "@/views/Products.vue";
import Transactions from "@/views/Transactions.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/users", component: Users },
  { path: "/products", component: Products },
  { path: "/transactions", component: Transactions }
];

const routermanager = createRouter({
  history: createWebHistory(),
  routes
});

export default routermanager;
