import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def draw_area1_map(base_url: str, output_path: str = 'map.png') -> None:
    """Visualize area 1 map with structures and save to image."""
    # 데이터 불러오기
    map_df = pd.read_csv(f"{base_url}/area_map.csv")
    struct_df = pd.read_csv(f"{base_url}/area_struct.csv")
    category_df = pd.read_csv(f"{base_url}/area_category.csv")

    # 컬럼명 공백 제거
    for df in (map_df, struct_df, category_df):
        df.columns = df.columns.str.strip()

    # 구조물 이름 매핑
    id_to_name = dict(zip(category_df['category'], category_df['struct']))
    struct_df['structure'] = struct_df['category'].map(id_to_name)

    # 병합 및 area 1 필터링
    merged = pd.merge(struct_df, map_df, on=['x', 'y'])
    area1 = merged.loc[merged['area'] == 1]

    # 그래프 설정
    x_max, y_max = area1['x'].max(), area1['y'].max()
    plt.figure(figsize=(8, 8))
    plt.xticks(range(1, x_max + 1)); plt.yticks(range(1, y_max + 1))
    plt.grid(True)
    plt.gca().invert_yaxis()

    # 마커 그리기 정의
    marker_settings = {
        'ConstructionSite': {'marker': 's', 'facecolor': 'gray', 'size': 200},
        'Apartment':        {'marker': 'o', 'facecolor': 'saddlebrown', 'size': 150},
        'Building':         {'marker': 'o', 'facecolor': 'saddlebrown', 'size': 150},
        'BandalgomCoffee':  {'marker': 's', 'facecolor': 'green', 'size': 180},
        'MyHome':           {'marker': '^', 'facecolor': 'green', 'size': 180},
    }

    for _, row in area1.iterrows():
        x, y = row['x'], row['y']
        if row.get('ConstructionSite', 0) == 1:
            cfg = marker_settings['ConstructionSite']
        else:
            cfg = marker_settings.get(row['structure'])
        plt.scatter(x, y, marker=cfg['marker'], s=cfg['size'], facecolor=cfg['facecolor'])

    # 범례 생성
    legend_elements = [
        Line2D([0], [0], marker=cfg['marker'], color='w', label=label,
               markerfacecolor=cfg['facecolor'], markersize=10)
        for label, cfg in marker_settings.items()
    ]
    plt.legend(handles=legend_elements, loc='upper right')

    # 제목 및 저장
    plt.title('BandalGom Coffee Map')
    plt.savefig(output_path)
    plt.close()


if __name__ == '__main__':
    base_raw_url = (
        'https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/'
        '1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/'
        '%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8'
    )
    draw_area1_map(base_raw_url)
