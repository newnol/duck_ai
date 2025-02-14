# Mô tả DuckDuckGo Chat CLI Client

Đây là một script Python đơn giản để tương tác với DuckDuckGo AI Chat thông qua command line interface (CLI). Dưới đây là phân tích chi tiết:

### Các thành phần chính:

1. **`fetch_vqd()`**
   - Lấy token xác thực (VQD token) từ DuckDuckGo
   - Gửi GET request đến endpoint `/duckchat/v1/status`
   - Trả về `x-vqd-4` header cần thiết cho các request tiếp theo

2. **`send_message(vqd, model, messages)`**
   - Gửi tin nhắn đến DuckDuckGo Chat API
   - Sử dụng streaming response để nhận phản hồi theo thời gian thực
   - Thu thập và hiển thị phản hồi từ AI

3. **`main()`**
   - Khởi tạo phiên chat với model "o3-mini"
   - Tạo vòng lặp để nhận input từ người dùng
   - Thoát khi người dùng nhập "exit"

### Cách sử dụng:

```bash
python test.py
```

### Ví dụ tương tác:
```
You: Hello
AI: Hi there! How can I help you today?

--- AI đã trả lời xong ---

You: exit
```

### Lưu ý:
- Script sử dụng model "o3-mini" mặc định
- Yêu cầu thư viện `requests` để hoạt động
- Các headers được cấu hình sẵn để mô phỏng trình duyệt web
- Phản hồi được stream theo thời gian thực để tăng trải nghiệm người dùng
