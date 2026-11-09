<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const employees = ref([])
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/employees/')
    employees.value = res.data
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="page-hero">
    <div class="container">
      <h1>Наша команда</h1>
      <p style="color: var(--gold); margin-top: 15px; letter-spacing: 2px;">РУКОВОДСТВО И СПЕЦИАЛИСТЫ</p>
    </div>
  </div>
  
  <div class="container" style="padding: 60px 20px;">
    <div class="projects-grid">
      <div v-for="emp in employees" :key="emp.id" class="project-card" style="padding: 40px; text-align: center;">
        <div style="width: 100px; height: 100px; border: 2px solid var(--gold); border-radius: 50%; margin: 0 auto 25px; display: flex; align-items: center; justify-content: center; font-size: 3rem; color: var(--gold); background: rgba(197, 160, 89, 0.05);">
          {{ emp.full_name.charAt(0) }}
        </div>
        <h3 style="font-size: 1.5rem; margin-bottom: 10px; color: var(--dark);">{{ emp.full_name }}</h3>
        <p style="color: var(--gold); text-transform: uppercase; font-size: 0.85rem; letter-spacing: 1px; font-weight: 600; margin-bottom: 15px;">{{ emp.position }}</p>
        <p style="color: var(--text-muted); font-size: 0.9rem;">Отдел: {{ emp.department }}</p>
      </div>
    </div>
  </div>
</template>