'''
All methods functions used
.add_page()--> orentation(P and L) format(letter A4 Legal size(100,200)) rotation()
.image()-->  name:(path of the image) position:(x= and y=) size(w= and h=) type("JPG", "JPEG", "PNG", "GIF", or "BMP".) link=
.set_font()--> family= style=(B I U) size=
.ln()--> sets cursor position
.cell()--> (width=, height=0, txt='', border=0(B L R T), ln=0, align=''(L C R), fill=False, link='')
.output()-->  




'''






from fpdf import FPDF #importing the library fpdf

#creating instance of FPDF() using variable pdf
pdf=FPDF()
pdf.add_page() # adding page using .add_page()
pdf.image("C:/Users/malit/OneDrive/Desktop/Question Generator/1589876919phpRBpsH0-removebg-preview.png",x=80, y=10, w=50, link="https://www.google.com")
pdf.set_font(family="Arial",style="B",size=9)#setting font for the pdf using .set_font() function with "Family,Style(B,I,U),Size"
pdf.ln(16)#placing cursor to line 16 below the image
pdf.cell(0,h=5,txt="March 2023 ",align="C",border="TLR",ln=1)#creating cell here width is set to 0 to cover whole horizontal plane on the page
#height, text to display, align(L C R), Border Positions(T L R B), ln sets cursor to next line, ln=2 will set cursor to 2nd line from the cell

pdf.cell(0,h=5,txt="Examination: End Semester -IV Examination (UG Programmes)",align="C",border="BLR",ln=1)

pdf.cell(w=0,h=5,txt="Programme code: 11",border="LR",ln=1)
pdf.cell(w=0,h=5,txt="Programme: Bsc. (hons)",border="LBR",ln=1)

pdf.cell(w=97.5,h=10,txt="Name of the Constituent College: S K Somaiya College (SKSC)",border="LB")

pdf.cell(w=92.5,h=10,txt="Name of the department/section/center: Computer Science",border="LBR",ln=1)

pdf.cell(w=50,h=10,txt="Duration: 2 Hr",border="LB")
pdf.cell(w=70,h=10,txt="Name of Course: Internet of Things",border="LB")
pdf.cell(w=70,h=10,txt="Max. Marks: 60",border="LRB", ln=1)

pdf.cell(0,h=3,txt="Instructions:",border="LR",ln=1)
pdf.cell(0,h=3,txt="i) All Questions are Compulsory",border="LR",ln=1)
pdf.cell(0,h=3,txt="ii)Draw diagrams Whereever necessary",border="LR",ln=1)
pdf.cell(0,h=3,txt="iii)Figures to right indicate full marks.",border="LRB",ln=1)

pdf.cell(0,h=5,border=False,ln=1)

pdf.cell(w=175,h=5,txt="Questions",border="TLR")
pdf.cell(w=15,h=5,txt="Marks",border="TLR",align="C",ln=1)
pdf.cell(w=175,h=180,border=1)
pdf.cell(w=15,h=180,border="TRB")


pdf.output("Question Paper Template.pdf")