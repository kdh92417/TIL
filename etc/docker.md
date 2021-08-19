## 도커란?

## 도커와 가상머신(VM)의 공통점 및 차이점

- 공통점 : 기본 하드웨어에서 격리된 환경 내의 애플리케이션을 배치하는 방법
- 차이점 : 가장 큰 차이점은 격리된
- 도커 시스템 모두삭제 : `docker system prune`
- 중단된 도커 컨테이너 모두 삭제 : `docker rm `docker ps -a -q``
- 이미 실행중인 컨테이너에 명령어를 전달하고 싶다면? : `docker exec <컨테이너 아이디> <명령어>`
- 실행되어져있는 `redis-cli` 안에 들어가서 redis client 실행 : `docker exec -it <컨테이너 ID> redis-cli`
    - -it 붙여줘야 명령어를 실행 한 후 계속 명령어를 적을 수 있다.
    - `-i` : Interactive 상호적인
    - `-t` : Terminal
        - ⇒ `-it`
- Docker 컨테이너 안의 터미널로 들어가기 : `docker exec -it <컨테이너 ID> sh`

## 이미지 만들기

---

- Dockerfile

```bash
# 베이스 이미지 명시
FROM alpine

# 추가적으로 필요한 파일들을 다운로드 받는다.
#RUN command

# 컨테이너 시작시 실행 될 명령어를 명시해준다.
CMD ["echo", "hello"]
```

- terminal

```bash
# 도커 파일이있는 Dockerfile 찾아서 이미지 생성
docker build ./

# 이미지 이름 명시하기
# docker build -t 도커허브아이디/프로젝트명:태그 Dockerfile찾을 위치
docker build -t kdh92417/hello:latest ./
```

<br>

## node.js 컨테이너에서 실행

---

```bash
# docker run -p <로컬포트>:<컨테이너포트> <이미지ID>
docker run -p 5000:8080 b21b64674253
```

```docker
FROM node:10

# 워크 디텍토리 지정
WORKDIR /usr/src/app

COPY ./ ./

RUN npm install

CMD ["node", "server.js"]
```

```docker
FROM node:10

# 워크 디텍토리 지정
WORKDIR /usr/src/app

# 변경된 코드만 빌드
COPY package.json ./

RUN npm install

# 종속성이 변경되지 않으면 캐쉬되어있으므로 변경되지않고 바로사용
COPY ./ ./

CMD ["node", "server.js"]
```

<br>

- **Volume 사용해서 어플리케이션 실행**

```docker
# 호스트 디텍토리에 node_modules은 없기에 컨테이너에 맵핑을 하지 말라고 하는 것
-v /usr/src/app/node_modules

# pwd 경로에 있는 디텍토리 혹은 파일을 /usr/arc/app 경로에서 참조
-v $(pwd):/usr/src/app

# 전체 명령어
docker run -p 5000:8080 -v /usr/src/app/node_modules -v $(pwd):/usr/src/app kdh92417/nodejs
```
<br>

### Yaml 파일이란?

Yaml : ain't markup language의 약자

XML 이나 json 포맷으로 많이 쓰였지만, 좀 더 사람이 읽기 쉬운 포맷으로 나타난 파일 구조

```bash
docker-compose up # 이미지가 없을때 이미지를 빌드하고 컨테이너 시작
doker-compose up --build # 이미지가 있든 없든 이미지를 빌드하고 컨테이너 시작
```
<br>
<br>

## Docker로 React App 배포

```bash
# Dockerfile.dev build
# -f 옵션 : Dockerfile.dev 를 강제로 찾기위한 옵션
# docker build -f <파일명> 찾을경로
docker build -f Dockerfile.dev ./
```