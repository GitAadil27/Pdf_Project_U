from django.core.exceptions import ValidationError
import re

def validate_12_digit_integer(civil_id):
    if not re.match(r'^\d{12}$',str(civil_id)):
        ValidationError('Civil ID Must be 12 digits long')