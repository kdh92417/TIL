# Github 폴더 충돌 Error

### 문제

Github 레포에 푸쉬하였는데, 폴더가 충돌되어 파일이 올라가지지 않음

### 이유

`.git` 폴더가 하위폴더(frontend)에도 있기 때문에 충돌하여 발생하는 문제

<br>

## 해결

```bash
# 충돌난 폴더로 들어가 .git 폴더 삭제
rm -rf .git

# 상위 폴더에서 캐쉬된 파일 삭제
git rm --cashed . -rf
```

의 명령어를 차례대로 입력한뒤 다시 `add -> commit -> push`