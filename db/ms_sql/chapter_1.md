## 데이터베이스

---

### 1. OLTP (Online Transaction Processing) 데이터베이스

- 주로 트랜잭션 처리(데이터 변경 처리)를 위한 용도로 사용하는 DB

### 2. OLAP(Online Analytical Processing) 데이터베이스

- 대량의 데이터를 체계화하고 요약 → 데이터에 대한 빠른 평가와 분석을 목적

## 시스템 데이터

---

- SQL Server를 설치하는 과정에서 SQL Server가 자체적으로 사용할 목적으로 자동으로 만드는 데이터베이스들

### 1. master 데이터베이스

- SQL Server의 여러 가지 환경 정보와 로그인 정보, 관리되는 모든 데이터베이스에 대한 정보를 저장

### 2. model 데이터베이스

- 새로 만들어지는 데이터베이스의 원형

### 3. tempdb 데이터베이스

- SQL Server가 운영될 때 자동으로, 또는 사용자에 의해 만들어지는 임시 테이블들이 저장되는 곳

### 4. msdb 데이터베이스

- 주로 자동화와 관련된 정보를 저장할 때 msdb 데이터베이스를 사용
- SQL Server 에이전트 서비스가 사용하는 데이터베이스

### 5. resource 데이터베이스

- SQL Server 운영과 관련된 시스템 개체를 모두 포함하고 있는 resource 데이터베이스
    
    → 읽기 전용의 숨겨진 데이트베이스여서 개체 탐색기에는 보이지 않는다.
    

## SQL 문

**요구사항**

- 데이터 베이스이름 : SconDB02
- 데이터 파일 :
    - 위치 : C:\SQLData
    - 처음 크기 : 1024MB, 자동 증가 크기 : 256MB, 최대 크기 : 뮂한
- 로그 파일
    - 위치 : C:\SQLLog
    - 처음 크기 : 256MB, 자동 증가 크기 : 128MB, 최대 크기 : 무제한

```sql
USE master
GO

CREATE DATABASE SeconDB02
ON PRIMARY (
	NAME = 'SeconDB02',
	FILENAME = 'C:\SQLData\SeconDB02.mdf',
	SIZE = 1024MB,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 256MB
)
LOG ON (
	NAME = 'SeconDB02_log',
	FILENAME = 'C:\SQLLog\SeconDB02_log.1df',
	SIZE = 256MB,
	MAXSIZE = UNLIMITED,
	FILEGROWTH = 128MB
)
GO

--  해당 라인 주석
/*
	범위 주석
*/
```

- `GO` : 한 번에 수행할 쿼리문을 명시하기 위함 ( 마우스 블록을 지정해 쿼리문을 수행해도 됨 )

## 파일 그룹 활용
---

- 데이터 파일 분산을 통한 성능 향상에 목적
- 데이터 파일을 여러 곳에 나눔으로써, 디스크 손상으로 인한 데이터 손실을 최소화하는 데 목적

**주 파일 그룹(Primary File Group)**

- PRIMARY 파일 그룹은 주 데이터 파일(`mdf` 확장자를 가진 파일) 을 포함한다.

**사용자 정의 파일 그룹(User-defined-File Groups)**

- PRIMARY 파일 그룹 외에 사용자가 만든 파일 그룹이 사용자 정의 파일 그룹.
- 테이블을 역할별로 구분하여 서로 다른 위치에 저장할 수 있다.
- PRIMARY 파일 그룹은 하나만 존재할 수 있지만, 사용자 정의 파일 그룹은 여러개 존재 가능

**기본 파일 그룹(Default File Group)**

- 테이블과 인덱스를 만들 때 어느 파일 그룹에 만들지(정확히 이야기하면, 어느파일 그룹에 포함된 파일에 만들지) 지정 가능
- 만일 파일 그룹을 지정하지 않으면 테이블과 인덱스는 기본 파일 그룹에 만들어짐
- 기본적으로 PRIMARY 파일 그룹이 기본 파일 그룹이다.

**SQL 문**

```sql
USE master
GO

-- UFG01 파일 그룹 추가
ALTER DATABASE FirstDB02
	ADD FILEGROUP UFG01
GO

-- UFG01 파일 그룹에 파일 추가
ALTER DATABASE FirstDB02
	ADD FILE (
		NAME = 'FirstDB02_02',
		FILENAME = 'C:\SQLData\FirstDB02_02.ndf',
		SIZE = 512MB,
		FILEGROWTH = 128MB
	) TO FILEGROUP UFG01
GO

-- UFG02 파일 그룹
ALTER DATABASE FirstDB02
	ADD FILEGROUP UFG02
GO

-- UFG02 파일 그룹에 파일 추가
ALTER DATABASE FirstDB02
	ADD FILE (
		NAME = 'FirstDB02_03',
		FILENAME = 'C:\SQLLog\FirstDB02_03.ndf',
		SIZE = 512MB,
		FILEGROWTH = 128MB,
	) TO FILEGROUP UFG02
GO

USE FirstDB02
GO

-- UFG01 파일 그룹을 기본 파일 그룹으로 변경
ALTER DATABASE FirstDB02
	MODIFY FILEGROUP UFG01 DEFAULT
GO
```

```sql
USE FirstDB02
GO

-- PRIMARY 파일 그룹에 TA 테이블 만들기
CREATE TABLE TA (
	col1 int,
	col2 int
) ON [PRIMARY]
GO

-- UFG01 파일 그룹에 TB 테이블 만들기
CREATE TABLE TB (
	col1 int,
	col2 int
) ON UFG01
GO

-- UFG02 파일 그룹에 TC 테이블 만들기
CREATE TABLE TB (
	col1 int,
	col2 int
) ON UFG02
GO

-- 기본 파일 그룹에 TD 테이블 만들기
CREATE TABLE TD (
	col1 int,
	col2 int
)
GO
```