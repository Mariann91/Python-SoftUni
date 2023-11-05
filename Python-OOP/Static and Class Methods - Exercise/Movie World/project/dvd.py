class DVD:
    def __init__(self,  name: str, dvd_id: int, creation_year: int, creation_month: str, age_restriction: int) -> None:
        self.name = name
        self.id = dvd_id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, dvd_id: int, name: str, date: str, age_restriction: int):
        day, month, year = [int(el) for el in date.split(".")]

        months_as_words = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

        return cls(name=name, dvd_id=dvd_id, creation_year=year, creation_month=months_as_words[month], age_restriction=age_restriction)

    def __repr__(self) -> str:
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) " \
               f"has age restriction {self.age_restriction}. Status: {'rented' if self.is_rented else 'not rented'}"
