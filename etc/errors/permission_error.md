# VSCODE로 SSH로 접근해서 편집 파일을 저장할때 permission 문제


### 상황

vscode로 ssh remote연결 했을 시 permission 에러가 뜸

### 문제 원인

해당 폴더를 root권한으로 생성하여서 다른계정으로 접근한 vscode에서 permission error가 뜬 것

<br>

## 해결

해당 폴더의 소유자를 vscode에서 접근한 계정으로 바꿔주면 된다.

```bash
sudo chown -R [계정] *
```