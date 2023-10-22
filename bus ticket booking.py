class BusTicket:
    def __init__(self, name, source, destination, date, seat_number):
        self.name = name
        self.source = source
        self.destination = destination
        self.date = date
        self.seat_number = seat_number

# Initialize an empty list to store booked tickets
bus_tickets = []

def book_ticket():
    print("Enter passenger details:")
    name = input("Name: ")
    source = input("Source: ")
    destination = input("Destination: ")
    date = input("Date: ")
    seat_number = input("Seat Number: ")

    ticket = BusTicket(name, source, destination, date, seat_number)
    bus_tickets.append(ticket)
    print("Ticket booked successfully!")

def display_tickets():
    if not bus_tickets:
        print("No tickets booked yet.")
    else:
        print("List of booked tickets:")
        for ticket in bus_tickets:
            print(f"Name: {ticket.name}, Source: {ticket.source}, Destination: {ticket.destination}, Date: {ticket.date}, Seat Number: {ticket.seat_number}")

def main():
    while True:
        print("\nBus Ticket Booking System")
        print("1. Book a ticket")
        print("2. Display booked tickets")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            book_ticket()
        elif choice == "2":
            display_tickets()
        elif choice == "3":
            print("Thank you for using our service. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
