import Vue from 'vue'
import Router from 'vue-router'
import Ebook from '@/Ebook'
import Home from '@/components/Home'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/ebook'
    },
    {
      path: '/ebook',
      component: Ebook
    },
    {
      path: '/home',
      component: Home
    }
  ]
})
