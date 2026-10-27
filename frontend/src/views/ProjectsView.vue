<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const projects = ref([])
const searchQuery = ref('')

const fetchData = async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/projects/')
    projects.value = res.data
  } catch (error) { 
    console.error("Ошибка API", error) 
  }
}
onMounted(() => fetchData())

const filteredProjects = computed(() => {
  if (!searchQuery.value) return projects.value
  const q = searchQuery.value.toLowerCase()
  return projects.value.filter(p => p.name.toLowerCase().includes(q))
})
</script>

<template>
  <div class="page-hero">
    <div class="container">
      <h1>Наши проекты</h1>
    </div>
  </div>

  <div class="container" style="padding-top: 40px; padding-bottom: 80px;">
    
    <div class="search-input-group">
      <input v-model="searchQuery" type="text" placeholder="Поиск по названию проекта...">
    </div>

    <div class="projects-grid">
      <div v-for="p in filteredProjects" :key="p.id" class="project-card">
        <!-- Картинка проекта -->
        <div class="project-image">
           <img v-if="p.image" :src="p.image" :alt="p.name">
           <div v-else class="placeholder">YALI</div>
        </div>
        
        <div class="project-content">
          <h3>{{ p.name }}</h3>
          <p><strong>ЗАКАЗЧИК:</strong> {{ p.customer_details?.company_name }}</p>
          <p><strong>БЮДЖЕТ:</strong> {{ p.formatted_budget }}</p>
          <p><strong>СРОК:</strong> {{ p.formatted_construction_period }}</p>
          
          <div style="margin-top: auto; padding-top: 25px;">
            <RouterLink :to="`/projects/${p.id}`" class="btn" style="width: 100%; text-align: center; display: block;">Подробнее о проекте</RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.project-image {
  height: 300px;
  overflow: hidden;
  background: #111;
  position: relative;
}

.project-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.8s ease;
}

.project-card:hover .project-image img {
  transform: scale(1.08); /* Зум при наведении */
}

.placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gold);
  font-family: var(--font-heading);
  font-size: 2rem;
  letter-spacing: 5px;
}
</style>