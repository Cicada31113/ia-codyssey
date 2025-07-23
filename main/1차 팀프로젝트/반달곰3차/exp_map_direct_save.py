# ✅ 전체 구조 요약: map_direct_save.py
# 이 파일은 크게 3단계로 작동해:

# 데이터 로딩 및 정제
# → area_map.csv, area_struct.csv, area_category.csv를 불러와서 하나의 merged_df로 병합

# 지도 그리드 구조 생성 + BFS 경로 탐색
# → 구조물과 공사 현장을 기준으로 “걸을 수 있는지 아닌지” 정보를 가진 grid 딕셔너리 생성
# → 내 집(MyHome)에서 가까운 BandalgomCoffee까지 최단 경로를 BFS로 탐색

# 최단경로 시각화 및 저장
# → 지형, 구조물, 공사현장을 표시하고
# → 최단 경로를 빨간 선으로 그린 뒤 map_final.png로 저장하고
# → 경로 정보는 home_to_cafe.csv로 저장




import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import deque         # deque -> BFS에 필요한 큐 자료구조 (빠른 pop, append 위해)
                                      # collections는 기본 리스트나 딕셔너리보다 조금 더 특수한 자료형들을 제공해줌
                                        # deque : 양쪽에서 넣고 뺄 수 있는 큐 (double-ended queue)
                                        # counter : 리스트에 있는 요소들의 개수를 세줌
                                        # defaultdict : 값이 없을 때 자동으로 기본값을 만들어주는 딕셔너리
                                        # namedtuple : 이름 붙은 튜플
                                           # 큐 :"줄 서기"
                                              # FIFO (Fisrt-in First-out) 선입선출 구조
                                           # 튜플 :"수정할 수 없는 리스트"
                                              # 리스트처럼 여러 값을 묶을 수 있음.
                                              # 근데 한 번 만들면 내용을 바꿀 수는 없음
                                                 # 예시 :
                                                 #  python
                                                 # t = (3,5)
                                                 # print(t[0]) # 3
                                                     # -> '리스트'는 [ ] 사용 -> 수정 가능
                                                     # -> '튜플'은 ( ) 사용 -> 수정 불가능
                                                 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_and_clean_csv(file_name):
    path = os.path.join(BASE_DIR, file_name)
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    return df

# Load data
map_df = load_and_clean_csv('area_map.csv')
struct_df = load_and_clean_csv('area_struct.csv')
category_df = load_and_clean_csv('area_category.csv')

# Merge structure name
struct_df = struct_df.merge(category_df, how='left', on='category')
merged_df = struct_df.merge(map_df, how='left', on=['x', 'y'])

# Create map grid
grid = {}                                # grid : 좌표별 정보(걸을 수 있는지, 구조물 종류)를 담는 딕셔너리
home = None                           
cafe_candidates = []                     # 여러개의 커피숍 위치를 저장할 리스트
for _, row in merged_df.iterrows():
    x, y = int(row['x']), int(row['y'])
    key = (x, y)                                    # -> 좌표를 (x, y) 형태의 튜플로 만들어서 고정
    grid[key] = {                                   # 공사현장이 아니면  walkable=True 
        'walkable': row['ConstructionSite'] != 1,   # 구조물 종류는 type에 저장
        'type': row['struct']
    }
    if row['struct'] == 'MyHome':
        home = (x, y)
    elif row['struct'] == 'BandalgomCoffee':
        cafe_candidates.append((x, y))              # append(): 리스트에 값을 뒤에 추가하는 기능
                                                    # 예시:
                                                        # nums = [1, 2]
                                                        # nums.append(3)
                                                        # print(nums)
                                                        # -> [1, 2, 3]
                                                    # 즉 여기선, 커피숍 좌표를 리스트에 하나씩 모아두는 용도
                                                
