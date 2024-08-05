import re


if re.match(r"^\d{10}$", "234567890"):
    print('True')
else:
    print('False')