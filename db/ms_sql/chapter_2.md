# 1. 테이블 만들기

```sql
USE HRDB2
GO

CREATE TABLE dbo.직원 (
	사원번호 char(5) NOT NULL,
	이름 nchar(10) NOT NULL,
	성별 char(1) NOT NULL,
	입사일 date NOT NULL,
	전자우편 varchar(60) NOT NULL,
	부서코드 char(3) NOT NULL
)
GO
```

- `dbo` : 데이터베이스 안에서 개체들을 또 한번 그룹으로 묶을 수 있는 계층 (스키마)
    - 기본적으로 `dbo` 스키마에 포함된다.
    - 생략해도되지만 붙여주는 것이 좋다
    
<br>

# 2. 테이블 관리

## **열 추가**

```sql
ALTER TABLE dbo.직원
	ADD 급여 int NULL
GO
```

### **NOT NULL**

- `NOT NULL` : 기존테이블에 `NOT NULL` 속성을 갖는 열을 추가할 수없다.
- 하지만 `DEFAULT` 제약과 `IDENTITY` 속성을 사용하면 `NOT NULL` 속성을 갖는 열 추가 가능
    
    ```sql
    -- 기본 값을 저장하는 DEFAULT 제약
    ALTER TABLE dbo.직원
    	ADD EngName varchar(2) DEFAULT('') NOT NULL
    GO
    
    -- 자동 증가 값을 저장하는 INDENTITY 속성
    ALTER TABLE dbo.직원
    	ADD CheckID int IDENTITY(1, 1) NOT NULL
    GO
    
    SELECT * FROM dbo.직원
    GO
    ```
    
    ```sql
    USE HRDB2
    GO
    
    INSERT INTO dbo.직원
    	VALUES('S002', N'일지매', 'M', '2011-01-12', 'jimae@db.com', 'GEN', 8200)
    
    INSERT INTO dbo.직원
    	VALUES('S001', N'홍길동', 'M', '2011-01-01', 'hong@db.com', 'SYS', 8500)
    GO
    ```
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ee70139d-f171-421e-b7ef-ceb4fcb7fa63/Untitled.png)


### 열 삭제

```sql
USE HRDB2
GO

ALTER TABLE dbo.직원
	DROP COLUMN 급여
GO
```

### 열 변경

- 이름 열의 데이터 형식 `nchar(10)` → `nvarchar(20)` 으로 변경
    
    ```sql
    USE HRDB2
    GO
    
    ALTER TABLE dbo.직원
    	ALTER COLUMN 이름 nvarchar(20) NOT NULL
    GO
    ```
    
- 운영중인 서버에서 테이블 구조를 변경하는 것은 쉽지 않다.
    - 사용 중인 테이블 구조를 변경하는 작업은 사용자 쿼리를 차단하거나, 사용자 쿼리에 의해 차단되어질 수 있음

### 열 이름 변경

- `전자우편` 열 이름을 `이메일` 로 변경
    
    ```sql
    USE HRDB2
    GO
    
    EXEC sp_rename 'dbo.직원.전자우편', '이메일', 'COLUMN'
    GO
    ```
    
- `EXEC` 구문
    - `EXEC` 는 저장 프로시저를 호출 할 때 사용하는 구문으로 `EXECUTE` 라고 써도 된다.
    

### 테이블 이름 변경

- `직원` 테이블 이름을 → `직원정보` 테이블로 이름 변경
    
    ```sql
    USE HRDB2
    GO
    
    EXEC sp_rename 'dbo.직원', '직원정보', 'OBJECT'
    GO
    ```
    
    - 'OBJECT'는 생략해도 된다.

### 종속성 보기

- 테이블을 삭제하거나 구조를 변경할 할 때는 다른 테이블이나 뷰 등이 테이블에 의존하고있는지 확인해야된다.
- [테이블] → [종속성 보기]

### 테이블 삭제

```sql
DROP TABLE dbo.직원정보
GO
```

## 데이터 정렬

어떤 언어의 문자 코드를 저장할지, 저장된 데이터를 비교할 때 대소문자 구분은 어떻게 할지, 액센트 구분은 어떻게 할지 등을 정의한 것

