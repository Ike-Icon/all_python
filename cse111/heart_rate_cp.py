"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
# function for computing the heart rate per minute 
def get_max_rate(age):
    heartRate = 220 - age
    return heartRate 

# function for conputing the heart rate around 65%
def get_low_rate(max_rate):
    low_rate =  max_rate * 0.65
    return low_rate

# function for conputing the heart rate around 85%
def get_high_rate(max_rate):
    high_rate = max_rate * 0.85
    return high_rate

# Ask the user for their age
yourAge = int(input("What is your age? "))

max_rate_per_min = get_max_rate(yourAge)

low_heart_rate = get_low_rate(max_rate_per_min)

high_heart_rate = get_high_rate(max_rate_per_min)

print(f"When exercising to strengthen your heart, you should keep your heart rate between {low_heart_rate:.0f} and {high_heart_rate:.0f} of your heart’s maximum rate.")