import './assets/main.css'
import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index.js' // Убедитесь, что путь правильный

const app = createApp(App)
app.use(router)
app.mount('#app')