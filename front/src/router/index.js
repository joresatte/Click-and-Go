import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/homePage.vue')
    },
    {
      path: `/client/:id`,
      name: 'customerDetails',
      props: true,
      component: () => import('../views/customerDetails.vue')
    }
  ]
})

export default router
