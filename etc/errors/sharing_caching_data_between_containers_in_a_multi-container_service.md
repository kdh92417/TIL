# 다중 컨테이너 서비스에서 컨테이너간 캐싱 데이터 공유

## 문제 상황

Django Filecaching System을 이용하여 캐싱 데이터를 파일로 만들어 캐싱 하였으나, 다중 컨테이너 서비스에서 스케쥴러 컨테이너안에서 캐싱 데이터를 만들어서 API 컨테이너에서는 스케쥴러 컨테이너에서 생성된 캐싱 데이터를 사용하지 못함

<br>

## 해결

다중 컨테이너서비스를 실행시킬 때 캐싱 데이터를 가져다 쓰는 API 컨테이너와 캐싱 데이터를 주기적으로 저장하는 스케쥴러 컨테이너를 로컬과 마운트 시켜 파일 캐싱데이터를 사용할 수 있게 만들 었다.

### Code

```yml
    api:
        volumes:
        - ./api/exporter/django_cache:/data/exporter/django_cache
    scheduler:
        volumes:
        - ./api/exporter/django_cache:/data/exporter/django_cache
```

- [해당 상황을 고친 PR](https://github.com/NexClipper/exporterhub.io/pull/113/commits/d3aac7450bf2ca6e24e56d29baf10fe7f8edd0dd)