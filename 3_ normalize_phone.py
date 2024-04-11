import re

# Function to normalize phone number
# Input: phone number
# Output: normalized phone number
def normalize_phone(phone):
    digits_only = re.sub(r"[^\d]", "", phone)
    
    if not digits_only.startswith("380"):
        normalized_number = "+38" + digits_only
    else:
        normalized_number = "+" + digits_only
    
    return normalized_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)