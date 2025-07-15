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



### 🧾 Git 주요 명령어 요약표

| 분류 | 명령어 | 설명 |
|------|--------|------|
| 작업 시작 | `clone` | 원격 저장소를 복제하여 새 디렉토리 생성 |
|            | `init`  | 새로운 Git 저장소 초기화 또는 재설정 |

| 변경 작업 | `add`     | 파일을 Git 스테이지에 추가 |
|           | `mv`      | 파일/디렉토리 이동 또는 이름 변경 |
|           | `restore` | 워킹 트리 파일 복원 |
|           | `rm`      | Git과 워킹 트리에서 파일 제거 |

| 상태 및 히스토리 | `status` | 현재 워킹 트리 상태 표시 |
|                  | `log`    | 커밋 로그 출력 |
|                  | `diff`   | 변경 내용 비교 |
|                  | `show`   | Git 객체 상세 출력 |
|                  | `grep`   | 특정 패턴이 포함된 줄 검색 |
|                  | `bisect` | 버그 발생 커밋을 이진 탐색으로 찾기 |

| 히스토리 조작 | `commit` | 변경 사항 커밋 |
|              | `branch` | 브랜치 생성/삭제/목록 |
|              | `merge`  | 브랜치 병합 |
|              | `rebase` | 커밋을 다른 브랜치 위에 재적용 |
|              | `reset`  | HEAD를 이전 상태로 되돌리기 |
|              | `switch` | 브랜치 전환 |
|              | `tag`    | 태그 생성/확인/삭제 |

| 협업 | `fetch` | 원격 저장소에서 변경 내용 가져오기 |
|      | `pull`  | 가져오고(fetch) 병합하기(merge) |
|      | `push`  | 로컬 커밋을 원격 저장소로 푸시 |

> 💡 전체 명령어: `git help -a`  
> 개념 가이드: `git help -g`  
> 명령어 설명: `git help <명령어>`
