<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const customers = ref([])
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/customers/')
    customers.value = res.data
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="page-hero">
    <div class="container">
      <h1>Наши партнеры</h1>
      <p style="color: var(--gold); margin-top: 15px; letter-spacing: 2px;">КОМПАНИИ, КОТОРЫЕ НАМ ДОВЕРЯЮТ</p>
    </div>
  </div>
  
  <div class="container" style="padding: 60px 20px;">
    <div class="projects-grid">
      <div v-for="c in customers" :key="c.id" class="project-card" style="padding: 40px; text-align: center;">
        <div style="font-size: 3rem; color: var(--gold); margin-bottom: 20px;">
          <i class="fas fa-building"></i>
        </div>
        <h3 style="font-size: 1.5rem; margin-bottom: 15px; color: var(--dark);">{{ c.company_name }}</h3>
        <p style="color: var(--text-muted); margin-bottom: 10px;"><strong>Контактное лицо:</strong> {{ c.contact_person }}</p>
        <p style="color: var(--text-muted);"><strong>Email:</strong> {{ c.email }}</p>
      </div>
    </div>
  </div>
</template>