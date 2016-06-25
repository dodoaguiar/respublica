from django.db import models

# Create your models here.

class ResultadoIdeb(models.Model):
	id = models.AutoField(primary_key=True)
	nome = models.CharField(verbose_name="Nome da Escola", max_length=500)
	data = models.DateField(verbose_name='Data', auto_now=False, auto_now_add=False, blank = True, null=True)
	resultado = models.DecimalField(verbose_name="Resultado Observado", max_digits=8 , decimal_places=5, blank=True, null=True)
	meta = models.DecimalField(verbose_name="Meta Projetado", max_digits=8 , decimal_places=5, blank=True, null=True)
	
	def __str__(self):
		return self.nome
	
	class Meta():
		verbose_name = "Resultado da Tabela"
		verbose_name_plural = "Resultado da Tabelas"
		ordering = ['nome']