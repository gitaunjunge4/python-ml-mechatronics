from exercises.starter import rpm_utils as ru
from solutions import rpm_utils_solution as sol

def test_rpm_roundtrip():
    vals = [60, 300, 1200]
    for v in vals:
        out = ru.rpm_to_rads(v)
        back = ru.rads_to_rpm(out)
        assert abs(back - v) < 1e-9
