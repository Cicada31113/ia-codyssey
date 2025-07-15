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
