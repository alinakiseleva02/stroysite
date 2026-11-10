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
    </div>
  </div>

  <div class="container catalog-container">
    <div class="catalog-list">
      <div 
        v-for="(m, index) in materials" 
        :key="m.id" 
        class="catalog-item" 
        :style="{ animationDelay: (index * 0.1) + 's' }"
      >
        <div class="catalog-image">
          <img v-if="m.image" :src="m.image" :alt="m.name">
          <div v-else class="img-placeholder">
            <i class="fas fa-gem"></i>
          </div>
        </div>
        
        <div class="catalog-details">
          <div class="item-header">
            <span class="name">{{ m.name }}</span>
            <div class="dots"></div>
            <span class="price">{{ m.unit_price }} ₽</span>
          </div>
          
          <div class="item-footer">
            <span>
              <i class="fas fa-cubes"></i> 
              В наличии: {{ m.available_quantity }} ед.
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.catalog-container {
  padding: 80px 20px;
  max-width: 1000px;
}

.catalog-list {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.catalog-item {
  display: flex;
  align-items: center;
  gap: 30px;
  padding: 20px;
  background: var(--white);
  border: 1px solid #EAEAEA;
  border-radius: 12px;
  opacity: 0;
  animation: fadeInUp 0.6s forwards;
  transition: all 0.4s ease;
}

.catalog-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(197, 160, 89, 0.15);
  border-color: var(--gold);
}

.catalog-image {
  width: 140px;
  height: 140px;
  flex-shrink: 0;
  border-radius: 8px;
  overflow: hidden;
  background: #FAFAFA;
  border: 1px solid #EEE;
}

.catalog-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.catalog-item:hover .catalog-image img {
  transform: scale(1.15);
}

.img-placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2.5rem;
  color: var(--gold);
  background: #f9f9f9;
}

.catalog-details {
  flex-grow: 1;
}

.item-header {
  display: flex;
  align-items: baseline;
  margin-bottom: 15px;
}

.name {
  font-family: var(--font-heading);
  font-size: 1.6rem;
  color: var(--dark);
  font-weight: 600;
}

.dots {
  flex-grow: 1;
  border-bottom: 2px dotted #CCC;
  margin: 0 20px;
  opacity: 0.5;
}

.price {
  font-size: 1.4rem;
  color: var(--gold);
  font-weight: bold;
  font-family: var(--font-heading);
}

.item-footer {
  font-size: 0.9rem;
  color: var(--text-muted);
  text-transform: uppercase;
  letter-spacing: 1px;
}

.item-footer i {
  color: var(--gold);
  margin-right: 5px;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .catalog-item {
    flex-direction: column;
    text-align: center;
  }
  
  .catalog-image {
    width: 100%;
    height: 200px;
  }
  
  .item-header {
    flex-direction: column;
    align-items: center;
    gap: 10px;
  }
  
  .dots {
    display: none;
  }
}
</style>