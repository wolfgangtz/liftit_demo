from celery.decorators import task
from invoices.helpers import process_csv
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@task(name="async_process_csv")
def async_process_csv(path, filename, session_name):
    response = process_csv(path, filename)

    layer = get_channel_layer()
    async_to_sync(layer.group_send)('ws_'+str(session_name), {
        'type': 'send.response',
        'content': response
    })

    return None