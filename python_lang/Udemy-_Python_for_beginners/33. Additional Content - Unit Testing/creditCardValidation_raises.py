# creditCardValidation_raises.py
from datetime import *
def validateCard(expDate):
    if expDate>datetime.now().date():
        return 'Valid'
    else:
        raise RuntimeError('Card has expired')