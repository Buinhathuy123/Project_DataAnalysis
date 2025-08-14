import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("/Users/buinhathuy/Data Engineer/Data-engineer/filedulieu/train.csv")
#print(df.head())
# Chuyển đổi cột ngày tháng
df['Order Date'] = pd.to_datetime(df['Order Date'],format='%d/%m/%Y')
df['Ship Date'] = pd.to_datetime(df['Ship Date'],format='%d/%m/%Y')
# Thêm cột Month và Year
df['Month'] = df['Order Date'].dt.to_period('M')
df['Year'] = df['Order Date'].dt.year

# Tính thời gian giao hàng
df['Shipping Time'] = (df['Ship Date'] - df['Order Date']).dt.days

# Tính tỷ suất lợi nhuận
df['Profit Margin'] = ((df['Sales'] * 0.2) / df['Sales']) * 100

# Doanh thu theo tháng
monthly_sales = df.groupby('Month')['Sales'].sum()
# Doanh thu theo năm
yearly_sales = df.groupby('Year')['Sales'].sum()

# Doanh thu theo danh mục
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)

# Top 5 phân danh mục bán chạy
top_subcategories = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(5)

# Doanh thu theo khu vực
region_sales = df.groupby('Region')['Sales'].sum()

# Doanh thu theo thành phố
city_sales = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(5)


df['Ship Date'] = pd.to_datetime(df['Ship Date'], format='%d/%m/%Y')
df['Shipping Time'] = (df['Ship Date'] - df['Order Date']).dt.days
shipping_time_by_mode = df.groupby('Ship Mode')['Shipping Time'].mean()

# Thiết lập kiểu Seaborn cho giao diện đẹp hơn
sns.set_style("whitegrid", {"grid.linestyle": "--", "grid.alpha": 0.3})

# Tạo biểu đồ
plt.figure(figsize=(14, 7), facecolor='white')

# Vẽ biểu đồ đường với màu gradient và điểm đánh dấu
line = sns.lineplot(
    x=monthly_sales.index.astype(str),
    y=monthly_sales.values,
    marker='o',
    markersize=8,
    color='#1f77b4',  # Màu xanh dương đậm
    linewidth=2.5,
    label='Doanh thu'
)

# Định dạng tiêu đề và nhãn trục
plt.title('Xu hướng Doanh thu Theo Tháng', fontsize=16, fontweight='bold', pad=20, color='#333333')
plt.xlabel('Tháng', fontsize=12, color='#333333')
plt.ylabel('Doanh thu (USD)', fontsize=12, color='#333333')

# Tùy chỉnh nhãn trục x
plt.xticks(rotation=45, ha='right', fontsize=10)

# Định dạng trục y với đơn vị tiền tệ
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))

# Thêm giá trị tại các điểm
for i, value in enumerate(monthly_sales.values):
    plt.text(
        i, value + value * 0.02,  # Đặt nhãn hơi trên điểm
        f'${value:,.0f}',
        ha='center',
        va='bottom',
        fontsize=10,
        color='#1f77b4',
        fontweight='bold'
    )

# Thêm chú thích cho điểm cao nhất
max_sales = monthly_sales.max()
max_month = monthly_sales.idxmax()
max_index = monthly_sales.index.get_loc(max_month)
plt.annotate(
    f'Tháng cao nhất: ${max_sales:,.0f}',
    xy=(max_index, max_sales),
    xytext=(max_index, max_sales + max_sales * 0.1),
    arrowprops=dict(facecolor='red', shrink=0.05, headwidth=8, width=2),
    fontsize=10,
    color='red',
    fontweight='bold'
)

# Tùy chỉnh nền và viền
plt.gca().set_facecolor('#f8f9fa')  # Nền nhạt
plt.gcf().set_facecolor('#ffffff')  # Nền trắng cho toàn bộ biểu đồ

# Thêm legend
plt.legend(fontsize=10)

# Tối ưu bố cục
plt.tight_layout()
# Lưu biểu đồ với độ phân giải cao
plt.savefig('monthly_sales_trend_improved.png', dpi=300, bbox_inches='tight')
plt.show()
