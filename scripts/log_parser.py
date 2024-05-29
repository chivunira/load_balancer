import re
import matplotlib.pyplot as plt

def parse_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    # dictionary to hold the count for each server
    counts = {}
    for log in logs:
        # use a regular expression to extract the server port
        match = re.search(r'http://localhost:(\d+)', log)
        if match:
            port = match.group(1)
            if port in counts:
                counts[port] += 1
            else:
                counts[port] = 1

    return counts

def generate_bar_chart(counts):
    servers = list(counts.keys())
    request_counts = list(counts.values())

    bars = plt.bar(servers, request_counts)
    plt.xlabel('Server Instance')
    plt.ylabel('Request Count')
    plt.title('Request Count per Server Instance')

    # Annotate the bars with the exact number of requests
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, yval, ha='center', va='bottom')

    plt.savefig('bar_chart.png', format='png', dpi=300)
    plt.show()

counts = parse_logs('C:/Users/Anne/Downloads/pythonProject1/pythonProject1/server_selection.log')
generate_bar_chart(counts)

def count_server_logs(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    # count the number of logs that are redirected to servers
    count = sum(1 for log in logs if "Request redirected to server:" in log)

    return count

count = count_server_logs('C:/Users/Anne/Downloads/pythonProject1/pythonProject1/server_selection.log')
print(f"There are {count} logs redirected to servers.")