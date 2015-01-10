__author__ = 'mahmood'


class BirthDate:
    year = 0
    month = 0
    day = 0

    def initialize(year, month, day):
        new_birth_date = BirthDate()
        new_birth_date.year = year
        new_birth_date.month = month
        new_birth_date.day = day

        return new_birth_date


    def dic(self):
        result = {"year": self.year,
                  "month": self.month,
                  "day": self.day}

        return result