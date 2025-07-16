## 📘 Git 주요 명령어 정리표

### 🛠 작업 영역 초기화 (start a working area)
| 명령어 | 설명 |
|--------|------|
| `git init` | 새 Git 저장소 초기화 또는 기존 저장소 재초기화 |
| `git clone [URL]` | 원격 저장소를 로컬로 복제 |

### ✍ 현재 변경 작업 (work on the current change)
| 명령어 | 설명 |
|--------|------|
| `git add [파일]` | 파일을 스테이지에 추가 |
| `git mv [기존] [새이름]` | 파일 또는 디렉토리 이동/이름 변경 |
| `git restore [파일]` | 작업 트리의 파일 복원 |
| `git rm [파일]` | 파일을 Git에서 삭제 (작업 디렉토리 및 인덱스에서 제거) |

### 🔍 이력 및 상태 확인 (examine the history and state)
| 명령어 | 설명 |
|--------|------|
| `git bisect` | 버그를 도입한 커밋을 이진 탐색으로 찾기 |
| `git diff` | 변경사항 비교 (커밋 간, 커밋과 작업트리 등) |
| `git grep [패턴]` | 특정 패턴을 포함한 라인 검색 |
| `git log` | 커밋 로그 보기 |
| `git show` | 커밋 상세 정보 보기 |
| `git status` | 현재 작업 상태 확인 (스테이징 여부 등) |

### 🌱 브랜치 및 커밋 관련 (grow, mark and tweak your common history)
| 명령어 | 설명 |
|--------|------|
| `git branch` | 브랜치 생성/삭제/목록 조회 |
| `git commit -m "[메시지]"` | 변경사항 커밋 |
| `git merge [브랜치]` | 브랜치를 병합 |
| `git rebase [브랜치]` | 브랜치 베이스 변경 (커밋 재적용) |
| `git reset [옵션]` | HEAD 및 인덱스/작업 디렉토리 상태 초기화 |
| `git switch [브랜치]` | 브랜치 전환 |
| `git tag [이름]` | 태그 생성, 목록 조회, 삭제 등 |

### 🤝 원격 저장소 협업 (collaborate)
| 명령어 | 설명 |
|--------|------|
| `git fetch` | 원격 저장소에서 최신 변경사항 가져오기 (병합은 하지 않음) |
| `git pull` | fetch + merge (원격 변경사항을 가져와 병합) |
| `git push` | 로컬 커밋을 원격 저장소에 업로드 |

---

### 🧩 기타 도움말
- `git help [명령어]` : 해당 명령어 상세 설명 보기  
- `git help -a` : 사용 가능한 모든 명령어 목록 출력  
- `git help -g` : 개념별 도움말 출력
