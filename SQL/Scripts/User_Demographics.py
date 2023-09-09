import random

# List of interests
interests = [
    "Music", "Travel", "Reading", "Photography", "Gaming", "Cooking",
    "Sports", "Movies", "Art", "Fashion", "Fitness", "Technology",
    "Hiking", "Shopping", "Dancing", "Food", "Singing", "Pets",
    "Crafts", "Yoga", "Writing", "Cycling", "Nature", "History",
]

# Function to generate a random user ID
def generate_user_id():
    return "U" + str(random.randint(1000, 9999))

# Function to generate a random age between 18 and 65
def generate_age():
    return random.randint(18, 65)

# Function to generate a random gender
def generate_gender():
    return random.choice(["Male", "Female"])

# Function to generate random interests
def generate_interests():
    num_interests = random.randint(1, 5)  # Randomly select 1 to 5 interests
    return random.sample(interests, num_interests)

# Generate mock data for 3 users
user_data = []

for _ in range(0,20):
    user_id = generate_user_id()
    age = generate_age()
    gender = generate_gender()
    user_interests = ";".join(generate_interests())
    user_data.append((user_id, age, gender, user_interests))

# Print the generated data
for data in user_data:
    print(data)