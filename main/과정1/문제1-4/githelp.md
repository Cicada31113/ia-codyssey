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

### 🧾 git <command> <args> 구조 요약

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



These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone     Clone a repository into a new directory
   init      Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add       Add file contents to the index
   mv        Move or rename a file, a directory, or a symlink
   restore   Restore working tree files
   rm        Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect    Use binary search to find the commit that introduced a bug
   diff      Show changes between commits, commit and working tree, etc
   grep      Print lines matching a pattern
   log       Show commit logs
   show      Show various types of objects
   status    Show the working tree status

grow, mark and tweak your common history
   branch    List, create, or delete branches
   commit    Record changes to the repository
   merge     Join two or more development histories together
   rebase    Reapply commits on top of another base tip
   reset     Reset current HEAD to the specified state
   switch    Switch branches
   tag       Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch     Download objects and refs from another repository
   pull      Fetch from and integrate with another repository or a local branch
   push      Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
See 'git help git' for an overview of the system.
