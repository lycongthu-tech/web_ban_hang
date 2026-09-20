import os
from flask import Flask, render_template_string

# Sử dụng cách khai báo chuỗi trực tiếp để tránh lỗi dính phông chữ hiển thị trên máy của bạn
app = Flask("_main_")

# 1. CƠ SỞ DỮ LIỆU SẢN PHẨM AFFILIATE (Dễ dàng thêm mới, chỉnh sửa tại đây)
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

# 2. TOÀN BỘ GIAO DIỆN HTML, CSS TAILWIND VÀ JAVASCRIPT BỘ LỌC
GIAO_DIEN_HTML = """
<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LÝ CÔNG THỨC STORE - Tiếp Thị Liên Kết Đồ Gym Cao Cấp</title>
    <script src="https://tailwindcss.com"></script>
    <style>
        .the-san-pham {
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .hidden-card {
            opacity: 0;
            transform: scale(0.9);
            position: absolute;
            visibility: hidden;
            width: 0;
            height: 0;
            padding: 0;
            margin: 0;
            border: none;
        }
    </style>
</head>
<body class="bg-gray-50 text-gray-800 font-sans min-h-screen flex flex-col justify-between">

    <header class="bg-white border-b border-gray-100 shadow-sm sticky top-0 z-50">
        <div class="max-w-6xl mx-auto px-4 py-4 flex flex-col sm:flex-row items-center justify-between gap-4">
            <div class="flex items-center gap-2">
                <span class="text-xl font-black text-red-600 tracking-wider">★ LÝ CÔNG THỨC STORE</span>
            </div>
            <p class="text-xs text-gray-500 font-medium bg-gray-50 px-3 py-1 rounded-full border border-gray-100">
                Chuyên phụ kiện tập gym chất lượng cao cho anh em tập luyện
            </p>
        </div>
    </header>

    <section class="max-w-6xl mx-auto px-4 mt-8 w-full">
        <div class="flex flex-wrap items-center justify-center gap-2 pb-2">
            <button onclick="locDanhMuc('all', this)" class="nut-loc px-5 py-2 text-xs font-semibold uppercase tracking-wider rounded-full bg-red-600 text-white shadow-sm border border-transparent transition-all">
                Tất cả sản phẩm
            </button>
            <button onclick="locDanhMuc('ao-gym', this)" class="nut-loc px-5 py-2 text-xs font-semibold uppercase tracking-wider rounded-full bg-white text-gray-600 border border-gray-200 hover:border-gray-400 transition-all">
                Áo tập gym
            </button>
            <button onclick="locDanhMuc('quan-gym', this)" class="nut-loc px-5 py-2 text-xs font-semibold uppercase tracking-wider rounded-full bg-white text-gray-600 border border-gray-200 hover:border-gray-400 transition-all">
                Quần tập gym
            </button>
            <button onclick="locDanhMuc('phu-kien', this)" class="nut-loc px-5 py-2 text-xs font-semibold uppercase tracking-wider rounded-full bg-white text-gray-600 border border-gray-200 hover:border-gray-400 transition-all">
                Phụ kiện & Đai lưng
            </button>
        </div>
    </section>

    <main class="max-w-6xl mx-auto px-4 py-6 w-full flex-grow">
        <div id="khung-chua-san-pham" class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6 relative">
            
            {% for sp in san_pham %}
            <div class="the-san-pham bg-white rounded-xl overflow-hidden border border-gray-100 shadow-sm flex flex-col justify-between group" data-category="{{ sp.danh_muc }}">
                <div class="w-full aspect-[3/4] bg-gray-50 overflow-hidden relative border-b border-gray-50">
                    <img src="{{ sp.anh }}" class="w-full h-full object-cover transition-transform duration-500 group-hover:scale-105" alt="{{ sp.ten }}">
                    <span class="absolute top-3 left-3 bg-red-600 text-white text-[10px] font-bold uppercase tracking-wide px-2 py-0.5 rounded shadow-sm">
                        {{ sp.tag }}
                    </span>
                </div>
                
                <div class="p-4 flex-grow flex flex-col justify-between text-center bg-white">
                    <div class="mb-4">
                        <h3 class="text-gray-800 font-bold text-sm line-clamp-2 min-h-[40px] px-1 mb-1 leading-tight group-hover:text-red-600 transition-colors">
                            {{ sp.ten }}
                        </h3>
                        <div class="flex items-center justify-center gap-2">
                            <span class="text-red-600 font-extrabold text-base">{{ sp.gia }}</span>
                            <span class="text-gray-400 line-through text-xs">{{ sp.gia_cu }}</span>
                        </div>
                    </div>
                    
                    <a href="{{ sp.link_affiliate }}" target="_blank" rel="noopener noreferrer" class="block w-full text-center bg-gray-900 hover:bg-red-600 text-white font-bold uppercase tracking-wider py-2.5 rounded-lg text-[11px] shadow-sm transition-colors duration-300">
                        Mua trên TikTok Shop
                    </a>
                </div>
            </div>
            {% endfor %}
            
        </div>
    </main>

    <footer class="bg-white border-t border-gray-100 py-6 mt-12 w-full text-center">
        <p class="text-xs text-gray-500 font-medium">
            📍 Địa chỉ kho: Quận 12, Thành phố Hồ Chí Minh
        </p>
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
                nut.classList.remove('bg-red-600', 'text-white', 'shadow-sm', 'border-transparent');
                nut.classList.add('bg-white', 'text-gray-600', 'border-gray-200');
            });

            element.classList.remove('bg-white', 'text-gray-600', 'border-gray-200');
            element.classList.add('bg-red-600', 'text-white', 'shadow-sm', 'border-transparent');
        }
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(GIAO_DIEN_HTML, san_pham=DANH_SACH_SAN_PHAM)

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)