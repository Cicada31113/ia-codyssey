import urllib.request
import matplotlib.pyplot as plt   # pyplot  -> 막대그래프, 점, 선, 지도 등 그릴 수 있게 해주는 서브 도구
                                        # pyplot 주요 기능
                                           # plt.scatter(x, y) -> 좌표(x,y)에 점 찍기
                                           # plt.plot() -> 선 그래프 그리기
                                           # plt.bar() -> 막대그래프 그리기
                                           # plt.imshow() -> 이미지 보여주기
                                           # plt.savefig() -> 그린 그림을 이미지 파일로 저장
                                           # plt.show() -> 화면에 보여주기

url_py = 'https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/caffee_map.py'
response = urllib.request.urlopen(url_py)
code = response.read().decode('utf-8')
exec(code)  # 이 안에 load_and_prepare_data() 함수가 정의됨

# 🔹 2. 함수 실행해서 merged 데이터 얻기
merged = load_and_prepare_data()


                         # exec(...):
                            # 문자열로 되어 있는 파이썬 코드를 실제로 실행해주는 함수.
                            # 즉, 마치 우리가 그 코드를 직접 여기에 타이핑한 것처럼 작동.
                         # .text -> 받아온 내용을 '텍스트' 형태로 꺼냄. 즉, 파이썬 코드가 적힌 긴 문자열이됨.
                         # requests.get(url_py) -> Github 주소 접속후, 그 페이지의 내용(response)을 받아옴.
                    
                         # .head() 판다스에서 데이터를 잠깐 미리 보기 위해 가장 자주 쓰이는 함수 중 하나.
                         # area1.head() -> area1이라는 표(DataFrame)에서 맨 위의 5줄만 보여줘

# 전체 지역을 대상으로 시각화(MyHome이 Area2에 존재하니)
all_areas = merged.copy()
# merged 라는 데이터프레임을 복사해서 all_areas라는 새이름으로 쓸거임. 
# merged는 caffee_map.py 안에서 생성된 전체데이터
#.copy()는 복사본을 만들어서 원본을 변경하지 않고 안전하게 쓰기 위한 방법 (exce(...)이게 실행 전제되어야함)


# 🔹 공백 제거
all_areas['struct_name'] = all_areas['struct_name'].str.strip()


# 전체 x축과 y축 범위를 미리 알아볼거임.
# 이전자료
# xmin, xmax = all_areas['x'].min(), all_areas['x'].max()
# ymin, ymax = all_areas['y'].min(), all_areas['y'].max()
xmin, xmax = all_areas['x_map'].min(), all_areas['x_map'].max()
ymin, ymax = all_areas['y_map'].min(), all_areas['y_map'].max()

# 이제 지도 사이즈와 좌표 범위 적용
plt.figure(figsize=(xmax - xmin, ymax - ymin))   # "그림판을 만들건데, 가로길이,세로길이는 이만큼 설정할게"
plt.xlim(xmin - 0.5, xmax + 0.5)               # "지도의 x축과 y축 범위를 지정할게"   
plt.ylim(ymax + 0.5, ymin - 0.5)                 # -> 양쪽에 0.5 만큼 여유를 둬서 점이 겹치지않게
plt.gca().invert_yaxis()
plt.grid(True, linestyle='--', color='gray')                
                                           # lim() -> python이 알아서 자동으로 축 범위를 정해버리는데,
                                           # 우리는 좌표 기반 지도를 정확하게 제어해야하니까 -> 명시적으로 지정
                              # plt.gca() -> 지금 그리고 있는 축(Axce)을 가져와줘
                              # gca = Get Current Axes // .invert_yaxis() -> y축 방향을 거꾸로 바꿔줘



# 구조물별로 나눠서 마커 찍을거임 (scatter) 우리에겐  Apartment/Building/MyHome/BandalgomCoffee 4곳이 있음.
df_apart = all_areas[all_areas['struct_name'] == 'Apartment']
df_build = all_areas[all_areas['struct_name'] == 'Building']
df_coffee = all_areas[all_areas['struct_name'] == 'BandalgomCoffee']
df_home = all_areas[all_areas['struct_name'] == 'MyHome']
df_const = all_areas[all_areas['struct_name'] == 'ConstructionSite']


plt.scatter(df_apart['x_struct'], df_apart['y_struct'], c='saddlebrown', marker='o', label='Apartment')
    # df_apart에 담긴 아파트들의 좌표 (x,y)를 지도 위에 갈색 동그라미(o)로 찍고, 범례에 'Apartment'라고 표시해줄게'
plt.scatter(df_build['x_struct'], df_build['y_struct'], c='saddlebrown', marker='o', label='Building')
plt.scatter(df_coffee['x_struct'], df_coffee['y_struct'], c='green', marker='s', label='BandalgomCoffee')
                                                         # 's' -> 사각형 마커 square
plt.scatter(df_home['x_struct'], df_home['y_struct'], c='green', marker='^', s=100, label='MyHome' )

# 공사 현장 먼저 그릴거임 (문제 조건: "건설 현장과 기타 구조물(아파트,빌딩)과 겹치면 건설현장으로 판단")
plt.scatter(df_const['x_map'], df_const['y_map'], c='gray', marker='s', label='ConstructionSite')



plt.title('전체 지역 지도 시각화 (반달곰 커피 프로젝트)')
plt.legend(loc='upper right')
plt.savefig('map.png', dpi=300)
plt.show()
