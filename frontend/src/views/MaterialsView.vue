<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const materials = ref([])
onMounted(async () => {
  const res = await axios.get('http://127.0.0.1:8000/api/materials/')
  materials.value = res.data
})
</script>

<template>
  <div class="page-hero">
    <div class="container"><h1>Премиальные материалы</h1></div>
  </div>
  <div class="container" style="padding-top: 40px;">
    <div class="projects-grid">
      <div v-for="m in materials" :key="m.id" class="project-card" style="padding: 40px; text-align:center;">
        <div style="font-size: 3rem; color: var(--gold); margin-bottom: 20px;"><i class="fas fa-gem"></i></div>
        <h3 style="font-size: 1.5rem; margin-bottom: 15px;">{{ m.name }}</h3>
        <p style="color: var(--text-muted);">Цена: {{ m.unit_price }} ₽</p>
        <p style="color: var(--text-muted);">В наличии: {{ m.available_quantity }} ед.</p>
      </div>
    </div>
  </div>
</template>