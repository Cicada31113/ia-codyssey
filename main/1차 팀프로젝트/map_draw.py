import pandas as pd
import matplotlib.pyplot as plt   # matplotlib -> 전체 그래픽 패키지(그림 그리는 도구 모음) -> 하지만 너무 크고 복잡
                                  # pyplot -> matplotlib 안에 있는 간편한 그림 도구 모음 상자

base_raw_url = (
    "https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/"
    "1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/"
    "%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8"
)

# 🔹 데이터 불러오기
map_df = pd.read_csv(f"{base_raw_url}/area_map.csv")
struct_df = pd.read_csv(f"{base_raw_url}/area_struct.csv")
category_df = pd.read_csv(f"{base_raw_url}/area_category.csv")

map_df.columns = map_df.columns.str.strip()
struct_df.columns = struct_df.columns.str.strip()
category_df.columns = category_df.columns.str.strip()

# 🔹 구조물 이름 매핑
id_to_name = dict(zip(category_df['category'], category_df['struct']))
struct_df['structure'] = struct_df['category'].map(id_to_name)

# 🔹 병합 및 필터링
merged_df = pd.merge(struct_df, map_df, on=['x', 'y'])
area1_df = merged_df[merged_df['area'] == 1]

x_max = area1_df['x'].max()
y_max = area1_df['y'].max()

plt.figure(figsize=(10, 10))
plt.xticks(range(1, x_max + 1))
plt.yticks(range(1, y_max + 1))
plt.grid(True)
plt.gca().invert_yaxis()

for _, row in area1_df.iterrows():
    x, y = row['x'], row['y']
    structure = row['structure']
    is_obstacle = row['ConstructionSite'] == 1

    if is_obstacle:
        plt.scatter(x, y, marker='s', color='gray', s=200)  # 건설현장
    elif structure == 'Apartment' or structure == 'Building':
        plt.scatter(x, y, marker='o', color='saddlebrown', s=150)  # 원형
    elif structure == 'BandalgomCoffee':
        plt.scatter(x, y, marker='s', color='green', s=180)  # 사각형
    elif structure == 'MyHome':
        plt.scatter(x, y, marker='^', color='green', s=180)  # 삼각형

from matplotlib.lines import Line2D

legend_elements = [
    Line2D([0], [0], marker='o', color='w', label='Apartment/Building',
           markerfacecolor='saddlebrown', markersize=10),
    Line2D([0], [0], marker='s', color='w', label='BandalgomCoffee',
           markerfacecolor='green', markersize=10),
    Line2D([0], [0], marker='^', color='w', label='MyHome',
           markerfacecolor='green', markersize=10),
    Line2D([0], [0], marker='s', color='w', label='ConstructionSite',
           markerfacecolor='gray', markersize=10)
]

plt.legend(handles=legend_elements, loc='upper right')

plt.title('BandalGom Coffee Map')
plt.savefig('map.png')
plt.show()
