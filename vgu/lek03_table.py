from docxtpl import DocxTemplate
import datetime as dt


doc = DocxTemplate("tpl.docx")
context = {
    'name': 'Иван Иванович',
    'event_name': 'лабораторные работы по 4 модулю',
    'place': 'корпусе ВятГУ',
    'date': dt.datetime.today(),
    'time': dt.datetime.now().strftime('%H:%M'),
    'items': ['картину',
              "корзину",
              "картонку",
              "и маленькую собачонку"],
}
doc.render(context)
doc.save("res.docx")