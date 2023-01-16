from django.db import models


from django.db import models
from django.contrib.auth.models import User




class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    department = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    address = models.TextField()
    def __str__(self):
        return self.nom
   

class LeaveRequest(models.Model):
    TYPES_OF_LEAVE = (
        ('Conge Malade', 'Conge Malade'),
        ('Conge Pro', 'Conge Pro'),
        ('Urgence Conge', 'Urgence Conge'),
        ('Conge Impaye', 'Conge Impaye '),
    )
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    type_of_leave = models.CharField(max_length=50, choices=TYPES_OF_LEAVE)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, default='pending')
    reason = models.TextField()
    # def __str__(self):
    #     return self.employee
