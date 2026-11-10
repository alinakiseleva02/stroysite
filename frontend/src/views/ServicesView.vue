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
    <div class="container">
      <h1>Наши услуги</h1>
    </div>
  </div>
  
  <div class="container services-container">
    <div class="timeline">
      <div 
        v-for="(s, index) in services" 
        :key="s.id" 
        class="timeline-item" 
        :class="index % 2 === 0 ? 'left' : 'right'"
      >
        <div class="timeline-content">
          <div class="icon-box">
            <i :class="'fas ' + s.icon"></i>
          </div>
          <h3>{{ s.title }}</h3>
          <p>{{ s.description }}</p>
          <div class="price">от {{ s.price }} ₽</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.services-container {
  padding: 80px 20px;
}

.timeline {
  position: relative;
  max-width: 1000px;
  margin: 0 auto;
}

.timeline::after {
  content: '';
  position: absolute;
  width: 2px;
  background: var(--gold);
  top: 0;
  bottom: 0;
  left: 50%;
  margin-left: -1px;
  opacity: 0.3;
}

.timeline-item {
  padding: 10px 40px;
  position: relative;
  background-color: inherit;
  width: 50%;
}

.timeline-item.left {
  left: 0;
}

.timeline-item.right {
  left: 50%;
}

.timeline-item::after {
  content: '';
  position: absolute;
  width: 20px;
  height: 20px;
  right: -10px;
  background-color: var(--white);
  border: 4px solid var(--gold);
  top: 50%;
  transform: translateY(-50%);
  border-radius: 50%;
  z-index: 1;
  transition: all 0.3s ease;
}

.timeline-item.right::after {
  left: -10px;
}

.timeline-item:hover::after {
  background-color: var(--gold);
  box-shadow: 0 0 15px var(--gold);
  transform: translateY(-50%) scale(1.2);
}

.timeline-content {
  padding: 30px;
  background: var(--white);
  position: relative;
  border-radius: 15px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  transition: all 0.4s ease;
}

.timeline-item:hover .timeline-content {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(197, 160, 89, 0.15);
}

.icon-box {
  font-size: 2rem;
  color: var(--gold);
  margin-bottom: 15px;
}

.timeline-content h3 {
  font-size: 1.5rem;
  color: var(--dark);
  margin-bottom: 10px;
}

.timeline-content p {
  color: var(--text-muted);
  font-size: 0.95rem;
  line-height: 1.6;
  margin-bottom: 15px;
}

.price {
  font-weight: bold;
  color: var(--gold);
  font-size: 1.2rem;
}

@media screen and (max-width: 768px) {
  .timeline::after {
    left: 31px;
  }
  
  .timeline-item {
    width: 100%;
    padding-left: 70px;
    padding-right: 25px;
  }
  
  .timeline-item.right {
    left: 0%;
  }
  
  .timeline-item::after {
    left: 21px;
  }
  
  .timeline-item.right::after {
    left: 21px;
  }
}
</style>