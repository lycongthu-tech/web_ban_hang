from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.responses import RedirectResponse

app = FastAPI()

# 📦 DANH SÁCH SẢN PHẨM (Hộp hồ sơ Dictionary nằm trong List)
DANH_SACH_SAN_PHAM = [
    {
        "id": 1,
        "ten": "Áo Thun Nén Gym Nam - Dài Tay",
        "gia": "109.000đ",
        "hinh_anh": "https://unsplash.com", # Link ảnh áo thun bạn dán
        "link_tiktok": "https://tiktok.com" # <-- Thay link affiliate áo của bạn vào đây
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
    # Tự động sinh danh sách sản phẩm theo chuẩn khung lưới hiện đại
    html_san_pham = ""
    for sp in DANH_SACH_SAN_PHAM:
        html_san_pham += f"""
        <div class="bg-slate-800 rounded-xl overflow-hidden shadow-lg border border-slate-700 hover:border-pink-500 transition-all duration-300 flex flex-col justify-between">
            <img src="{sp['hinh_anh']}" class="w-full h-48 object-cover" alt="{sp['ten']}">
            <div class="p-4 flex-grow flex flex-col justify-between">
                <div>
                    <h3 class="text-white font-semibold text-base line-clamp-2 mb-2">{sp['ten']}</h3>
                    <p class="text-pink-500 font-bold text-lg mb-4">{sp['gia']}</p>
                </div>
                <a href="/mua/{sp['id']}" class="block text-center bg-pink-600 hover:bg-pink-700 text-white font-medium py-2 rounded-lg transition duration-200 shadow-md hover:shadow-pink-500/20">
                    🛒 Mua Ngay Trên TikTok
                </a>
            </div>
        </div>
        """

    # Giao diện tổng thể chuẩn uy tín như trang mẫu
    html_content = f"""
    <!DOCTYPE html>
    <html lang="vi">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Lý Công Thức - Gym & Sports Store</title>
        <!-- Nhúng khung thiết kế hiện đại Tailwind CSS -->
        <script src="https://tailwindcss.com"></script>
    </head>
    <body class="bg-slate-900 text-slate-300 font-sans min-h-screen flex flex-col justify-between">

        <!-- 1. THANH MENU (NAVIGATION BAR) -->
        <nav class="bg-slate-950 border-b border-slate-800 sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 py-4 flex justify-between items-center">
                <span class="text-white font-black text-xl tracking-wider uppercase">
                    💥 LÝ CÔNG THỨC <span class="text-pink-500">STORE</span>
                </span>
                <div class="space-x-6 text-sm font-medium hidden md:block">
                    <a href="#" class="text-pink-500">Trang Chủ</a>
                    <a href="#" class="hover:text-white transition">Sản Phẩm</a>
                    <a href="#" class="hover:text-white transition">Phụ Kiện Gym</a>
                    <a href="#" class="hover:text-white transition">Liên Hệ</a>
                </div>
            </div>
        </nav>

        <!-- 2. BANNER LỚN CHUYÊN NGHIỆP (HERO SECTION) -->
        <div class="relative bg-slate-950 overflow-hidden border-b border-slate-800">
            <div class="absolute inset-0 opacity-20 bg-[url('https://unsplash.com')] bg-cover bg-center filter blur-sm"></div>
            <div class="relative max-w-7xl mx-auto px-4 py-16 text-center">
                <h2 class="text-4xl md:text-5xl font-black text-white mb-4 uppercase tracking-tight">
                    Bộ Sưu Tập <span class="text-pink-500">Thời Trang & Phụ Kiện Gym</span>
                </h2>
                <p class="text-slate-400 max-w-xl mx-auto text-base">
                    Chuyên phụ kiện tập gym chất lượng cao cho anh em thể hình. Uy tín, chất lượng, đồng hành cùng cơ bắp của bạn.
                </p>
            </div>
        </div>

        <!-- 3. KHU VỰC HIỂN THỊ CHÍNH (CHIA CỘT SẢN PHẨM VÀ TIN TỨC) -->
        <main class="max-w-7xl mx-auto px-4 py-10 flex-grow w-full grid grid-cols-1 lg:grid-cols-4 gap-8">
            
            <!-- CỘT TRÁI: DƠN DANH SÁCH SẢN PHẨM (Chiếm 3 phần diện tích) -->
            <div class="lg:col-span-3">
                <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
                    {html_san_pham}
                </div>
            </div>

            <!-- CỘT PHẢI: SIDEBAR THÔNG TIN PHỤ (Chiếm 1 phần diện tích - Giống trang mẫu) -->
            <div class="space-y-6">
                <!-- Hộp Đánh Giá Khách Hàng -->
                <div class="bg-slate-950 p-5 rounded-xl border border-slate-800 shadow-md">
                    <h4 class="text-white font-bold text-sm uppercase tracking-wider mb-4 border-l-4 border-pink-500 pl-2">Khách Hàng Nói Về Chúng Tôi</h4>
                    <div class="space-y-4">
                        <div class="bg-slate-900 p-3 rounded-lg border border-slate-800">
                            <p class="text-xs italic text-slate-400">"Áo mặc ôm body rất khít, tập gym tôn dáng lắm shop ơi! Sẽ ủng hộ tiếp."</p>
                            <p class="text-right text-xs text-pink-500 font-semibold mt-2">- Tuấn Anh Nguyễn</p>
                        </div>
                    </div>
                </div>
                <!-- Hộp Hỗ Trợ -->
                <div class="bg-slate-950 p-5 rounded-xl border border-slate-800 shadow-md text-center">
                    <p class="text-xs text-slate-400 mb-2">Cần hỗ trợ tư vấn trực tiếp?</p>
                    <a href="tel:0900000000" class="inline-block w-full bg-slate-800 hover:bg-slate-700 text-white font-bold py-2 rounded-lg text-sm border border-slate-700 transition">
                        📞 Hotline: 090.xxx.xxxx
                    </a>
                </div>
            </div>
        </main>

        <!-- 4. CHÂN TRANG ĐEN UY TÍN (FOOTER - Giống trang mẫu) -->
        <footer class="bg-slate-950 border-t border-slate-800 text-xs text-slate-500 py-8">
            <div class="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
                <div>
                    <h5 class="text-white font-bold uppercase mb-3">Về LÝ CÔNG THỨC STORE</h5>
                    <p class="leading-relaxed">Hệ thống phân phối phụ kiện gym, áo nén thể thao hàng đầu cho Gymer. Kết nối trực tiếp sản phẩm chính hãng qua TikTok Shop.</p>
                </div>
                <div>
                    <h5 class="text-white font-bold uppercase mb-3">Thông Tin Liên Hệ</h5>
                    <p class="mb-1">📍 Địa chỉ kho: Quận 12, Thành phố Hồ Chí Minh</p>
                    <p class="mb-1">✉️ Email: [lycongthu@gmail.com](mailto:lycongthu@gmail.com)</p>
                    <p>📞 Điện thoại: [090.xxx.xxxx](tel:0900000000)</p>
                </div>
                <div>
                    <h5 class="text-white font-bold uppercase mb-3">Đối Tác Đáng Tin Cậy</h5>
                    <div class="flex flex-wrap gap-3 pt-1">
                        <span class="bg-slate-900 border border-slate-800 text-slate-400 px-3 py-1 rounded font-bold">TIKTOK SHOP</span>
                        <span class="bg-slate-900 border border-slate-800 text-slate-400 px-3 py-1 rounded font-bold">FASTAPI</span>
                        <span class="bg-slate-900 border border-slate-800 text-slate-400 px-3 py-1 rounded font-bold">GITHUB</span>
                    </div>
                </div>
            </div>
            <div class="text-center mt-8 pt-4 border-t border-slate-900 text-slate-600">
                © 2026 LÝ CÔNG THỨC STORE. All rights reserved.
            </div>
        </footer>

    </body>
    </html>
    """
    return html_content

@app.get("/mua/{{id_san_pham}}")
def dieu_huong_tiktok(id_san_pham: int):
    # Tìm link affiliate của sản phẩm dựa trên ID khách bấm
    for sp in DANH_SACH_SAN_PHAM:
        if sp["id"] == id_san_pham:
            print(f"LOGIC: Khách bấm vào {sp['ten']} - Chuyển sang link: {sp['link_tiktok']}")
            return RedirectResponse(url=sp["link_tiktok"])
    return RedirectResponse(url="/")