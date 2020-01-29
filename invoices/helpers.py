import csv
import os
import json
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from invoices.serializers import InvoiceSerializer
from invoices.serializers import FileSerializer
from invoices.serializers import ListFileSerializer

def validate_headers(headers):
    return headers == settings.AVAILABLE_HEADERS

def process_csv(path, filename):
    errors = []
    total = 0
    result = (True, errors)

    file_serializer = FileSerializer(data={'filename': filename, 'total_items_price': 0})

    if file_serializer.is_valid():
        file = file_serializer.save()

        #TODO: create logic to change the delimiter.
        with open(path, mode='r', encoding='utf-8-sig') as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            line_count = 0

            for row in reader:
                if line_count == 0:
                    if not validate_headers(row):
                        result = (False, 'Wrong Headers')
                        break
                    line_count += 1
                else:
                    try:
                        line_count += 1
                        invoice_data = {
                            'invoice_number': row[0],
                            'client_name': row[1],
                            'client_lastname': row[2],
                            'client_id': row[3],
                            'item_code': row[4],
                            'item_description': row[5],
                            'item_amount': row[6],
                            'item_price': row[7],
                            'item_discount_rate': row[8],
                            'file': file.id
                        }

                        invoice_serializer = InvoiceSerializer(data=invoice_data)
                        if invoice_serializer.is_valid():
                            invoice_serializer.save()
                            total = total + float(row[7])
                        else:
                            errors.append(
                                {
                                'error_line': line_count,
                                'error_description': 'The file ' + filename + ' is corrupt, validate file on line ' + str(line_count),
                                'error_capturated':invoice_serializer.errors
                                }
                            )

                    except IndexError:
                        result = (False, 'Index error, validate the delimiter of the CSV must be ;')
                        break
                    except Exception as e:
                        result = (False, 'The file ' + filename + ' is corrupt, validate file on line ' + str(line_count) + '. Error capturated: ' + str(e))
                        break

        file.total_items_price = total
        file.save()

        os.remove(path)

        if result[0]:
            serialized_result = ListFileSerializer(file)
            content_result = json.loads(JSONRenderer().render(serialized_result.data))
            result = (True, errors, content_result)

        return result

    os.remove(path)
    return (False, 'File corrupt')