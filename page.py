from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import json

with open('data_to_json.json', 'r') as file:
    data = json.load(file)

pdf_canvas = canvas.Canvas('output.pdf', pagesize=letter)
width, height = letter


page_elements = data.get('page', {}).get('elements', [])

for element in page_elements:
    if element['type'] == 'text':
        content = element.get('content', '')
        x = element['position']['x']
        y = element['position']['y']
        pdf_canvas.drawString(x, height - y, content)
    elif element['type'] == 'rectangle':
        x = element['position']['x']
        y = height - element['position']['y'] - element['size']['height']
        width = element['size']['width']
        height = element['size']['height']
        pdf_canvas.rect(x, y, width, height)

pdf_canvas.save()
