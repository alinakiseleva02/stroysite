<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const exp = ref(0)
const projects = ref(0)
const clients = ref(0)

const form = ref({ name: '', phone: '', message: '' })
const submitStatus = ref('')

onMounted(() => {
  const animateValue = (refVar, target, duration) => {
    let startTimestamp = null
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp
      const progress = Math.min((timestamp - startTimestamp) / duration, 1)
      refVar.value = Math.floor(progress * target)
      if (progress < 1) window.requestAnimationFrame(step)
    }
    window.requestAnimationFrame(step)
  }
  animateValue(exp, 15, 2000)
  animateValue(projects, 200, 2000)
  animateValue(clients, 100, 2000)
})

const submitForm = async () => {
  submitStatus.value = 'loading'
  try {
    await axios.post('http://127.0.0.1:8000/api/contacts/', form.value)
    submitStatus.value = 'success'
    form.value = { name: '', phone: '', message: '' }
  } catch (error) {
    submitStatus.value = 'error'
    console.error('Ошибка отправки:', error)
  }
}

const resetForm = () => { submitStatus.value = '' }
</script>

<template>
  <!-- 1. ГЛАВНЫЙ ЭКРАН -->
  <section class="main-frame">
    <img src="/images/dubai-bg.png" alt="Dubai" class="frame-background">
    <div class="dark-overlay"></div>
    
    <div class="frame-content">
      <p class="main-subtitle">Искусство элитного строительства</p>
      <h1 class="main-title">Строим будущее в Дубае</h1>
      <p class="main-description">Создаем эксклюзивные резиденции и небоскребы с безупречным вниманием к деталям.</p>
      <RouterLink to="/projects" class="btn">Смотреть проекты</RouterLink>
    </div>

    <div class="hero-bubble-container">
      <div class="hero-bubble">
        <img src="/images/dubai-bubble.png" alt="Architecture">
      </div>
    </div>
  </section>

  <!-- 2. СТАТИСТИКА И КЛИЕНТЫ (Возвращаем сюда) -->
  <section class="stats-section">
    <div class="container">
      <div class="stats-grid">
        <div class="stat-item">
          <div class="stat-ring"></div>
          <div class="stat-number">{{ exp }}+</div>
          <div class="stat-label">Лет опыта</div>
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

  <!-- 3. ПРЕМИАЛЬНАЯ ФОРМА ОБРАТНОЙ СВЯЗИ -->
  <section class="contact-section">
    <div class="container">
      <div class="contact-card">
        
        <!-- Успешная отправка -->
        <div v-if="submitStatus === 'success'" class="success-block">
          <div class="success-icon">✓</div>
          <h2>Заявка принята</h2>
          <p>Наш персональный менеджер свяжется с вами в ближайшее время.</p>
          <button @click="resetForm" class="btn" style="margin-top: 30px;">Отправить еще одну</button>
        </div>

        <!-- Сама форма -->
        <div v-else>
          <h2>Обсудить проект</h2>
          <p>Оставьте свои контакты, и мы откроем для вас двери в мир роскоши.</p>
          
          <form @submit.prevent="submitForm" class="premium-form">
            <div class="input-group">
              <input v-model="form.name" type="text" placeholder="Ваше имя" required>
            </div>
            <div class="input-group">
              <input v-model="form.phone" type="tel" placeholder="Номер телефона" required>
            </div>
            <div class="input-group">
              <textarea v-model="form.message" placeholder="Расскажите о вашей идее..."></textarea>
            </div>
            
            <button type="submit" class="btn submit-btn" :disabled="submitStatus === 'loading'">
              {{ submitStatus === 'loading' ? 'Отправка...' : 'Отправить заявку' }}
            </button>
          </form>

          <div v-if="submitStatus === 'error'" class="error-msg">
            <i class="fas fa-exclamation-triangle"></i> Ошибка соединения. Убедитесь, что сервер Django запущен.
          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<style scoped>
