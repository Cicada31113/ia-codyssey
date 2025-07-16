## ✅ Git 초기 상태 명령어 흐름 정리

```bash
# 현재 상태 확인 (커밋 없음, staged 파일 있음)
git status

# 아직 커밋한 적이 없어서 로그는 에러 발생
git log
# fatal: your current branch 'main' does not have any commits yet

# 변경사항 비교해도 아직 차이가 없음 (이미 staged 상태라 diff 없음)
git diff

# ✅ 첫 커밋 진행
git commit -m "Initial commit"

# 이제부터 log 확인 가능
git log

# 파일 수정 예시
echo "# Hello" >> app.py

# 수정된 내용 비교
git diff

# 수정된 내용 스테이지에 올리고 커밋
git add app.py
git commit -m "Add header to app.py"

# 최종 확인
git log
git status
```
