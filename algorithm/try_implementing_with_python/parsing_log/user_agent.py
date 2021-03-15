import csv
from user_agents            import parse
import matplotlib.pyplot    as plt
import numpy                as np

with open('apache_logs.txt', newline='') as f:
    reader = csv.reader(f)
    os_list = {}
    for row in reader:
        row = str(row)
        row_remain = row.split("\"")
        user_info = ' '.join(row_remain[4:]).strip('\"').strip(']').strip('\'').strip(' ')
        user_agent = parse(user_info)

        if user_agent.os.family not in os_list:
            os_list[user_agent.os.family] = 1
        elif user_agent.os.family in os_list:
            os_list[user_agent.os.family] += 1


# OS별 접속자 통계 딕트 리스트 출력
print(os_list)

total_os = 0
os_len = 0
for i in os_list.values():
    total_os += i
    os_len += 1

# OS별 접속자 통계 차트
x = np.arange(os_len)
os_num = os_list.keys()
values = os_list.values()

plt.bar(x, values, width=0.5)
plt.title('Contact Statistics by os')
plt.xticks(x, os_num, rotation=50)
plt.show()



