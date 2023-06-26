from django.db.models import Manager

from frequencias.models import Projeto

from bolsistas.users import models

class ProReitorManager(Manager):
    
    def create(self, matricula, name, email, username, password, inicio_m, fim_m):
        new_user = models.User.objects.create_user(
            matricula=matricula,
            username=username,
            name=name,
            email=email
        )
        new_user.set_password(password)
        new_user.save()

        proreitor = super().create(user=new_user, inicio_m=inicio_m, fim_m=fim_m)
        return proreitor

class CoodenadorManager(Manager):
    
    def create(self, matricula, nome, email, username, password, campus_id):
        new_user = models.User.objects.create_user(
            matricula=matricula,
            username=username,
            name=nome,
            email=email
        )
        new_user.set_password(password)
        new_user.save()

        campus = models.Campus.objects.get(id=campus_id)
        coordenador = super().create(user=new_user, campus=campus)
        return coordenador

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
        orientador = super().create(user=new_user, projeto=project, campus=campus, situacao="ATIVO")
        return orientador

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

