class User:
    registered_user_count = 0

    def __init__(self, first_name, last_name, age, postal_code):
        if not first_name.isalpha():
            raise ValueError("First name must only contain alphabetical characters.")
        if not last_name.isalpha():
            raise ValueError("Last name must only contain alphabetical characters.")
        if not isinstance(age, int) or age <= 13:
            raise ValueError("Age must be an integer greater than 13.")
        if not postal_code.isalnum():
            postal_code = 'X0X0X0'
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.postal_code = postal_code

    def registered(self, status):
        self.registered = status
        User.registered_user_count += 1


def main():
    try:
        user1 = User("John", "Doe", 14, "A1B2C3")
        user1.registered(True)
        print(f"Registered users: {User.registered_user_count}")
        
        user2 = User("Jane", "Smith", 15, "123456")
        user2.registered(True)
        print(f"Registered users: {User.registered_user_count}")

        user3 = User("Alice", "Cooper", 12, "D4E5F6")  # This will raise an error
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


students_scores = [
    ("Alice James", 85),
    ("Adam Bonson", 90),
    ("Matt Fowler", 78),
    ("David Curry", 92),
    ("Eva Porter", 80),
    ("Azure Kelsey", 79),
    ("Billie Jose", 64),
    ("Willian Maxime", 86),
]

honour_students = {
    f"{name.split()[0][0]}. {name.split()[1]}": score
    for name, score in students_scores
    if score >= 80
}

print(honour_students)


numbers = range(1, 75, 3)
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))


numbers = range(1, 75, 3)
filtered_squares = []
for number in numbers:
    if number % 2 == 0:
        filtered_squares.append(number**2)


import time

# Using map, filter, and lambda
start_time = time.time()
result_map_filter = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
end_time = time.time()
time_map_filter = end_time - start_time

# Using for loops
start_time = time.time()
filtered_squares_loop = []
for number in numbers:
    if number % 2 == 0:
        filtered_squares_loop.append(number**2)
end_time = time.time()
time_for_loops = end_time - start_time

# Print results and compute times
print("Result using map, filter, and lambda:", result_map_filter)
print("Compute time using map, filter, and lambda:", time_map_filter)

print("Result using for loops:", filtered_squares_loop)
print("Compute time using for loops:", time_for_loops)
