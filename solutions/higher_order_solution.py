from functools import reduce
import math

def rpm_to_rads_list(rpms):
    return [r*2*math.pi/60.0 for r in rpms]

def filter_noise(values, threshold):
    return [v for v in values if v <= threshold]

def cumulative_energy(power_list):
    return reduce(lambda a,b: a+b, power_list, 0.0)
