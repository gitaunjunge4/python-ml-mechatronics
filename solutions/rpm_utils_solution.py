import math
def rpm_to_rads(rpm):
    return rpm * 2 * math.pi / 60.0

def rads_to_rpm(rads):
    return rads * 60.0 / (2 * math.pi)
