from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

#Para testar é necessário alterar a porta no GitCodes de private para public na sessão PORTAS.
#curl -X POST https://localhost/webhook_app/webhook/ -H 'content-type: application/json' -d '{"title": "É o amor", "seconds": 305}'

@csrf_exempt  # Desabilita a proteção CSRF para requisições externas
def webhook(request):
    if request.method == "POST":
        try:
            # Tenta carregar os dados recebidos como JSON
            data = json.loads(request.body)
            print("Dados recebidos:", data)
            
            # Retorna uma resposta de sucesso
            return JsonResponse({"message": "Webhook recebido com sucesso!", "status": "OK"}, status=200)
        except json.JSONDecodeError:
            # Retorna um erro se os dados não forem JSON válidos
            return JsonResponse({"message": "Dados inválidos, formato JSON esperado.", "status": "Error"}, status=400)
    else:
        # Retorna um erro se o método não for POST
        return JsonResponse({"message": "Método não permitido, use POST.", "status": "Error"}, status=405)
