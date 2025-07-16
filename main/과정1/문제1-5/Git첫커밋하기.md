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


## ✅ `git commit` 은 어떤 파일을 커밋하는가?

```bash
# 기본 원칙:
# git commit은 "스테이징된 (staged) 파일만" 커밋한다.

# 예시 디렉토리 상태
~/Desktop/git_practice/
├── app.py        # ✅ git add 함 (staged)
├── secret.txt    # ❌ git add 안 함 (unstaged)
├── readme.md     # ❌ git add 안 함 (unstaged)

# 이 상태에서 커밋 실행
git commit -m "Initial commit"

# 👉 결과: 오직 app.py 만 커밋됨
```

---

## ✅ 커밋 대상 확인 방법

```bash
# 현재 어떤 파일이 커밋될지 확인
git status

# 출력 예시
Changes to be committed:
  new file:   app.py

Untracked files:
  secret.txt
  readme.md
```

---

## ✅ 추가 팁

```bash
# 모든 변경된 파일을 한꺼번에 스테이징할 경우:
git add .        # 현재 디렉토리 이하 전체
git add -A       # 삭제 포함 전체 변경사항

# 원하는 파일만 선택적으로 스테이징:
git add app.py
git add readme.md
```

---

## ✅ 핵심 요약

- `git commit`은 **반드시 `git add`로 스테이징된 파일만** 커밋됨
- 디렉토리에 파일이 존재해도, 스테이징되지 않으면 커밋되지 않음
- 커밋 전에는 반드시 `git status`로 확인할 것