# BFS implementation
def bfs(start, goal, grid):                  # BFS(너비 우선 탐색) 알고리즘의 시작함수
    queue = deque([(start, [start])])          # start:출발좌표/goal:목표좌표/grid:아까 만든 좌표별 정보 딕셔너리
    visited = set()                            # 여기서는 grid를 주의깊게 보자!
                                               # queue: 탐색할 노드를 저장하는 큐
    while queue:                                  # 형식은 (현재위치, 지금까지의 경로) 형태로 저장
        current, path = queue.popleft()        # visited: 이미 지나간 곳을 기록해서 중복탐색방지
        if current == goal:                    # [(start, [start])] 이 구조
            return path                             # 튜플 구조임
        if current in visited:                      # 두번째 값: 지금까지 지나온 경로. 처음이니까 아직은 출발점 하나뿐.
            continue                                # 예시: 
        visited.add(current)                        # "나는 지금(2,3)에 있고, 여태까지의 경로는 [(2,3)]이야"
                                                    # [start] : 경로 리스트 (처음이니까 출발점만 들어가 있음)
        x, y = current                          # set() : 중복없는 데이터 모음(집합)
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x + dx, y + dy
            neighbor = (nx, ny)
            if neighbor in grid and grid[neighbor]['walkable'] and neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    return []
                
                                    # x, y = current -> 지금 내가 있는 위치 current에서 x, y 좌표를 꺼냄
                                    # for dx, dy in [ ~ ] : 내 주변 네 방향을 차례로 본다는 뜻 (델타값)
                                    # if neighbor ~ <- 3가지 조건을 모두 만족해야 큐에 넣게되는 조건
                                       # 1. neighbor in grid: 좌표가 지도 안에 실제로 존재하는가
                                       # 2. grid[neighbor]['walkable']: 공사현장이 아닌가?(걸을 수 있는가)
                                       # 3. neighbor not in visited: 이기 가본 곳이 아닌가?
                                    # 조건 충족시, neighbor -> 다음 갈 좌표 / path + [neighbor]-> 지금까지의 경로에 새 좌표 붙임

            #우측 return []주의->>>      # 경로 못찾으면 return [] 반환 (실패시 빈리스트 내놓음)
                                       # 왜 [] 리스트를 쓰냐면, None을 쓸경우 len(path)에서 에러남
                                       # 하지만 []는 길이가 0인 정상 리스트니까 오류없이 작동함

# BFS 예시 시뮬레이션 
# 1️⃣ 시작                                   
# queue = deque([ ((1,1), [(1,1)]) ])
# visited = set()
# → (현재위치, 경로기록) 구조로 큐에 저장됨.

# 2️⃣ 첫 루프
# current, path = queue.popleft()              # popleft():큐의 가장 앞에 있는 값 꺼내기
# → current = (1,1), path = [(1,1)]
# → 이제 네 방향으로 움직여 봄:

# (0,1) ❌ 범위 밖 or 벽이라 패스
# (2,1) ✅ 갈 수 있으면 → ((2,1), [(1,1), (2,1)]) 큐에 추가 
# (1,0) ❌ 패스
# (1,2) ✅ 가능하면 → ((1,2), [(1,1), (1,2)]) 추가  -> "지금 나는 (1,2)에 있고, 여기까지 온길은 [(1,1), (2,1)]이야"

# queue = deque([
#     ((2,1), [(1,1), (2,1)]),
#     ((1,2), [(1,1), (1,2)])
# ])
# visited = {(1,1)}

# 3️⃣ 두 번째 루프
# current, path = queue.popleft()
# # current = (2,1), path = [(1,1), (2,1)]
# → 목표인 (3,1)까지 한 칸 남았음!
# (3,1) ✅ 도착 가능!
# → 경로는 [(1,1), (2,1), (3,1)]
# 이걸 return 해!

# ✅ 결과:
# python
# 코드 복사
# [(1,1), (2,1), (3,1)]
# 즉, 내 집에서 커피숍까지 어떻게 걸어가는지 좌표 리스트로 돌려주는 거야





