import pandas as pd

# 1. GitHub raw 링크에서 데이터 불러오기
url_map = 'https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/area_map.csv'
url_struct = 'https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/area_struct.csv'
url_cat = 'https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/area_category.csv'

# map 에는 x, y, Construction site 건물좌표,구역번호만 존재            map <> struct   (x, y) 중첩
# struct 에는 x, y, category, area 건물 어떤 종류인지, 어떤 지역인지    stuct <> category (category) 중첩
# catagory 에는 category, struct 카테고리 번호에 이름을을 붙여주는 이름표 역할


area_map = pd.read_csv(url_map)
area_struct = pd.read_csv(url_struct)
area_cat = pd.read_csv(url_cat)

# 2. 카테고리 번호 -> 이름으로 바꿀거임.
area_cat.columns = ['category', 'struct_name']  # 컬럼명 공백 제거 -> columns (컬럼 이름을 새로 지정하는 코드)
area_struct = pd.merge(area_struct, area_cat, on='category')  # merge는 두 표를 같은 값(category) 기준으로 옆으로 이어붙임
                                                              # 이때, 없는 컬럼(sturct_name)은 붙는 쪽에서 따라옴.
# 3. ID를 붙이기 위해 area_map에 ID 부여
area_map = area_map.rename(columns={'ConstructionSite': 'id'})
area_struct['id'] = area_map['id']

                            # area_map에는 Constructionsite 라는 칼럼이 있음. 
                            # 이 컬럼은 각 건물을 구분하는 고유한 이름 또는 번호 역할(id)을 함.
                            # 그래서 이름을 더 쓰기 쉽게, 그리고 병합하기 편하게 하기위해 'id'로 바꾸는거임.
                            # rename 구조 :
                            # DataFrame.rename(cloumns={기존이름: 새이름})

         # area_stuct['id] = area_map['id'] -> 건물 정보(area_struct)에 id 컬럼을 새로 추가하는 코드
         # area_map에는 건물의 고유번호(id)가 있었는데, area_struct)에는 그 정보가 없었음.
         # 하지만, 병합하려면 기준이 되는 공통 컬럼이 필요함 -> 그래서 id 컬럼을 area_struct에도 복붙해주는겅미.
            # 이 코드는, 행 순서가 동일하다는 가정 하에 작동함.
            # area_map의 0번째 행 = 0번 건물의 좌표와 id
            # area_struct의 0번째 행 = 같은 건물의 category, area
            # -> 순서가 정확히 맞는다면 그냥 area_map['id'] 값을 복사해도 무방함.
            # area_map['id']는 "Series" 라고 하는 데이터의 한 열인데, 이걸 area_struct라는 표에
            # 'id'라는 새로운 열로 붙이는 것임.
            # 파이썬에서 []는 기본적으로 리스트 만들기이지만, pandas 에서는 열을 꺼내는 형태 (Series)
            # area_map['id'] -> "id라는 키에 해당하는 열"을 꺼낸거임 -> pandas는 내부적으로 DataFrame을 딕셔너리 비슷하게 다룸.

        # 파이썬에는 객체가 [] 동작을 커스터마이징하려면 이런 메서드를 정의할 수 있음.
        # __getitem__(self, key) -> df[key] 가 호출될때 작동
        # __setitem__(self, key, value) -> df[key] = value 일 때 작동
        # pandas는 내부적으로 이 메서드들을 직접 구현해서 자기 방식대로 []를 해석하도록 만든거임.

# 4. 병합 + 정렬
merged = pd.merge(area_map, area_struct, on='id')   # 두 개의 표를 'id'를 기준으로 가로로 합치는 함수
merged = merged.sort_values(by='area')                  # pd.merge(df1, df2, on='공통컬럼')
                             
                             # sort_values(by='area')
                             # 병합된 표를 area 값 기준으로 정렬.
                             # 숫자가 작은 지역부터 큰 지역 순으로 행의 순서를 재배열함.

# 5. area == 1만 필터링
area1 = merged[merged['area'] == 1]
             
                             # merged['area'] == 1   -> "merged 표에서 area 값이 1인 곳만 찾아줘"
                             # 결과는 True, False로 구성된 시리즈 (필터 마스크)
                                # merged[merged['area'] == 1] 
                                   # 위에서 만든 True/False 리스트를 이용해서
                                   # True인 행만 뽑아서 새표(area1)에 저장

# 6. 출력
print("[area 1 정보]")
print(area1)

# 7. (보너스) 구조물 종류별 요약 통계
print("\n[구조물 요약 통계]")
print(area1['struct_name'].value_counts())

                          # area1['struct_name'] -> area1 표에서 '구조물 이름' 열만 꺼냄.
                          # .value_counts() -> 각 값이 몇 번 나왔는지를 세어줌.
