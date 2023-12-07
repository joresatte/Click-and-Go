import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/loginPage',
      name: 'loginPage',
      component: () => import('../views/loginPage.vue')
    },
    {
      path: '/customersPage',
      name: 'customersPage',
      component: () => import('../views/customersPage.vue')
    },
    {
      path: '/client/:id',
      name: 'customerDetails',
      component: () => import('../views/customerDetails.vue')
    },
  ]
})

export default router
