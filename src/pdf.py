from fpdf import FPDF

def imprimepdf():
    pdf = FPDF('P', 'mm', 'A4')
    pdf.add_page()

    pdf.set_font('Times', 'B', 16)
    pdf.cell(190, 10, 'REPORTE FRANQUICIA', 1, 1, align = 'C')
    pdf.set_font('Times', 'B',14)
    pdf.text(90, 30, 'Actual Plantilla')
    pdf.image('output/graficos/roster_equipo.png',x=10, y=30, w=190, h=100)
    pdf.image('output/graficos/dist_jug_pais.png',x=30, y=110, w=70, h=70)
    pdf.set_font('Times', '',8)
    pdf.text(135, 115, 'USO DE LA PLANTILLA')
    pdf.image('output/graficos/uso_plantilla.png',x=112, y=125, w=90, h=100)
    pdf.image('output/graficos/pct_tiro.png',x=20, y=190, w=90, h=90)
    pdf.set_font('Times', '',8)
    pdf.image('output/graficos/est_jug_equipo.png',x=112, y=155, w=90, h=100)

    pdf.output('output/report.pdf', 'F')