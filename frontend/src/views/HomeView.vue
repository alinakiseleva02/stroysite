<script setup>
import { ref, onMounted } from 'vue'

// Анимация счетчиков
const exp = ref(0)
const projects = ref(0)
const clients = ref(0)

onMounted(() => {
  const animateValue = (refVar, target, duration) => {
    let startTimestamp = null
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp
      const progress = Math.min((timestamp - startTimestamp) / duration, 1)
      refVar.value = Math.floor(progress * target)
      if (progress < 1) {
        window.requestAnimationFrame(step)
      }
    }
    window.requestAnimationFrame(step)
  }
  
  animateValue(exp, 15, 2000)
  animateValue(projects, 200, 2000)
  animateValue(clients, 100, 2000)
})
</script>

<template>
  <!-- ГЛАВНЫЙ ЭКРАН С ПУЗЫРЬКОМ -->
  <section class="main-frame">
    <!-- ВАЖНО: здесь теперь .png, как у вас в папке -->
    <img src="/images/dubai-bg.png" alt="Dubai" class="frame-background">
    <div class="dark-overlay"></div>
    
    <div class="frame-content">
      <p class="main-subtitle">Премиум недвижимость в ОАЭ</p>
      <h1 class="main-title">Строим будущее в Дубае</h1>
      <p class="main-description">Создаем эксклюзивные резиденции и небоскребы с безупречным вниманием к деталям. Ваш личный оазис роскоши.</p>
      <RouterLink to="/projects" class="btn">Смотреть проекты</RouterLink>
    </div>

    <!-- Тот самый анимированный пузырек -->
    <div class="hero-bubble-container">
      <div class="hero-bubble">
        <img src="/images/dubai-bubble.png" alt="Dubai Architecture">
      </div>
    </div>
  </section>

  <!-- ИНТЕРЕСНЫЙ БЛОК О КОМПАНИИ (КОЛЛАЖ) -->
  <section class="about-section">
    <div class="container about-grid">
      <div class="about-image-collage">
        <img src="/images/dubai-bubble.png" alt="Dubai" class="about-img-main">
        <img src="/images/about-dubai.png" alt="Interior" class="about-img-sub">
        <div class="about-badge">TOP<br>DEVELOPER</div>
      </div>
      <div class="about-content">
        <h2>Архитектура, покоряющая мир</h2>
        <p>YALI — это синоним элитного строительства в Дубае. Мы объединяем передовые технологии, лучших архитекторов и безграничную роскошь.</p>
        <p>От пентхаусов с видом на Бурдж-Халифа до частных вилл на Пальме — мы реализуем проекты любой сложности для тех, кто привык к лучшему.</p>
      </div>
    </div>
  </section>

  <!-- СТАТИСТИКА С АНИМАЦИЕЙ И АРАБСКИМИ КЛИЕНТАМИ -->
  <section class="stats-section">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item">
          <div class="stat-ring"></div>
          <div class="stat-number">{{ exp }}+</div>
          <div class="stat-label">Лет опыта в Дубае</div>
        </div>
        <div class="stat-item">
          <div class="stat-ring" style="animation-direction: reverse;"></div>
          <div class="stat-number">{{ projects }}+</div>
          <div class="stat-label">Премиум объектов</div>
        </div>
        <div class="stat-item">
          <div class="stat-ring"></div>
          <div class="stat-number">{{ clients }}%</div>
          <div class="stat-label">Довольных клиентов</div>
        </div>
      </div>

      <!-- Блок счастливых клиентов -->
      <div class="happy-clients">
        <div class="client-avatars">
          <img src="/images/client1.png" alt="Client">
          <img src="/images/client2.png" alt="Client">
          <img src="/images/client3.png" alt="Client">
        </div>
        <div class="clients-text">Наши клиенты рекомендуют нас</div>
      </div>
    </div>
  </section>
</template>