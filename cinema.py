#  Movie Ticket System

movies = [
    "The Dark Knight",
    "Titanic",
    "Jurassic Park",
    "Gladiator"
]
seat_types = ["Standard", "VIP"]

print("Welcome to the Movie Ticket System!")

# Movie Selection
user_choice_input = input("Choose the movie from the list :" + ", ".join(movies) + ": ").strip()
user_choice = None

# Validate movie choice
for movie in movies:
    if movie.lower() == user_choice_input.lower():
        user_choice = movie
        break

if user_choice is None:
    print("Invalid movie choice. Please restart the program and choose a valid movie.")
else:
    pass

# Seat Type Selection
user_ticket_input = input("Choose the seat type(Standard or VIP): ").strip()
user_ticket = None

# Validate seat type choice
for seat in seat_types:
    if seat.lower() == user_ticket_input.lower():
        user_ticket = seat
        break

if user_ticket is None:
    print("Invalid seat type. Please restart the program and choose a valid seat type.")
else:
    pass


# Age Input
user_age = int(input("Enter your age : "))


# --- Set ticket price based on seat type ---
if user_ticket == "Standard":
    ticket_price = 1500
elif user_ticket == "VIP":
    ticket_price = 3000

# --- Apply age-based discounts --
if user_age <= 18:
    discount = 0.3 # 30% discount for children
elif user_age >= 60:
    discount = 0.4 # 40% discount for seniors
else:
    discount = 0

total_price = ticket_price
final_price = ticket_price *(1 - discount)

# --- Display final ticket price ---
print("............Ticket Summary...............")
print(f" Movie: {user_choice}\n Age: {user_age}\n Ticket Type: {user_ticket}\n Total price: {total_price}\n Final Price after Discount: {final_price}")
print("Thank you for booking with us!")