import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProjectsView from '../views/ProjectsView.vue'
import ProjectDetailView from '../views/ProjectDetailView.vue'
import MaterialsView from '../views/MaterialsView.vue'
import TeamView from '../views/TeamView.vue'
import ContactsView from '../views/ContactsView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', name: 'home', component: HomeView },
    { path: '/projects', name: 'projects', component: ProjectsView },
    { path: '/projects/:id', name: 'project-detail', component: ProjectDetailView },
    { path: '/materials', name: 'materials', component: MaterialsView },
    { path: '/team', name: 'team', component: TeamView },
    { path: '/contacts', name: 'contacts', component: ContactsView }
  ]
})

export default router