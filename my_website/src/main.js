import { createApp } from 'vue'
import App from './App.vue'
import { createWebHistory, createRouter } from 'vue-router'

import HomePage from './components/HomePage.vue'
import BlogPage from './components/BlogPage.vue'
import ProjectsPage from './components/ProjectsPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/blog', component: BlogPage },
  { path: '/projects', component: ProjectsPage}
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
