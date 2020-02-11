import logging

import azure.functions as func

def main(message: func.ServiceBusMessage):

    value = message.get_body().decode('utf-8')
    logging.info('Message: %s', value)
