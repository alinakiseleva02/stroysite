<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const materials = ref([])
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/materials/')
    materials.value = res.data
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="page-hero">
    <div class="container">
      <h1>Премиальные материалы</h1>
      <p style="color: var(--gold); margin-top: 15px; letter-spacing: 2px;">ТОЛЬКО ЛУЧШЕЕ ДЛЯ ВАШЕГО ДОМА</p>
    </div>
  </div>
  
  <div class="container" style="padding: 60px 20px;">
    <div class="projects-grid">
      <div v-for="m in materials" :key="m.id" class="project-card" style="padding: 40px; text-align: center;">
        <div style="font-size: 3rem; color: var(--gold); margin-bottom: 20px;">
          <i class="fas fa-gem"></i>
        </div>
        <img v-if="m.image" :src="m.image" alt="Фото" style="width: 100%; height: 200px; object-fit: cover; border-radius: 4px; margin-bottom: 20px; border: 1px solid #eee;">
        <h3 style="font-size: 1.5rem; margin-bottom: 15px; color: var(--dark);">{{ m.name }}</h3>
        <div style="border-top: 1px solid #EEE; padding-top: 20px; margin-top: 20px;">
          <p style="color: var(--text-muted); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px;">Цена за ед.</p>
          <p style="font-size: 1.5rem; font-family: var(--font-heading); color: var(--gold); margin-bottom: 15px;">{{ m.unit_price }} ₽</p>
          <p style="color: var(--text-muted); font-size: 0.9rem;">
            В наличии: <strong style="color: var(--dark);">{{ m.available_quantity }} ед.</strong>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>