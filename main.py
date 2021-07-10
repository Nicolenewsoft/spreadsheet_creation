import xlwt
import shutil

class GetNUmbers():
    def __init__(self, initial_number, final_numbers):
        self.initial_number = initial_number
        self.final_numbers = final_numbers + 1

    def compose_list(self):
        list = []
        for i in range(self.initial_number, self.final_numbers):
            #print(i)
            list.append(i)
        #print(list)

        wb = xlwt.Workbook()
        style0 = xlwt.easyxf('pattern: pattern solid, fore_colour aqua;')

        ws = wb.add_sheet('Teste')

        titles = ['Números', 'Nome', 'Assunto', 'Símbolo', 'Observações', 'Data']

        for i in range(len(titles)):
            ws.write(0, i, titles[i], style0)

        for i in list:
            ws.write(i, 0, i)

        wb.save('spreadsheet.xls')


x = GetNUmbers(int(input("Digite o primeiro número: ")), int(input("Digite o último número: ")))
print("Preparando sua planilha...")
x.compose_list()
shutil.move('spreadsheet.xls','/home/usuario/Área de trabalho')
print("Sua planilha está pronta! ")

