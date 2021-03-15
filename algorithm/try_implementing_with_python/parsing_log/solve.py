import csv
from collections import Counter

with open('apache_logs.txt', newline='') as f:
    reader = csv.reader(f)

    ip_list = []
    status_code_list = []
    for row in reader:
        row = str(row)
        row = row.split(" ")
        ip_list.append(row[0].split('\'')[1],)
        status_code_list.append(row[8])

counter_status_code = Counter(status_code_list)
counter_ip = Counter(ip_list)

total_status_code = 0
for i in counter_status_code.values():
    total_status_code += i

if __name__ == '__main__':
    print('IP 주소 68.184.202.186의 요청 횟수 : {}'.format(counter_ip['68.184.202.186']))
    print('200 응답 코드의 비율 : {}'.format(counter_status_code['200'] / total_status_code))
