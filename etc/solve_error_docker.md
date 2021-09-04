# Golang & Mysql 컴포즈로 컨테이너 실행시 오류 해결

## Dockerfile

```docker
# FROM golang:1.11
FROM golang:1.15.7

LABEL version=0.1
LABEL name=go_revel

ENV GOPATH $GOPATH:/go/src

#RUN apt-get update && \
#    apt-get upgrade -y

RUN go get github.com/revel/revel
RUN go get github.com/revel/cmd/revel
RUN go get github.com/jinzhu/gorm
RUN go get github.com/go-sql-driver/mysql

RUN mkdir /go/src/myapp

ENTRYPOINT systemctl run test_app

EXPOSE 9000
```

원래는 BaseImage가 `golang:1.11` 이었는데, 고랭의 상위버전인 `golang:1.15.7` 로 빌드하니 해결되었다.