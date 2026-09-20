from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

DANH_SACH_SAN_PHAM = [
    {
        "id": 1,
        "ten": "Áo Thun Nén Gym Nam - Dài Tay",
        "gia": "109.000đ",
        "hinh_anh": "https://img.lazcdn.com/g/p/f2e518da82946459f147d1911bcc3ea5.jpg_720x720q80.jpg",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 2,
        "ten": "Đai Lưng Hỗ Trợ Gánh Đùi Deadlift",
        "gia": "310.000đ",
        "hinh_anh": "https://unsplash.com",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 3,
        "ten": "Thảm Tập Yoga Chống Trượt Cao Cấp",
        "gia": "220.000đ",
        "hinh_anh": "https://unsplash.com",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 4,
        "ten": "Bình Nước Thể Thao Giữ Nhiệt 1L",
        "gia": "150.000đ",
        "hinh_anh": "https://unsplash.com",
        "link_tiktok": "https://tiktok.com"
    },
    {
        "id": 5,
        "ten": "Găng Tay Tập Gym Có Cuốn Cổ Tay",
        "gia": "125.000đ",
        "hinh_anh": "https://unsplash.com",
        "link_tiktok": "https://tiktok.com"
    }
]

@app.get("/", response_class=HTMLResponse)
def trang_chu():
    html_san_pham = "" 
    for sp in DANH_SACH_SAN_PHAM:
        id_sp = sp["id"]
        ten_sp = sp["ten"]
        gia_sp = sp["gia"]
        anh_sp = sp["hinh_anh"]
        html_san_pham += f"""
        <div class="col">
            <div class="card h-100 border-secondary shadow-sm overflow-hidden bg-dark text-start d-flex flex-column">
                <!-- 1. Phần hình ảnh nằm phía trên: Khung chữ nhật đứng 3:4 tôn dáng -->
                <div class="overflow-hidden bg-secondary w-100">
                    <img src="{anh_sp}" alt="{ten_sp}" class="w-100" style="aspect-ratio: 3 / 4 !important; object-fit: cover; display: block;">
                </div>
                <!-- 2. Phần thông tin chữ và nút bấm nằm phía dưới -->
                <div class="p-2 d-flex flex-column justify-content-between flex-grow-1">
                    <div class="lh-sm mb-2">
                        <h6 class="card-title text-white fw-bold mb-1" style="font-size: 0.8rem; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; white-space: normal;">{ten_sp}</h6>
                        <p class="card-text text-danger fw-bold mb-0" style="font-size: 0.85rem;">{gia_sp}đ</p>
                    </div>
                    <a href="/mua/{id_sp}" class="btn btn-danger btn-sm w-100 fw-bold py-1 mt-auto" style="font-size: 0.65rem; white-space: normal; line-height: 1.1;">
                        Mua Trên TikTok
                    </a>
                </div>
            </div>
        </div>
        """
    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lý Công Thức - Gym & Sports Store</title>
        <!-- Thay sang CSS Bootstrap ổn định, không bị Render chặn -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    
