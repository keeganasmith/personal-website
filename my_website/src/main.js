import { createApp } from 'vue'
import App from './App.vue'
import { createWebHistory, createRouter } from 'vue-router'
import Notifications from '@kyvg/vue3-notification'
import { notify } from "@kyvg/vue3-notification";
import HomePage from './components/HomePage.vue'
import BlogPage from './components/BlogPage.vue'
import ProjectsPage from './components/ProjectsPage.vue'
import NewPostForm from './components/NewPostForm.vue'
import LoginPage from './components/LoginPage.vue'
import { check_admin } from './helper/permissions.js'
import './assets/tailwind.css';
const routes = [
  { path: '/', component: HomePage },
  { path: '/blog', component: BlogPage, meta: { requiresAuth: true } },
  { path: '/projects', component: ProjectsPage },
  { path: '/new_post', component: NewPostForm, meta: { requiresAdmin: true }},
  { path: '/login', component: LoginPage}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})
const isAuthenticated = () => {
  return sessionStorage.getItem("token")
};

// Navigation guard
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!isAuthenticated()) {
      notify({
        title: "Not Authorized",
        text: "Howdy, you need to be signed in to google to view my blog.",
      });
      next({ path: '/login' });
    } else {
      next();
    }
  } else if(to.matched.some(record => record.meta.requiresAdmin)) {
    if(!check_admin()){
      notify({
        title: "Not Authorized",
        text: "Howdy, this account is not authorized to create new posts.",
      })
      next({ path: '/login' })
    }
    else{
      next()
    }
  } else {
    next();
  }
});
createApp(App).use(router).use(Notifications).mount('#app')
