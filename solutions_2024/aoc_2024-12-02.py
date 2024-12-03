from aocd import get_data
from aocd import submit

# SETUP , READ DATA
YEAR = 2024
DAY = 2
input_raw = get_data(day=DAY, year=YEAR)


# FUNCTIONS
def check_safe_report(report):
    diff_list = [report[i] - report[i + 1] for i in range(len(report) - 1)]
    condition_1 = all(x < 0 for x in diff_list)
    condition_2 = all(x > 0 for x in diff_list)
    condition_3 = all(x != 0 for x in diff_list)
    condition_4 = all(abs(x) <= 3 for x in diff_list)
    return condition_3 and condition_4 and (condition_1 or condition_2)

def pop_and_check_safe_report(report, drop_index):
    report_copy = report.copy()
    report_copy.pop(drop_index)
    return check_safe_report(report_copy)

# PART 1
safe_reports_count= 0
for line in input_raw.strip().split('\n'):
    tmp_report = [int(x) for x in line.split()]
    
    if check_safe_report(tmp_report):
        safe_reports_count += 1
        
print(safe_reports_count)       # 631
# submit(safe_reports_count, part="a", day=DAY, year=YEAR)

# PART 2
safe_reports_count= 0
debug_count = 0
for line in input_raw.strip().split('\n'):
    tmp_report = [int(x) for x in line.split()]
    checked = False
    while not checked:
        if check_safe_report(tmp_report):
            safe_reports_count += 1
            checked = True
        else:
            for i in range(len(tmp_report)):
                if pop_and_check_safe_report(tmp_report, i):
                    safe_reports_count += 1
                    checked = True
                    break
        checked = True
                    
print(safe_reports_count)       # 665
# submit(safe_reports_count, part="b", day=DAY, year=YEAR)
