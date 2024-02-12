import { createRouter, createWebHistory } from 'vue-router'
import ListView from '../views/ListView.vue'
import AddView from '../views/AddView.vue'
import TransactionLogView from '../views/TransactionLogView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/list',
      name: 'list',
      component: ListView
    },
    {
      path: '/add',
      name: 'add',
      component: AddView
    },
    {
      path: '/transactions',
      name: 'transactions',
      component: TransactionLogView
    },

  ]
})

export default router
