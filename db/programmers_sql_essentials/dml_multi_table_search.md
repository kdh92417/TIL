# DML - 다중 테이블 검색문

## 목차

# 1. 집합 연산자

## 1.1 합집합

> 형식이 같은 두개의 테이블을 하나로 합하는 연산

### 제약조건
- 컬럼개수 동일
- 동일 위치에 존재하는 컬럼의 데이터 타입이 상호 호환 가능해야 됨

### 종류
- UNION
- CROSS JOIN (카디션 프로덕트 - 곱집합)

### 일반 형식

```mysql
SELECT [컬럼명 ALL | DISTINCT]
FROM [테이블 리스트]
WHERE [`AND` / `OR` / `NOT` 과 `IN` / `NOT IN` 등을 이용한 투플 조건식]

UNION [DISTINCT | ALL]

SELECT [컬럼명 ALL | DISTINCT]
FROM [테이블 리스트]
WHERE [`AND` / `OR` / `NOT` 과 `IN` / `NOT IN` 등을 이용한 투플 조건식]
ORDER BY [컬럼명]
```

- `DISTINCT` : SELECT 절은 ALL이 기본이나 UNION은 `DISTINCT`가 기본
- `ORDER BY` : 최종 결과에 대한 정렬 -> 가장 마지막 줄에 한번만 작성
- MySQL에서는 `INTERSECT` 과 `EXCEPT` 을 `AND` / `OR` / `NOT` 과 `IN` / `NOT IN`를 이용하여 연산

<br>

### UNION ALL 과 UNION의 차이
- `UNION ALL` : 합집합하는 테이블들의 중복 컬럼들을 제거하지 않고 모두 합침
- `UNION (DISTINCT)` : 합집합하는 테이블들의 중복된 컬럼들을 제거하여 테이블을 합침

<br>

# 2. 순수 관계 연산자 JOIN

## 2.1 JOIN 연산

- 형식이 다른 두개의 테이블을 합치는 것


### 다중 조인의 실행계획 (Execution Plans)
Query optimizer에 의해서 결정 (내부적으로 가장빠른 순서를 결정하여 조인순서를 자동으로 결정)

### WHERE절 조인
- 검색 조건과 조인 조건이 혼재된 형태
- INNER JOIN 연산만 제공

### FROM절 조인
- INNER JOIN
- NATURAL JOIN
- OUTER JOIN 
- CROSS JOIN

-> FROM 절에 조인 조건을 명시하는 것이 가장 깔끔하고 가독성이 좋다.

### SELF JOIN
- 동일테이블 사이의 조인
- 반드시 테이블 `ALIAS`를 사용
- 같은 테이블이지만 서로 다른 접두사를 사용하여 논리적으로 다른 테이블을 조인하는 것