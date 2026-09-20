import os
from flask import Flask, render_template_string

app = Flask(__name__)

DANH_SACH_SAN_PHAM = [
    {
        "id": 1,
        "ten": "(Mua 3 giảm 10k tặng móc khoá) Áo Thun Unisex From Rộng Top Women",
        "gia": "89.000đ",
        "gia_cu": "140.000đ",
        "danh_muc": "the-thao-nu",
        "tag": "Lượt mua 127k",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhtpBg81aX-I6p9s/",
        "anh": "https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lzxbv3atd8i558.webp"
    },    
    {       
        "id": 2,
        "ten": "Bộ Đồ Đùi Thể Thao Nữ NQ Có Túi Kéo, Gym, Yoga, Chạy Bộ, Mặc Nhà",
        "gia": "89.000đ",
        "gia_cu": "140.000đ",
        "danh_muc": "the-thao-nu",
        "tag": "-36%",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhpyXqkUpR-VFFsR/",
        "anh": "https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lynof44a080xc7.webp"
    },
    {
        "id": 3,
        "ten": "Áo Thun Nén Gym Nam - Dài Tay Cao Cấp",
        "gia": "109.000đ",
        "gia_cu": "169.000đ",
        "danh_muc": "the-thao-nam",
        "tag": "Hàng Việt",
        "link_affiliate": "https://vt.tiktok.com/ZS9AroE8UMsfw-ydKK6/",
        "anh": "https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-louoqxybyqyzf2.webp"
    },
    {
        "id": 4,
        "ten": "Găng Tay Tập Gym Chống Trượt Bảo Vệ Tay",
        "gia": "12x.000đ",
        "gia_cu": "200.000đ",
        "danh_muc": "phu-kien",
        "tag": "Chính hãng",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhxJcV9y7a-9vJhC/",
        "anh": "https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lyetjvzf69whe0.webp"
    },
    {    
        "id": 5,
        "ten": "Thảm Tập Gym Yoga Chống Trượt Giảm Chấn",
        "gia": "225.000đ",
        "gia_cu": "350.000đ",
        "danh_muc": "phu-kien",
        "tag": "mall",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhQa7MJMBa-BPWUt/",
        "anh": "https://down-vn.img.susercontent.com/file/sg-11134201-820nt-mnavz44ql6v91d.webp"
    },
    {
        "id": 6,
        "ten": "Quần Jogger Thể Thao Nam vải poly cao cấp",
        "gia": "140.000đ",
        "gia_cu": "179.000đ",
        "danh_muc": "the-thao-nam",
        "tag": "Hàng Việt",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhC5Moeddf-WlmzF/",
        "anh": "https://down-vn.img.susercontent.com/file/vn-11134207-7r98o-lpc25e8dopce45.webp"
    },
    {
        "id": 7,
        "ten": "Áo 3 Lỗ Thun Gân, Co Giãn Thoáng Mát",
        "gia": "52.000đ",
        "gia_cu": "150.000đ",
        "danh_muc": "the-thao-nam",
        "tag": "-65%",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhXFoEKkpq-VVSPv/",
        "anh": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT2arFvo8BmKG7VYBJMXXNFc-QrF0fB49LcvEFsI0JvuQCVDr6G"
    },
    {
        "id": 8,
        "ten": "Áo Thun Thể Thao Nam Fron Ôm, Thun Lạnh Cao Cấp",
        "gia": "95.000đ",
        "gia_cu": "149.000đ",
        "danh_muc": "the-thao-nam",
        "tag": "-36%",
        "link_affiliate": "https://vt.tiktok.com/ZS9Ahq3tcdLfB-i2kKQ/",
        "anh": "https://down-vn.img.susercontent.com/file/vn-11134207-7qukw-lhyfmy2e4mo164.webp"
    },    
    {
        "id": 9,
        "ten": "Sữa Dinh Dưỡng Muscle Mass Gainer 12lbs, WHEYSTORE",
        "gia": "2.890.000đ",
        "gia_cu": "3.200.000đ",
        "danh_muc": "whey-tpbs",
        "tag": "Giảm 300k",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhnEJxHYHk-Q7j5m/",
        "anh": "https://www.wheystore.vn/images/products/2023/12/14/large/inforgraphic-muscle-mass-gainer-12lbs_1702548078.jpg.webp"
    },    
    {
        "id": 10,
        "ten": "Viên Kẽm AMAGAIN bổ sung kẽm Chelamax Bisglycinate",
        "gia": "152.000đ",
        "gia_cu": "175.000đ",
        "danh_muc": "whey-tpbs",
        "tag": "Hơn 400k lượt mua",
        "link_affiliate": "https://vt.tiktok.com/ZS9Ah7QRcrLQ1-TVFV9/",
        "anh": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlxZv08rKht6wDB9mEAgl1ukLBQmGvzUQDxH85D7qJVw&s=10"
    },
    {   "id": 11,
        "ten": "Bộ Đồ Đùi Thể Thao Nữ NQ Có Túi Kéo, Gym, Yoga, Chạy Bộ, Mặc Nhà",
        "gia": "89.000đ",
        "gia_cu": "140.000đ",
        "danh_muc": "the-thao-nu",
        "tag": "-36%",
        "link_affiliate": "https://vt.tiktok.com/ZS9AhpyXqkUpR-VFFsR/",
        "anh": "data:image/jpeg;base64,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"
    }
]

