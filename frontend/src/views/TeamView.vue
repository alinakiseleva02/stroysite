<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const employees = ref([])
onMounted(async () => {
  const res = await axios.get('http://127.0.0.1:8000/api/employees/')
  employees.value = res.data
})
</script>

<template>
  <div class="page-hero">
    <div class="container"><h1>Наша команда</h1></div>
  </div>
  <div class="container" style="padding-top: 40px;">
    <div class="projects-grid">
      <div v-for="emp in employees" :key="emp.id" class="project-card" style="padding: 40px; text-align:center;">
        <div style="width: 90px; height: 90px; border: 2px solid var(--gold); color: var(--gold); font-size: 2.5rem; font-family: var(--font-heading); display:flex; align-items:center; justify-content:center; border-radius: 50%; margin: 0 auto 20px;">
          {{ emp.full_name.charAt(0) }}
        </div>
        <h3 style="font-size: 1.5rem; margin-bottom: 10px;">{{ emp.full_name }}</h3>
        <p style="color: var(--gold); text-transform: uppercase; letter-spacing: 1px; font-size: 0.85rem;">{{ emp.position }}</p>
      </div>
    </div>
  </div>
</template>