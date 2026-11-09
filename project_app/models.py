from django.db import models

class Employees(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    position = models.CharField(max_length=50, verbose_name='Должность')
    department = models.CharField(max_length=50, verbose_name='Отдел')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Зарплата')
    hire_date = models.DateField(verbose_name='Дата приема на работу')
    
    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
    
    def __str__(self):
        return self.full_name

class Customers(models.Model):
    company_name = models.CharField(max_length=100, verbose_name='Название компании')
    contact_person = models.CharField(max_length=100, verbose_name='Контактное лицо')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    email = models.EmailField(verbose_name='Электронная почта')
    
    class Meta:
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'
    
    def __str__(self):
        return self.company_name

class Materials(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название материала')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена за единицу')
    available_quantity = models.IntegerField(verbose_name='Доступное количество')
    
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Материалы'
    
    def __str__(self):
        return self.name 

class Projects(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название проекта')
    construction_period = models.IntegerField(verbose_name='Срок строительства')
    budget = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Бюджет')
    start_date = models.DateField(verbose_name='Дата приема в работу')
    employee = models.ForeignKey(Employees, on_delete=models.PROTECT, verbose_name='Сотрудник')
    customer = models.ForeignKey(Customers, on_delete=models.PROTECT, verbose_name='Заказчик')
    image = models.ImageField(upload_to='projects/', verbose_name='Изображение проекта', blank=True, null=True)
    description = models.TextField(verbose_name='Описание проекта', blank=True)
    
    def formatted_budget(self):
        return f"{self.budget:,.0f}".replace(',', ' ') + ' руб.'
    
    def formatted_start_date(self):
        months = {1: 'января', 2: 'февраля', 3: 'марта', 4: 'апреля', 5: 'мая', 6: 'июня', 7: 'июля', 8: 'августа', 9: 'сентября', 10: 'октября', 11: 'ноября', 12: 'декабря'}
        return f"{self.start_date.day} {months[self.start_date.month]} {self.start_date.year} г."
    
    def formatted_construction_period(self):
        days = self.construction_period
        if days >= 30:
            months = days // 30
            remaining_days = days % 30
            if remaining_days > 0:
                return f"{months} мес. {remaining_days} дн."
            return f"{months} мес."
        return f"{days} дн."

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
    
    def __str__(self):
        return self.name

class Services(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость от')
    icon = models.CharField(max_length=50, verbose_name='Иконка (например, fa-home)', default='fa-building')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title

class Reviews(models.Model):
    client_name = models.CharField(max_length=100, verbose_name='Имя клиента')
    text = models.TextField(verbose_name='Текст отзыва')
    rating = models.IntegerField(verbose_name='Оценка (1-5)', default=5)
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f"Отзыв от {self.client_name}"

class ProjectImage(models.Model):
    project = models.ForeignKey(Projects, related_name='gallery', on_delete=models.CASCADE, verbose_name='Проект')
    image = models.ImageField(upload_to='projects/gallery/', verbose_name='Фотография')

    class Meta:
        verbose_name = 'Фотография галереи'
        verbose_name_plural = 'Галерея проекта'

    def __str__(self):
        return f"Фото для {self.project.name}"

class ContactRequest(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(verbose_name='Сообщение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата заявки')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки (Обратная связь)'

    def __str__(self):
        return f"Заявка от {self.name}"