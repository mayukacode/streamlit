import streamlit as st
import matplotlib
matplotlib.use('Agg')  # バックエンドを非対話型に設定

import matplotlib.pyplot as plt
import japanize_matplotlib  # 日本語表示用ライブラリ

def calculate_lighting_cost(watt, hours):
    cost_per_kwh = 27  # 円/kWh
    kwh = watt / 1000 * hours  # kWh
    cost = kwh * cost_per_kwh  # 円
    return cost

def calculate_cooking_cost(device_watts_hours):
    cost_per_kwh = 27  # 円/kWh
    total_cost = 0
    for watt, hours in device_watts_hours:
        kwh = watt / 1000 * hours  # kWh
        cost = kwh * cost_per_kwh  # 円
        total_cost += cost
    return total_cost

def calculate_laundry_cost(device_watts_hours):
    cost_per_kwh = 27  # 円/kWh
    total_cost = 0
    for watt, hours in device_watts_hours:
        kwh = watt / 1000 * hours  # kWh
        cost = kwh * cost_per_kwh  # 円
        total_cost += cost
    return total_cost

def calculate_airconditioner_cost(device_watts_hours):
    cost_per_kwh = 27  # 円/kWh
    total_cost = 0
    for watt, hours in device_watts_hours:
        kwh = watt / 1000 * hours  # kWh
        cost = kwh * cost_per_kwh  # 円
        total_cost += cost
    return total_cost

def calculate_hobbywork_cost(device_watts_hours):
    cost_per_kwh = 27  # 円/kWh
    total_cost = 0
    for watt, hours in device_watts_hours:
        kwh = watt / 1000 * hours  # kWh
        cost = kwh * cost_per_kwh  # 円
        total_cost += cost
    return total_cost

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
