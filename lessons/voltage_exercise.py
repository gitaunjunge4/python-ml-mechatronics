#Given voltage and resistance inputs (strings), convert to numbers and compute current (I = V/R).

#steps
#map thru the data and ensure they are in the correct type, int
#get the voltages
#get the resistance values
#perform I=V/R

#zip() pairs elements from two or more iterables (like lists) together by their indexs

import re
#data
voltages = [" 12V ", "5 volts", "9.0", "ten", "24.5V"]
resistances = ["4 ohms", " 2 ", "3.0Ω", "five", "0"]

def cleanNumber(value):
    cleaned = re.sub(r"[^0-9].\-", "", value)
    try:
        return float(cleaned)
    except ValueError:
        return None
    
for v, r in zip(voltages, resistances):
    V = cleanNumber(v)
    R = cleanNumber(r)

    if V is None or R is None:
        print(f"Input invalid for {V} and {R}")
        continue #skips to the next pair in the loop to avoid using invalid data

    if R == 0:
        print(f"Error: Resistance can not be zero{r}")
        continue

    I = V / R
    print(I)