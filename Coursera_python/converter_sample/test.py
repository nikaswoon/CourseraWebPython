import requests
from decimal import Decimal
from Coursera_python.converter_sample.currency import convert


correct = Decimal('1088.0091')
result = convert(Decimal("1000.1000"), 'EUR', 'USD', "17/04/2020", requests)
if result == correct:
    print("Correct")
else:
    print("Incorrect: %s != %s" % (result, correct))
