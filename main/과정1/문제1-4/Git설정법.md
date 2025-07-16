# ✅ Git 전역 설정 전체 명령어 모음 (Linux/macOS 기준)

# 1. 개행문자 설정
# Windows인 경우: true
git config --global core.autocrlf true

# macOS/Linux인 경우: input
git config --global core.autocrlf input

# 2. 사용자 이름 설정
git config --global user.name "Your Name"

# 3. 사용자 이메일 설정
git config --global user.email "your.email@example.com"

# 4. 기본 브랜치명을 main으로 설정
git config --global init.defaultBranch main

# 5. 현재 전역 설정 목록 확인
git config --global --list

# 6. 설정 파일을 VS Code 에디터로 열기
code ~/.gitconfig

# 7. Git 기본 에디터를 VS Code로 지정
git config --global core.editor "code --wait"

# 8. 작업 디렉토리로 이동 (예시: app.py가 있는 폴더)
cd ~/Desktop/your_project_directory

# 9. 해당 폴더에 Git 저장소 초기화
git init



-----------------------------정리-------------------

## ✅ Git 기초 환경 설정 (Linux/macOS 기준)

| 단계 | 설명 | 명령어 / 방법 |
|------|------|----------------|
| (1) | Git 설치 확인 (이미 설치되어 있다면 생략) | `git --version` |
| (2) | 개행문자 설정 (macOS/Linux는 input) | `git config --global core.autocrlf input` |
| (3) | 사용자 이름/이메일 설정 | `git config --global user.name "Your Name"`<br>`git config --global user.email "your.email@example.com"` |
| (4) | 기본 브랜치명을 main으로 설정 | `git config --global init.defaultBranch main` |
| (5) | VSCode를 Git의 기본 에디터로 설정 | `git config --global core.editor "code --wait"` |
| (6) | 현재 Git 전역 설정 확인 | `git config --global --list` |
| (7) | 설정파일을 VSCode로 열기 | `code ~/.gitconfig`<br>※ 만약 위 명령어가 작동하지 않으면:<br>① VSCode 실행 → 새 파일 열기<br>② `Ctrl + H`로 숨김 파일 보기 활성화<br>③ 홈 디렉토리에서 `.gitconfig` 클릭 |
| (8) | Git 저장소 생성할 디렉토리로 이동 | `cd ~/Desktop/git` *(예시 경로)* |
| (9) | Git 저장소 초기화 | `git init` |


## ✅ Git 실습용 디렉토리 생성 및 초기화 명령어 정리

| 단계 | 설명 | 명령어 |
|------|------|--------|
| 1 | 바탕화면에 git_practice 폴더 생성 (중간 폴더 없을 경우 자동 생성) | `mkdir -p ~/Desktop/git_practice` |
| 2 | 해당 폴더로 이동 | `cd ~/Desktop/git_practice` |
| 3 | app.py 파일 생성 | `touch app.py` |
| 4 | Git 저장소 초기화 (버전관리 시작) | `git init` |


# ✅ 버전 관리 시스템의 종류 3가지

버전 관리 시스템(Version Control System, VCS)은
프로젝트의 파일(코드, 문서 등) 변경 이력을 저장하고,
필요할 때 과거로 되돌릴 수 있게 도와주는 시스템입니다.

아래는 대표적인 3가지 종류입니다:

| 종류 | 설명 |
|------|------|
| 1. 로컬 버전 관리 시스템 | 한 컴퓨터 안에서만 변경 이력을 관리합니다. <br>예: `RCS`, `SCCS` <br>단점: 다른 컴퓨터나 사람과 공유 불가능 |
| 2. 중앙 집중식 버전 관리 시스템 | 모든 이력이 한 중앙 서버에 저장됩니다. <br>예: `CVS`, `Subversion (SVN)` <br>장점: 협업 가능 <br>단점: 서버가 꺼지면 아무도 작업 못 함 |
| 3. 분산 버전 관리 시스템 (Git) | 모든 참여자가 전체 변경 이력을 복사해서 가집니다. <br>예: `Git`, `Mercurial` <br>장점: 인터넷 없어도 작업 가능, 백업이 여러 곳에 있어 안정적 |

---

# ✅ `.git` 디렉토리의 역할

Git 명령어 `git init`을 실행하면,
현재 폴더 안에 `.git`이라는 **숨겨진 디렉토리**가 생성됩니다.

이 `.git` 폴더는 **Git의 두뇌** 역할을 합니다.

| 역할 | 설명 |
|------|------|
| 🧠 변경 이력 저장 | 누가 언제 어떤 파일을 어떻게 바꿨는지 기록함 |
| 🛠️ 복구 기능 | 실수했을 때 과거 버전으로 되돌릴 수 있음 (`rollback`) |
| 🧾 커밋, 브랜치 정보 저장 | 프로젝트의 모든 스냅샷(기록)을 담고 있음 |
| 🔒 Git이 없으면 버전 관리 불가능 | `.git` 폴더가 삭제되면 Git은 해당 폴더를 더 이상 추적하지 않음 |

> 즉, `.git` 폴더는 Git이 작동하기 위한 **엔진** 같은 존재이며,  
> 이게 있어야 **Git 프로젝트**로 인식됩니다.
>
> # ✅ Git의 장단점 정리

Git은 전 세계적으로 가장 많이 쓰이는 **분산 버전 관리 시스템(DVCS)**입니다.  
혼자서도, 여러 명이 함께 작업할 때도 코드나 문서 변경 이력을 체계적으로 관리할 수 있게 도와줍니다.

---

## ✅ 장점 (Git이 좋은 이유)

| 장점 | 설명 |
|------|------|
| 1. 인터넷 없이도 작업 가능 | 내 컴퓨터에 전체 이력이 저장되므로 인터넷 없어도 버전 관리 가능 |
| 2. 실수해도 되돌릴 수 있음 | 과거 상태로 쉽게 돌아갈 수 있어 "Undo" 기능처럼 사용 가능 |
| 3. 여러 명이 동시에 작업 가능 | 협업에 최적화, 브랜치를 나눠서 각자 작업 후 병합 가능 |
| 4. 속도 빠름 | 로컬에서 작동하므로 서버 없이도 빠르게 동작함 |
| 5. 무료 + 오픈소스 | 누구나 자유롭게 사용할 수 있음 (GitHub과 함께 사용 가능) |
| 6. 히스토리 남음 | 누가 언제 어떤 변경을 했는지 기록으로 남아 추적 가능 |

---

## ❌ 단점 (처음엔 어렵게 느껴질 수 있음)

| 단점 | 설명 |
|------|------|
| 1. 명령어가 낯설고 어렵다 | `commit`, `merge`, `pull`, `push` 등 초보자에게 어렵게 느껴질 수 있음 |
| 2. 실수하면 충돌(conflict) 발생 가능 | 두 사람이 같은 파일을 동시에 바꾸면 충돌이 나고 직접 해결해야 함 |
| 3. `.git` 폴더가 삭제되면 끝 | 실수로 `.git` 디렉토리를 삭제하면 버전 관리가 완전히 끊어짐 |
| 4. 시각화가 약함 | GUI보다는 CLI 중심이라 직관적으로 보기 어려움 (물론 GUI 도구도 있음) |

---

## 💬 비유로 이해하면?

> Git은 마치 **자동 저장되는 문서 히스토리 + 백업 시스템 + 협업 도구**를 합친 것과 같음  
> 처음엔 조작법이 어렵지만, 익숙해지면 실수 복구·협업·버전 추적에 압도적으로 유리함



