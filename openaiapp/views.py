from django.shortcuts import render

# Create your views here.

# app_name/views.py

import openai
from django.http import JsonResponse

### Start keyvault
#from azure.identity import DefaultAzureCredential
#from azure.keyvault.secrets import SecretClient

#vault_url = "https://ma-app-test-key.vault.azure.net/"
#credential = DefaultAzureCredential()

#client = SecretClient(vault_url=vault_url, credential=credential)

#openai_api_key = client.get_secret("OPENAI-API-KEY").value
#### End keyvault

def get_openai_response(request):
    user_input = request.GET.get('prompt', '')
    openai.api_key = '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'  # Later, move this to a secure location like environment variables
    #openai_api_key = client.get_secret("OPENAI-API-KEY").value

    response = openai.Completion.create(
      model="text-davinci-002",
      prompt=user_input,
      max_tokens=100
    )

    return JsonResponse({"response": response.choices[0].text.strip()})

