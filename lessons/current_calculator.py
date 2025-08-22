#Given voltage and resistance inputs (strings), convert to numbers and compute current (I = V/R).

#steps
#map thru the data and ensure they are in the correct type, int
#get the voltages
#get the resistance values
#perform I=V/R

#zip() pairs elements from two or more iterables together by their indexes
#re.sub(pattern, replacement, string)- checks if the str has matches then replaces it with what is specified and returns a stristrng

import re

#data
voltages = [" 12V ", "5 volts", "9.0", "ten", "24.5V"]
resistances = ["4 ohms", " 2 ", "3.0Ω", "five", "0"]

def clean_number(value):
    cleaned = re.sub(r"[^0-9\.\-]", "", value)        #returns str of numbers only
    # print(cleaned)
    try:
        return float(cleaned)
    except ValueError:
        return None
    
for v, r in zip(voltages, resistances):
    V = clean_number(v)
    R = clean_number(r)
    
    if V is not None and R is not None and R != 0:
        I = V / R
        print (f"{I:.1f}A")
    else:
        print(f"Skipping invalid data {V}, {R}")