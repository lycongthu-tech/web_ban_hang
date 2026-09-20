import os
from flask import Flask, render_template_string

app = Flask(__name__)

# 1. CƠ SỞ DỮ LIỆU SẢN PHẨM AFFILIATE (Duyệt dữ liệu mượt mà)
DANH_SACH_SAN_PHAM = [
    {
        "id": 1,
        "ten": "Áo Thun Nén Gym Nam - Dài Tay Cao Cấp",
        "gia": "109.000đ",
        "gia_cu": "180.000đ",
        "danh_muc": "ao-gym",
        "tag": "Bán chạy",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    },
    {
        "id": 2,
        "ten": "Đai Lưng Hỗ Trợ Gánh Đùi Deadlift Chuyên Nghiệp",
        "gia": "310.000đ",
        "gia_cu": "450.000đ",
        "danh_muc": "phu-kien",
        "tag": "Bảo hộ",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    },
    {
        "id": 3,
        "ten": "Thảm Tập Yoga Chống Trượt Giảm Chấn",
        "gia": "225.000đ",
        "gia_cu": "350.000đ",
        "danh_muc": "phu-kien",
        "tag": "Êm ái",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    },
    {
        "id": 4,
        "ten": "Quần Short Tập Gym Nam 2 Lớp Co Giãn thoải mái",
        "gia": "145.000đ",
        "gia_cu": "220.000đ",
        "danh_muc": "quan-gym",
        "tag": "Mới về",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    },
    {
        "id": 5,
        "ten": "Áo Ba Lỗ Tập Gym Nam Sát Nách Thấm Hút Mồ Hôi",
        "gia": "89.000đ",
        "gia_cu": "135.000đ",
        "danh_muc": "ao-gym",
        "tag": "Trending",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    },
    {
        "id": 6,
        "ten": "Quần Dài Jogger Thể Thao Nam Co Giãn 4 Chiều",
        "gia": "195.000đ",
        "gia_cu": "290.000đ",
        "danh_muc": "quan-gym",
        "tag": "Basic",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    }
]

