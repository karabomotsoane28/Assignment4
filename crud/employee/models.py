from django.db import models  
class Employee(models.Model):  
    eid = models.AutoField(primary_key=True)  
    ename = models.CharField(max_length=100) 
    econtact = models.CharField(max_length=10000) 

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"  