ex) `Korean_Wansung_CI_AS` : 한글 완성형 문자를 저장할 것이며, 대소문자 구분하지 않고, 액센트는 구분 할 것

### 데이터 정렬 정보 확인

- SQL Server 데이터 정렬 확인
    
    ```sql
    SELECT SERVERPROPERTY('collation')
    GO
    
    /*
    Korean_Wansung_CI_AS
    */
    ```
    

- HRDB2 데이터베이스 데이터 정렬 확인(방법1)
    
    ```sql
    USE HRDB2
    GO
    
    SELECT DATABASEPROPERTYEX('HRDB2', 'collation')
    GO
    
    /*
    Korean_Wansung_CI_AS
    */
    ```
    

- HRDB2 데이터베이스 데이터 정렬 확인(방법2)
    
    ```sql
    SELECT collation_name
    	FROM sys.databases
    	WHERE name = 'HRDB2'
    GO
    
    /*
    Korean_Wansung_CI_AS
    */
    ```
    

### 데이터 정렬을 지정하여 테이블 만들기

```sql
USE HRDB2
GO

CREATE TABLE dbo.직원 (
	사원번호 char(5) COLLATE Korean_Wansung_CI_AS NOT NULL,
	이름 nchar(10) COLLATE Korean_Wansung_CI_AS NOT NULL,
	성별 char(1) COLLATE Korean_Wansung_CI_AS NOT NULL,
	입사일 date NOT NULL,
	전자우편 varchar(60) COLLATE Korean_Wansung_CI_AS NOT NULL,
	부서코드 char(3) COLLATE Korean_Wansung_CI_AS NOT NULL
)
GO
```

### 데이터 정렬 힌트

- `COLLATE` 문을 사용해 쿼리 수행시만 데이터 정렬 방식을 변경 할 수 있다.
- `Korean_Wansung_CI_AS` 는 대소문자를 구분하는 데이터 정렬 방식이다.

```sql
USE HRDB2
GO

SELECT 사원번호, 이름, 성별, 입사일, 이메일, 부서코드
	FROM dbo.직원정보
	WHERE 성별 = 'M' COLLATE Korean_Wansung_CI_AS
GO
```

# 3. 다양한 데이터 형식

### 데이터 형식에 대한 이해

- `DCLARE` 문으로 변수를 선언한 뒤, `SET` 문으로 값을 할당
    
    ```sql
    DECLARE @num int
    SET @num = 45000
    SET @num = @num + 55000
    SELECT @num
    
    -- 100000
    ```
    
    ```sql
    DECLARE @num int = 45000
    SET @num += 55000
    SELECT @num
    
    -- 100000
    ```
    
    - 산술 오버플로 오류 발생
    
    ```sql
    -- 산술 오버플로 오류 발생
    -- bigint 자료형으로 선언해야함
    DECLARE @num int
    SET @num = 45000
    SET @num = @num * 55000
    SELECT @num
    GO
    ```
    

### 시스템 데이터 형식

- `SQL Server` 가 기본적으로 제공하는 데이터 형식을 **시스템 데이터 형식** 이라고 부른다.
- 가장 적절한 데이터 형식은 저장될 데이터를 모두 포함할 수 있으면서 가장 작은 크기의 데이터형식

### 수치 데이터 형식

- 정수 데이터 형식 : 정확한 수치를 저장
- 실수 데이터 형식 : 부동 소수점 데이터를 저장

### 실수 데이터 형식

```sql
DECLARE @num decimal(10, 3)
SET @num = 1234567.67890
SELECT @num -- 1234567.679
```

```sql
DECLARE @num decimal(10, 3)
SET @num = 12345678.67890
SELECT @num  

-- numeric을(를) 데이터 형식 numeric(으)로 변환하는 중 산술 오버플로 오류가 발생했습니다.
-- 전체자리가 11자리가되어 산술 오버플로 발생
```

### 날짜와 시간 데이터 형식

