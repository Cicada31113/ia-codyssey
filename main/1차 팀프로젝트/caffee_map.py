import pandas as pd
import os

print("📍 현재 작업 디렉토리:", os.getcwd())       # get current working directory

base_raw_url = (
    "https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/"
    "1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8"
)  # 파이썬은 "현재 실행 중인 위치" 기준으로 파일 찾음.

                     # pandas가 읽게 만드는중
map_df = pd.read_csv(f'{base_raw_url}/area_map.csv')               # 3개 파일로 표(DataFrame)에 담을게.
struct_df = pd.read_csv(f'{base_raw_url}/area_struct.csv')         # f'{변수{}/..' 
category_df = pd.read_csv(f'{base_raw_url}/area_category.csv')     # -> 문자열 안에 변수값을 넣어주는 문법(f-string)

map_df.columns = map_df.columns.str.strip()            # 엑셀 파일 안에는 구조물 이름이 들어있는데
struct_df.columns = struct_df.columns.str.strip()      # 열 제목에 공백이 붙어 있어서 파이썬이 "struct" 몾찾음
category_df.columns = category_df.columns.str.strip()  # 모든 열 이름에서 앞뒤 공백을 제거해줘야함 -> str.strip()
                                                       # .columns -> 열 제목만 뽑아오는 기능
                                                       # .str.strip(): 문자열 양옆 붙은 공백을 없애줌

print("📦 map_df 열:", map_df.columns.tolist())                     # .tolist() : 열 목록을 리스트 형태로 출력
print("🏗  struct_df 열:", struct_df.columns.tolist())             
print("📘 category_df 열:", category_df.columns.tolist())


# area_map.csv는 말그대로 지도 좌표정보를 담고 있음. 어떤 건물이 어느 지역 안에 있고, 좌표(x,y)로 어디에 있는지 알려줌.
# are_struct.csv -> 구조물의 위치와 숫자 ID만 들어있음
# are_category.csv -> 그 숫자 ID에 해당하는 이름이 들어 있음 (1:아파트, 2:빌딩..)
# 그래서 두 데이터를 연결해서 좌표&구조물ID -> 이름으로 바꿔줘야됨

id_to_name = dict(zip(category_df['category'], category_df['struct']))
 # id_to_name 이라는 이름으로 ID -> 이름을 연결해주는 사전(dictionary)을 만든다.
   # 구조물 ID란?
   # 우리가 가진 데이터는 지역 지도에 있는 건물들(구조물)을 표현하는데
   # CSV 파일을 보면 그 구조물들의 이름이 바로 써 있지 않고 숫자 코드로 되어있어
   # 구조물 ID [1] -> 아파트 // 구조물 ID [2] -> 빌딩  이런식으로
   # 왜 숫자로 되어있냐면, 컴퓨터는 숫자를 처리하는 게 훨씬 쉬워서 데이터를 저장할 때 이렇게 숫자로 표현하는 경우가 많아
   # 하지만 우리는 사람이니까 "1"보다는 "아파트"라고 써 있는게 보기 쉽겠지?
   
   # 그래서 이 숫자들을 -> 사람이 이해하기 쉬운 이름으로 바꿔주는 작업이 바로 아래 structue_df 부분이야.

   # *추가용어설명*
   # zip -> 두 줄을 짝짓기하는 도구 -> (1, '아파트') 이런식으로
   # dict -> 딕셔너리 (사전) 만들기
      # 예시:
      # dict([(1, '아파트'), (2, '빌딩'), (3, '반달곰커피')])
      # -> {1: '아파트', 2: '빌딩', 3: '반달곰커피'}
      # 즉, 두 리스트를 딕셔너리로 번호: 이름 형태로 바꿔줌 -> 이게 id_to_name의 정체


struct_df['structure'] = struct_df['category'].map(id_to_name)
 # structure_id라는 숫자 코드를, 우리가 만든 사전을 이용해 이름으로 바꿔준다. 

   # *추가용어설명*
   # map -> 변환기 역할                 ----> map은 "이 숫자에 해당하는 이름이 뭐야?" 라고 물어서 하나씩 바꿔주는 역할.
   # 예시 :                                  
   # id_to_name = {                         # map()은 각 숫자를 딕셔너리에서 찾아서 이름으로 바꿔줌
   #     1: '아파트',                         # 그런데 ! category == 0 인 값은 딕셔너리에 없음
   #     2: '빌딩',                           # 딕셔너리에 없는 값은 -> NaN 으로 바뀜 
   #     3: '반달곰커피'                        # 만약 NaN 제거하고 싶으면, 
   # }                                         # area1_df = area1_df.drpna(subset=['structure']) 쓰면됨
   # 구조물_id_리스트 = [1, 3, 2]                 # "structure 열이 비어 있는 건 버려줘" 라는 뜻.
   # [1, 3, 2].map(id_to_name) ---> ['아파트', '반달곰커피', '빌딩']

merged_df = pd.merge(struct_df, map_df, on=['x', 'y'])  # 병합 기준에, map_df에는 'area'라는 열이없음.
                                                        # 두 파일 모두 공통으로 갖고 있는 열만 병합기준으로 쓰자.
                                                            


 # pd.merge(...) -> 두 개의 표(데이터프레임)를 합치는 함수. // SQL에서 말하는 JOIN과 같은 개념
    # 왼쪽 표 : 구조물 정보 (어떤 건물인지, 이름 등)
    # 오른쪽 표 : 지도 정보 (그 좌표가 실제로 존재하는가)
 
 # on=['area', 'x', 'y']
    # 두표를 합칠 때 기준이 되는 공통된 열(column) 이름
    # 즉 "같은 지역번호,x좌표,y좌표"가 있는 줄을 서로 연결하게됨.

area1_df = merged_df[merged_df['area'] == 1]   # -> area가 1인 행만 골라내서 'area1_df'라는 표로 만들거임
print("\n🧾 area1 데이터 샘플:")
print(area1_df.head())
print("\n📊 구조물 종류별 개수:")
print(area1_df['structure'].value_counts())


############################# 여기서부터는 시각화할거임. matplotlib.pyplot 쓸겨 (그래프/이미지 그리는 도구)