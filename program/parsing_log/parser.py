import csv

# 로그를 csv로 파싱하는 코드
def extract_full_logs(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)

        log_list = []
        for row in reader:
            row = str(row)
            row_remain = row.split("\"")
            row = row.split(" ")
            row_list = {
                'ip': row[0].split('\'')[1],
                'date': row[3].strip('[') + ' ' + row[4].strip(']'),
                'method': row[5].strip("\""),
                'url': row[6],
                'http': row[7].strip('\"'),
                'status_code': row[8],
                'data_size': row[9],
                'ref_url': row_remain[3].strip("\'"),
                'request_header': ' '.join(row_remain[4:]).strip('\"').strip(']').strip('\'').strip(' ')
            }
            log_list.append(row_list)

    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)

        header = ['Client IP Address', 'Access Time', 'Client Method', 'Request URI', 'Protocol Version', 'Status Code',
                  'Data Size', 'Reference URL', 'User-Agent HTTP Request Header']

        writer.writerow(header)

        for i in range(len(log_list)):
            writer.writerow(log_list[i].values())
    return

# IP주소, URI, Status code 으로 구성된 CSV로 파싱하는 코드
def extract_partially(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)

        log_list = []
        for row in reader:
            row = str(row)
            row = row.split(" ")

            row_list = {
                'ip' : row[0].split('\'')[1],
                'url' : row[6],
                'status_code' : row[8],
            }
            log_list.append(row_list)

    with open('partially.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        header = ['Client IP Address', 'Request URI', 'Status Code' ]
        writer.writerow(header)

        for i in range(len(log_list)):
            writer.writerow(log_list[i].values())
    return

if __name__ == '__main__':
    # 전부 추출
    extract_full_logs('apache_logs.txt')
    # IP 주소, URI, Status code 추출
    extract_partially('apache_logs.txt')