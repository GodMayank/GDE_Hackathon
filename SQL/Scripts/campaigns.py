import random
from datetime import datetime, timedelta

# List of 20 campaign names for sales
campaigns = [
    "Super Savings Extravaganza",
    "Deal-a-Palooza",
    "Flash Sale Frenzy",
    "Clearance Spectacular",
    "Summer Savings Bonanza",
    "Autumn Harvest Sale",
    "Winter Wonderland Deals",
    "Spring Fever Discounts",
    "Holiday Shopping Spree",
    "Back-to-School Bargains",
    "Black Friday Blowout",
    "Cyber Monday Madness",
    "End-of-Year Clearance",
    "New Year, New Savings",
    "Customer Appreciation Sale",
    "Weekend Shopping Specials",
    "Midnight Madness Sale",
    "Red Tag Clearance Event",
    "Buy One, Get One Free",
    "Limited-Time Mega Discounts",
]

# Function to generate a random ad_id
def generate_ad_id():
    return random.randint(1001, 2000)

# Function to generate random product names
def generate_product_name():
    products = ["Laptop", "Smartphone", "Jacket","Shoes", "Grocery"]
    return random.choice(products)

# Function to generate a random target start date and end date within a range
def generate_target_dates():
    start_date = datetime(2023, 7, 1)
    end_date = datetime(2023, 12, 31)
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    target_start_date = start_date + timedelta(days=random_days)
    target_end_date = target_start_date + timedelta(days=random.randint(30, 90))  # Random duration between 30 to 90 days
    return target_start_date.strftime("%Y-%m-%d"), target_end_date.strftime("%Y-%m-%d")

# Generate mock data for 3 campaigns
campaign_data = []

for ad_id in range(1001, 1021):
    campaign = random.choice(campaigns)
    product = generate_product_name()
    target_start_date, target_end_date = generate_target_dates()
    campaign_data.append((ad_id,campaign,product,target_start_date,target_end_date))

# Print the generated data
for data in campaign_data:
    print(data)