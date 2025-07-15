# git help
## usage: 
- git [--version]
- git [--help]
- git [-C <path>]
- git [-c <name>=<value>]
- git [--exec-path[=<path>]]
- git [--html-path]
- git [--man-path]
- git [--info-path]
- git [-p | --paginate | -P | --no-pager]
- git [--no-replace-objects]
- git [--bare]
- git [--git-dir=<path>]
- git [--work-tree=<path>]
- git [--namespace=<name>]
- git [--super-prefix=<path>]
- git [--config-env=<name>=<envvar>]
           <command> <args>

### 🧾 git [ command ]  [ args ] 구조 요약

- `<command>`: 실행할 Git 명령어 (예: `add`, `commit`, `clone`)
- `<args>`: 해당 명령어에 전달할 **인자(옵션/대상)**

#### 🔹 예시

- `git add file.py`  
  → `add` = 명령어, `file.py` = 인자

- `git commit -m "메시지"`  
  → `commit` = 명령어, `-m "메시지"` = 인자

#### 📌 요약

`[<args>]`는 명령어 뒤에 따라오는 추가 정보로,  
Git 명령어에 **무엇을 어떻게 적용할지 지정**하는 역할을 함.



T### 🧾 Git 주요 명령어 요약표 (분야별 분류)

| 구분 | 명령어 | 설명 (한글 번역) |
|------|--------|------------------|
| **🛠 작업 디렉토리 시작** <br>(`git help tutorial`) | `clone` | 원격 저장소를 복제하여 새로운 디렉토리 생성 |
|  | `init` | 빈 Git 저장소 생성 또는 기존 저장소 재초기화 |

| **📂 변경 작업 수행** <br>(`git help everyday`) | `add` | 파일을 Git 스테이지(index)에 추가 |
|  | `mv` | 파일/디렉토리/심볼릭 링크 이동 또는 이름 변경 |
|  | `restore` | 워킹 디렉토리의 파일 복원 |
|  | `rm` | 파일을 Git과 워킹 디렉토리에서 삭제 |

| **🔍 히스토리와 상태 확인** <br>(`git help revisions`) | `bisect` | 버그를 만든 커밋을 이진 탐색으로 찾기 |
|  | `diff` | 변경 사항 비교 (커밋 간, 커밋과 워킹트리 등) |
|  | `grep` | 패턴과 일치하는 줄을 출력 |
|  | `log` | 커밋 로그 출력 |
|  | `show` | 다양한 Git 객체 정보 표시 |
|  | `status` | 현재 작업 트리 상태 확인 |

| **📈 히스토리 관리/브랜치 작업** | `branch` | 브랜치 목록 보기/생성/삭제 |
|  | `commit` | 변경 사항을 커밋으로 기록 |
|  | `merge` | 다른 브랜치의 변경사항 병합 |
|  | `rebase` | 다른 브랜치 위에 커밋 다시 적용 |
|  | `reset` | 현재 HEAD를 특정 상태로 되돌리기 |
|  | `switch` | 다른 브랜치로 전환 |
|  | `tag` | GPG 서명된 태그 생성/조회/삭제/검증 |

| **🤝 협업/원격 저장소 연동** <br>(`git help workflows`) | `fetch` | 원격 저장소로부터 객체와 참조 정보 다운로드 |
|  | `pull` | fetch + merge (또는 rebase) 자동 실행 |
|  | `push` | 로컬 커밋을 원격 저장소로 전송 |

> ℹ️ 전체 명령어 목록은 `git help -a`  
> 개념별 가이드는 `git help -g`  
> 특정 명령어 도움말은 `git help <명령어>`

