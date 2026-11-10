<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const customers = ref([])

onMounted(async () => {
  try {
    const res = await axios.get('http://127.0.0.1:8000/api/customers/')
    customers.value = res.data
  } catch (error) {
    console.error(error)
  }
})
</script>

<template>
  <div class="page-hero partners-hero">
    <div class="container">
      <p class="hero-subtitle">ДОВЕРИЕ, ПОДТВЕРЖДЕННОЕ ВРЕМЕНЕМ</p>
      <h1>Наши партнеры</h1>
      <p class="hero-desc">Мы работаем с лидерами рынка. Их выбор — это гарантия качества, которой доверяют тысячи клиентов.</p>
    </div>
  </div>
  
  <div class="container partners-container">
    <div class="partners-grid">
      
      <div 
        v-for="(c, index) in customers" 
        :key="c.id" 
        class="partner-card" 
        :style="{ animationDelay: (index * 0.1) + 's' }"
      >
        <div class="logo-watermark">{{ c.company_name.charAt(0) }}</div>
        
        <div class="card-content">
          <div class="badge">Authorized Partner</div>
          <h2 class="company-name">{{ c.company_name }}</h2>
          <div class="gold-line"></div>
          
          <div class="contact-block">
            <div class="contact-row">
              <i class="fas fa-user-tie"></i>
              <span>{{ c.contact_person }}</span>
            </div>
            <div class="contact-row">
              <i class="fas fa-phone-alt"></i>
              <a :href="'tel:' + c.phone_number">{{ c.phone_number }}</a>
            </div>
            <div class="contact-row">
              <i class="fas fa-envelope"></i>
              <a :href="'mailto:' + c.email">{{ c.email }}</a>
            </div>
          </div>
        </div>
      </div>

    </div>
    
    <div class="trust-banner">
      <h3>Станьте частью круга избранных</h3>
      <p>Мы всегда открыты для сотрудничества с ведущими застройщиками и инвесторами.</p>
      <RouterLink to="/#contact-form" class="btn">Обсудить партнерство</RouterLink>
    </div>
  </div>
</template>

<style scoped>
.partners-hero {
  background: #111;
  padding: 120px 0 100px;
  text-align: center;
}

.hero-subtitle {
  color: var(--gold);
  letter-spacing: 4px;
  font-size: 0.85rem;
  font-weight: 600;
  margin-bottom: 20px;
}

.hero-desc {
  color: #A0A0A0;
  max-width: 600px;
  margin: 20px auto 0;
  font-size: 1.1rem;
  line-height: 1.6;
}

.partners-container {
  padding: 80px 20px;
  background: #FDFDFD;
}

.partners-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(380px, 1fr));
  gap: 40px;
}

.partner-card {
  background: #FFFFFF;
  border: 1px solid #EFEFEF;
  padding: 50px 40px;
  position: relative;
  overflow: hidden;
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
  opacity: 0;
  animation: slideUp 0.8s forwards;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.02);
}

.partner-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 25px 50px rgba(197, 160, 89, 0.15);
  border-color: var(--gold);
}

.logo-watermark {
  position: absolute;
  top: -20px;
  right: -10px;
  font-size: 15rem;
  font-family: var(--font-heading);
  color: var(--gold);
  opacity: 0.03;
  line-height: 1;
  transition: 0.4s;
  pointer-events: none;
}

.partner-card:hover .logo-watermark {
  opacity: 0.08;
  transform: scale(1.1);
}

.card-content {
  position: relative;
  z-index: 2;
}

.badge {
  display: inline-block;
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--text-muted);
  margin-bottom: 15px;
  font-weight: 600;
}

.company-name {
  font-size: 2rem;
  color: var(--dark);
  margin-bottom: 20px;
  font-family: var(--font-heading);
  line-height: 1.2;
}

.gold-line {
  width: 40px;
  height: 3px;
  background: var(--gold);
  margin-bottom: 30px;
  transition: width 0.4s ease;
}

.partner-card:hover .gold-line {
  width: 80px;
}

.contact-block {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.contact-row {
  display: flex;
  align-items: center;
  gap: 15px;
  color: #555;
  font-size: 0.95rem;
}

.contact-row i {
  color: var(--gold);
  font-size: 1.1rem;
  width: 20px;
  text-align: center;
}

.contact-row a {
  color: #555;
  text-decoration: none;
  transition: 0.3s;
}

.contact-row a:hover {
  color: var(--gold);
}

.trust-banner {
  margin-top: 100px;
  text-align: center;
  padding: 60px 40px;
  background: var(--dark);
  color: white;
  border-top: 4px solid var(--gold);
}

.trust-banner h3 {
  font-size: 2.5rem;
  font-family: var(--font-heading);
  margin-bottom: 15px;
}

.trust-banner p {
  color: #A0A0A0;
  margin-bottom: 30px;
  font-size: 1.1rem;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(40px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 768px) {
  .partners-grid {
    grid-template-columns: 1fr;
  }
  
  .partner-card {
    padding: 40px 30px;
  }
  
  .company-name {
    font-size: 1.6rem;
  }
}
</style>