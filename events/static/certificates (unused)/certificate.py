import pdfkit


def GenAttendCerti1(user):
    config = pdfkit.configuration(
        wkhtmltopdf='D:/cncwebsitedjango/events/static/certificates/wkhtmltopdf/bin/wkhtmltopdf.exe')
    out = user + 'pdf'
    pdfkit.from_file('D:/cncwebsitedjango/events/static/certificates/certi.html', out, configuration=config)
