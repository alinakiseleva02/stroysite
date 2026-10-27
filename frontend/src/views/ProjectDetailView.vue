<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const project = ref(null)

// Логика карусели
const currentSlide = ref(0)
let slideInterval = null

const nextSlide = () => {
  if (project.value && project.value.gallery && project.value.gallery.length > 0) {
    currentSlide.value = (currentSlide.value + 1) % project.value.gallery.length
  }
}

const setSlide = (index) => {
  currentSlide.value = index
}

onMounted(async () => {
  try {
    const res = await axios.get(`http://127.0.0.1:8000/api/projects/${route.params.id}/`)
    project.value = res.data
    
    if (project.value.gallery && project.value.gallery.length > 1) {
      slideInterval = setInterval(nextSlide, 3000) // Смена каждые 3 сек
    }
  } catch (error) {
    console.error("Ошибка загрузки", error)
  }
})

onUnmounted(() => {
  if (slideInterval) clearInterval(slideInterval)
})
</script>

<template>
  <div class="page-hero" v-if="project">
    <div class="container">
      <h1>{{ project.name }}</h1>
    </div>
  </div>
  
  <div v-if="project" class="container" style="padding: 60px 20px; padding-bottom: 100px;">
    
    <!-- ГЛАВНАЯ КАРТИНКА ПРОЕКТА -->
    <div v-if="project.image" class="hero-image-container">
      <img :src="project.image" :alt="project.name">
    </div>

    <div class="project-layout">
      
      <!-- ИНФОРМАЦИЯ -->
      <div class="info-section">
        <h2>О проекте</h2>
        <p class="description">{{ project.description }}</p>
        
        <div class="specs">
          <div class="spec-item">
            <span class="label">Стоимость:</span>
            <span class="value">{{ project.formatted_budget }}</span>
          </div>
          <div class="spec-item">
            <span class="label">Срок реализации:</span>
            <span class="value">{{ project.formatted_construction_period }}</span>
          </div>
          <div class="spec-item">
            <span class="label">Заказчик:</span>
            <span class="value">{{ project.customer_details.company_name }}</span>
          </div>
          <div class="spec-item">
            <span class="label">Архитектор:</span>
            <span class="value">{{ project.employee_details.full_name }}</span>
          </div>
        </div>

        <RouterLink to="/projects" class="btn">← Вернуться в каталог</RouterLink>
      </div>

      <!-- ГАЛЕРЕЯ С АВТОПРОКРУТКОЙ -->
      <div class="gallery-section" v-if="project.gallery && project.gallery.length > 0">
        <div class="carousel">
          <div 
            v-for="(img, index) in project.gallery" 
            :key="img.id"
            class="carousel-slide"
            :class="{ active: index === currentSlide }"
          >
            <img :src="img.image" :alt="project.name">
          </div>
          
          <div class="carousel-dots">
            <span 
              v-for="(img, index) in project.gallery" 
              :key="index"
              class="dot"
              :class="{ active: index === currentSlide }"
              @click="setSlide(index)"
            ></span>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<style scoped>
/* Стили для главной картинки */
.hero-image-container {
  width: 100%;
  height: 600px;
  margin-bottom: 60px;
  border: 2px solid var(--gold);
  padding: 10px;
  box-shadow: 0 20px 50px rgba(197, 160, 89, 0.15);
}

.hero-image-container img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

/* Сетка */
.project-layout {
  display: grid;
  grid-template-columns: 1fr 1.2fr;
  gap: 60px;
  align-items: start;
}

/* Текст */
.info-section h2 { font-size: 3rem; color: var(--dark); margin-bottom: 20px; }
.description { font-size: 1.1rem; color: var(--text-muted); line-height: 1.8; margin-bottom: 40px; }
.specs { border-top: 1px solid #EEE; padding-top: 30px; margin-bottom: 40px; }
.spec-item { display: flex; justify-content: space-between; padding: 15px 0; border-bottom: 1px solid #f5f5f5; }
.spec-item .label { color: var(--text-muted); font-weight: 500; }
.spec-item .value { color: var(--dark); font-weight: 600; font-size: 1.1rem; }

/* Галерея */
.gallery-section {
  position: relative;
  width: 100%;
  height: 500px;
  border: 2px solid var(--gold);
  padding: 10px;
  box-shadow: 0 20px 50px rgba(197, 160, 89, 0.15);
}

.carousel { position: relative; width: 100%; height: 100%; overflow: hidden; }

.carousel-slide {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
  transform: scale(1.05);
}

.carousel-slide.active {
  opacity: 1;
  transform: scale(1);
  transition: opacity 1s ease-in-out, transform 6s linear; /* Эффект плавного зума */
}

.carousel-slide img { width: 100%; height: 100%; object-fit: cover; display: block; }

/* Точки */
.carousel-dots {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 12px;
  z-index: 10;
}

.dot {
  width: 12px; height: 12px; border-radius: 50%;
  background: rgba(255,255,255,0.5); cursor: pointer; transition: 0.3s;
}

.dot.active {
  background: var(--gold); transform: scale(1.3);
  box-shadow: 0 0 10px rgba(197, 160, 89, 0.8);
}

@media (max-width: 900px) {
  .project-layout { grid-template-columns: 1fr; }
  .hero-image-container { height: 300px; }
  .gallery-section { height: 300px; }
}
</style>