# Пример записив XLSX файл
import xlsxwriter # pip install xlsxwriter

DATA = (
    ["Water", 25],
    ["Cola", 37],
    ["Butter", 85],
    ["Bread", 15],
)

with xlsxwriter.Workbook("sample.xlsx") as workbook:
    print(dir(workbook))
    worksheet = workbook.add_worksheet(name="Calculation")

    row = 0
    col = 0

    for item, cost in DATA:
        worksheet.write(row, col,     item) # A1 (10) "COLA"
        worksheet.write(row, col + 1, cost) # B1 (11) 37
        row += 1

    # Можно использовать формулы (только общепринятые, не локаль)
    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')

#workbook.close()

