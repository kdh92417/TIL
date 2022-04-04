# 무결성 유지 메카니즘

> 여기서 무결성이란 데이터베이스안의 저장된 데이터 값이 정확하고 모순이 없도록 유지하는 것을 말한다.

- 무결성을 유지하는 것이 중요한 이유는 수많은 데이터중에서 단하나라도 정확하지 않다면 나머지 데이터를 신뢰할 수 없기때문에 무결성 유지를 하는 것이 중요하다.


## 1. 무결성 제약의 기술

### 1.1 무결성 제약
1. 개체 무결성
   - 기본키(PK)값은 유일하며(UNIQUE), 넓값을 가질 수 없다(NOT NULL).
   - PRIMARY KEY 제약조건
2. 참조 무결성
   - 외래키(FK)값은 부모 테이블의 기본키(PK)값과 같거나, NULL값을 가진다.
   - FOREIGN KEY 제약조건

<br>

CASCADE DELETE의 전파

GROUP BY : 같은값끼리 그룹화 되어지는 것
HAVING : 그룹되어진 튜플들을 필터링 하는 것 (GROUP BY는 그룹을 필터링)
WHERE : 튜플을 필터링

WHERE 절 조건 과 HAVING 절 조건

- GROUP BY 는 오퍼레이션을 많이 잡아먹음 why?

HAVING과 WHERE절의 성능차이는 엄청크다.


```mysql
WITH temp AS (
    SELECT AVG(t.고객수) AS 평균고객수
    FROM (
            SELECT COUNT(customerId) AS 고객수
            FROM s_customers
            GROUP BY country 
         ) AS t
)
SELECT country
     , COUNT(customerId) AS 고객수
     , T.평균고객수
FROM s_customers C, temp T
GROUP BY country
HAVING 고객수 > T.평균고객수
ORDER BY 고객수 DESC, country
```

