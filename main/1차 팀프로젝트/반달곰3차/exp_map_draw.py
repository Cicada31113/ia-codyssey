# 📌 전체 흐름 단계별 정리
# 📂 area_map.csv, area_struct.csv, area_category.csv 파일 불러오기

# 🧩 구조물 ID → 이름(struct) 매칭 (category 기준 병합)

# 🗺️ 지도 좌표 정보(area_map)와 병합

# 🎨 area 색깔 → 배경 칠하기

# ⚠️ 건설현장(ConstructionSite) 회색으로 덧칠

# 🏠 구조물(집, 카페, 아파트 등) 표시

# #️⃣ 격자 라인 추가

# 🧾 범례(Legend) 넣기

# 🎯 축 설정, 제목 설정

# 💾 map.png로 저장



import pandas as pd
import matplotlib.pyplot as plt
import os           # 현재 이 코드 파일 있는 위치 알기위한 도구

# 현재 파일 경로 기준으로 상대경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_and_clean_csv(file_name):
    path = os.path.join(BASE_DIR, file_name)
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()
    return df

# 파일 불러오기
map_df = load_and_clean_csv('area_map.csv')
struct_df = load_and_clean_csv('area_struct.csv')
category_df = load_and_clean_csv('area_category.csv')

# 구조물 이름 병합
struct_df = struct_df.merge(category_df, how='left', on='category')

# 공사현장 정보 병합
merged_df = struct_df.merge(map_df, how='left', on=['x', 'y'])

# 좌표 범위 설정
max_x = merged_df['x'].max() + 1
max_y = merged_df['y'].max() + 1
                                
# ➡️ merged_df에 있는 모든 좌표 중에서
#    가장 오른쪽(x)과 가장 아래쪽(y)의 최대값을 찾은 다음 +1을 해줌

# 왜 +1 하냐면?
# → 나중에 그릴 때 “격자선을 넘지 않게” 여유를 주기 위해서임
#    즉, 끝 좌표도 포함되도록 범위를 조정한 것

# 🧠 예시:
# 좌표 최대값이 x=9면 → 9까지만 그리면 9칸이 안 보일 수 있으니까
# → max_x = 10으로 해서 축을 1~10까지 보이게 만드는 거야
# 🔎 이걸 왜 미리 해두냐면:
# 격자 그릴 때 범위를 알아야 하고
# 구조물이나 배경 칠할 때도 “지도의 전체 크기”를 알아야 하기 때문이야
# 특히 ax.set_xlim(), ax.set_xticks() 같은 축 관련 함수에서 바로 써






# 시각화 시작
fig, ax = plt.subplots(figsize=(12, 12))
# ➡️ `matplotlib`에서 그림 그릴 때 기본 구조는 fig(그림판 전체), ax(그림 안 축 영역) 두 개로 나뉘어

# - `fig`: 전체 도화지
# - `ax`: 실제로 도형, 선, 점 등을 그리는 구역

# ➡️ `figsize=(12, 12)`: 그림 크기를 12인치 × 12인치 정사각형으로 만든다는 의미
#    → 넉넉하게 키운 거. 나중에 구조물, 색상 등 시각요소가 많기 때문

# subpolots
  # 여러개의 그래프(축)를 한 번에 만들기 위한 기능  (하나 또는 여러개의 축(ax)를 동시에 만들기 위해 쓰는 함수)
  # 여기선 한개의 축만 생성하지만, fig랑 ax를 한줄로 동시에 만들 수 있어서 간편함에 사용.


# Area 구간 배경색 칠하기
def get_area_color(area):
    colors = {0: '#fff8dc', 1: '#e6f2ff', 2: '#e6ffe6', 3: '#ffe6cc'}
    return colors.get(area, '#ffffff')

# Area 구간 배경색 칠하기 구체화
for _, row in merged_df.iterrows():
    x, y, area = row['x'], row['y'], row['area']
    ax.add_patch(plt.Rectangle((x - 0.5, y - 0.5), 1, 1, color=get_area_color(area), zorder=0))
                # merged_df라는 표에서 한 줄씩 꺼내서 row라는 이름으로 써볼게"
                  # iterrows() : 행(row) 하나하나 꺼내주는 기능
                  # _ : 인덱스 번호는 안쓸거니까 버림
                  # 즉, 지도 전체를 돌면서 하나하나 셀 정보를 꺼낼거라는 의미.

                # ax.add_patch(...) : 그림판(ax)에 사각형 하나를 덧붙일게
                  # patch: 쉽게 말해 '그림조각'이라고 보면됨 (사각형, 원 등)
                  # (x - 0.5, y - 0.5): 사각형의 왼쪽 아래 꼭짓점 위치
                    # -0.5 하는 이유는 셀 중심(x,y)을 기준으로 1칸짜리 사각형 만들려면 
                    # 반 칸씩 좌우/상하로 빼줘야됨
                  # 1,1 => 가로 1칸, 세로 1칸짜리 사각형
                  # color=get_area_color(area) -> 지역번호(area)에 맞는 색깔로 칠함
                  # zorder=0 -> 가장 밑바닥에 깔아라 (나중에 구조물은 위에 올릴거니까)
                    # zorder 숫자가 클수록 -> 더 위에 그려짐
                    # zorder 숫자가 작을수록 -> 밑에 깔림
            # 요약 : plt.Rectangle()이 만들어질때, 왼쪽 아래 꼭짓점기준
                  # matplotlib 좌표계는 왼쪽 아래가 기준점임.
            # 그래서 -0.5 씩 안빼주면 어긋나는 문제가 발생 !!!!!!! [[[[주의]]]]
                  # 우리가 CSV파일에서 들고있는 좌표값들은 "셀중심기준임" 
                  # 이걸 고려안하게되면 오른쪽 위로 셀 배경색칠이 치우치게됨


