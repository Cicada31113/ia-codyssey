import matplotlib
matplotlib.use('Agg')  # 파일 저장 전용 백엔드 사용

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.lines import Line2D

# 📦 1. 데이터 로딩 및 전처리
def load_and_clean(base_url: str, filename: str) -> pd.DataFrame:
    """
    base_url에서 filename.csv를 불러와 컬럼명과 문자열 내 공백을 제거합니다.
    """
    try:
        df = pd.read_csv(f"{base_url}/{filename}.csv")
    except Exception as e:
        raise RuntimeError(f"CSV 로딩 실패: {filename}.csv - {e}")
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include='object').columns:
        df[col] = df[col].astype(str).str.strip()
    return df

# 📦 2. 지도 데이터 구축
def build_map(base_url: str) -> pd.DataFrame:
    """
    area_map, area_struct, area_category 데이터를 불러와 구조물 이름을 매핑하고 병합합니다.
    """
    map_df      = load_and_clean(base_url, "area_map")
    struct_df   = load_and_clean(base_url, "area_struct")
    category_df = load_and_clean(base_url, "area_category")

    id2name = dict(zip(category_df['category'], category_df['struct']))
    struct_df['structure'] = struct_df['category'].map(id2name).fillna('Unknown')

    merged = pd.merge(struct_df, map_df, on=['x', 'y'], how='inner')
    if merged.empty:
        raise RuntimeError("병합된 데이터가 없습니다. x,y 매칭을 확인하세요.")
    return merged

# 📌 3. 시작/도착 좌표 추출
def find_positions(df: pd.DataFrame, start_label: str = 'MyHome', end_label: str = 'BandalgomCoffee') -> tuple:
    df['structure'] = df['structure'].astype(str).str.strip()
    start_df = df.loc[df['structure'] == start_label]
    end_df   = df.loc[df['structure'] == end_label]
    if start_df.empty or end_df.empty:
        available = sorted(df['structure'].unique())
        raise ValueError(f"필수 구조물 누락: {start_label} 또는 {end_label} 없음. 현재: {available}")
    start = (int(start_df.iloc[0]['x']), int(start_df.iloc[0]['y']))
    end   = (int(end_df.iloc[0]['x']),   int(end_df.iloc[0]['y']))
    return start, end

# 📌 4. BFS 최단 경로 탐색
def bfs_shortest_path(start: tuple, end: tuple, walkable: set) -> list:
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    visited = {start}
    prev = {}
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur == end:
            break
        for dx, dy in directions:
            neighbor = (cur[0] + dx, cur[1] + dy)
            if neighbor in walkable and neighbor not in visited:
                visited.add(neighbor)
                prev[neighbor] = cur
                queue.append(neighbor)
    if end not in prev and start != end:
        raise RuntimeError("경로 탐색 실패: 시작지와 도착지를 연결할 수 없습니다.")
    path = []
    node = end
    while node != start:
        path.append(node)
        node = prev[node]
    path.append(start)
    return list(reversed(path))

# 📌 5. 지도 시각화 및 경로 저장 (y축 방향 수정)
def visualize_map(df: pd.DataFrame, path: list, output_file: str) -> None:
    plt.figure(figsize=(10,10))
    max_x, max_y = df['x'].max(), df['y'].max()
    plt.xticks(range(1, max_x+1))
    plt.yticks(range(1, max_y+1))
    plt.grid(True)

    # invert_yaxis 제거: 기본적으로 y축 1이 하단, max가 상단
    # plt.gca().invert_yaxis()

    for _, r in df.iterrows():
        x, y = int(r['x']), int(r['y'])
        s = r['structure']
        if r.get('ConstructionSite',0) == 1:
            plt.scatter(x, y, marker='s', color='gray', s=200, zorder=2)
        elif s in ['Apartment','Building']:
            plt.scatter(x, y, marker='o', color='saddlebrown', s=150, zorder=2)
        elif s == 'BandalgomCoffee':
            plt.scatter(x, y, marker='s', color='green', s=180, zorder=2)
        elif s == 'MyHome':
            plt.scatter(x, y, marker='^', color='green', s=180, zorder=2)

    xs, ys = zip(*path)
    plt.plot(xs, ys, color='red', linewidth=2, zorder=3)

    legend_elems = [
        Line2D([0],[0], marker='o', color='w', label='Apartment/Building', markerfacecolor='saddlebrown', markersize=10),
        Line2D([0],[0], marker='s', color='w', label='BandalgomCoffee', markerfacecolor='green', markersize=10),
        Line2D([0],[0], marker='^', color='w', label='MyHome', markerfacecolor='green', markersize=10),
        Line2D([0],[0], marker='s', color='w', label='ConstructionSite', markerfacecolor='gray', markersize=10),
        Line2D([0],[0], color='red', lw=2, label='Path')
    ]
    plt.legend(handles=legend_elems, loc='upper right')
    plt.title('Path from MyHome to BandalgomCoffee')
    plt.savefig(output_file)
    plt.close()

# 🚀 6. Main 실행부
if __name__ == '__main__':
    BASE_URL = (
        "https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/"
        "1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/"
        "%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8"
    )
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        df = build_map(BASE_URL)
        print("\n📊 구조물 종류별 개수:")
        print(df['structure'].value_counts())
        start, end = find_positions(df)
        print(f"출발지: {start}, 도착지: {end}")
        walkable = {(int(r['x']), int(r['y'])) for _, r in df.iterrows() if r.get('ConstructionSite',0) != 1}
        path = bfs_shortest_path(start, end, walkable)
        csv_path = os.path.join(script_dir, 'home_to_cafe.csv')
        img_path = os.path.join(script_dir, 'map_final.png')
        pd.DataFrame(path, columns=['x','y']).to_csv(csv_path, index=False)
        visualize_map(df, path, img_path)
        print(f"✅ 파일 생성 완료: {csv_path}, {img_path}")
    except Exception as err:
        print(f"오류 발생: {err}")
        sys.exit(1)
