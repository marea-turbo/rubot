import io
import requests

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage


def get_pdf_text_from_url(url: str):
    pdf_response = requests.get(url)
    pdf_stream = io.BytesIO(pdf_response.content)
    string_stream = io.StringIO()

    rscm = PDFResourceManager()
    laparams = LAParams()
    device = TextConverter(
        rscm, string_stream, laparams=laparams
    )

    interpreter = PDFPageInterpreter(rscm, device)

    for page in PDFPage.get_pages(
            pdf_stream,
            set(),
            maxpages=0,
            password="",
            caching=True,
            check_extractable=True,
    ):
        interpreter.process_page(page)

    text = string_stream.getvalue()

    device.close()
    string_stream.close()
    pdf_stream.close()

    return str(text)
