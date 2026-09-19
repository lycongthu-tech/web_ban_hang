from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

# CƠ SỞ DỮ LIỆU LOGIC SẢN PHẨM (Bạn tự thay tên và link TikTok của bạn vào đây)
DANH_SACH_SAN_PHAM = [
    {
        "id": 1,
        "ten": "Giày Thể Thao Nam Chạy Bộ",
        "gia": "350.000đ",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 2,
        "ten": "Áo Khoác Gió Chống Nước",
        "gia": "250.000đ",
        "link_tiktok": "https://tiktok.com"
    }
]

@app.get("/", response_class=HTMLResponse)
def trang_chu():
    html_content = """
    <html>
        <head>
            <title>Cửa Hàng Của Lý Công Thức</title>
            <style>
                body { font-family: Arial; background-color: #f4f4f4; text-align: center; padding: 50px; }
                .san-pham { background: white; padding: 20px; display: inline-block; margin: 20px; border-radius: 8px; box-shadow: 0 0 10px rgba(0,0,0,0.1); width: 250px; }
                .nut-mua { background-color: #ff0050; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; text-decoration: none; display: inline-block; margin-top: 10px; font-weight: bold; }
            </style>
        </head>
        <body>
            <h1>XIN CHÀO! CHÀO MỪNG ĐẾN VỚI CỬA HÀNG</h1>
            <p>Chọn sản phẩm bạn yêu thích bên dưới:</p>
    """
    for sp in DANH_SACH_SAN_PHAM:
        html_content += f"""
        <div class="san-pham">
            <h3>{sp['ten']}</h3>
            <p style="color: red; font-size: 18px; font-weight: bold;">{sp['gia']}</p>
            <a href="/mua/{sp['id']}" class="nut-mua">Mua Ngay Trên TikTok</a>
        </div>
        """
    html_content += "</body></html>"
    return html_content

@app.get("/mua/{id_san_pham}")
def dieu_huong_tiktok(id_san_pham: int):
    for sp in DANH_SACH_SAN_PHAM:
        if sp["id"] == id_san_pham:
            print(f"LOGIC: Khách bấm vào {sp['ten']} -> Tự động chuyển hướng sang TikTok Shop!")
            return RedirectResponse(url=sp["link_tiktok"])
    return {"Thong bao": "Khong tim thay san pham"}