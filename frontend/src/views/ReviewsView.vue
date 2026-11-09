<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const reviews = ref([])
onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/reviews/')
    reviews.value = res.data
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="page-hero">
    <div class="container">
      <h1>Отзывы клиентов</h1>
      <p style="color: var(--gold); margin-top: 15px; letter-spacing: 2px;">ЧТО О НАС ГОВОРЯТ</p>
    </div>
  </div>
  
  <div class="container" style="padding: 60px 20px;">
    <div class="projects-grid">
      
      <div v-for="(r, index) in reviews" :key="r.id" class="review-card" :style="{ animationDelay: (index * 0.1) + 's' }">
        <div class="stars-container">
          <i v-for="n in 5" :key="n" class="fas fa-star star" :class="{ active: n <= r.rating }"></i>
        </div>
        <p class="review-text">"{{ r.text }}"</p>
        <div class="review-author">— {{ r.client_name }}</div>
        <div class="gold-line"></div>
      </div>

    </div>
  </div>
</template>

<style scoped>
.review-card {
  background: var(--white);
  padding: 40px;
  border: 1px solid #EAEAEA;
  position: relative;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275); 
  opacity: 0;
  animation: slideUpFade 0.8s forwards;
}

.review-card:hover {
  transform: translateY(-10px) scale(1.02);
  box-shadow: 0 20px 40px rgba(197, 160, 89, 0.2);
  border-color: var(--gold);
}

.gold-line {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 4px;
  width: 0%;
  background: var(--gold);
  transition: width 0.4s ease;
}
.review-card:hover .gold-line {
  width: 100%;
}

.stars-container {
  display: flex;
  gap: 8px;
  margin-bottom: 25px;
}

.star {
  font-size: 1.2rem;
  color: #DDD;
  transition: all 0.3s ease;
}

.star.active {
  color: var(--gold);
  text-shadow: 0 0 10px rgba(197, 160, 89, 0.5);
}

.review-card:hover .star.active {
  animation: starBounce 0.6s ease infinite alternate;
}

.review-card:hover .star:nth-child(1) { animation-delay: 0s; }
.review-card:hover .star:nth-child(2) { animation-delay: 0.1s; }
.review-card:hover .star:nth-child(3) { animation-delay: 0.2s; }
.review-card:hover .star:nth-child(4) { animation-delay: 0.3s; }
.review-card:hover .star:nth-child(5) { animation-delay: 0.4s; }

.review-text {
  font-style: italic;
  color: var(--dark);
  font-size: 1.1rem;
  line-height: 1.7;
  margin-bottom: 25px;
  position: relative;
  z-index: 2;
}

.review-author {
  font-weight: 700;
  text-transform: uppercase;
  font-size: 0.9rem;
  color: var(--text-muted);
  letter-spacing: 1px;
}


@keyframes slideUpFade {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes starBounce {
  0% { transform: translateY(0); }
  100% { transform: translateY(-8px) scale(1.1); }
}
</style>