# Find shortest path among multiple cafes
shortest_path = []                          # 처음엔 경로가 아무것도 없는 상태로 시작
for cafe in cafe_candidates:                # 후보 리스트 하나씩 돌아본다
    path = bfs(home, cafe, grid)            # 그 경로까지 BFS 돌림
    if path and (not shortest_path or len(path) < len(shortest_path)):
        shortest_path = path                 # 경로가 존재하며 + 지금까지의 최단 경로보다 짧으면
                                                    # -> 갱신 -> 저장

                        # 여러개의 커피숍 후보중 가장 가까운 곳으로 가보자잇~



# Save path to CSV        # [(x1,y1), (x2,y2)..] 이런 좌표리스트를 'x','y'라는 컬럼 이름 붙여서 테이블 만듦
path_df = pd.DataFrame(shortest_path, columns=['x', 'y'])
path_df.to_csv(os.path.join(BASE_DIR, 'home_to_cafe.csv'), index=False)
                                                 # index=False 는 행 번호(0,1,2...) 저장하지말라는 의미 
# Draw map with path(시각화 파트)
max_x = merged_df['x'].max() + 1
max_y = merged_df['y'].max() + 1

fig, ax = plt.subplots(figsize=(12, 12))

# Area background
area_colors = {0: '#fff8dc', 1: '#e6f2ff', 2: '#e6ffe6', 3: '#ffe6cc'}
for _, row in merged_df.iterrows():
    x, y, area = row['x'], row['y'], row['area']
    ax.add_patch(plt.Rectangle((x - 0.5, y - 0.5), 1, 1, color=area_colors.get(area, '#ffffff'), zorder=0))

# Construction sites            공사현장 그려보자잇~~~~~ 회색이다잇~
for (x, y), info in grid.items():
    if not info['walkable']:
        ax.add_patch(plt.Rectangle((x - 0.35, y - 0.35), 0.7, 0.7, color='gray', zorder=1))

# Structures                             # .items() 딕셔너리에서 자주 쓰는 기능
for (x, y), info in grid.items():           # 딕셔너리의 (key, value) 쌍을 하나씩 꺼내주는 함수.
    if not info['walkable']:                 # d = { 'a': 10, 'b': 20}
        continue                             # for k, v in d.items():
    struct = info['type']                    #     print(k, v)
    if struct == 'BandalgomCoffee':          # -> a 10    b 20 
        ax.add_patch(plt.Rectangle((x - 0.4, y - 0.4), 0.8, 0.8, color='green', zorder=2))
    elif struct == 'MyHome':
        ax.plot(x, y, marker='^', color='green', markersize=12, zorder=2)
    elif struct == 'Apartment':
        ax.plot(x, y, 'o', color='saddlebrown', markersize=10, zorder=2)
    elif struct == 'Building':
        ax.plot(x, y, 'o', color='saddlebrown', markersize=10, zorder=2)

# Path drawing                         빨간선 그릴거야~ 말리지마~
if shortest_path:                                         # matplotlib 에서 필요한 형식임.
    px, py = zip(*shortest_path)                          # zip() : 여러리스트를 짝지어서 묶어주는 함수
    ax.plot(px, py, color='red', linewidth=2, zorder=3)   # 여러개의 리스트를 병렬로 묶어서
                                                          # 한 덩어리씩 뽑을 수 있게 해줌.
# Grid lines                                              # 그렇게 px: x좌표만 / py: y좌표만
for x in range(1, max_x + 1):                             # ax.plot(px,py)에 넣어서 선연결
    ax.axvline(x, color='lightgray', linewidth=0.5, zorder=4)
for y in range(1, max_y + 1):
    ax.axhline(y, color='lightgray', linewidth=0.5, zorder=4)

# Final settings
ax.set_xlim(0.5, max_x + 0.5)
ax.set_ylim(0.5, max_y + 0.5)
ax.set_xticks(range(1, max_x + 1))
ax.set_yticks(range(1, max_y + 1))
ax.set_aspect('equal')
ax.invert_yaxis()
ax.set_title('Bandalgom Coffee - Shortest Path')

plt.savefig(os.path.join(BASE_DIR, 'map_final.png'))
plt.show()