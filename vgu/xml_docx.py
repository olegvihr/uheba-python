from docx import Document


document = Document()

# document.add_heading('Заголовок документа', 0)
# document.add_heading('Заголовок первого уровня', level=1)
# document.add_paragraph('простой параграф без стиля')
# document.add_paragraph('элемент ненумерованого списка', style='List Bullet')
# document.add_paragraph('элемент нумерованого списка', style='List Numbered')
# document.add_paragraph('абзац текста в виде цитаты', style='Intense Quote')


p = document.add_paragraph('Абзац обычного текста этого документа')
p.add_run('часть жырным шрифтом, ').bold = True
p.add_run(' а часть ')
p.add_run('курсивом.').italic = True

document.save('heading.doc')
