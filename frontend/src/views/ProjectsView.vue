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

  <div class="container" style="padding-top: 40px;">
    
    <!-- Только поиск, никаких форм добавления -->
    <div class="search-input-group">
      <input v-model="searchQuery" type="text" placeholder="Поиск по названию проекта...">
    </div>

    <div class="projects-grid">
      <div v-for="p in filteredProjects" :key="p.id" class="project-card">
        <div class="project-image">
           <img v-if="p.image" :src="p.image" :alt="p.name">
           <div v-else style="background:#1E1E1E; height:100%; display:flex; align-items:center; justify-content:center; color:#C5A059;">YALI</div>
        </div>
        <div class="project-content">
          <h3>{{ p.name }}</h3>
          <p><strong>Заказчик:</strong> {{ p.customer_details?.company_name }}</p>
          <p><strong>Бюджет:</strong> {{ p.formatted_budget }}</p>
          <p><strong>Срок:</strong> {{ p.formatted_construction_period }}</p>
          
          <div style="margin-top: auto; padding-top: 20px;">
            <!-- Ссылка на подробную страницу -->
            <RouterLink :to="`/projects/${p.id}`" class="btn" style="width: 100%; text-align: center;">Подробнее о проекте</RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>