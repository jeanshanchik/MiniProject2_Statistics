import csv
from Fileutilities.absolutepath import absolute_path


class CsvNormalReader:

    def __len__(self):
        return len(self.data)

    def __init__(self, filepath):
        self.data = []
        with open(absolute_path(filepath), encoding='utf-8-sig') as list_data:
            csv_data = csv.reader(list_data, delimiter=',')
            for row in csv_data:
                self.data.append(row)
            self.data = [num for elem in self.data for num in elem]