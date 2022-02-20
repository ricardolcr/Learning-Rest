from rest_framework import serializers
from desafio.ip.models import IpInfo

#Cria a serialização do modelo IpInfo
class IpInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = IpInfo
		fields = ['status', 'country', 'countryCode', 'region',
		'regionName', 'city', 'zip', 'lat', 'lon', 'timezone',
		'isp', 'org', 'asn', 'query', 'consulted']