import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, sendGridMessage: func.Out[str]) -> func.HttpResponse:

    value = "Sent from Azure Functions"

    message = {
        "personalizations": [ {
          "to": [{ 
            "email": "user@contoso.com"
            }]}],
        "subject": "Azure Functions email with SendGrid",
        "content": [{ 
            "type": "text/plain", 
            "value": value }]}
    
    sendGridMessage.set(json.dumps(message))

    return func.HttpResponse(f"Sent")
