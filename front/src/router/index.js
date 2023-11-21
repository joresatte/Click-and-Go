import { createRouter, createWebHistory } from 'vue-router'
const home = () => import('@/views/HomePage.vue')
const customerDetailsPage = () => import('@/views/customerDetailsPage.vue')
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: home
    },
    {
      path: '/client/:id',
      name: 'customerDetails',
      component: customerDetailsPage
    }
  ]
})

export default router
