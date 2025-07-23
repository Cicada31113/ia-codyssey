# caffee_map.py -> 1단계: 데이터 정제 및 분석
# - 역할: CSV 파일들(지도, 구조물, 카테고리)을 불러와서 전처리하고,
# 구조물 이름 병합 및 area=1만 필터링해서 정렬된 분석 데이터를 만들고 출력.
# - 핵심: area1_df라는 데이터셋 생성 -> 이후 모든 단계 기반됨.


# map_map -> 2단계: 구조물 중심 지도 시각화
# - 역할: 구조물 중심 시각화
# - 모든 구조물을 격자지도에 보기 좋게 그림
# - 공사현장 회색, 카페 초록 네모, 집 초록 세모, 나머지 건물 갈색 원으로 표시
# - 시각적으로 정보 한눈에 보여주는 '전시용'지도

# map_direct_save.py -> 2단계: 경로 탐색+최단경로저장+시각화
# - 역할: MyHome -> BandalgomCoffee 최단 경로를 BFS로 탐색
# - 경로를 home_to_cafe.csv에 저장
# - map_final.png로 이미지 출력









import pandas as pd
import os  #파일 경로를 다루려고 불러옴 (폴더 경로 운영체제)

# 현재 파일 경로 기준으로 상대경로 설정
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# → 이 코드 한 줄은 "현재 이 파이썬 파일이 저장된 폴더 경로"를 자동으로 찾아서 BASE_DIR에 저장하는 거야.
# → 왜 필요하냐면, 나중에 파일 불러올 때 매번 'C:/Users/어쩌구/폴더명/파일명.csv'처럼 쓰는 건 너무 위험하고 귀찮아.
# → 그래서 이 py파일이 있는 위치를 기준으로 상대경로를 만들기 위한 '기준점(Base)'으로 이 코드를 쓰는 거야.
# os.path.abspath(__file__) 상대 경로든 무조건 절대 경로로 바꿔줘 
# 상대경로 = 내 기준에서 어디 있는지 // 절대경로 = 전체주소
# os.path.dirname(~) -> 위 절대 경로에서 파일명(caffee_map.py)을 제거하고 디렉토리 경로만 추출해줌.
   # __file__ 은 '내가 지금 실행 중인 파일'의 전체경로 + 파일명 
   # __file__ = 'C:/Users/user/project/caffee_map.py'
   # 근데 내가 불러오고자하는건 c:/Users/user/project/area_map.csv
   # 그래서 최종결과가  BASE_DIR = 'C:/Users/user/Desktop/project' 이런식으로 남음
   # 즉, 이 파일이 있는 폴더 경로만 뽑

def load_and_clean_csv(file_name):                          # 예: 'area_map.csv' 불러옴
    file_path = os.path.join(BASE_DIR, file_name)           # file_name 붙여서, 전체 파일 경로 만들기
    df = pd.read_csv(file_path)                     
    df.columns = df.columns.str.strip()  # 열 이름 공백 제거         # 파이썬은 약어 써도됨 'col'
    for col in df.select_dtypes(include=['object']).columns:      # object는 pandas에서 str을뜻함 
        df[col] = df[col].str.strip()  # 문자열 데이터 공백 제거      # 숫자(int, float)는 제외됨
    return df                                                    # df[col] 지금 반복중인컬럼
        #깔끔하게 정리된 데이터프레임 반환                       
                                        # for col in df.select_dtypes(include=['object']).columns:
                                        # 데이터 타입이 object인 컬럼들(문자열 컬럼)을 골라서
                                        # df[col] = df[col].str.strip()
                                        # 그 컬럼 안의 각 데이터 값도 공백 제거
                                           # select_dtypes()는 pandas 전용함수
                                           # DataFrame.select_dtypes(include=None, exclude=None)
                                           # include=['object'] // exclude['int'] 
                                        # .columns -> 위에서 골라낸 열들중 "열의 이름들"만 리스트처럼 뽑기
                            # 마지막 두줄 더 이해하기 쉽게 설명해보자면
                              # "데이터프레임 안에서, 문자열로 되어있는 열들을 하나씩 찾아 그리고 
                              # 그 열 안에 들어 있는 값들 전부 다 앞뒤 공백을 싹 지워"

# 파일 불러오기
map_df = load_and_clean_csv('area_map.csv')
struct_df = load_and_clean_csv('area_struct.csv')
category_df = load_and_clean_csv('area_category.csv')

