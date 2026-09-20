import os
from flask import Flask, render_template_string

app = Flask(__name__)

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
        "ten": "Quần Short Tập Gym Nam 2 Lớp Co Giãn",
        "gia": "145.000đ",
        "gia_cu": "220.000đ",
        "danh_muc": "quan-gym",
        "tag": "Mới về",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    },
    {
        "id": 5,
        "ten": "Áo Ba Lỗ Tập Gym Nam Sát Nách Thấm Hút",
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
    },
     {
        "id": 7,
        "ten": "Whey Protein Tăng Cơ Giảm Mỡ Hấp Thu Nhanh Cao Cấp",
        "gia": "890.000đ",
        "gia_cu": "1.200.000đ",
        "danh_muc": "whey-tpbs",
        "tag": "Bán chạy",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    },
    {
        "id": 8,
        "ten": "BCAA Hỗ Trợ Phục Hồi Cơ Bắp Trong Lúc Tập",
        "gia": "550.000đ",
        "gia_cu": "750.000đ",
        "danh_muc": "whey-tpbs",
        "tag": "Giá tốt",
        "link_affiliate": "https://tiktok.com",
        "anh": "https://unsplash.com"
    }
]

GIAO_DIEN_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LÝ CÔNG THỨC STORE - Đồ Gym Cao Cấp</title>
    <style>
        * { box-sizing: border-box; }
        body { background-color: #f3f4f6; color: #1f2937; font-family: system-ui, sans-serif; margin: 0; padding: 0; min-height: 100vh; display: flex; flex-direction: column; }
        header { background-color: #ffffff; border-bottom: 1px solid #e5e7eb; padding: 12px 16px; width: 100%; text-align: center; }
        .logo { font-size: 18px; font-weight: 900; color: #dc2626; letter-spacing: 0.05em; }
        .slogan { font-size: 11px; color: #6b7280; margin: 4px 0 0 0; }
        .menu-section { max-w: 1140px; width: 100%; margin: 20px auto 10px auto; padding: 0 12px; }
        .menu-container { display: flex; overflow-x: auto; white-space: nowrap; gap: 8px; padding-bottom: 12px; border-bottom: 1px solid #e5e7eb; }
        @media (min-width: 640px) { .menu-container { justify-content: center; } }
        .nut-loc { padding: 8px 16px; font-size: 12px; font-weight: 600; text-transform: uppercase; border-radius: 9999px; border: 1px solid #d1d5db; background-color: #ffffff; color: #4b5563; cursor: pointer; }
        .nut-loc.active { background-color: #dc2626; color: #ffffff; border-color: transparent; }
        main { max-w: 1140px; width: 100%; margin: 0 auto; padding: 10px 12px 40px 12px; flex-grow: 1; }
        .grid-container { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
        @media (min-width: 768px) { .grid-container { grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; } }
        .the-san-pham { background-color: #ffffff; border-radius: 10px; overflow: hidden; border: 1px solid #e5e7eb; box-shadow: 0 1px 3px rgba(0,0,0,0.05); display: flex; flex-direction: column; justify-content: space-between; }
        .img-container { width: 100%; position: relative; padding-top: 133.33%; background-color: #f9fafb; }
        .img-container img { width: 100%; height: 100%; object-fit: cover; position: absolute; top: 0; left: 0; }
        .tag-san-pham { position: absolute; top: 8px; left: 8px; background-color: #dc2626; color: #ffffff; font-size: 9px; font-weight: 700; padding: 2px 6px; border-radius: 4px; }
        .info-container { padding: 12px; flex-grow: 1; display: flex; flex-direction: column; justify-content: space-between; text-align: center; }
        .ten-san-pham { color: #1f2937; font-weight: 700; font-size: 13px; margin: 0 0 8px 0; line-height: 1.4; min-height: 36px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .price-container { display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 2px; margin-bottom: 12px; }
        @media (min-width: 400px) { .price-container { flex-direction: row; gap: 8px; } }
        .gia-moi { color: #dc2626; font-weight: 800; font-size: 14px; }
        .gia-cu { color: #9ca3af; text-decoration: line-through; font-size: 11px; }
        .btn-affiliate { display: block; width: 100%; text-align: center; background-color: #111827; color: #ffffff; font-weight: 700; text-transform: uppercase; padding: 10px 0; border-radius: 6px; font-size: 11px; text-decoration: none; }
        footer { background-color: #ffffff; border-top: 1px solid #e5e7eb; padding: 20px 0; text-align: center; width: 100%; }
        footer p { margin: 0; font-size: 11px; color: #6b7280; }
        .hidden-card { opacity: 0; transform: scale(0.9); position: absolute; visibility: hidden; width: 0; height: 0; padding: 0; margin: 0; border: none; }
    </style>
</head>
<body>
    <header>
        <div class="logo">★ LÝ CÔNG THỨC STORE</div>
        <p class="slogan">Chuyên phụ kiện tập gym chất lượng cao cho anh em tập luyện</p>
    </header>

    <section class="menu-section">
        <div class="menu-container">
            <button onclick="locDanhMuc('all', this)" class="nut-loc active">Tất cả sản phẩm</button>
            <button onclick="locDanhMuc('ao-gym', this)" class="nut-loc">Áo tập gym</button>
            <button onclick="locDanhMuc('quan-gym', this)" class="nut-loc">Quần tập gym</button>
            <button onclick="locDanhMuc('phu-kien', this)" class="nut-loc">Phụ kiện & Đai lưng</button>
            <button onclick="locDanhMuc('whey-tpbs', this)" class="nut-loc">Whey & TPBS</button>
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
            tatCaNut.forEach(nut => { nut.classList.remove('active'); });
            element.classList.add('active');
        }
    </script>
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
            tatCaNut.forEach(nut => { nut.classList.remove('active'); });
            element.classList.add('active');
        }
    </script>
    <!-- BONG BÓNG MESSENGER LIÊN KẾT NỔI CỐ ĐỊNH Ở GÓC MÀN HÌNH -->
    <a href="https://m.me/thuc.ly.165" target="_blank" rel="noopener noreferrer" 
       style="position: fixed; bottom: 145px; right: 20px; z-index: 9999; display: flex; align-items: center; justify-content: center; width: 55px; height: 55px; background-color: #0084ff; border-radius: 50%; box-shadow: 0 4px 10px rgba(0, 132, 255, 0.35); transition: transform 0.3s ease-in-out;"
       onmouseover="this.style.transform='scale(1.1)'" 
       onmouseout="this.style.transform='scale(1)'">
        <img src="https://scontent.fsgn5-7.fna.fbcdn.net/v/t39.30808-1/626864756_2559365824465215_7073198888247271318_n.jpg?stp=dst-jpg_tt6&cstp=mx635x642&ctp=s200x200&_nc_cat=104&_nc_map=urlgen_bucketless&ccb=1-7&_nc_sid=e99d92&_nc_eui2=AeHi4JHl0fGLLAfsw_Sr_kZi_EgIi-FIPff8SAiL4Ug99yEJ5BmVOB5z_2V14Brpm4GQi5SmoYrejPFctXaPChLw&_nc_ohc=w9zw0aWggrAQ7kNvwHMFJUY&_nc_oc=AdrZcrL3mB4bpOotbAY-xaVXgisZkjurWSUulAwct1HHhgsUKeH8sv9dnRpzuJyjylR-D8ypMdUt9R5_z21xeYiI&_nc_zt=24&_nc_ht=scontent.fsgn5-7.fna&_nc_gid=eIuwbgM8YzoOInap5Cq2pA&_nc_ss=7b2a8&oh=00_AQK-uRENhSZ1wspUmh68VJmlN8Q70kwhhPaPafKSN515Dw&oe=6AB5BB0A" 
     alt="Liên hệ Messenger" 
     style="width: 100%; height: 100%; object-fit: cover; border-radius: 50%;">
    </a>

    <!-- BONG BÓNG ZALO LIÊN KẾT NỔI CỐ ĐỊNH Ở GÓC MÀN HÌNH -->
    <a href="https://zalo.me/0962731032" target="_blank" rel="noopener noreferrer" 
       style="position: fixed; bottom: 80px; right: 20px; z-index: 9999; display: flex; align-items: center; justify-content: center; width: 55px; height: 55px; background-color: #0068ff; border-radius: 50%; box-shadow: 0 4px 10px rgba(0, 104, 255, 0.35); transition: transform 0.3s ease-in-out;"
       onmouseover="this.style.transform='scale(1.1)'" 
       onmouseout="this.style.transform='scale(1)'">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQIcHyrB2HX3UcU5IVx-DdWJJLol-jGa_rSuTDHLCQzmg&s=10" 
             alt="Liên hệ Zalo" style="width: 32px; height: 32px; object-fit: contain;">
    </a>

</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(GIAO_DIEN_HTML, san_pham=DANH_SACH_SAN_PHAM)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)