# 2. TOÀN BỘ GIAO DIỆN HỆ THỐNG MỚI
GIAO_DIEN_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LÝ CÔNG THỨC STORE - Tiếp Thị Liên Kết Đồ Gym Cao Cấp</title>
    <style>
        /* CSS Gốc tự dựng - Đảm bảo giao diện luôn hiển thị 100% không sợ bị chặn link */
        body { background-color: #f3f4f6; color: #1f2937; font-family: system-ui, -apple-system, sans-serif; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-col: column; justify-content: space-between; }
        header { background-color: #ffffff; border-bottom: 1px solid #e5e7eb; padding: 15px 20px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); sticky: top; z-index: 50; }
        .header-container { max-w: 1140px; margin: 0 auto; display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; }
        .logo { font-size: 20px; font-weight: 900; color: #dc2626; letter-spacing: 0.05em; }
        .slogan { font-size: 12px; color: #6b7280; font-weight: 500; background-color: #f9fafb; padding: 4px 12px; border-radius: 9999px; border: 1px solid #e5e7eb; }
        
        .menu-section { max-width: 1140px; margin: 30px auto 10px auto; padding: 0 15px; text-align: center; }
        .menu-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; border-bottom: 1px solid #e5e7eb; padding-bottom: 15px; }
        .nut-loc { px: 20px; padding: 8px 20px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; border-radius: 9999px; border: 1px solid #d1d5db; background-color: #ffffff; color: #4b5563; cursor: pointer; transition: all 0.3s; }
        .nut-loc:hover { border-color: #9ca3af; }
        .nut-loc.active { bg-color: #dc2626; background-color: #dc2626; color: #ffffff; border-color: transparent; box-shadow: 0 1px 3px rgba(0,0,0,0.1); }
        
        main { max-width: 1140px; margin: 0 auto; padding: 20px 15px; flex-grow: 1; }
        .grid-container { display: grid; grid-template-columns: repeat(1, minmax(0, 1fr)); gap: 24px; }
        @media (min-width: 640px) { .grid-container { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
        @media (min-width: 1024px) { .grid-container { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
        
        .the-san-pham { background-color: #ffffff; border-radius: 12px; overflow: hidden; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between; transition: all 0.4s ease-in-out; }
        .the-san-pham:hover { transform: translateY(-4px); box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
        .img-container { width: 100%; position: relative; padding-top: 133.33%; bg-color: #f9fafb; overflow: hidden; border-bottom: 1px solid #f3f4f6; }
        .img-container img { width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; transition: transform 0.5s; }
        .the-san-pham:hover .img-container img { transform: scale(1.05); }
        .tag-san-pham { absolute: top-3 left-3; position: absolute; top: 12px; left: 12px; background-color: #dc2626; color: #ffffff; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 2px 8px; border-radius: 4px; box-shadow: 0 1px 2px rgba(0,0,0,0.05); z-index: 10; }
        
        .info-container { padding: 16px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; text-align: center; }
        .ten-san-pham { color: #1f2937; font-weight: 700; font-size: 14px; margin: 0 0 8px 0; line-height: 1.4; min-height: 40px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .price-container { display: flex; align-items: center; justify-content: center; gap: 8px; margin-bottom: 16px; }
        .gia-moi { color: #dc2626; font-weight: 800; font-size: 16px; }
        .gia-cu { color: #9ca3af; text-decoration: line-through; font-size: 12px; }
        
        .btn-affiliate { display: block; width: 100%; text-align: center; background-color: #111827; color: #ffffff; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; padding: 10px 0; border-radius: 8px; font-size: 11px; text-decoration: none; box-shadow: 0 1px 2px rgba(0,0,0,0.05); transition: background-color 0.3s; }
        .btn-affiliate:hover { background-color: #dc2626; }
        
        footer { background-color: #ffffff; border-top: 1px solid #e5e7eb; padding: 24px 0; text-align: center; margin-top: 48px; width: 100%; }
        footer p { margin: 0; font-size: 12px; color: #555555; font-weight: 500; }
        
        .hidden-card { opacity: 0; transform: scale(0.9); position: absolute; visibility: hidden; width: 0; height: 0; padding: 0; margin: 0; border: none; }
    </style>
</head>
<body>

    <header>
        <div class="header-container">
            <div class="logo">★ LÝ CÔNG THỨC STORE</div>
            <p class="slogan">Chuyên phụ kiện tập gym chất lượng cao cho anh em tập luyện</p>
        </div>
    </header>

    <section class="menu-section">
        <div class="menu-container">
            <button onclick="locDanhMuc('all', this)" class="nut-loc active">Tất cả sản phẩm</button>
            <button onclick="locDanhMuc('ao-gym', this)" class="nut-loc">Áo tập gym</button>
            <button onclick="locDanhMuc('quan-gym', this)" class="nut-loc">Quần tập gym</button>
            <button onclick="locDanhMuc('phu-kien', this)" class="nut-loc">Phụ kiện & Đai lưng</button>
        </div>
    </section>

    <main>
        <div id="khung-chua-san-pham" class="grid-container">
            {% for sp in san_pham %}
            <div class="the-san-pham" data-category="{{ sp.danh_muc }}">
                <div class="img-container">
                    <img src="{{ sp.anh }}" alt="{{ sp.ten }}">
                    <span class="tag-san-pham">{{ sp.tag }}</span>
                </div>
                <div class="info-container">
                    <div>
                        <h3 class="ten-san-pham">{{ sp.ten }}</h3>
                        <div class="price-container">
                            <span class="gia-moi">{{ sp.gia }}</span>
                            <span class="gia-cu">{{ sp.gia_cu }}</span>
                        </div>
                    </div>
                    <a href="{{ sp.link_affiliate }}" target="_blank" rel="noopener noreferrer" class="btn-affiliate">
                        Mua trên TikTok Shop
                    </a>
                </div>
            </div>
            {% endfor %}
        </div>
    </main>

    <footer>
        <p>📍 Địa chỉ kho: Quận 12, Thành phố Hồ Chí Minh</p>
    </footer>

    <script>
        function locDanhMuc(category, element) {
            const tatCaThe = document.querySelectorAll('.the-san-pham');
            tatCaThe.forEach(the => {
                if (category === 'all' || the.getAttribute('data-category') === category) {
                    the.classList.remove('hidden-card');
                } else {
                    the.classList.add('hidden-card');
                }
            });

            const tatCaNut = document.querySelectorAll('.nut-loc');
            tatCaNut.forEach(nut => {
                nut.classList.remove('active');
            });
            element.classList.add('active');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(GIAO_DIEN_HTML, san_pham=DANH_SACH_SAN_PHAM)

if __name__ == "__main__":
    app.run(debug=True)