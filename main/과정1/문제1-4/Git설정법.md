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

