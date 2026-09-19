from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

DANH_SACH_SAN_PHAM = [
    {
        "id": 1,
        "ten": "Áo Thun Nén Gym Nam - Dài Tay",
        "gia": "109.000đ",
        "hinh_anh": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSpXnJFkIaYCNTqwtkDGxYdVb_X8U8joDtbh1CA-pM0TQ&s=10",
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
            <div class="card h-100 bg-secondary text-white border-dark shadow-sm">
                <img src="{anh_sp}" class="card-img-top" alt="{ten_sp}" style="height: 200px; object-fit: cover;">
                <div class="card-body d-flex flex-column justify-content-between">
                    <div>
                        <h5 class="card-title text-truncate-2">{ten_sp}</h5>
                        <p class="card-text text-warning fw-bold fs-5">{gia_sp}</p>
                    </div>
                    <a href="/mua/{id_sp}" class="btn btn-danger w-full mt-3 fw-bold">
                        🛒 Mua Ngay Trên TikTok
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
            body {{ background-color: #111827; color: #d1d5db; }}
            .navbar {{ background-color: #030712 !important; border-b: 1px solid #1f2937; }}
            .hero-section {{ background-color: #030712; padding: 60px 20px; border-bottom: 1px solid #1f2937; }}
            .footer {{ background-color: #030712; border-t: 1px solid #1f2937; color: #6b7280; font-size: 0.8rem; py: 30px; }}
            .text-truncate-2 {{ display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }}
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
                <div class="col-lg-9">
                    <div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 g-4">
                        {html_san_pham}
                    </div>
                </div>
                <!-- CỘT PHẢI SIDEBAR -->
                <div class="col-lg-3 mt-4 mt-lg-0">
                    <div class="p-3 bg-dark rounded border border-secondary shadow-sm mb-4">
                        <h6 class="text-white uppercase fw-bold border-start border-danger border-3 ps-2 mb-3">Đánh Giá Khách Hàng</h6>
                        <p class="small text-secondary italic">"Áo mặc ôm body rất khít, tập gym tôn dáng lắm shop ơi!"</p>
                        <p class="small text-danger fw-bold text-end mb-0">- Tuấn Anh Nguyễn</p>
                    </div>
                </div>
            </div>
        </div>

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