# ConstructionSite만 추려서 따로 그림
construction_sites = merged_df[merged_df['ConstructionSite'] == 1][['x', 'y']]
construction_coords = set((row.x, row.y) for _, row in construction_sites.iterrows())
                       # merged_df에서 "공사현장 표시가 있는 셀"만 뽑아올거임
                       # 그 중에서 x, y 좌표만 추려냄   -> 공사현장 좌표만 있는 표가 만들어짐

                       # set() : 파이썬에서 "중복 없이 저장하는 집합"
                          # 예시 : set([1, 2, 2, 3]) -> {1, 2, 3}
                          # -> 공사현장 좌표가 중복돼 있을 수 있어서 제거용으로 쓴거임

for (x, y) in construction_coords:
    ax.add_patch(plt.Rectangle((x - 0.35, y - 0.35), 0.7, 0.7, color='gray', zorder=1))
                       # 배경색상은 살려둘거니까 -0.35씩만 빼며 크기 조정 
                       # zorder 값은 배경색이 0 이니까 그위에 덧칠용으로 1로 지정.

# 구조물 그리기 (단, ConstructionSite와 겹치면 무시)
for _, row in merged_df.iterrows():                # 모든 셀 한줄 씩 다 돌거임
    x, y = row['x'], row['y']                      # 현재 셀의 좌표값 꺼냄
    if (x, y) in construction_coords:              # 만약 이 좌표가 공사 중이면 건너뜀
        continue  # 건설 현장이 우선            # continue의 기능
            # 겹칩방지로 기억                   # 반복문 안에서 만나면
                                               # "이번 반복은 여기서 끝내고, 다음 반복으로 넘어가"
    

    struct = row['struct']                   # 지금 셀에 들어 있는 구조물 이름을 가져옴
    if struct == 'BandalgomCoffee':
        ax.add_patch(plt.Rectangle((x - 0.4, y - 0.4), 0.8, 0.8, color='green', zorder=2))
    elif struct == 'MyHome':
        ax.plot(x, y, marker='^', color='green', markersize=12, zorder=2)
    elif struct == 'Apartment':
        ax.plot(x, y, 'o', color='saddlebrown', markersize=10, zorder=2)
    elif struct == 'Building':
        ax.plot(x, y, 'o', color='saddlebrown', markersize=10, zorder=2)
                                              # 위에서 continue 써서 건설현장 
                                              # 구조물 끼리도 "z 순서"를 가져야
                                              # 나중에 격자선, 텍스트, 범례 등과 충돌 안남.

# 격자 그리기
for x in range(1, max_x + 1):                         # X축방향 세로줄 그릴거임 1부터 max_x까지 반복
    ax.axvline(x, color='lightgray', linewidth=0.5, zorder=3)
for y in range(1, max_y + 1):
    ax.axhline(y, color='lightgray', linewidth=0.5, zorder=3)


                                            # axvline : vertical line
                                            # axhline : horizontal line

# 범례 추가
from matplotlib.patches import Patch         # patch는 "네모 상자 같은 도형"을 범례로 만들 때 씀
from matplotlib.lines import Line2D          # line은 "선이나 마커(삼각형,원 등)" 모양을 범례로 만들때 씀
legend_elements = [                          # 실제 범례에 들어갈 아이템들 리스트
    Patch(facecolor='gray', edgecolor='gray', label='ConstructionSite'),
    Patch(facecolor='green', edgecolor='green', label='BandalgomCoffee'),
    Line2D([0], [0], marker='^', color='w', label='MyHome', markerfacecolor='green', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Apartment', markerfacecolor='saddlebrown', markersize=10),
    Line2D([0], [0], marker='o', color='w', label='Building', markerfacecolor='saddlebrown', markersize=10)
]
ax.legend(handles=legend_elements, loc='upper left')
                         # 위에서 만든 범례 요소들을 그림에 표시함
                         # handles=legend_elements : 어떤 아이템을 범례로 쓸지
                         # loc='upper left': 범례 위치는 왼쪽 위

# 좌표 축 설정
ax.set_xlim(0.5, max_x + 0.5)            # 왜 0.5 씩 하냐면, 셀 전체가 다 보이게 여유 주는 범위임
ax.set_ylim(0.5, max_y + 0.5)
ax.set_xticks(range(1, max_x + 1))       # x, t축 눈금 숫자를 직접 지정하는 부분 
ax.set_yticks(range(1, max_y + 1))       # 1부터 최대값까지 셀 단위로 숫자가 딱딱 찍히게 눈금 맞춤
ax.set_aspect('equal')                   # x,y축 비율을 1:1로 유지하겠다는 뜻
ax.invert_yaxis()                        # y축을 위아래 반대로 뒤집음
ax.set_title('Bandalgom Coffee Map')

# 이미지 저장
output_path = os.path.join(BASE_DIR, 'map.png')       # 저장경로 만드는거임
plt.savefig(output_path)
plt.show()