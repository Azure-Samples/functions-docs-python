import logging

import azure.functions as func


def main(msg: func.QueueMessage) -> None:

    value = msg.get_body().decode('utf-8')

    logging.info('Python queue trigger function processed a queue item: %s', value)
