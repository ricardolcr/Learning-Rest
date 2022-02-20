from django.db import models

#Criação do modelo com os campos do JSON para salvar no Banco
class IpInfo(models.Model):
	status = models.CharField(max_length=15, default='')
	country = models.CharField(max_length=30, blank=True, default='')
	countryCode = models.CharField(max_length=2, default='')
	region = models.CharField(max_length=2, default='')
	regionName = models.CharField(max_length=30, default='')
	city = models.CharField(max_length=30, default='')
	zip = models.CharField(max_length=10, default='')
	lat = models.CharField(max_length=10, default='')
	lon = models.CharField(max_length=10, default='')
	timezone = models.CharField(max_length=25, default='')
	isp = models.CharField(max_length=50, default='')
	org = models.CharField(max_length=50, default='')
	asn = models.CharField(max_length=50, default='')
	query = models.CharField(max_length=15, default='')
	consulted = models.DateTimeField(auto_now_add=True)
	
	class Meta:
		ordering = ['consulted']