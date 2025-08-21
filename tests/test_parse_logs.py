from exercises.starter import parse_logs as pl
from solutions import parse_logs_solution as sol

def test_parse_log_line():
    line = "2025-08-01T08:00:00 Temp: 23.45 C Vib: 0.5123 RPM: 1012"
    expected = sol.parse_log_line(line)
    out = pl.parse_log_line(line)
    assert out == expected

def test_parse_log_file_to_csv():
    lines = [
        "2025-08-01T08:00:00 Temp: 23.45 C Vib: 0.5123 RPM: 1012",
        "bad line",
        "2025-08-01T08:00:30 Temp: 23.52 C Vib: 0.5010 RPM: 1008"
    ]
    expected = sol.parse_log_file_to_csv(lines)
    out = pl.parse_log_file_to_csv(lines)
    assert out == expected