/* ===============================
   ПРЕМИАЛЬНЫЙ ДИЗАЙН (ДОРОГО-БОГАТО)
   =============================== */

/* --- Блок клиентов --- */
.happy-clients {
  margin-top: 70px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 20px;
  animation: fadeIn 1.5s ease;
}
.client-avatars {
  display: flex;
}
.client-avatars img {
  width: 65px;
  height: 65px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid var(--gold);
  margin-left: -15px;
  box-shadow: 0 10px 20px rgba(0,0,0,0.15);
  transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.client-avatars img:first-child { margin-left: 0; }
.client-avatars img:hover {
  transform: translateY(-8px) scale(1.1);
  z-index: 10;
  position: relative;
  border-color: #fff;
  box-shadow: 0 15px 30px rgba(197, 160, 89, 0.5);
}
.clients-text {
  font-weight: 600;
  color: var(--dark);
  font-size: 0.95rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  font-family: var(--font-body);
}

/* --- Секция с формой --- */
.contact-section {
  padding: 120px 0;
  background: var(--dark);
  position: relative;
  overflow: hidden;
}

/* Декоративное золотое свечение на фоне */
.contact-section::before {
  content: '';
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, rgba(197, 160, 89, 0.15) 0%, transparent 70%);
  z-index: 1;
  pointer-events: none;
}

.contact-card {
  max-width: 800px;
  margin: 0 auto;
  background: #141414; /* Темный премиальный фон карточки */
  padding: 70px 60px;
  text-align: center;
  border: 1px solid rgba(197, 160, 89, 0.3);
  border-top: 4px solid var(--gold);
  position: relative;
  z-index: 2;
  box-shadow: 0 30px 60px rgba(0,0,0,0.6), inset 0 0 20px rgba(197, 160, 89, 0.05);
}

.contact-card h2 {
  font-size: 3rem;
  color: var(--white);
  margin-bottom: 15px;
  letter-spacing: 1px;
}

.contact-card p {
  color: #999;
  margin-bottom: 50px;
  font-size: 1.1rem;
  font-weight: 300;
}

/* Поля ввода */
.premium-form {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.input-group {
  position: relative;
}

.premium-form input,
.premium-form textarea {
  width: 100%;
  padding: 20px;
  background: transparent;
  border: 1px solid #333;
  color: var(--white);
  font-family: var(--font-body);
  font-size: 1rem;
  transition: all 0.4s ease;
  border-radius: 2px;
}

.premium-form input::placeholder,
.premium-form textarea::placeholder {
  color: #666;
}

.premium-form input:focus,
.premium-form textarea:focus {
  border-color: var(--gold);
  outline: none;
  background: rgba(197, 160, 89, 0.05);
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.1);
}

.premium-form textarea {
  height: 140px;
  resize: vertical;
}

.submit-btn {
  margin-top: 10px;
  background: linear-gradient(135deg, #C5A059, #E6C887, #B08D46);
  color: var(--dark);
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: 20px;
  border: none;
  cursor: pointer;
  transition: all 0.4s ease;
}

.submit-btn:hover {
  background: linear-gradient(135deg, #E6C887, #C5A059, #E6C887);
  transform: translateY(-3px);
  box-shadow: 0 15px 30px rgba(197, 160, 89, 0.3);
}

/* Блок успеха */
.success-block {
  padding: 40px 0;
  animation: fadeIn 0.6s cubic-bezier(0.165, 0.84, 0.44, 1);
}

.success-icon {
  width: 90px;
  height: 90px;
  background: linear-gradient(135deg, #C5A059, #E6C887);
  color: var(--dark);
  font-size: 3rem;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  margin: 0 auto 30px;
  box-shadow: 0 0 30px rgba(197, 160, 89, 0.4);
}

.error-msg {
  margin-top: 25px;
  color: #ff4d4d;
  font-weight: 500;
  background: rgba(255, 77, 77, 0.1);
  padding: 15px;
  border-radius: 4px;
  border: 1px solid rgba(255, 77, 77, 0.3);
}

@keyframes fadeIn {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>