from reportlab.lib.pagesizes import A1
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Table, TableStyle
# from functools import partial
from reportlab.platypus.doctemplate import SimpleDocTemplate
from reportlab.graphics.charts import barcharts
from reportlab.graphics.shapes import Drawing,Rect
from reportlab.lib.pagesizes import A1
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Frame, Paragraph
from reportlab.lib.units import inch

drawing = Drawing(400, 200)

cm = 2.58
styles = getSampleStyleSheet()

data = [["Register","S.No.", "PON","Description","Quantity","Cost","Supplier","DOR","RVN","Alloted Lab",
"TON","TOD","Transferred Dept./Lab","Remarks"],
    ["Register REG1", 12, 56, Paragraph('database', styles['Normal']), 4,"4466561", "SHAKTI", "2021-09-05", 778, "Iron Man Lab", 4566, "2021-09-04", "Tony Stark Lab", "This is the remark for REG1"]]

for i in range(0,6):
    data.extend(data)

doc = SimpleDocTemplate('testtable.pdf', pagesize=A1)

table = Table(data, repeatRows=1)

# add style

numberofcols = len(data[0])


# style = TableStyle([
#     ('BACKGROUND', (0,0), (numberofcols,0), colors.blue),
#     ('TEXTCOLOR',(0,0),(-1,0),colors.black),
#     ('ALIGN',(0,0),(-1,-1),'CENTER'),
#     ('FONTNAME', (0,0), (-1,0), 'Courier-Bold'),
#     ('FONTSIZE', (0,0), (-1,0), 14),
#     ('BOTTOMPADDING', (0,0), (-1,0), 12),
#     ('BACKGROUND',(0,1),(-1,-1),colors.beige),
# ])
# table.setStyle(style)


# 2) Alternate backgroud color -- formatting
# rowNumb = len(data)
# for i in range(1, rowNumb):
#     if i % 2 == 0:
#         bc = colors.burlywood
#     else:
#         bc = colors.beige
    
#     ts = TableStyle(
#         [('BACKGROUND', (0,i),(-1,i), bc)]
#     )
#     table.setStyle(ts)

# 3) Add borders -- formatting 
ts = TableStyle(
    [
    ('BOX',(0,0),(-1,-1),2,colors.black),
    ('LINEBEFORE',(2,1),(2,-1),2,colors.red),
    
    ('GRID',(0,1),(-1,-1),2,colors.black),
    ]
)
table.setStyle(ts)

# Create a frame for the rectangle
frame_width = 400  # Width of the frame
frame_height = 200  # Height of the frame
frame = Frame(inch, inch, frame_width, frame_height, showBoundary=1)  # Adjust the position as needed

elems = []

# Add the rectangle drawing to the elements list
elems.append(drawing)

# Add the table to the elements list
elems.append(table)

doc = SimpleDocTemplate('testtable.pdf', pagesize=A1)

# Define a PageTemplate and add the frame to it
page_template = PageTemplate(id='main', frames=[frame])
doc.addPageTemplates(page_template)

# Build the document with elements
doc.build(elems)
