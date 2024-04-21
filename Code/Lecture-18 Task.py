class Seats:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.amount_paid = 0


total_seats = 5
seats = []


class SeatReservation:
    def __init__(self):
        for i in range(5):
            seats[i] = Seats()

    def print_receipt(self):
        print()
