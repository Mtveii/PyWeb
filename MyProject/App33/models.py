from django.db import models

# Create your models here.
# Моделі - це класи, призначені для відображення на базу даних
# є "представниками" таблиць у БД
class User(models.Model) :                         # в моделях ID створюється автоматично 
    first_name = models.CharField(max_length=64)   # і не вимагає явного оголошення.
    last_name  = models.CharField(max_length=64)   # SQL-аналог: name VARCHAR(64) 
    email      = models.CharField(max_length=128)
    phone      = models.CharField(max_length=16)    
    birthdate  = models.DateField(null=True)  



class Role(models.Model) :
    name         = models.CharField(max_length=32)     # опис ролі, очікується, що відповідає посаді співробітника
    create_level = models.IntegerField(default=0)      # Рівень доступу
    read_level   = models.IntegerField(default=0)      # до секретних даних
    update_level = models.IntegerField(default=0)      # з відповідними 
    delete_level = models.IntegerField(default=0)      # операціями

    def __str__(self):
        return f"{self.name} ({self.create_level},{self.read_level},{self.update_level},{self.delete_level})"


class Access(models.Model) :
    user  = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    role  = models.ForeignKey(Role, on_delete=models.DO_NOTHING)

    login = models.CharField(max_length=32)   
    
    salt  = models.CharField(max_length=32)    
    dk    = models.CharField(max_length=32)    

# ---------дз -----------
class AccessLog(models.Model) :
    datetime    = models.DateTimeField(auto_now_add=True) 
    access      = models.ForeignKey(Access, on_delete=models.CASCADE)  
    status_code = models.IntegerField()  
    
    def __str__(self):
        return f"{self.datetime.strftime('%Y-%m-%d %H:%M:%S')} - {self.access.login} - {self.status_code}"
# ---------дз -----------

'''
Д.З. Реалізувати представлення моделі користувача у панелі адміністратора
при відображенні його як посилання (у таблиці Access) замість 
"User object (2)" як "Name(id=2)LastName"
До звіту з ДЗ додати скріншот адмін сторінки на таблиці Access
'''