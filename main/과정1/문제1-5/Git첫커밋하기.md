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

## ✅ 리눅스 터미널에서 파일 수정하는 방법 정리

```bash
# 📌 1. 명령어로 직접 파일 생성 또는 수정

echo "print('Hello, world!')" > app.py     # ▶ 새로 작성 또는 기존 내용 덮어쓰기
echo "print('Append this line')" >> app.py # ▶ 기존 파일 맨 아래에 추가

# 📌 2. 텍스트 에디터로 직접 수정 (CLI 편집기 사용)

# nano: 가장 쉬운 편집기 (GUI 느낌 있음)
nano app.py
# 저장: Ctrl + O → Enter / 종료: Ctrl + X

# vim: 강력하지만 복잡한 편집기
vim app.py
# i (수정 시작), ESC, :wq (저장 후 종료)

# vi: vim의 기본 버전
vi app.py

# VSCode GUI 에디터로 열기 (code 명령어 등록 필요)
code app.py

# 📌 3. Git과 연동해 커밋하기

git add app.py
git commit -m "Update app.py with print message"

# 결과: 터미널 안에서 작성 → Git 커밋까지 한 번에 처리 가능
```

---

## ✅ 요약

| 항목 | 설명 |
|------|------|
| echo > 파일 | 파일 새로 쓰기 (덮어씀) |
| echo >> 파일 | 파일 내용 맨 아래에 추가 |
| nano 파일명 | 터미널 기반 간편 편집기 |
| vim 파일명 | 전문가용 강력한 편집기 |
| git add + commit | Git 버전 기록까지 가능 |
