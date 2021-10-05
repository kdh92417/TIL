# Programmers SQL Problem

- [SELECT 문](##select)
    - [상위 n개 레코드](###상위-n개-레코드)
    - [IS NULL](###is-null)


## SELECT

### 상위 n개 레코드
- [문제](https://programmers.co.kr/learn/courses/30/lessons/59405)
- 해결 방법
    - DATETIME 순으로 정렬한 뒤 첫번째 컬럼만 출력할 수 있게 LIMIT을 이용
- 코드
    ```sql
    SELECT NAME ㄴ
    FROM ANIMAL_INS 
    ORDER BY DATETIME
    LIMIT 1;
    ```

### IS NULL
- [문제](https://programmers.co.kr/learn/courses/30/lessons/59407)
- 해결방법
    - 해당 이름컬럼이 `not NULL` 을 찾아 출력
- 코드
    ```sql
    SELECT 
        ANIMAL_ID
    FROM 
        ANIMAL_INS
    WHERE
        NAME is not NULL
    ORDER BY
        ANIMAL_ID
    ```