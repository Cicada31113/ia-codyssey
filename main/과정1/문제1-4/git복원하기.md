# 1. 백업
cp -r .git ../git_backup

# 2. 삭제
rm -rf .git

# 3. Git 상태 확인
git status    # → fatal 오류 나야 정상

# 4. 복원
cp -r ../git_backup .git

# 5. 다시 확인
git status    # → 원래처럼 돌아와야 정상
