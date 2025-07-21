import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
import urllib.request
import os

# GitHub에서 caffee_map.py 코드 불러오기
url_py = 'https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/caffee_map.py'
response = urllib.request.urlopen(url_py)
code = response.read().decode('utf-8')
exec(code)

def bfs(start, goal, obstacles):
    queue = deque([(start, [start])])
    visited = set()
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (nx, ny) not in visited and (nx, ny) not in obstacles:
                visited.add((nx, ny))
                queue.append(((nx, ny), path + [(nx, ny)]))
    return []

def draw_path(merged, path, savefile):
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

    if path:
        xs, ys = zip(*path)
        plt.plot(xs, ys, color='red', linewidth=2, label='Path')

    plt.title(savefile)
    plt.legend(loc='upper right')
    try:
        plt.savefig(savefile, dpi=300)
        print(f"✅ 이미지 저장 성공: {savefile}")
    except Exception as e:
        print(f"❌ 이미지 저장 실패: {e}")
    plt.close()

def main():
    merged = load_and_prepare_data()

    home = merged[merged['struct_name'] == 'MyHome'][['x_struct', 'y_struct']].iloc[0]
    cafe = merged[merged['struct_name'] == 'BandalgomCoffee'][['x_struct', 'y_struct']].iloc[0]
    start = (int(home['x_struct']), int(home['y_struct']))
    goal = (int(cafe['x_struct']), int(cafe['y_struct']))

    obstacles = set(merged[merged['struct_name'] == 'ConstructionSite'][['x_map', 'y_map']].apply(tuple, axis=1))

    shortest_path = bfs(start, goal, obstacles)
    pd.DataFrame(shortest_path, columns=['x', 'y']).to_csv('home_to_cafe.csv', index=False)
    draw_path(merged, shortest_path, 'map_final.png')

    key_structs = merged[merged['struct_name'].isin(['Apartment', 'Building', 'BandalgomCoffee', 'MyHome'])]
    points = list(set(key_structs[['x_struct', 'y_struct']].apply(lambda row: (int(row['x_struct']), int(row['y_struct'])), axis=1)))

    visited = set()
    current = start
    bonus_path = []
    fail_safe = 0

    while points:
        points = [p for p in points if p not in visited]
        if not points:
            break
        valid_paths = [(p, bfs(current, p, obstacles)) for p in points]
        valid_paths = [(p, path) for p, path in valid_paths if path]
        if not valid_paths:
            print("[보너스 종료] 더 이상 갈 수 있는 구조물이 없음.")
            break
        nearest, segment = min(valid_paths, key=lambda x: len(x[1]))
        bonus_path += segment[:-1]
        visited.add(nearest)
        current = nearest
        fail_safe += 1
        if fail_safe > 100:
            print("[보너스 종료] 무한 루프 방지용 중단")
            break

    bonus_path.append(current)

    print("\n▶ 보너스 경로 길이:", len(bonus_path))
    print("▶ 보너스 경로 앞쪽:", bonus_path[:10])
    print("▶ 현재까지 방문한 구조물 수:", len(visited))

    if len(bonus_path) >= 2:
        pd.DataFrame(bonus_path, columns=['x', 'y']).to_csv('bonus_all_structures_path.csv', index=False)
        draw_path(merged, bonus_path, 'map_bonus.png')
        print("✅ [map_bonus.png] 저장 완료")
    else:
        print("❌ [보너스 실패] 경로가 너무 짧음")

if __name__ == '__main__':
    main()