# 구조물 ID를 이름으로 변환 (category → struct)
struct_df = struct_df.merge(category_df, how='left', on='category')
                     # stuct_df 안에 들어있는 category를 struct 로 병합
                     # how='left'
                        # 왼쪽에 있는 데이터프레임(=앞에 쓰인 것 struct파일)을 기준으로 행을 유지하면서
                        # 오른쪽에 있는 데이터프레임에서 필요한 열만 붙이는 방식

# 데이터 병합: 지도 정보와 구조물 정보 합치기
merged_df = struct_df.merge(map_df, how='left', on=['x', 'y'])

# area 기준 정렬
merged_df = merged_df.sort_values(by=['area', 'x', 'y'])
                     # 병합된 데이터를 정렬하는데, 먼저 area기준으로 묶고, 
                     # 그 안에서 x, y 순서대로 정렬하는거임.
                     # 여러 열(2개 이상)로 정렬할땐 [ ] 이 꼭 필요. 파이썬 문법임.

# area 1 데이터만 필터링
area1_df = merged_df[merged_df['area'] == 1].copy()
                     # merged_df 안에서 area 값이 1인 행만 골라서
                     # 새로 area1_df라는 데이터프레임으로 복사한거임.
                     # .copy() -> 복사본을 만들어서 원본과 독립적으로 다루기 위해 사용
                     # merged_df[...] -> True인 행만 골라냄 = area가 1인 행들.
                       # 안쪽 merged_df -> area열이 1인 곳만 True로 표시하는 조견표 만듬(마스크). 조건생성.
                       # 바깥 -> 이 마스크를 이용해서, True인 행만 골라서 꺼냄 
                         # -> Pandas의 표준 필터링 문법임
                         # merged_df['area'] == 1
                            #  → 결과:
                            # 0     True
                            # 1     False
                            # 2     True
                            # 3     False
                               # 조건표만 만든 상태이지, 아직 데이터는 안꺼냈음.
                         # 바깥 merged_df[...] -> 이게 진짜 데이터 꺼내는 동작
                            # 이걸 Boolean Indexing 이라고함. 조건이 True인 행만 필터링함.
                            # pandas 특징임.


# 결과 출력
print('--- Area 1 데이터 ---')
print(area1_df.head())
                                # .head() -> 이건 표(데이터프레임)의 앞 5줄만 보여주는 함수임.
                                # 기본값은 5줄이고, head(10)처럼 숫자 지정도 가능
# 구조물 종류별 통계 출력 (보너스)
summary = area1_df['struct'].value_counts()
                                     #area1_df안에서 'struct'(구조물 이름)이 몇개씩 있는지 셀거고
                                     # 그 결과를 summary에 저장해서 출력.
                                     # .value_counts()
                                       # 열안에 있는 값들이 각각 몇번씩 나왔는지 세주는 함수
                                       # "columns" 에만 쓰는 함수임
   
print('\n--- 구조물 종류별 개수 ---')
print(summary)

# 결과 저장 (선택)
# area1_df.to_csv('area1_structures.csv', index=False)
# summary.to_csv('area1_summary.csv')


             # 전체 요약
              # 지도 정보, 구조물 정보, 구조물 이름표를 합쳐서
              # area 1만 필터링한 후,
              # 구조물 종류별로 몇개인지 확인하는 전처리 분석코드

#               | 단계           | 설명                                                        
# | ------------ | ----------------------------------------------------------- |
# | 📂 경로 설정     | `BASE_DIR`로 현재 파일 기준 경로 설정 (상대경로 안전하게 쓰려고)                 
# | 🧼 전처리 함수 정의 | `load_and_clean_csv()` → 공백 제거하고 파일 읽는 함수                  
# | 📥 파일 불러오기   | 3개 파일(csv) 불러와서 각각 `map_df`, `struct_df`, `category_df`에 저장
# | 🔗 구조물 이름 병합 | `category` 번호를 `struct` 이름으로 매칭 (left join)                
# | 🔗 지도 정보 병합  | 구조물 위치(x, y)에 area, 공사현장 정보 붙이기 (left join)               
# | 📊 정렬        | area → x → y 순서로 보기 좋게 정렬                                 
# | 🎯 필터링       | area=1번 지역만 따로 떼서 `area1_df` 저장                            
# | 👀 출력        | 앞부분 5줄만 프린트해서 확인                                           
# | 📈 통계        | 구조물 이름별로 몇 개인지 `.value_counts()`로 요약 출력                  
