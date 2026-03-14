import cloudscraper
import os

products = [
      { 'id': 'c1', 'image': 'https://www.bigbasket.com/media/uploads/p/xxl/40107568_4-himalaya-purifying-neem-face-wash.jpg'},
      { 'id': 'c2', 'image': 'https://images.mamaearth.in/catalog/product/1/_/1_d6ea38a1-0f92-4cfe-8490-5ecc60b1c559.jpg'},
      { 'id': 'c3', 'image': 'https://www.bigbasket.com/media/uploads/p/xxl/40087096_2-cetaphil-gentle-skin-cleanser.jpg'},
      { 'id': 'c4', 'image': 'https://beardo.in/cdn/shop/products/Beardo_Activated_Charcoal_Face_Wash_100ml_1.jpg'},
      { 'id': 'm1', 'image': 'https://www.bigbasket.com/media/uploads/p/xxl/40155557_3-neutrogena-hydro-boost-water-gel.jpg'},
      { 'id': 'm2', 'image': 'https://www.nykaa.com/media/catalog/product/d/o/dot-key-barrier-repair-cream-50ml.jpg'},
      { 'id': 'm3', 'image': 'https://plumgoodness.com/cdn/shop/products/green-tea-renewed-clarity-night-gel-40ml.jpg'},
      { 'id': 'm4', 'image': 'https://themancompany.com/cdn/shop/products/face-moisturizer.jpg'},
      { 'id': 's1', 'image': 'https://beminimalist.co/cdn/shop/products/1_NIACINAMIDE-10-ZINC-1.jpg'},
      { 'id': 's2', 'image': 'https://www.nykaa.com/media/catalog/product/d/o/dot-key-vitamin-c-face-serum.jpg'},
      { 'id': 's3', 'image': 'https://thedermacompany.com/cdn/shop/products/salicylic-acid-serum.jpg'},
      { 'id': 's4', 'image': 'https://beardo.in/cdn/shop/products/Beardo_Anti_Acne_Serum_30ml.jpg'},
      { 'id': 'su1', 'image': 'https://reequil.com/cdn/shop/products/reequil-ultra-matte-dry-touch-sunscreen-gel.jpg'},
      { 'id': 'su2', 'image': 'https://www.bigbasket.com/media/uploads/p/xxl/250548_7-lotus-herbals-safe-sun-uv-screen-matte-gel.jpg'},
      { 'id': 'su3', 'image': 'https://aqualogica.in/cdn/shop/products/glow-plus-dewy-sunscreen-spf50-pa.jpg'},
      { 'id': 'su4', 'image': 'https://themancompany.com/cdn/shop/products/spf-50-sunscreen.jpg'},
      { 'id': 't1', 'image': 'https://images.mamaearth.in/catalog/product/s/k/skin-illuminate-toner_1_1.jpg'},
      { 'id': 't2', 'image': 'https://plumgoodness.com/cdn/shop/products/green-tea-pore-cleansing-face-toner.jpg'},
      { 'id': 'mk1', 'image': 'https://mcaffeine.com/cdn/shop/products/coffee-face-pack.jpg'},
      { 'id': 'mk2', 'image': 'https://images.mamaearth.in/catalog/product/m/u/multani-mitti-face-pack_1_1.jpg'}
]

os.makedirs(os.path.join('frontend', 'assets'), exist_ok=True)
scraper = cloudscraper.create_scraper(browser={'browser': 'chrome', 'platform': 'windows', 'mobile': False})

for prod in products:
    img_path = os.path.join('frontend', 'assets', f"{prod['id']}.jpg")
    try:
        response = scraper.get(prod['image'], stream=True, timeout=15)
        if response.status_code == 200:
            with open(img_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded {prod['id']}")
        else:
            print(f"Failed {prod['id']} - Status: {response.status_code}")
    except Exception as e:
         print(f"Error {prod['id']}: {e}")
