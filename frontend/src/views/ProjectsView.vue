<script setup>
import { ref, computed, onMounted } from 'vue'
import axios from 'axios'

const projects = ref([])
const employees = ref([])
const customers = ref([])
const searchQuery = ref('')
const form = ref({ id: null, name: '', budget: 0, construction_period: 30, start_date: '', employee: null, customer: null, description: '' })
const isEditing = ref(false)

const fetchData = async () => {
  try {
    const [resProj, resEmp, resCust] = await Promise.all([
      axios.get('http://127.0.0.1:8000/api/projects/'),
      axios.get('http://127.0.0.1:8000/api/employees/'),
      axios.get('http://127.0.0.1:8000/api/customers/')
    ])
    projects.value = resProj.data
    employees.value = resEmp.data
    customers.value = resCust.data
  } catch (error) { console.error("Ошибка API", error) }
}
onMounted(() => fetchData())

const filteredProjects = computed(() => {
  if (!searchQuery.value) return projects.value
  const q = searchQuery.value.toLowerCase()
  return projects.value.filter(p => p.name.toLowerCase().includes(q))
})

const saveProject = async () => {
  try {
    if (isEditing.value) {
      await axios.patch(`http://127.0.0.1:8000/api/projects/${form.value.id}/`, form.value)
    } else {
      await axios.post('http://127.0.0.1:8000/api/projects/', form.value)
    }
    resetForm(); fetchData()
  } catch (error) { alert("Ошибка! Проверьте поля.") }
}

const deleteProject = async (id) => {
  if (confirm('Вы уверены, что хотите удалить проект?')) {
    await axios.delete(`http://127.0.0.1:8000/api/projects/${id}/`)
    fetchData()
  }
}

const editProject = (p) => { form.value = { ...p }; isEditing.value = true; window.scrollTo(0, 0) }
const resetForm = () => { form.value = { id: null, name: '', budget: 0, construction_period: 30, start_date: '', employee: null, customer: null, description: '' }; isEditing.value = false }
</script>

<template>
  <div class="page-hero">
    <div class="container">
      <h1>Наши проекты</h1>
    </div>
  </div>

  <div class="container">
    
    <div class="admin-form">
      <h3>{{ isEditing ? 'Редактировать проект' : 'Добавить проект' }}</h3>
      <form @submit.prevent="saveProject">
        <input v-model="form.name" type="text" placeholder="Название проекта" required>
        <input v-model="form.budget" type="number" placeholder="Бюджет (руб.)" required>
        <input v-model="form.construction_period" type="number" placeholder="Срок (дней)" required>
        <input v-model="form.start_date" type="date" required>
        
        <select v-model="form.employee" required>
          <option :value="null" disabled>Ответственный архитектор</option>
          <option v-for="e in employees" :key="e.id" :value="e.id">{{ e.full_name }}</option>
        </select>
        <select v-model="form.customer" required>
          <option :value="null" disabled>Заказчик</option>
          <option v-for="c in customers" :key="c.id" :value="c.id">{{ c.company_name }}</option>
        </select>
        
        <textarea v-model="form.description" placeholder="Краткое описание проекта"></textarea>
        
        <button type="submit" class="search-button">{{ isEditing ? 'Сохранить изменения' : 'Создать проект' }}</button>
        <button type="button" v-if="isEditing" @click="resetForm" class="btn-delete" style="margin-left: 15px;">Отмена</button>
      </form>
    </div>

    <div class="search-input-group">
      <input v-model="searchQuery" type="text" placeholder="Поиск по названию...">
    </div>

    <div class="projects-grid">
      <div v-for="p in filteredProjects" :key="p.id" class="project-card">
        <div class="project-image">
           <img v-if="p.image" :src="p.image" :alt="p.name">
           <div v-else style="background:#1E1E1E; height:100%; display:flex; align-items:center; justify-content:center; color:#C5A059;">YALI</div>
        </div>
        <div class="project-content">
          <h3>{{ p.name }}</h3>
          <p><strong>Заказчик:</strong> {{ p.customer_details?.company_name }}</p>
          <p><strong>Бюджет:</strong> {{ p.formatted_budget }}</p>
          <p><strong>Срок:</strong> {{ p.formatted_construction_period }}</p>
          
          <div style="margin-top: auto; padding-top: 20px;">
            <button @click="editProject(p)" class="btn-edit">Изменить</button>
            <button @click="deleteProject(p.id)" class="btn-delete">Удалить</button>
            <RouterLink :to="`/projects/${p.id}`" style="display:block; margin-top:15px; color: #C5A059; text-decoration:none; font-weight:600; text-transform:uppercase; font-size:0.85rem; letter-spacing:1px;">Подробнее →</RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>