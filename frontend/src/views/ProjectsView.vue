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
      <h1>Наше портфолио</h1>
    </div>
  </div>

  <div class="container portfolio-container">
    <div class="search-wrapper">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="Поиск по названию..." 
        class="fancy-search"
      >
    </div>

    <div class="portfolio-grid">
      <div v-for="p in filteredProjects" :key="p.id" class="portfolio-item">
        <div class="portfolio-card">
          <div class="tape"></div>
          
          <div class="image-frame">
            <img v-if="p.image" :src="p.image" :alt="p.name">
            <div v-else class="placeholder">YALI</div>
          </div>
          
          <div class="card-details">
            <h3>{{ p.name }}</h3>
            <p><strong>Заказчик:</strong> {{ p.customer_details?.company_name }}</p>
            <p><strong>Бюджет:</strong> {{ p.formatted_budget }}</p>
            <RouterLink :to="`/projects/${p.id}`" class="view-btn">
              Изучить проект <i class="fas fa-arrow-right"></i>
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.portfolio-container {
  padding: 60px 20px;
  padding-bottom: 120px;
}

.search-wrapper {
  text-align: center;
  margin-bottom: 60px;
}

.fancy-search {
  width: 100%;
  max-width: 500px;
  padding: 18px;
  border: none;
  border-bottom: 2px solid #CCC;
  background: transparent;
  text-align: center;
  outline: none;
  font-family: var(--font-body);
  font-size: 1rem;
  transition: 0.3s;
}

.fancy-search:focus {
  border-color: var(--gold);
}

.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  gap: 60px;
  perspective: 1000px;
}

.portfolio-item {
  perspective: 1000px;
}

.portfolio-card {
  background: #FAFAFA;
  padding: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  position: relative;
  transition: all 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  border: 1px solid #EAEAEA;
}

.portfolio-item:nth-child(odd) .portfolio-card {
  transform: rotate(-2deg);
}

.portfolio-item:nth-child(even) .portfolio-card {
  transform: rotate(2deg);
}

.portfolio-card:hover {
  transform: rotate(0deg) translateY(-15px) scale(1.05) !important;
  box-shadow: 0 30px 60px rgba(197, 160, 89, 0.25);
  z-index: 10;
}

.tape {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%) rotate(-2deg);
  width: 100px;
  height: 30px;
  background: rgba(255, 255, 255, 0.8);
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  border: 1px dashed rgba(0, 0, 0, 0.1);
  transition: 0.4s;
}

.portfolio-card:hover .tape {
  background: var(--gold);
  border-color: var(--gold);
  transform: translateX(-50%) rotate(0deg);
}

.image-frame {
  height: 250px;
  overflow: hidden;
  background: #111;
}

.image-frame img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: 0.8s ease;
}

.portfolio-card:hover .image-frame img {
  transform: scale(1.1);
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
}

.card-details {
  padding: 25px 10px 10px;
  text-align: center;
}

.card-details h3 {
  font-size: 1.6rem;
  color: var(--dark);
  margin-bottom: 10px;
  font-family: var(--font-heading);
}

.card-details p {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin-bottom: 5px;
}

.view-btn {
  display: inline-block;
  margin-top: 20px;
  padding: 12px 30px;
  border: 1px solid var(--gold);
  color: var(--gold);
  text-decoration: none;
  text-transform: uppercase;
  font-size: 0.85rem;
  letter-spacing: 1px;
  transition: 0.4s;
}

.view-btn:hover {
  background: var(--gold);
  color: white;
}
</style>