```sql
-- [소스 2-21] 다양한 날짜와 시간 데이터 형식

-- 변수 선언
DECLARE @dt01 datetime
DECLARE @dt02 smalldatetime
DECLARE @dt03 date
DECLARE @dt04 time
DECLARE @dt05 datetime2
DECLARE @dt06 datetimeoffset

-- 변수에 날짜와 시간 관련 함수 값 대입
SET @dt01 = GETDATE()
SET @dt02 = GETDATE()
SET @dt03 = SYSDATETIME()
SET @dt04 = SYSDATETIME()
SET @dt05 = SYSDATETIME()
SET @dt06 = SYSDATETIMEOFFSET()

-- 변수의 값 표시
-- AS문을 활용해 열의 별칭(Alias)을 지정
SELECT @dt01 AS [datetime] 
SELECT @dt02 AS [smalldatetime]
SELECT @dt03 AS [date] 
SELECT @dt04 AS [time] 
SELECT @dt05 AS [datetime2]
SELECT @dt06 AS [datetimeoffset]
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/10f211e2-e59d-446b-9da7-d2edb7cbdb58/Untitled.png)

```sql
-- 자릿수 지정하여 변수 선언
DECLARE @dt01 time(2)
DECLARE @dt02 datetime2(3)
DECLARE @dt03 datetimeoffset(4)

-- 변수에 날짜와 시간 관련 함수 값 대입
SET @dt01 = SYSDATETIME()
SET @dt02 = SYSDATETIME()
SET @dt03 = SYSDATETIMEOFFSET()

-- 변수의 값 표시
SELECT @dt01 AS [time] 
SELECT @dt02 AS [datetime2] 
SELECT @dt03 AS [datetimeoffset]
GO
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/06abddd4-7b3b-4d75-b6fa-1eba1354bec4/Untitled.png)

### 문자 데이터 형식

- 업무에서 다루는 문자 데이터는 길이가 고정된 데이터와 길이가 고정되지 않은 데이터로 구분
    
    [Untitled](https://www.notion.so/1b14b45fe24f461fa6ffb4a260a25f85)
    
- 문자 데이터 길이가 일관된 경우는 `char` , 그렇지 않으면 `varchar`
- `char` 나 `varchar` 모두 최대 크기가 8000byte 이기 때문에 저장할 데이터가 8000byte를 초과하면 `varchar(max)` 로 선언

```sql
-- 고정 길이와 가변 길이

-- 변수 선언
DECLARE @str01 char(20) -- 고정 길이
DECLARE @str02 varchar(20) -- 가변 길이

-- 변수에 값 대입
SET @str01 = 'Gildong!'
SET @str02 = 'Gildong!'

-- 변수에 문자열 결합한 결과 확인
SELECT @str01 + 'Do you know Jiemae?' AS [Result]
SELECT @str02 + 'Do you know Jiemae?' AS [Result]
GO
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1ce9a1a3-710b-4ba5-90ed-aadfa3642782/Untitled.png)

### 유니코드 문자열 데이터 형식

- 유니코드(Unicode) 문자열 데이터 형식은 문자 하나가 2byte 크기를 차지하면서, 모든 나라 문자를 저장할 수 있는 데이터 형식

[유니코드 문자열 데이터 형식](https://www.notion.so/37652cbffca14d16b1946cc822d79933)

- 유니코드 변수나 유니코드 열에 값을 전달할 때는 문자열 앞에 N을 붙여야 한다.
- `varchar(20)` : 20byte크기의 가변길이 문자열이라는 의미로 한글 10글자만 저장할 수 있어 문자열이 잘렸다.
- `nvarchar(20)` : 40byte크기의 가변길이 문자열이라는 의미로 한글 20글자 저장할 수 있어 문자열이 자리지 않는다.

```sql
-- [소스 2-24] 유니코드 문자열

-- 변수 선언
DECLARE @str01 varchar(20) -- 20byte 크기의 가변길이 문자열
DECLARE @str02 nvarchar(20) -- 유니코드

-- 변수에 값 대입
SET @str01 = '홍길동은 일지매를 알지 못한다.'
SET @str02 = N'홍길동은 일지매를 알지 못한다.'

-- 변수 값 확인
SELECT @str01 AS [Result]
SELECT @str02 AS [Result]
GO
```

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/73f4df59-77fc-4083-a6aa-b6f736d6b83d/Untitled.png)