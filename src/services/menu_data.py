# Req 3
import csv


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.source_path = source_path
        self.set = [False]

    def read_csv_rows(self):
        with open(self.source_path, newline="") as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                yield row

    def print_csv_rows(self):
        for row in self.read_csv_rows():
            print(row)


menu_data = MenuData("tests/mocks/menu_base_data.csv")
menu_data.print_csv_rows()
