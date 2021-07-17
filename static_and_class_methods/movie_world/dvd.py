import calendar


class DVD:

    def __init__(self, name, dvd_id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id, name, date, age_restriction):
        day, month, year = date.split(".")
        result_month = calendar.month_name[int(month)]
        return cls(name, dvd_id, int(year), result_month, age_restriction)

    def __repr__(self):
        rented_map = {True: "rented", False: "not rented"}
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {rented_map[self.is_rented]}"
