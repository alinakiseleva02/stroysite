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
  <div class="split-bg">
    <div class="half dark"></div>
    <div class="half light"></div>
  </div>

  <div class="page-hero hero-transparent">
    <div class="container hero-content">
      <h1 class="glitch-title">Отзывы клиентов</h1>
      <p class="subtitle">ЧТО О НАС ГОВОРЯТ</p>
    </div>
  </div>
  
  <div class="container grid-container">
    <div class="playful-grid">
      <div 
        v-for="(r, index) in reviews" 
        :key="r.id" 
        class="toy-card" 
        :class="index % 2 === 0 ? 'card-light tilt-left' : 'card-dark tilt-right'"
      >
        <div class="stars-container">
          <i 
            v-for="n in 5" 
            :key="n" 
            class="fas fa-star star" 
            :class="{ active: n <= r.rating }"
          ></i>
        </div>
        
        <p class="review-text">"{{ r.text }}"</p>
        
        <div class="author-block">
          <div class="avatar-icon">{{ r.client_name.charAt(0) }}</div>
          <span class="author-name">{{ r.client_name }}</span>
        </div>
        
        <div class="corner-accent"></div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.hero-transparent {
  background: transparent;
  border-bottom: none;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.grid-container {
  padding: 40px 20px 120px;
  position: relative;
  z-index: 2;
}

.split-bg {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  display: flex;
  z-index: 0;
  pointer-events: none;
}

.half {
  flex: 1;
}

.half.dark {
  background: #111111;
}

.half.light {
  background: #f9f9f9;
}

.glitch-title {
  color: #fff;
  text-shadow: 3px 3px 0 var(--gold), -1px -1px 0 rgba(255, 255, 255, 0.2);
  font-size: 4rem;
}

.subtitle {
  color: var(--gold);
  font-weight: bold;
  letter-spacing: 5px;
}

.playful-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 50px;
  perspective: 1200px;
}

.toy-card {
  padding: 40px 30px;
  border-radius: 30px;
  position: relative;
  transition: all 0.6s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
  overflow: hidden;
  animation: float 4s ease-in-out infinite;
}

.card-light {
  background: var(--white);
  color: var(--dark);
  border: 3px solid var(--gold);
}

.card-dark {
  background: #1E1E1E;
  color: #E0E0E0;
  border: 3px solid #333;
}

.tilt-left {
  transform: rotate(-3deg);
}

.tilt-right {
  transform: rotate(3deg);
}

.toy-card:hover {
  transform: scale(1.08) rotate(0deg) translateY(-15px);
  box-shadow: 0 30px 60px rgba(197, 160, 89, 0.4);
  animation-play-state: paused;
  z-index: 10;
}

.stars-container {
  display: flex;
  gap: 10px;
  margin-bottom: 25px;
}

.star {
  font-size: 1.5rem;
  color: #444;
  transition: 0.3s;
}

.card-light .star {
  color: #ddd;
}

.star.active {
  color: var(--gold);
  text-shadow: 0 0 20px rgba(197, 160, 89, 0.8);
}

.toy-card:hover .star.active {
  animation: bounce 0.5s infinite alternate;
}

.toy-card:hover .star:nth-child(1) {
  animation-delay: 0s;
}

.toy-card:hover .star:nth-child(2) {
  animation-delay: 0.1s;
}

.toy-card:hover .star:nth-child(3) {
  animation-delay: 0.2s;
}

.toy-card:hover .star:nth-child(4) {
  animation-delay: 0.3s;
}

.toy-card:hover .star:nth-child(5) {
  animation-delay: 0.4s;
}

.review-text {
  font-size: 1.1rem;
  font-style: italic;
  line-height: 1.8;
  margin-bottom: 30px;
  font-weight: 300;
}

.author-block {
  display: flex;
  align-items: center;
  gap: 15px;
}

.avatar-icon {
  width: 45px;
  height: 45px;
  border-radius: 50%;
  background: linear-gradient(135deg, var(--gold), #E6C887);
  color: #111;
  font-weight: bold;
  font-size: 1.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 5px 15px rgba(197, 160, 89, 0.4);
}

.author-name {
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 1px;
  font-size: 0.9rem;
}

.corner-accent {
  position: absolute;
  top: 0;
  right: 0;
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, transparent 50%, var(--gold) 50%);
  opacity: 0.2;
  transition: 0.4s;
}

.toy-card:hover .corner-accent {
  opacity: 1;
  width: 80px;
  height: 80px;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-10px);
  }
}

@keyframes bounce {
  0% {
    transform: translateY(0) scale(1);
  }
  100% {
    transform: translateY(-10px) scale(1.3);
  }
}

@media (max-width: 768px) {
  .split-bg {
    display: none;
  }

  .glitch-title {
    font-size: 2.5rem;
  }

  .toy-card {
    transform: none !important;
    margin-bottom: 20px;
  }
}
</style>