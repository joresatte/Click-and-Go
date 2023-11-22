import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home page',
      name: 'home page',
      component: () => import('../views/homePage.vue')
    }
  ]
})

export default router
