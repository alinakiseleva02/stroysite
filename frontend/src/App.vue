<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
import Footer from './components/Footer.vue'

const mouseX = ref(0)
const mouseY = ref(0)
const cursorX = ref(0)
const cursorY = ref(0)
const isHovering = ref(false)

const handleMouseMove = (e) => {
  mouseX.value = e.clientX
  mouseY.value = e.clientY
}

const animateCursor = () => {
  cursorX.value += (mouseX.value - cursorX.value) * 0.2
  cursorY.value += (mouseY.value - cursorY.value) * 0.2
  requestAnimationFrame(animateCursor)
}

onMounted(() => {
  window.addEventListener('mousemove', handleMouseMove)
  animateCursor()

  document.addEventListener('mouseover', (e) => {
    if (e.target.closest('a') || e.target.closest('button') || e.target.closest('.project-card') || e.target.closest('.playful-card')) {
      isHovering.value = true
    }
  })
  
  document.addEventListener('mouseout', (e) => {
    if (e.target.closest('a') || e.target.closest('button') || e.target.closest('.project-card') || e.target.closest('.playful-card')) {
      isHovering.value = false
    }
  })
})

onUnmounted(() => {
  window.removeEventListener('mousemove', handleMouseMove)
})
</script>

<template>
  <div 
    class="custom-cursor" 
    :style="{ left: cursorX + 'px', top: cursorY + 'px' }"
    :class="{ 'hovering': isHovering }"
  ></div>

  <Header />
  <main>
    <RouterView />
  </main>
  <Footer />
</template>

<style>
@media (min-width: 1024px) {
  body, 
  a, 
  button, 
  input, 
  textarea, 
  select {
    cursor: none !important;
  }
}

.custom-cursor {
  position: fixed;
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background: var(--gold);
  pointer-events: none;
  z-index: 99999;
  transform: translate(-50%, -50%);
  transition: width 0.3s, height 0.3s, background 0.3s, border 0.3s;
  box-shadow: 0 0 15px rgba(197, 160, 89, 0.6);
}

.custom-cursor.hovering {
  width: 60px;
  height: 60px;
  background: rgba(197, 160, 89, 0.1);
  border: 2px solid var(--gold);
  box-shadow: 0 0 30px rgba(197, 160, 89, 0.4);
}
</style>