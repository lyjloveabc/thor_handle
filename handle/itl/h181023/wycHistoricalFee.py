from utils.file.excel.readUtil import ReadUtil


class WycHistoricalFee:
    def __init__(self):
        pass

    def handle(self, file, field_index):
        ReadUtil.read_file(file, field_index)
        pass


if __name__ == '__main__':
    obj = WycHistoricalFee()
    obj.handle(
        'file/逸郡截至2017年12月待缴物业费+车位费.xlsx',
        {
            'house_code': 1,
            'bill_tile': 3,
        }
    )
