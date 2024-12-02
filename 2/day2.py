
def get_reports():
    with open("input.txt", "r") as f:
        lines = f.read().split("\n")
        f.close()

        reports = [report.split() for report in lines]
        print(f"{reports[0]}")
        return reports

def print_report_info(report, i, report_state, difference):
    print(f""" Unhandled state transition:
    report: {report}
    index: {i}
    report_state: {report_state}
    difference: {difference}
""")

UNDETERMINED = 0
INCREASING = 1
DECREASING = 2
def part_1():
    reports = get_reports()

    number_of_safe_reports = 0
    for report in reports:
        report_state = UNDETERMINED
        safe = True
        for i in range(1, len(report)):
            difference = int(report[i]) - int(report[i-1])
            
            if difference == 0:
                safe = False
                break

            if report_state == UNDETERMINED:
                report_state = INCREASING if difference > 0 else DECREASING
            elif report_state == INCREASING and difference < 0:
                safe = False
                break
            elif report_state == DECREASING and difference > 0:
                safe = False
                break
            # else: safe  
                

            if abs(difference) > 3:
                safe = False
                break
        
        if safe == True:
            number_of_safe_reports += 1
    print(f"Number of safe reports: {number_of_safe_reports}")

if __name__ == "__main__":
    part_1()