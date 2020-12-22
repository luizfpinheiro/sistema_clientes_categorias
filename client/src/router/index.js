import Vue from 'vue'
import VueRouter from 'vue-router'
import Clientes from '../views/Clientes.vue'
import Categorias from '../views/Categorias.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/clientes',
    name: 'Clientes',
    component: Clientes
  },
  {
    path: '/categorias',
    name: 'Categorias',
    component: Categorias,
  }
]

const router = new VueRouter({
  mode: 'history',
  routes: routes
})

export default router
