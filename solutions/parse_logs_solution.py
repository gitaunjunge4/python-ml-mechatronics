import re
from datetime import datetime
LOG_LINE_RE = r'(?P<timestamp>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})\s+Temp:\s*(?P<temp>[0-9.]+)\s*C\s+Vib:\s*(?P<vib>[0-9.]+)\s+RPM:\s*(?P<rpm>\d+)'

def parse_log_line(line):
    m = re.search(LOG_LINE_RE, line)
    if not m:
        return None
    ts = datetime.fromisoformat(m.group('timestamp'))
    temp = float(m.group('temp'))
    vib = float(m.group('vib'))
    rpm = int(m.group('rpm'))
    return (ts.isoformat(), temp, vib, rpm)

def parse_log_file_to_csv(lines):
    rows = []
    for line in lines:
        p = parse_log_line(line)
        if p:
            rows.append(p)
    return rows
