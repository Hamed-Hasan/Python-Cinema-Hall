class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        self.__show_list = []
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no
        Star_Cinema.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        self.__seats[id] = [['F' for _ in range(self._cols)] for _ in range(self._rows)]

    def book_seats(self, show_id, seat_list):
        try:
            for seat in seat_list:
                row, col = seat
                if self.__seats[show_id][row][col] == 'F':
                    self.__seats[show_id][row][col] = 'B' 
                else:
                    print(f"Seat ({row}, {col}) is already booked.")
        except KeyError:
            print("Invalid show ID!")
        except IndexError:
            print("Invalid seat number!")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    def view_show_list(self):
        for id, movie_name, time in self.__show_list:
            print(f"ID: {id}, Movie: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        try:
            for i, row in enumerate(self.__seats[show_id]):
                print(f"Row {i}: ", end="")
                for seat in row:
                    print(seat, end=" ")
                print()
        except KeyError:
            print("Invalid show ID!")

hall1 = Hall(5, 5, 1)  
show_id = input("Enter show ID: ")
movie_name = input("Enter movie name: ")
show_time = input("Enter show time: ")

hall1.entry_show(show_id, movie_name, show_time)

print("\nShowing All Shows:")
hall1.view_show_list()

# Booking seats
try:
    num_seats_to_book = int(input("\nNumber of seats to book: "))
    seats_to_book = []
    for _ in range(num_seats_to_book):
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        seats_to_book.append((row, col))
    hall1.book_seats(show_id, seats_to_book)
except ValueError:
    print("Invalid input. Please enter integer values.")
print("\nAvailable Seats:")
hall1.view_available_seats(show_id)
