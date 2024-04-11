import random

# Function to generate random numbers for a ticket
# Input: min, max, quantity
# Output: list of random numbers
def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    if min > max or quantity > (max - min) or quantity < 1 or min < 1 or max > 1000:
        return list()
    
    
    result = random.sample(range(min, max), quantity)
    result.sort()
    
    return result


print(get_numbers_ticket(1, 1000, 6)) # valid case
print(get_numbers_ticket(20, 10, 5)) # invalid case - min > max
print(get_numbers_ticket(1, 1000, 1001)) # invalid case - quantity > (max - min)
print(get_numbers_ticket(0, 1000, 6)) # invalid case - min < 1
print(get_numbers_ticket(1, 1001, 6)) # invalid case - max > 1000
print(get_numbers_ticket(1, 1000, 0)) # invalid case - quantity < 1