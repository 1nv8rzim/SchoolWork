import csv
import os

csv_users = {}
bad_users = {}

with open('Lab02_Users.csv', 'r') as csvfile:
    csv = csv.reader(csvfile, delimiter=',')
    for line in csv:
        if line[0] == 'EmployeeID':
            continue
        csv_users[line[0]] = line[1:]


def make_usernames(id, user):
    last = user[0].lower().replace("'", '')
    first = user[1].lower().replace("'", '')
    if last == '':
        bad_users[id] = f'User ID {id}: Invalid last name "{last}"'
        return None
    if first == '':
        bad_users[id] = f'Invalid first name "{first}"'
        return None
    username = first[0] + last[:5]
    while True:
        with open('/etc/passwd') as passwd:
            if username in passwd.readlines():
                username, value = username[:5], username[5]
                try:
                    value = int(value)
                    username += str(value + 1)
                except:
                    username += '1'
            else:
                break
    full_name = user[1] + ' ' + user[0]
    return (username, full_name, id)


def get_office(id, data):
    office = data[2]
    try:
        temp = office.replace('-', '')
        int(temp)
        if '-' not in office:
            raise KeyError
    except:
        bad_users[id] = f'Invalid office "{office}"'
        return None
    return office


def get_department(id, user):
    department = user[4]
    if department == '':
        bad_users[id] = f'Invalid department ""'
        return None
    return department


def get_group(id, user):
    group = user[5]
    if group == '':
        bad_users[id] = f'Invalid group ""'
        return None
    return group


def group_exist(group):
    with open('/etc/group', 'r') as groups:
        return group in groups.readlines()


for user in csv_users.items():
    temp = make_usernames(*user)
    if temp is None:
        continue
    username, full_name, id = temp

    office = get_office(*user)
    if office is None:
        continue

    password = username[::-1]

    department = get_department(*user)
    if department is None:
        continue

    group = get_group(*user)
    if group is None:
        continue

    shell = '/bin/bash' if group != 'office' else '/bin/csh'

    if not group_exist(group):
        os.system(f'groupadd -f {group}')
        print(f'groupadd -f {group}')

    if not os.path.exists(f'/home/{department}'):
        os.system(f'mkdir /home/{department}')
        print(f'mkdir /home/{department}')

    os.system(
        f'useradd -m -d /home/{department}/{username} -s {shell} -g {group} -c "{full_name}" {username}')
    print(
        f'useradd -m -d /home/{department}/{username} -s {shell} -g {group} -c "{full_name}" {username}')
    os.system(f'echo -e {password}\n{password} | passwd {username}')
    print(f'echo -e {password}\n{password} | passwd {username}')
    os.system(f'passwd -e {username}')
    print(f'passwd -e {username}')

for user, reason in bad_users.items():
    print(f'BAD RECORD: EMPLOYEE_ID={user}, REASON=\'{reason}\'')
