import pandas as pd
import os

print("📍 현재 작업 디렉토리:", os.getcwd())

base_raw_url = (
    "https://raw.githubusercontent.com/Cicada31113/ia-codyssey/main/main/"
    "1%EC%B0%A8%20%ED%8C%80%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8/%EB%B0%98%EB%8B%AC%EA%B3%B0%EC%BB%A4%ED%94%BC%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8"
)

map_df = pd.read_csv(f"{base_raw_url}/area_map.csv")
struct_df = pd.read_csv(f"{base_raw_url}/area_struct.csv")
category_df = pd.read_csv(f"{base_raw_url}/area_category.csv")

map_df.columns = map_df.columns.str.strip()            
struct_df.columns = struct_df.columns.str.strip()    
category_df.columns = category_df.columns.str.strip() 

print("📦 map_df 열:", map_df.columns.tolist())
print("🏗  struct_df 열:", struct_df.columns.tolist())
print("📘 category_df 열:", category_df.columns.tolist())

id_to_name = dict(zip(category_df['category'], category_df['struct']))
struct_df['structure'] = struct_df['category'].map(id_to_name)
merged_df = pd.merge(struct_df, map_df, on=['x', 'y']) 

area1_df = merged_df[merged_df['area'] == 1]

print("\n🧾 area1 데이터 샘플:")
print(area1_df.head())

print("\n📊 구조물 종류별 개수:")
print(area1_df['structure'].value_counts())

##############################################



