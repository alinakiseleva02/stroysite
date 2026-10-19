<script setup>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const project = ref(null)

onMounted(async () => {
  const res = await axios.get(`http://127.0.0.1:8000/api/projects/${route.params.id}/`)
  project.value = res.data
})
</script>

<template>
  <div class="page-hero" v-if="project">
    <div class="container">
      <h1>{{ project.name }}</h1>
    </div>
  </div>
  
  <div v-if="project" class="container" style="padding: 80px 20px;">
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 50px; align-items: start;">
      <div>
        <img v-if="project.image" :src="project.image" style="width: 100%; box-shadow: var(--shadow); border: 1px solid #EEE;">
      </div>
      <div>
        <h2 style="font-size: 2.5rem; margin-bottom: 20px;">О проекте</h2>
        <p style="font-size: 1.1rem; color: var(--text-muted); margin-bottom: 30px; line-height: 1.8;">{{ project.description }}</p>
        
        <div style="border-top: 1px solid #EEE; padding-top: 20px; margin-bottom: 30px;">
          <p style="margin-bottom: 10px;"><strong>Стоимость:</strong> {{ project.formatted_budget }}</p>
          <p style="margin-bottom: 10px;"><strong>Срок реализации:</strong> {{ project.formatted_construction_period }}</p>
          <p style="margin-bottom: 10px;"><strong>Заказчик:</strong> {{ project.customer_details.company_name }}</p>
          <p><strong>Архитектор:</strong> {{ project.employee_details.full_name }}</p>
        </div>

        <RouterLink to="/projects" class="btn">← Вернуться в каталог</RouterLink>
      </div>
    </div>
  </div>
</template>