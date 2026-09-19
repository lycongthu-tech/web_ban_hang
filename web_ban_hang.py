from fastapi import FastAPI
from fastapi.responses import RedirectResponse, HTMLResponse

app = FastAPI()

# CƠ SỞ DỮ LIỆU SẢN PHẨM (Đã sửa link ảnh hệ thống chuẩn hiển thị 100%)
DANH_SACH_SAN_PHAM = [
    {
        "id": 1,
        "ten": "Bình Nước Thể Thao Giữ Nhiệt 1L",
        "gia": "180.000đ",
        "hinh_anh":"https://n7media.coolmate.me/uploads/September2025/ao-thun-nam-gym-power-dang-tights-co-gian-exdry-thoang-mat-den-1.jpg?aio=w-1100",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 2,
        "ten": "Dây Kháng Lực Tập Gym Tại Nhà (Set 5 Mức)",
        "gia": "125.000đ",
        "hinh_anh": "https://thegioidotap.vn/wp-content/uploads/2024/05/Ao-tap-gym-nam-1.jpg",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 3,
        "ten": "Thảm Tập Yoga Chống Trượt Cao Cấp",
        "gia": "220.000đ",
        "hinh_anh": "https://placehold.co",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 4,
        "ten": "Đai Lưng Hỗ Trợ Gánh Đùi Deadlift",
        "gia": "310.000đ",
        "hinh_anh": "https://placehold.co",
        "link_tiktok": "https://tiktok.com"
    }
]

@app.get("/", response_class=HTMLResponse)
def trang_chu():
    html_content = """
    <html>
        <head>
            <title>Store Thể Thao Lý Công Thức</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #0f172a; color: #f8fafc; text-align: center; padding: 20px; margin: 0; }
                h1 { color: #38bdf8; margin-bottom: 5px; font-size: 28px; }
                .mo-ta { color: #94a3b8; font-size: 14px; margin-bottom: 30px; }
                .khung-chua { display: flex; flex-wrap: wrap; justify-content: center; max-width: 1000px; margin: 0 auto; }
                .san-pham { background: #1e293b; padding: 15px; margin: 15px; border-radius: 12px; border: 1px solid #334155; width: 260px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); text-align: left; }
                .san-pham img { width: 100%; height: 180px; border-radius: 8px; object-fit: cover; }
                .san-pham h3 { font-size: 16px; margin: 12px 0 6px 0; height: 44px; overflow: hidden; color: #e2e8f0; }
                .gia-tien { color: #f43f5e; font-size: 18px; font-weight: bold; margin: 8px 0; }
                .nut-mua { background-color: #ff0050; color: white; padding: 10px; border: none; border-radius: 6px; cursor: pointer; text-decoration: none; display: block; text-align: center; font-weight: bold; margin-top: 12px; transition: 0.2s; }
                .nut-mua:hover { background-color: #e60047; }
            </style>
        </head>
        <body>
            <h1>LÝ CÔNG THỨC - GYM & SPORTS STORE</h1>
            <p class="mo-ta">💥 Chuyên phụ kiện tập gym chất lượng cao cho anh em thể hình 💥</p>
            <div class="khung-chua">
    """
    
    for sp in DANH_SACH_SAN_PHAM:
        html_content += f"""
        <div class="san-pham">
            <img src="{sp['hinh_anh']}">
            <h3>{sp['ten']}</h3>
            <p class="gia-tien">{sp['gia']}</p>
            <a href="/mua/{sp['id']}" class="nut-mua">Mua Ngay Trên TikTok</a>
        </div>
        """
        
    html_content += "</div></body></html>"
    return html_content

@app.get("/mua/{id_san_pham}")
def dieu_huong_tiktok(id_san_pham: int):
    for sp in DANH_SACH_SAN_PHAM:
        if sp["id"] == id_san_pham:
            print(f"LOGIC: Khách bấm vào {sp['ten']} -> Đang chuyển hướng sang TikTok Shop!")
            return RedirectResponse(url=sp["link_tiktok"])
    return {"Thong bao": "Khong tim thay san pham"}