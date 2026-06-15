from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# ВАЖНО: скачай DejaVuSans.ttf и положи рядом
pdfmetrics.registerFont(TTFont("DejaVu", "DejaVuSans.ttf"))

styles = getSampleStyleSheet()
for s in styles.byName.values():
    s.fontName = "DejaVu"

def box(title, content):
    return Table([
        [Paragraph(f"<b>{title}</b>", styles['Heading3'])],
        [Paragraph(content, styles['Normal'])]
    ], colWidths=[450],
    style=[
        ('BOX', (0,0), (-1,-1), 1, colors.black),
        ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ('INNERPADDING', (0,0), (-1,-1), 8),
    ])

doc = SimpleDocTemplate("Maksim_Ivanouski1_CV.pdf", pagesize=A4)

story = []

story.append(box("Maksim Ivanouski", "Poznań | 507 306 953 | ivanouskimaksim@gmail.com"))
story.append(Spacer(1,12))

story.append(box("Podsumowanie zawodowe",
"Student informatyki z zainteresowaniem obszarem systemów IT i administracji. "
"Posiadam podstawową wiedzę z zakresu systemów operacyjnych (Windows Server, Linux), baz danych oraz sieci komputerowych. "
"Interesuję się utrzymaniem i rozwojem systemów IT oraz analizą i rozwiązywaniem problemów technicznych. "
"Szybko się uczę i chcę rozwijać się w kierunku administracji systemami"))

story.append(Spacer(1,12))

story.append(box("Wykształcenie",
"Collegium Da Vinci<br/>Kierunek: Informatyka<br/>Status: Student 1 roku"))

story.append(Spacer(1,12))

story.append(box("Kompetencje techniczne",
"• Systemy operacyjne: Windows Server, Linux (podstawy administracji)<br/>"
"• Bazy danych: PostgreSQL – podstawy (zapytania SQL, konfiguracja)<br/>"
"• Podstawy sieci LAN (TCP/IP, DNS, DHCP)<br/>"
"• Microsoft Office 365<br/>"))

story.append(Spacer(1,12))

story.append(box("Kompetencje miękkie",
"• Samodzielność<br/>"
"• Umiejętność analizy problemów<br/>"
"• Praca zespołowa<br/>"
"• Szybkie uczenie się<br/>"
"• Dokładność i odpowiedzialność"))

story.append(Spacer(1,12))

story.append(box("Języki",
"• Angielski – B2<br/>"
"• Polski – B2<br/>"
"• Rosyjski – native"))

story.append(Spacer(1,12))

story.append(box("Dodatkowe informacje",
"• Zainteresowanie systemami IT oraz ich utrzymaniem<br/>"
"• Podstawowa wiedza o bazach danych i ich administracji<br/>"
"• Chęć rozwoju w obszarze Linux i Windows Server<br/>"
"• Gotowość do pracy stacjonarnej w Poznaniu<br/>"
"• Umiejętność czytania dokumentacji technicznej w języku angielskim"))

story.append(Spacer(1,12))


doc.build(story)