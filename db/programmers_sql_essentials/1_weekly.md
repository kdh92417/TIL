### 1주차 과제

- 9문제중 7문제 반 정답
- 7번문제는 등록테이블에 고유한 학번만 저장되는 것이 아니라서 `학수번호 != 100` 연산으로 풀면 안됨
- 9번 문제는 기말시험컬럼이 `NULL` 만 조인해야되기 때문에 `LEFT OUTER JOIN` 해야됨

전체적으로 조인할 때 셀렉을 먼저해야 성능의 이점을 가져갈 수 있다는 것을 배움

![1주차 과제 1](https://user-images.githubusercontent.com/58774316/156185313-4e8138b7-e3fd-46bc-a52e-1897be3fe81e.jpg)
![1주차 과제 2](https://user-images.githubusercontent.com/58774316/156185896-eadf6475-c514-4403-8276-dbfa050bb445.jpg)
