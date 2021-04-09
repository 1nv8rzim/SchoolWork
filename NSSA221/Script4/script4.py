from sys import argv
from geoip import geolite2
from pycountry import countries
from tabulate import tabulate

# exit 1 if file is not passed
if len(argv) == 1:
    print('No Log File Provided')
    exit(1)

# file passed as an argument to the script
file = argv[1]

# exit 1 if file cant be opened
try:
    with open(argv[1]) as file:
        log = file.read().split('\n')
except IOError:
    print('file {} could not be opened'.format(argv[1]))
    exit(1)

# parse logs for ips, and count sort and filter them
attempts = []

for line in log:
    if 'Failed password' in line:
        attempts.append(line)

ips = [line.split()[-4] for line in attempts]

# counts
attempts = {}

for ip in ips:
    if ip in attempts:
        attempts[ip] += 1
    else:
        attempts[ip] = 1

# sorts
sorted_attempts = []
for ip, attempts in attempts.items():
    sorted_attempts.append((attempts, ip))

sorted_attempts = list(reversed(sorted(sorted_attempts)))

# adds headers
attackers = [('Count', 'IP', 'Country')]

# gets country name for each IP
for attempt in sorted_attempts:
    if attempt[0] < 20:
        break
    else:
        attackers.append(
            (attempt[0], attempt[1], countries.get(alpha_2=geolite2.lookup(attempt[1]).country).name))

# prints output
print(tabulate(attackers, headers='firstrow', tablefmt='fancy_grid'))

# export to csv
with open('results.csv', 'w') as output:
    for attacker in attackers:
        attacker = (str(i) for i in attacker)
        output.write(','.join(attacker) + '\n')
