import { createRouter, createWebHistory } from 'vue-router';
import Login from '../views/Login.vue';
import Register from '../views/Register.vue';
import Home from '../views/Home.vue';
import self from '../views/self.vue';
const routes = [
  {
    path: '/',
    redirect: '/login' // 默认重定向到登录页面
  },
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/register',
    name: 'Register',
    component: Register
  },
  {
    path: '/home',
    name: 'Home',
    component: Home
  },
  {
    path: '/self',
    name: 'self',
    component: self
  },
  {
    path: '/book/:id',
    name: 'book',
    component: () => import('../views/BookView.vue')
  },
  {
    path: '/author/:id',
    name: 'author',
    component: () => import('../views/AuthorView.vue')
  },
  {
    path: '/libraryown',
    name: 'libraryuser',
    component: () => import('../views/LibraryView.vue')
  },
  {
    path: '/library',
    name: 'library',
    component: () => import('../views/LibraryView.vue')
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;

