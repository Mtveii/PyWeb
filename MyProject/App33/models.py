from django.db import models
from django.utils import timezone

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

    login = models.CharField(max_length=32)    # https://www.rfc-editor.org/rfc/rfc7617
    
    salt  = models.CharField(max_length=32)    # PKCS #5: Password-Based Cryptography
    dk    = models.CharField(max_length=32)    # https://datatracker.ietf.org/doc/html/rfc2898

# -------------------дз----------------
class AccessLog(models.Model):
    """Журнал доступу до сайту"""
    access_datetime = models.DateTimeField(default=timezone.now, verbose_name="Дата-час доступу")
    status_code = models.IntegerField(verbose_name="Статус відповіді сервера")
    
    def __str__(self):
        return f"{self.access_datetime.strftime('%Y-%m-%d %H:%M:%S')} - {self.status_code}"
    
    class Meta:
        verbose_name = "Журнал доступу"
        verbose_name_plural = "Журнали доступу"
        ordering = ['-access_datetime']
#---------------------------------------

'''
Д.З. Реалізувати представлення моделі користувача у панелі адміністратора
при відображенні його як посилання (у таблиці Access) замість 
"User object (2)" як "Name(id=2)LastName"
До звіту з ДЗ додати скріншот адмін сторінки на таблиці Access
'''