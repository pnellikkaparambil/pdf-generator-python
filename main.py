# from reportlab.lib.pagesizes import A1
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from reportlab.platypus import Frame, PageTemplate, Paragraph, Table, TableStyle,Image
# # from functools import partial
# from reportlab.platypus.doctemplate import SimpleDocTemplate
# from reportlab.lib.pagesizes import A1
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.lib import colors
# from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Frame, Paragraph
# from reportlab.lib.units import inch


# cm = 2.58
# styles = getSampleStyleSheet()

# data = [["Register","S.No.", "PON","Description","Quantity","Cost","Supplier","DOR","RVN","Alloted Lab",
# "TON","TOD","Transferred Dept./Lab","Remarks"],
#      ["Register REG1", 12, 10, Paragraph('database', styles['Normal']), 4,"4466561", "SHAKTI", "2021-09-05", 778, "Iron Man Lab", 4566, "2021-09-04", "Tony Stark Lab", "This is the remark for REG1"]]

# for i in range(0,6):
#     data.extend(data)

# table = Table(data, repeatRows=1)

# # add style

# numberofcols = len(data[0])

# # 3) Add borders -- formatting
# ts = TableStyle(
#     [
#     ('BOX',(0,0),(-1,-1),2,colors.black),
#     ('LINEBEFORE',(2,1),(2,-1),2,colors.red),

#     ('GRID',(0,1),(-1,-1),2,colors.black),
#     ]
# )
# table.setStyle(ts)

# # Create a frame for the rectangle

# elems = []

# # Add the table to the elements list
# elems.append(table)


# story = []
#     # Initialise the simple document template
# doc = SimpleDocTemplate(f"blog.pdf",
#                             page_size=A4,
#                             bottomMargin=.4 * inch,
#                             topMargin=.4 * inch,
#                             rightMargin=.8 * inch,
#                             leftMargin=.8 * inch)
# # set the font style
# styles = getSampleStyleSheet()
# styleN = styles['Normal']

# image = Image("./assets/download.png", 1 * inch, 1 * inch, hAlign='LEFT')
# story.append(image)


# # Define a PageTemplate and add the frame to it
# # page_template = PageTemplate(id='main', frames=[frame])
# # doc.addPageTemplates(page_template)

# # Build the document with elements
# doc.build(story)
# doc.build(elems)