GIAO_DIEN_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LÝ THỨC STORE - Đồ Gym Cao Cấp</title>
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
         .category-btn, .btn-affiliate {
            transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
            position: relative;
            overflow: hidden;
        }

        /* Rê chuột hoặc chạm vào: Nút nổi nhẹ lên và sáng hơn */
        .category-btn:hover, .btn-affiliate:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            filter: brightness(1.1);
        }

        /* Khi bấm giữ nút: Thu nhỏ nhẹ tạo cảm giác đàn hồi tốt */
        .category-btn:active, .btn-affiliate:active {
            transform: translateY(1px);
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

/* 2. Hiệu ứng bong bóng Zalo tự bay nhấp nhô liên tục */
.zalo-bubble {
    animation: floatAnimation 3s ease-in-out infinite;
    transition: transform 0.3s ease;
}

/* Rê chuột vào icon Zalo sẽ tự phóng to và hơi xoay nhẹ nhẹ */
.zalo-bubble:hover {
    transform: scale(1.1) rotate(5deg);
}

@keyframes floatAnimation {
    0% { transform: translateY(0px); }
    50% { transform: translateY(-10px); }
    100% { transform: translateY(0px); }
}

/* 3. Hiệu ứng xuất hiện mượt mà khi tải trang cho các thẻ sản phẩm */
.grid-container > div {
    animation: fadeInProduct 0.6s cubic-bezier(0.25, 1, 0.5, 1) forwards;
    opacity: 0;
}

@keyframes fadeInProduct {
    from {
        opacity: 0;
        transform: translateY(15px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
.btn-affiliate {
    animation: breathingAnimation 2s ease-in-out infinite;
}

@keyframes breathingAnimation {
    0% {
        transform: scale(1);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    50% {
        transform: scale(1.04); /* Phóng to nhẹ 4% */
        box-shadow: 0 8px 20px rgba(254, 44, 85, 0.4); /* Tạo quầng sáng mờ màu đỏ thương hiệu TikTok */
    }
    100% {
        transform: scale(1);
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
}
    </style>
</head>
<body>
    <header>
        <div class="logo">★ LÝ THỨC STORE 💪</div>
        <p class="slogan">Chuyên sưu tầm thời trang, phụ kiện nam nữ giá giảm sâu sập sàn, chất lượng, uy tín cho anh em</p>
    </header>

    <section class="menu-section">
        <div class="menu-container">
            <button onclick="locDanhMuc('all', this)" class="nut-loc active">Tất cả sản phẩm</button>
            <button onclick="locDanhMuc('the-thao-nam', this)" class="nut-loc">🏋️‍♀️Thể Thao Nam</button>
            <button onclick="locDanhMuc('the-thao-nu', this)" class="nut-loc">💃Đồ Thể Thao Nữ</button>
            <button onclick="locDanhMuc('gym-and-run', this)" class="nut-loc">🏃‍♂️Đồ Chuyên Gym and Run</button>
            <button onclick="locDanhMuc('phu-kien', this)" class="nut-loc">🏅Phụ kiện & Dụng Cụ</button>
            <button onclick="locDanhMuc('whey-tpbs', this)" class="nut-loc">🥤Whey & Thực Phẩm Bổ Sung</button>
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