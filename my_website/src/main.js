import { createApp } from 'vue'
import App from './App.vue'
import { createMemoryHistory, createRouter } from 'vue-router'

import HomePage from './components/HomePage.vue'
import BlogPage from './components/BlogPage.vue'
import ProjectsPage from './components/ProjectsPage.vue'

const routes = [
  { path: '/', component: HomePage },
  { path: '/blog', component: BlogPage },
  { path: '/projects', component: ProjectsPage}
]

const router = createRouter({
  history: createMemoryHistory(),
  routes,
})

createApp(App).use(router).mount('#app')
