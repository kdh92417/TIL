import re

while True:
    regis_num = input("주민번호를 입력하세요 : ")
    if regis_num == 'q':
        break

    regex = re.compile(r'\d\d\d\d\d\d-\d\d\d\d\d\d\d')
    match = regex.search(regis_num)
    phone_number = match.group()
    marking_number = phone_number[:8] + '******'
    num_dict = [phone_number, marking_number]
    print("마킹 주민번호 : {}".format(num_dict[1]))


