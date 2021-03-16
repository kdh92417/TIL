# 아파치 로그파일을 CSV 파일로 Parsing

- 아파치 로그 파일을 형식에 맞게 CSV 파일로 만들기
- 특정 데이터를 뽑아서 통계 내보기
- 로그의 IP주소, URI, Status Code만을 뽑아서 CSV 파일 만들기

<br>

## Output

- parser.py : apache.txt 를 전부 또는 일부분을 csv파일로 parsing
- ip_address_and_200status_code, user_agent : 특정 데이터 뽑아서 통계
