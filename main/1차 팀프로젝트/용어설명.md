# 📦 라이브러리(Library)란?

- 파이썬 기능을 미리 만들어둔 **도구 상자**
- 필요한 기능을 쉽게 불러와서 쓸 수 있음
- 설치해서 import하면 됨

```
pip install pandas matplotlib
```

---

# 🧰 pandas (판다스)

- 데이터를 표처럼 다룰 수 있는 라이브러리 (엑셀처럼 행/열 구조)
- CSV, Excel 파일 불러오기/저장, 데이터 분석에 유용
- DataFrame이라는 자료구조를 사용

```python
import pandas as pd  # pandas를 pd라는 별명(alias)으로 불러옴

data = {'이름': ['철수', '영희'], '나이': [20, 22]}
df = pd.DataFrame(data)
print(df)
```

출력 결과:
```
   이름  나이
0  철수   20
1  영희   22
```

---

# 📊 matplotlib (맷플롯립)

- 데이터를 시각화할 수 있는 그래프 라이브러리
- 선형 그래프, 막대 그래프, 파이 차트 등 그리기 가능
- `pyplot` 모듈을 자주 씀

```python
import matplotlib.pyplot as plt  # 줄여서 plt로 많이 씀

x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.title("샘플 그래프")
plt.xlabel("X 값")
plt.ylabel("Y 값")
plt.show()
```

---

# 🆔 alias (별명) 관습

| 라이브러리                | 별명(alias) |
|---------------------------|-------------|
| `pandas`                 | `pd`        |
| `numpy`                  | `np`        |
| `matplotlib.pyplot`      | `plt`       |

> ✅ 이건 파이썬 커뮤니티에서 통용되는 표준처럼 굳어진 약속이야.  
> 길어서 줄여 쓰는 거고, 필수는 아니지만 거의 모두가 이렇게 써.
