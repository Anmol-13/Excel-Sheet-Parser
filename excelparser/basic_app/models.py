from django.db import models

class Address(models.Model):
    Instruction_ID = models.CharField(max_length=30)
    Case_Ref_No = models.CharField(max_length=30)
    Client_Name = models.CharField(max_length=30)
    Candidate_Name = models.CharField(max_length=30)
    Complete_Address = models.CharField(max_length=100)
    Period_of_Stay = models.DateField(null=True)


    def __str__(self):
        return self.Instruction_ID