<style>
       body {{ 
            background-color: #111827; 
            color: #d1d5db; 
        }}
        .navbar {{ 
            background-color: #030712 !important; 
            border-bottom: 1px solid #1f2937; 
        }}
        .hero-section {{ 
            background-color: #030712; 
            padding: 25px 20px; 
            border-bottom: 1px solid #1f2937; 
        }}
        .footer {{ 
            background-color: #030712; 
            border-top: 1px solid #1f2937; 
        }}

        /* Hộp sản phẩm tự co giãn theo nội dung ảnh 3:4 */
        .card {{
            background-color: #1f2937 !important;
            border: 1px solid #374151 !important;
            border-radius: 12px !important;
            overflow: hidden;
            display: flex !important;
            flex-direction: column !important;
            margin-bottom: 12px;
            height: 100% !important; /* Xóa bỏ max-height để hộp tự kéo dài ra */
        }}

        .card img {{
            width: 100% !important;
            aspect-ratio: 3 / 4 !important; /* Khung chữ nhật đứng thời trang gym */
            object-fit: cover !important;
            display: block;
        }}

        .card-title {{
            font-size: 0.8rem !important;
            font-weight: 600;
            color: #f3f4f6;
            margin-bottom: 4px !important;
            line-height: 1.3;
        }}

        .card-text {{
            font-size: 0.85rem !important;
            font-weight: 700;
            color: #f59e0b !important;
            margin-bottom: 6px !important;
        }}

        .btn-danger {{
            font-size: 0.65rem !important;
            padding: 6px 0px !important;
            border-radius: 8px !important;
            background-color: #ef4444 !important;
            border: none !important;
            width: 100% !important;
            display: block !important;
            text-align: center;
        }}
    /* Hiệu ứng nhịp thở phập phồng tỏa sáng cho nút bấm */
        @keyframes nhipThoButton {{
            0% {{
                transform: scale(1);
                box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7);
            }}
            50% {{
                transform: scale(1.03); /* Phóng to nhẹ nút */
                background-color: #dc2626 !important; /* Đỏ đậm hơn */
                box-shadow: 0 0 10px 3px rgba(239, 68, 68, 0.5); /* Tỏa ánh hào quang */
            }}
            100% {{
                transform: scale(1);
                box-shadow: 0 0 0 0 rgba(239, 68, 68, 0.7);
            }}
        }}

        /* Ép nút bấm chạy hiệu ứng liên tục */
        .btn-danger {{
            animation: nhipThoButton 1.8s infinite ease-in-out !important;
            transition: all 0.3s ease !important;
        }}

        /* Hiệu ứng nhấc nhẹ hộp sản phẩm khi xem trên máy tính */
        .card {{
            transition: transform 0.3s ease, border-color 0.3s ease !important;
        }}
        .card:hover {{
            transform: translateY(-5px) !important;
            border-color: #ef4444 !important;
        }}
        /* Định dạng bong bóng Zalo nổi ở góc phải màn hình */
        .zalo-bubble {{
            position: fixed !important;
            bottom: 20px !important;
            right: 20px !important;
            z-index: 9999 !important; /* Đảm bảo luôn nổi lên trên cùng */
            width: 60px;
            height: 60px;
            background-color: #0068ff;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: 0 4px 15px rgba(0, 104, 255, 0.4);
            transition: transform 0.3s ease;
        }}

        /* Hiệu ứng lắc lư tự động để thu hút khách bấm vào */
        @keyframes lacZalo {{
            0%, 100% {{ transform: rotate(0deg) scale(1); }}
            10%, 30% {{ transform: rotate(-10deg) scale(1.05); }}
            20%, 40% {{ transform: rotate(10deg) scale(1.05); }}
            50% {{ transform: rotate(0deg) scale(1); }}
        }}

        .zalo-bubble {{
            animation: lacZalo 2.5s infinite ease-in-out;
        }}

        .zalo-bubble:hover {{
            transform: scale(1.1) !important;
            background-color: #0056d6;
        }}

        .zalo-bubble img {{
            width: 35px;
            height: 35px;
            object-fit: contain;
        }}
        </style>
    </head>
    <body>

        <!-- MENU -->
        <nav class="navbar navbar-dark bg-dark sticky-top">
            <div class="container">
                <a class="navbar-brand fw-bold text-uppercase tracking-wider" href="#">
                    💥 LÝ CÔNG THỨC <span class="text-danger">STORE</span>
                </a>
            </div>
        </nav>

        <!-- BANNER -->
        <div class="hero-section text-center">
            <div class="container">
                <h1 class="display-5 fw-bold text-white uppercase">Bộ Sưu Tập <span class="text-danger">Thời Trang & Gym</span></h1>
                <p class="lead text-secondary max-w-xl mx-auto fs-6">Chuyên phụ kiện tập gym chất lượng cao cho anh em thể hình. Uy tín, chất lượng.</p>
            </div>
        </div>

        <!-- MAIN CONTENT -->
        <div class="container my-5">
            <div class="row">
                <!-- CỘT TRÁI SẢN PHẨM -->
                <div class="col-12">
                    <div class="row row-cols-2 row-cols-md-3 row-cols-lg-4 g-3">
                        {html_san_pham}
                    </div>
                </div>
                <!-- BONG BÓNG ZALO LIÊN KẾT NỔI -->
                <a href="https://zalo.me/0962731032" target="_blank" class="zalo-bubble" title="Chat qua Zalo">
                    <img src="https://wikimedia.org" alt="Zalo">
                </a>
        <!-- FOOTER -->
        <footer class="footer bg-dark py-4 text-center border-top border-secondary">
            <div class="container">
                <p class="mb-1">📍 Địa chỉ kho: Quận 12, Thành phố Hồ Chí Minh</p>
                <p class="mb-1">✉️ Email: lycongthu@gmail.com</p>
                <p class="text-muted mb-0">© 2026 LÝ CÔNG THỨC STORE. All rights reserved.</p>
            </div>
        </footer>

    </body>
    </html>
    """
    return html_content

@app.get("/mua/{id_san_pham}")
def dieu_huong_tiktok(id_san_pham: int):
    for sp in DANH_SACH_SAN_PHAM:
        if sp["id"] == id_san_pham:
            return RedirectResponse(url=sp["link_tiktok"])
    return RedirectResponse(url="/")