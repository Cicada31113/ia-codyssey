import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.lines import Line2D


def find_shortest_path(area_df: pd.DataFrame, start: tuple, end: tuple) -> list:
    """BFS to find shortest path avoiding construction sites."""
    walkable = {(x, y) for x, y, cs in zip(
        area_df['x'], area_df['y'], area_df['ConstructionSite']
    ) if cs != 1}

    prev = {}
    visited = {start}
    queue = deque([start])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        cur = queue.popleft()
        if cur == end:
            break
        for dx, dy in directions:
            nxt = (cur[0] + dx, cur[1] + dy)
            if nxt in walkable and nxt not in visited:
                visited.add(nxt)
                prev[nxt] = cur
                queue.append(nxt)

    # 경로 되짚기
    path = []
    node = end
    while node != start:
        path.append(node)
        node = prev.get(node)
        if node is None:
            return []  # No path found
    path.append(start)
    return path[::-1]


def draw_path_map(area_df: pd.DataFrame, path: list, output_path: str) -> None:
    """Visualize map and overlay shortest path, then save image."""
    x_max, y_max = area_df['x'].max(), area_df['y'].max()
    plt.figure(figsize=(8, 8))
    plt.xticks(range(1, x_max + 1)); plt.yticks(range(1, y_max + 1))
    plt.grid(True)
    # y-axis is now standard orientation (origin bottom-left)

    marker = {
        'ConstructionSite': ('s', 'gray', 200),
        'Apartment':        ('o', 'saddlebrown', 150),
        'Building':         ('o', 'saddlebrown', 150),
        'BandalgomCoffee':  ('s', 'green', 180),
        'MyHome':           ('^', 'green', 180),
    }

    for _, row in area_df.iterrows():
        key = 'ConstructionSite' if row['ConstructionSite'] == 1 else row['structure']
        m, c, s = marker.get(key, ('o', 'white', 100))
        plt.scatter(row['x'], row['y'], marker=m, s=s, facecolor=c)

    if path:
        xs, ys = zip(*path)
        plt.plot(xs, ys, color='red', linewidth=2, label='Path')

    legends = [
        Line2D([0], [0], marker=m, color='w', label=lbl,
               markerfacecolor=c, markersize=10)
        for lbl, (m, c, _) in marker.items()
    ]
    legends.append(Line2D([0], [0], color='red', lw=2, label='Path'))
    plt.legend(handles=legends, loc='upper right')

    plt.title('Path to Bandalgom Coffee')
    plt.savefig(output_path)
    plt.close()


def main(base_url: str) -> None:
    """Load data, compute shortest path, save CSV and map image."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"📍 Script directory: {script_dir}")

    map_df = pd.read_csv(f"{base_url}/area_map.csv")
    struct_df = pd.read_csv(f"{base_url}/area_struct.csv")
    cat_df = pd.read_csv(f"{base_url}/area_category.csv")

    for df in (map_df, struct_df, cat_df):
        df.columns = df.columns.str.strip()
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].str.strip()

    id2name = dict(zip(cat_df['category'], cat_df['struct']))
    struct_df['structure'] = struct_df['category'].map(id2name)

    area_df = pd.merge(struct_df, map_df, on=['x', 'y'])

    start_df = area_df.loc[area_df['structure'] == 'MyHome', ['x', 'y']]
    end_df   = area_df.loc[area_df['structure'] == 'BandalgomCoffee', ['x', 'y']]
    if start_df.empty or end_df.empty:
        raise ValueError('Start or end position not found in data.')
    start = tuple(start_df.iloc[0])
    end   = tuple(end_df.iloc[0])
    print(f"🚩 Start at: {start}, End at: {end}")

    path = find_shortest_path(area_df, start, end)
    if not path:
        print("⚠️ No path found.")
    else:
        print(f"🛣 Path length: {len(path)} steps.")

    csv_path = os.path.join(script_dir, 'home_to_cafe.csv')
    pd.DataFrame(path, columns=['x', 'y']).to_csv(csv_path, index=False)
    print(f"✅ Saved path CSV to: {csv_path}")

    img_path = os.path.join(script_dir, 'map_final.png')
    draw_path_map(area_df, path, img_path)

