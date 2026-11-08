<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const employees = ref([])
const teams = ref([]) 

onMounted(async () => {
  try {

    const resEmp = await axios.get('/api/employees/')
    employees.value = resEmp.data
    

    const resTeams = await axios.get('/api/teams/')
    teams.value = resTeams.data
  } catch (error) {
    console.error("Ошибка загрузки данных", error)
  }
})
</script>

<template>

  <div class="page-hero">
    <div class="container"><h1>Наша команда</h1></div>
  </div>
  
  <div class="container" style="padding-top: 60px;">
    <h2 class="section-title">Руководство и специалисты</h2>
    <div class="projects-grid">
      <div v-for="emp in employees" :key="emp.id" class="project-card" style="padding: 40px; text-align:center;">
        <div class="avatar-container">
          <img 
            v-if="emp.photo" 
            :src="emp.photo" 
            :alt="emp.full_name" 
            class="employee-photo"
          >
          <div v-else class="avatar-placeholder">
            {{ emp.full_name.charAt(0) }}
          </div>
        </div>
        <h3 style="font-size: 1.5rem; margin-bottom: 10px;">{{ emp.full_name }}</h3>
        <p style="color: var(--gold); text-transform: uppercase; letter-spacing: 1px; font-size: 0.85rem;">{{ emp.position }}</p>
      </div>
    </div>
  </div>

  <div class="teams-section">
    <div class="container">
      <h2 class="section-title" style="color: var(--white); margin-top: 80px;">Наши строительные бригады</h2>
      <p style="text-align: center; color: #999; margin-bottom: 50px;">Профессионалы, которые воплощают проекты в жизнь</p>
      
      <div class="projects-grid">
        <div v-for="team in teams" :key="team.id" class="project-card team-card">
          

          <div class="team-image">
            <img v-if="team.image" :src="team.image" :alt="team.specialty">
            <div v-else class="placeholder">YALI TEAM</div>
          </div>

          <div class="team-content">
            <h3 style="font-size: 1.4rem; margin-bottom: 15px;">{{ team.specialty }}</h3>
            
            <div class="team-info">
              <p><strong>Руководитель:</strong> {{ team.employee_name }}</p>
              <p><strong>Состав:</strong> {{ team.member_count }} человек</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>

.avatar-container {
  width: 140px;
  height: 140px;
  margin: 0 auto 25px;
  border-radius: 50%;
  overflow: hidden;
  border: 3px solid var(--gold);
  box-shadow: 0 10px 25px rgba(197, 160, 89, 0.2);
}
.employee-photo {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center top;
}
.avatar-placeholder {
  width: 100%;
  height: 100%;
  background: var(--light);
  color: var(--gold);
  font-size: 3.5rem;
  font-family: var(--font-heading);
  display: flex;
  align-items: center;
  justify-content: center;
}


.section-title {
  font-size: 2.5rem;
  color: var(--dark);
  text-align: center;
  margin-bottom: 40px;
  font-family: var(--font-heading);
}

.teams-section {
  background: var(--dark-gray); 
  padding: 80px 0 120px;
  margin-top: 80px;
  border-top: 4px solid var(--gold);
}

.team-card {
  background: var(--white);
  border: none;
  overflow: hidden;
}

.team-image {
  height: 250px;
  width: 100%;
  overflow: hidden;
  position: relative;
  background: #222;
}

.team-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.6s ease;
}

.team-card:hover .team-image img {
  transform: scale(1.08);
}

.placeholder {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--gold);
  font-family: var(--font-heading);
  font-size: 1.5rem;
  letter-spacing: 3px;
}

.team-content {
  padding: 30px;
}

.team-info p {
  color: var(--text-muted);
  font-size: 0.95rem;
  margin-bottom: 8px;
}

.team-info strong {
  color: var(--dark);
  font-weight: 600;
}
</style>