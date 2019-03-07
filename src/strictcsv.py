import csv


class NotSameColNumError(Exception):
    pass

class ColIdxOutOfBoundError(Exception):
    pass


class StrictCsv:

    def __init__(self, file_name):
        self.file_name = file_name

        self.parse()
        self.validate()

    def parse(self):
        with open(self.file_name, 'r') as f:
            self.content = list(csv.reader(f))

    def validate(self):
        self.col_num = len(self.content[0])
        has_diff_col_num = lambda e: len(e) != self.col_num

        invalid_rows = list(filter(has_diff_col_num, self.content))
        if invalid_rows:
            raise NotSameColNumError

    def get_nth_col(self, col_idx):
        if self.col_num < col_idx:
            raise ColIdxOutOfBoundError

        get_nth = lambda e: e[col_idx-1]
        return list(map(get_nth, self.content))
