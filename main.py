import xlwt

class GetNUmbers():
    def __init__(self, initial_number, final_numbers):
        self.initial_number = initial_number
        self.final_numbers = final_numbers

    def compose_list(self):
        list = []
        for i in range(self.initial_number, self.final_numbers):
            #print(i)
            list.append(i)
        #print(list)

        wb = xlwt.Workbook()
        ws = wb.add_sheet('Teste')

        ws.write(0, 0, str(list))

        wb.save('spreadsheet.xls')


x = GetNUmbers(1, 5)
x.compose_list()