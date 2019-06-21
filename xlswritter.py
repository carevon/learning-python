import xlsxwriter


# CREATE FILE (workbook) and worksheet
outWorkbook = xlsxwriter.Workbook("out.xlsx")
outSheet = outWorkbook.add_worksheet()

# DECLARE DATA
headers = ["Names", "Scores"]
names = ["Felipe","Bob", "Mary"]
values = [70, 82, 71]

# WRITE HEADERS
outSheet.write("A1", "Names")
outSheet.write("B1", "Scores")

# WRITE DATA TO FILE
for item in range(len(names)):
    outSheet.write(item+1, 0, names[item])
    outSheet.write(item+1, 1, values[item])

outSheet.write("D1", "Total")
outSheet.write_formula("D2", "=SUM(B2:B4)")

# MANUAL WAY
'''
outSheet.write("A2", names[0])
outSheet.write("A3", names[1])
outSheet.write("A4", names[2])

outSheet.write("B2", values[0])
outSheet.write("B3", values[1])
outSheet.write("B4", values[2])

    OR MAYBE USE

outSheet.write(1, 0, names[0])
outSheet.write(2, 0, names[1])
outSheet.write(3, 0, names[2])

outSheet.write(1, 1, values[0])
outSheet.write(2, 1, values[1])
outSheet.write(3, 1, values[2])

'''


outWorkbook.close()