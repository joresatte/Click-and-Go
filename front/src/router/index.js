import { createRouter, createWebHistory } from 'vue-router'
const home = () => import('@/views/HomeView.vue')
const about = () => import('@/views/AboutView.vue')
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: home
    },
    {
      path: '/about',
      name: 'about',
      component: about
    }
  ]
})

export default router
