import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# 創建 Basemap 實例，設定地圖投影為經典的 Mercator 投影
m = Basemap(projection='merc', llcrnrlat=20, urcrnrlat=25.5, llcrnrlon=119, urcrnrlon=124.5, resolution='i')

# 繪製海岸線、國界和省界
m.drawcoastlines()
m.drawcountries()
m.drawstates()

# 定義台灣的主要城市及其經緯度
cities = {
    'Taipei': (25.0330, 121.5654),
    'Kaohsiung': (22.6273, 120.3014),
    'Taichung': (24.1477, 120.6736),
    'Tainan': (22.9999, 120.2270),
    'Hualien': (23.9767, 121.6076)
}

# 在地圖上標註城市
for city, (lat, lon) in cities.items():
    x, y = m(lon, lat)  # 經緯度轉換為地圖坐標
    m.plot(x, y, 'bo', markersize=12)  # 標註點
    plt.text(x, y, city, fontsize=12, ha='right', color='red')  # 城市名稱

# 設置標題並顯示地圖
plt.title('台灣地圖')
plt.show()