import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque

# 1. caffee_map.py 코드 로딩
url_py = 'https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/caffee_map.py'
response = urllib.request.urlopen(url_py)
code = response.read().decode('utf-8')
exec(code)

# 2. 데이터 준비
merged = load_and_prepare_data()

# 3. 위치 추출
home = merged[merged['struct_name'] == 'MyHome'][['x_struct', 'y_struct']].iloc[0]
cafe = merged[merged['struct_name'] == 'BandalgomCoffee'][['x_struct', 'y_struct']].iloc[0]
start = (int(home['x_struct']), int(home['y_struct']))
goal = (int(cafe['x_struct']), int(cafe['y_struct']))

# 4. 장애물 설정
obstacles = set(merged[merged['struct_name'] == 'ConstructionSite'][['x_map', 'y_map']].apply(tuple, axis=1))

# 5. 이동 가능한 방향
moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 6. BFS 최단 경로 탐색
def bfs(start, goal, obstacles):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and (nx, ny) not in obstacles:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return []

path = bfs(start, goal, obstacles)

# 7. 경로 저장
df_path = pd.DataFrame(path, columns=['x', 'y'])
df_path.to_csv('home_to_cafe.csv', index=False)

# 8. 지도 시각화 (기존 + 빨간 경로 추가)
plt.figure(figsize=(10, 10))
plt.gca().invert_yaxis()
plt.grid(True, linestyle='--', color='gray')

for name, color, marker in [
    ('Apartment', 'saddlebrown', 'o'),
    ('Building', 'saddlebrown', 'o'),
    ('BandalgomCoffee', 'green', 's'),
    ('MyHome', 'green', '^'),
    ('ConstructionSite', 'gray', 's')
]:
    df = merged[merged['struct_name'] == name]
    x_col = 'x_struct' if name != 'ConstructionSite' else 'x_map'
    y_col = 'y_struct' if name != 'ConstructionSite' else 'y_map'
    plt.scatter(df[x_col], df[y_col], c=color, marker=marker, label=name)

# 빨간 경로 추가
xs, ys = zip(*path)
plt.plot(xs, ys, color='red', linewidth=2, label='Path')

plt.title('최단 경로 시각화')
plt.legend(loc='upper right')
plt.savefig('map_final.png', dpi=300)
plt.show()
