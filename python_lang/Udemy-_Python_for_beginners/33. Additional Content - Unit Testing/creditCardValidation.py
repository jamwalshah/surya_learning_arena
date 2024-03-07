# creditCardValidation.py
from datetime import *
def validateCard(expDate):
    if expDate>datetime.now().date():
        return 'Valid'
    else:
        return 'expired'
# print(validateCard(date(2025, 2, 2)))