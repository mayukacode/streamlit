import streamlit as st
import matplotlib
matplotlib.use('Agg')  # バックエンドを非対話型に設定

import matplotlib.pyplot as plt
import japanize_matplotlib  # 日本語表示用ライブラリ

# 関数定義（省略）

st.title('一日ごとの電気代（カテゴリ別）')

# 各部分の入力と計算（省略）

# 円グラフの表示
labels = '照明', '調理', '洗濯', '空調', '趣味/仕事'
sizes = [lighting_cost, cooking_cost, laundry_cost, airconditioner_cost, hobbywork_cost]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']
explode = (0.1, 0, 0, 0, 0)  # 照明部分を少し突き出す

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
       shadow=True, startangle=140)
ax.axis('equal')  # 円を正しく表示する
ax.set_title('一日ごとの電気代（カテゴリ別）')
st.pyplot(fig)
