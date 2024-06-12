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
      path: '/pending',
      name: 'pending',
      component: () => import('../views/pendingCustomersPage.vue')
    },
    {
      path: '/delivered',
      name: 'delivered',
      component: () => import('../views/deliveredCustomersPage.vue')
    },
    {
      path: '/optionPage',
      name: 'optionPage',
      component: () => import('../views/optionPage.vue')
    },
    {
      path: '/client/:id',
      name: 'customerDetails',
      component: () => import('../views/customerDetails.vue')
    },
    // {
    //   path: '/optionPage',
    //   name: 'optionPage',
    //   component: () => import('../views/optionPage.vue')
    // },
  ]
})

export default router
