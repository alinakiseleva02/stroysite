<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const services = ref([])
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/services/')
    services.value = res.data
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="page-hero">
    <div class="container"><h1>Наши услуги</h1></div>
  </div>
  <div class="container" style="padding: 60px 20px;">
    <div class="projects-grid">
      <div v-for="s in services" :key="s.id" class="project-card" style="padding: 40px; text-align: center;">
        <div style="font-size: 3rem; color: var(--gold); margin-bottom: 20px;">
          <i :class="'fas ' + s.icon"></i>
        </div>
        <h3 style="font-size: 1.5rem; margin-bottom: 15px; color: var(--dark);">{{ s.title }}</h3>
        <p style="color: var(--text-muted); margin-bottom: 20px; line-height: 1.6;">{{ s.description }}</p>
        <div style="font-size: 1.2rem; font-weight: bold; color: var(--gold);">от {{ s.price }} руб.</div>
      </div>
    </div>
  </div>
</template>