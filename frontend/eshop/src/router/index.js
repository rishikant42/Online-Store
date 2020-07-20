import Vue from "vue";
import VueRouter from "vue-router";
import Products from "../views/Products.vue";
import Home from "../views/Products.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    redirect: "/products",
    component: Home
  },
  {
    path: "/products",
    name: "Products",
    component: Products
  }
];

const router = new VueRouter({
  routes
});

export default router;
