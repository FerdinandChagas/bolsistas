from django.db.models import Manager

from frequencias.models import Projeto

from bolsistas.users import models

class ProReitorManager(Manager):
    
    def create(self, matricula, nome, email, username, password, project_id, campus_id):
        new_user = models.User.objects.create_user(
            matricula=matricula,
            username=username,
            name=nome,
            email=email
        )
        new_user.set_password(password)
        new_user.save()

        project = models.Projeto.objects.get(id=project_id)
        campus = models.Campus.objects.get(id=campus_id)
        bolsista = super().create(user=new_user, projeto=project, campus=campus)
        return bolsista

class CoodenadorManager(Manager):
    
    def create(self, matricula, nome, email, username, password, project_id, campus_id):
        new_user = models.User.objects.create_user(
            matricula=matricula,
            username=username,
            name=nome,
            email=email
        )
        new_user.set_password(password)
        new_user.save()

        project = models.Projeto.objects.get(id=project_id)
        campus = models.Campus.objects.get(id=campus_id)
        bolsista = super().create(user=new_user, projeto=project, campus=campus)
        return bolsista

class OrientadorManager(Manager):
    
    def create(self, matricula, nome, email, username, password, project_id, campus_id):
        new_user = models.User.objects.create_user(
            matricula=matricula,
            username=username,
            name=nome,
            email=email
        )
        new_user.set_password(password)
        new_user.save()

        project = models.Projeto.objects.get(id=project_id)
        campus = models.Campus.objects.get(id=campus_id)
        bolsista = super().create(user=new_user, projeto=project, campus=campus)
        return bolsista

class BolsistaManager(Manager):
    
    def create(self, matricula, nome, email, username, password, project_id, campus_id):
        new_user = models.User.objects.create_user(
            matricula=matricula,
            username=username,
            name=nome,
            email=email
        )
        new_user.set_password(password)
        new_user.save()

        project = models.Projeto.objects.get(id=project_id)
        campus = models.Campus.objects.get(id=campus_id)
        bolsista = super().create(user=new_user, projeto=project, campus=campus)
        return bolsista

