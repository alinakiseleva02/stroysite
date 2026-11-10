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
    </div>
  </div>

  <div class="container team-container">
    <div class="team-grid">
      <div v-for="emp in employees" :key="emp.id" class="team-card">
        <div class="img-wrapper">
          <img v-if="emp.image" :src="emp.image" alt="Фото">
          <div v-else class="placeholder">{{ emp.full_name.charAt(0) }}</div>
          
          <div class="overlay">
            <p>{{ emp.department }}</p>
          </div>
        </div>
        
        <div class="info">
          <h3>{{ emp.full_name }}</h3>
          <p class="pos">{{ emp.position }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.team-container {
  padding: 80px 20px;
}

.team-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 30px;
}

.team-card {
  background: var(--white);
  overflow: hidden;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: all 0.4s ease;
}

.team-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(197, 160, 89, 0.15);
}

.img-wrapper {
  position: relative;
  height: 380px;
  overflow: hidden;
  background: #111;
}

.img-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: grayscale(100%);
  transition: all 0.6s ease;
}

.placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 5rem;
  color: var(--gold);
  font-family: var(--font-heading);
  background: #1a1a1a;
}

.team-card:hover .img-wrapper img {
  filter: grayscale(0%);
  transform: scale(1.08);
}

.overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 20px;
  background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
  opacity: 0;
  transition: 0.4s ease;
}

.team-card:hover .overlay {
  opacity: 1;
}

.overlay p {
  color: var(--gold);
  text-transform: uppercase;
  font-size: 0.8rem;
  letter-spacing: 2px;
}

.info {
  padding: 25px;
  text-align: center;
  border-bottom: 3px solid transparent;
  transition: 0.4s;
}

.team-card:hover .info {
  border-color: var(--gold);
}

.info h3 {
  font-size: 1.4rem;
  color: var(--dark);
  margin-bottom: 5px;
}

.info .pos {
  color: var(--text-muted);
  font-size: 0.9rem;
}
</style>