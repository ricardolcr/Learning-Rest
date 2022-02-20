from django.shortcuts import render
import requests
from desafio.ip.models import IpInfo
from desafio.ip.serializers import IpInfoSerializer
from django.http import JsonResponse

def home(request):
	#Tela inicial, conexão direta com o IP API
	ipData = {}
	
	if 'IP' in request.GET:
		
		IP = request.GET['IP'] #Pega o IP da caixa de texto
		
		searchURL = 'http://ip-api.com/json/%s' % IP
		response = requests.get(searchURL)
		
		ipData = response.json() #Pesquisa no IP API
		
		try:
			#Renomeia o campo 'as' para 'asn' para não
			#ter problema com palavra reservada 
			ipData['asn'] = ipData.pop('as')
			
			serializer = IpInfoSerializer(data=ipData)
		
			if serializer.is_valid():
				serializer.save() #Salva a pesquisa
		
		except KeyError:#Campo 'as' não existe, não salva
			pass

	return render(request, 'core/home.html', ipData)

def previous(request):
	#Pesquisas anteriores, fornece os JSONs com os dados
	#pesquisados anteriormente

	ipData = IpInfo.objects.all()
	serializer = IpInfoSerializer(ipData, many=True)
	
	#Retorna os dados como JSON
	return JsonResponse(serializer.data, safe=False)