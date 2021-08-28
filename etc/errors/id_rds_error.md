# ssh 연결할 때 Error - “Permissions 0644 for '/root/.ssh/id_rsa' are too open.” 

## 해결

```bash
chmod 600 ~/.ssh/id_rsa
```