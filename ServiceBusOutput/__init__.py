import logging
import azure.functions as func

def main(req: func.HttpRequest, message: func.Out[str]) -> func.HttpResponse:

    value = req.params.get('message')
    message.set(value)
    return 'Message sent'
