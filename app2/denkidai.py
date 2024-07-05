import streamlit as st
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import japanize_matplotlib

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

# 照明の入力
st.header('照明')
lighting_watt = st.number_input('照明のワット数 (W)', min_value=0, value=60)
lighting_hours = st.number_input('照明の使用時間 (時間)', min_value=0.0, value=5.0)
lighting_cost = calculate_lighting_cost(lighting_watt, lighting_hours)
lighting_cost = int(lighting_cost)
st.write(f'照明の電気代: {lighting_cost}円')

# 調理機器の入力
st.header('調理機器')
device_watts_hours = []
device_watts_hours.append((st.number_input('炊飯器のワット数 (W)', min_value=0, value=700),
                           st.number_input('炊飯器の使用時間 (時間)', min_value=0.0, value=1.0)))
device_watts_hours.append((st.number_input('電子レンジのワット数 (W)', min_value=0, value=1000),
                           st.number_input('電子レンジの使用時間 (時間)', min_value=0.0, value=0.5)))
device_watts_hours.append((st.number_input('オーブントースターのワット数 (W)', min_value=0, value=1200),
                           st.number_input('オーブントースターの使用時間 (時間)', min_value=0.0, value=0.2)))
device_watts_hours.append((st.number_input('IH調理器のワット数 (W)', min_value=0, value=1400),
                           st.number_input('IH調理器の使用時間 (時間)', min_value=0.0, value=0.5)))
cooking_cost = calculate_cooking_cost(device_watts_hours)
cooking_cost = int(cooking_cost)
st.write(f'調理機器の合計電気代: {cooking_cost}円')

# 洗濯の入力
st.header('洗濯')
device_watts_hours = []
device_watts_hours.append((st.number_input('洗濯機のワット数 (W)', min_value=0, value=500),
                           st.number_input('洗濯機の使用時間 (時間)', min_value=0.0, value=1.0)))
device_watts_hours.append((st.number_input('乾燥機のワット数 (W)', min_value=0, value=1000),
                           st.number_input('乾燥機の使用時間 (時間)', min_value=0.0, value=1.0)))
laundry_cost = calculate_laundry_cost(device_watts_hours)
laundry_cost = int(laundry_cost)
st.write(f'洗濯の合計電気代: {laundry_cost}円')

# 空調の入力
st.header('空調')
device_watts_hours = []
device_watts_hours.append((st.number_input('クーラーのワット数 (W)', min_value=0, value=880),
                           st.number_input('クーラーの使用時間 (時間)', min_value=0.0, value=1.0)))
device_watts_hours.append((st.number_input('暖房のワット数 (W)', min_value=0, value=1500),
                           st.number_input('暖房の使用時間 (時間)', min_value=0.0, value=1.0)))
device_watts_hours.append((st.number_input('こたつのワット数 (W)', min_value=0, value=60),
                           st.number_input('こたつの使用時間 (時間)', min_value=0.0, value=0.5)))
device_watts_hours.append((st.number_input('ホットカーペットのワット数 (W)', min_value=0, value=800),
                           st.number_input('ホットカーペットの使用時間 (時間)', min_value=0.0, value=2.0)))
airconditioner_cost = calculate_airconditioner_cost(device_watts_hours)
airconditioner_cost = int(airconditioner_cost)
st.write(f'空調の合計電気代: {airconditioner_cost}円')

# 趣味/仕事の入力
st.header('趣味/仕事')
device_watts_hours = []
device_watts_hours.append((st.number_input('ＴＶのワット数 (W)', min_value=0, value=150),
                           st.number_input('ＴＶの使用時間 (時間)', min_value=0.0, value=1.0)))
device_watts_hours.append((st.number_input('パソコンのワット数 (W)', min_value=0, value=150),
                           st.number_input('パソコンの使用時間 (時間)', min_value=0.0, value=0.5)))
hobbywork_cost = calculate_hobbywork_cost(device_watts_hours)
hobbywork_cost = int(hobbywork_cost)
st.write(f'趣味/仕事の合計電気代: {hobbywork_cost}円')

# 総計
total_cost = lighting_cost + cooking_cost + laundry_cost + airconditioner_cost + hobbywork_cost
rounded_total_cost = round(total_cost)
st.write(f'総合計電気代: {rounded_total_cost}円')

# 円グラフの表示
labels = '照明', '調理', '洗濯', '空調', '趣味/仕事'
sizes = [lighting_cost, cooking_cost, laundry_cost, airconditioner_cost, hobbywork_cost]
colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen', 'lightpink']
explode = (0.1, 0, 0, 0, 0)  # 照明部分を少し突き出す

fig, ax = plt.subplots()
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
ax.axis('equal')  # 円を円として表示

st.pyplot(fig)
