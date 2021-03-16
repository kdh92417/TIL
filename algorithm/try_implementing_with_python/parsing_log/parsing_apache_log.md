# 아파치 로그파일을 CSV 파일로 Parsing

- 아파치 로그 파일을 형식에 맞게 CSV 파일로 만들기
- 특정 데이터를 뽑아서 통계 내보기
- 로그의 IP주소, URI, Status Code만을 뽑아서 CSV 파일 만들기

<br>

## Output

- [parser.py](https://github.com/kdh92417/TIL/blob/master/algorithm/try_implementing_with_python/parsing_log/parser.py) : apache.txt 를 전부 또는 일부분을 csv파일로 parsing
- [ip_address_and_200status_code](https://github.com/kdh92417/TIL/blob/master/algorithm/try_implementing_with_python/parsing_log/ip_address_and_200status_code.png) : status code 200 응답률과 특정 아이피주소가 접속한 횟수
  - [code](https://github.com/kdh92417/TIL/blob/master/algorithm/try_implementing_with_python/parsing_log/solve.py)
- [user_agent](https://github.com/kdh92417/TIL/blob/master/algorithm/try_implementing_with_python/parsing_log/user_agent_statistics.png) : OS 별 접속자 수 통계 with user_agent

  - [code_user_agent](hhttps://github.com/kdh92417/TIL/blob/master/algorithm/try_implementing_with_python/parsing_log/user_agent.py)

- [output.csv](https://github.com/kdh92417/TIL/blob/master/algorithm/try_implementing_with_python/parsing_log/output.csv) : log 파일을 apache 형식에 맞게 csv 파일로 파싱
- [partially.csv](https://github.com/kdh92417/TIL/blob/master/algorithm/try_implementing_with_python/parsing_log/partially.csv) : IP주소, URI, Status Code 만 csv파일로 파싱
