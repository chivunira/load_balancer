import re
import os
import matplotlib.pyplot as plt

def parse_logs(log_file):
    if not os.path.exists(log_file):
        print(f"Log file '{log_file}' does not exist.")
        return {}

    with open(log_file, 'r') as file:
        logs = file.readlines()

    counts = {}
    for log in logs:
        match = re.search(r'http://localhost:(\d+)', log)
        if match:
            port = match.group(1)
            if port in counts:
                counts[port] += 1
            else:
                counts[port] = 1

    return counts

def generate_bar_chart(counts):
    if not counts:
        print("No data to plot.")
        return

    servers = list(counts.keys())
    request_counts = list(counts.values())

    bars = plt.bar(servers, request_counts)
    plt.xlabel('Server Instance')
    plt.ylabel('Request Count')
    plt.title('Request Count per Server Instance')

    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center', va='bottom')

    plt.savefig('bar_chart.png', format='png', dpi=300)
    plt.show()

log_file_path = 'logs/server_selection.log'
counts = parse_logs(log_file_path)
if counts:
    generate_bar_chart(counts)

def count_server_logs(log_file):
    if not os.path.exists(log_file):
        print(f"Log file '{log_file}' does not exist.")
        return 0

    with open(log_file, 'r') as file:
        logs = file.readlines()

    count = sum(1 for log in logs if "Request redirected to server:" in log)

    return count

count = count_server_logs(log_file_path)
print(f"There are {count} logs redirected to servers.")
