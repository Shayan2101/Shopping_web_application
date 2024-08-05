import re


phone_number = "+989092301202"
def validate_mobile_number(number):
    pattern = r'^\+98912\d{7}$'
    if re.match(pattern, number):
        return True
    else:
        return False
print(f"{validate_mobile_number(phone_number)}")