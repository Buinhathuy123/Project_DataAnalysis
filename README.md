Phân Tích Dữ Liệu Bán Hàng - Sales Analysis
Mô tả dự án
Dự án này thực hiện phân tích dữ liệu bán hàng từ một tập dữ liệu giao dịch, trích xuất các thông tin chi tiết về xu hướng doanh thu, hiệu suất theo danh mục và khu vực, cũng như hiệu quả vận chuyển. Dự án sử dụng Python cùng với các thư viện Pandas, Matplotlib và Seaborn để xử lý và trực quan hóa dữ liệu.

Tính năng chính
Phân tích xu hướng doanh thu: Theo dõi doanh thu theo tháng và năm

Phân tích theo danh mục: Xác định danh mục và phân danh mục bán chạy nhất

Phân tích theo khu vực: Đánh giá hiệu suất bán hàng theo vùng và thành phố

Phân tích hiệu quả vận chuyển: Tính toán thời gian giao hàng trung bình theo phương thức vận chuyển

Tính toán tỷ suất lợi nhuận: Đánh giá hiệu quả kinh doanh thông qua tỷ suất lợi nhuận

Công nghệ sử dụng
Python 3.x

Pandas: Để xử lý và phân tích dữ liệu

Matplotlib: Để tạo biểu đồ cơ bản

Seaborn: Để tạo biểu đồ nâng cao với giao diện đẹp mắt

Cài đặt và chạy dự án
Clone repository này về máy local của bạn

Cài đặt các thư viện cần thiết:

bash
pip install pandas matplotlib seaborn
Đảm bảo bạn có file dữ liệu train.csv trong đường dẫn được chỉ định trong code

Chạy script Python để thực hiện phân tích và tạo biểu đồ:

bash
python sales_analysis.py
Cấu trúc dữ liệu
Tập dữ liệu bao gồm các cột sau:

Order Date: Ngày đặt hàng

Ship Date: Ngày giao hàng

Ship Mode: Phương thức vận chuyển

Category: Danh mục sản phẩm

Sub-Category: Phân danh mục sản phẩm

Sales: Doanh số

Region: Khu vực

City: Thành phố

Kết quả đầu ra
Script sẽ tạo ra một biểu đồ đường thể hiện xu hướng doanh thu theo tháng, được lưu dưới dạng file ảnh monthly_sales_trend_improved.png với các đặc điểm:

Hiển thị doanh thu hàng tháng

Đánh dấu điểm cao nhất

Hiển thị giá trị tại mỗi điểm dữ liệu

Định dạng trục Y với ký hiệu tiền tệ

Thiết kế chuyên nghiệp với màu sắc và bố cục rõ ràng

Phân tích dữ liệu được thực hiện
Chuyển đổi định dạng ngày tháng

Trích xuất thông tin tháng và năm từ ngày đặt hàng

Tính toán thời gian giao hàng

Tính toán tỷ suất lợi nhuận (giả định tỷ lệ lợi nhuận là 20%)

Phân tích doanh thu theo nhiều chiều: thời gian, danh mục, khu vực

Xác định top 5 phân danh mục bán chạy nhất

Tính thời gian giao hàng trung bình theo phương thức vận chuyển  
