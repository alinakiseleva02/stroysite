document.addEventListener('DOMContentLoaded', function() {

    const allProjects = window.allProjects || [];
    const projectsGrid = document.getElementById('projectsGrid');
    const searchInput = document.getElementById('searchInput');
    const searchButton = document.getElementById('searchButton');
    const searchResultsInfo = document.getElementById('searchResultsInfo');
    const foundCountSpan = document.getElementById('foundCount');
    const totalCountSpan = document.getElementById('totalCount');
    const clearSearchBtn = document.getElementById('clearSearch');
    

    function displayProjects(projects) {
        if (!projectsGrid) return;
        
        if (projects.length === 0) {
            projectsGrid.innerHTML = `
                <div class="empty-state">
                    <div class="empty-icon">
                        <i class="fas fa-search"></i>
                    </div>
                    <h3>Проекты не найдены</h3>
                    <p>Попробуйте изменить поисковый запрос</p>
                    <button onclick="clearSearch()" class="btn btn-primary">
                        Показать все проекты
                    </button>
                </div>
            `;
            return;
        }
        
        let html = '';
        projects.forEach(project => {
            html += createProjectCard(project);
        });
        projectsGrid.innerHTML = html;

        if (searchResultsInfo && foundCountSpan) {
            if (projects.length !== allProjects.length) {
                searchResultsInfo.style.display = 'flex';
                foundCountSpan.textContent = projects.length;
            } else {
                searchResultsInfo.style.display = 'none';
            }
        }
    }

    function createProjectCard(project) {
        const imageHtml = project.image 
            ? `<img src="${project.image}" alt="${project.name}" class="project-img">`
            : `<div class="placeholder-text">
                <i class="fas fa-home"></i>
                <span>Изображение проекта</span>
               </div>`;
        
        return `
            <a href="/projects/${project.id}" class="project-card-link">
                <div class="project-card">
                    <div class="project-image">
                        ${imageHtml}
                        <div class="project-overlay">
                            <span>Подробнее <i class="fas fa-arrow-right"></i></span>
                        </div>
                    </div>
                    
                    <div class="project-content">
                        <div class="project-header">
                            <h3>${escapeHtml(project.name)}</h3>
                        </div>
                        
                        <div class="project-details">
                            <div class="detail-row">
                                <i class="fas fa-building"></i>
                                <span><strong>Заказчик:</strong> ${escapeHtml(project.customer.company_name)}</span>
                            </div>
                            <div class="detail-row">
                                <i class="fas fa-user-tie"></i>
                                <span><strong>Ответственный:</strong> ${escapeHtml(project.employee.full_name)}</span>
                            </div>
                            <div class="detail-row">
                                <i class="fas fa-money-bill-wave"></i>
                                <span><strong>Бюджет:</strong> ${project.formatted_budget}</span>
                            </div>
                            <div class="detail-row">
                                <i class="fas fa-calendar-alt"></i>
                                <span><strong>Срок:</strong> ${project.formatted_construction_period}</span>
                            </div>
                            <div class="detail-row">
                                <i class="fas fa-calendar-check"></i>
                                <span><strong>Начало:</strong> ${project.formatted_start_date}</span>
                            </div>
                        </div>
                        
                        ${project.description ? `
                            <div class="project-description">
                                <p>${escapeHtml(truncateText(project.description, 150))}</p>
                            </div>
                        ` : ''}
                        
                        <div class="project-footer">
                            <span class="click-hint">Нажмите для просмотра деталей</span>
                        </div>
                    </div>
                </div>
            </a>
        `;
    }

    function searchProjects(query) {
        if (!query.trim()) {
            return allProjects;
        }
        
        const searchLower = query.toLowerCase().trim();
        
        return allProjects.filter(project => {
            return (
                (project.name && project.name.toLowerCase().includes(searchLower)) ||
                (project.description && project.description.toLowerCase().includes(searchLower)) ||
                (project.customer && project.customer.company_name && 
                 project.customer.company_name.toLowerCase().includes(searchLower)) ||
                (project.employee && project.employee.full_name && 
                 project.employee.full_name.toLowerCase().includes(searchLower))
            );
        });
    }

    function handleSearch() {
        const query = searchInput.value;
        const filteredProjects = searchProjects(query);
        displayProjects(filteredProjects);
        const url = new URL(window.location);
        if (query) {
            url.searchParams.set('search', query);
        } else {
            url.searchParams.delete('search');
        }
        window.history.pushState({}, '', url);
    }

    window.clearSearch = function() {
        searchInput.value = '';
        displayProjects(allProjects);
        searchResultsInfo.style.display = 'none';
        const url = new URL(window.location);
        url.searchParams.delete('search');
        window.history.pushState({}, '', url);
    };

    function escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    function truncateText(text, length) {
        if (!text) return '';
        return text.length > length ? text.substring(0, length) + '...' : text;
    }

    if (totalCountSpan) {
        totalCountSpan.textContent = allProjects.length;
    }
    displayProjects(allProjects);

    const urlParams = new URLSearchParams(window.location.search);
    const searchParam = urlParams.get('search');
    if (searchParam && searchInput) {
        searchInput.value = searchParam;
        handleSearch();
    }
    if (searchButton) {
        searchButton.addEventListener('click', handleSearch);
    }
    
    if (searchInput) {
        searchInput.addEventListener('keyup', function(e) {
            if (e.key === 'Enter') {
                handleSearch();
            }
        });
        
        let timeout = null;
        searchInput.addEventListener('input', function() {
            clearTimeout(timeout);
            timeout = setTimeout(handleSearch, 300); 
        });
    }
    
    if (clearSearchBtn) {
        clearSearchBtn.addEventListener('click', function(e) {
            e.preventDefault();
            clearSearch();
        });
    }
});