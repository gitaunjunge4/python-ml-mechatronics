from exercises.starter import higher_order as ho
from solutions import higher_order_solution as sol

def test_rpm_to_rads_list():
    data = [60, 120, 600]
    expected = sol.rpm_to_rads_list(data)
    out = ho.rpm_to_rads_list(data)
    assert all(abs(a-b) < 1e-9 for a,b in zip(out, expected))

def test_filter_noise():
    vals = [0.1, 0.5, 1.2, 3.5, 0.2]
    expected = sol.filter_noise(vals, threshold=1.0)
    out = ho.filter_noise(vals, threshold=1.0)
    assert out == expected

def test_cumulative_energy():
    p = [1,2,3,4]
    expected = sol.cumulative_energy(p)
    out = ho.cumulative_energy(p)
    assert abs(out - expected) < 1e-9
