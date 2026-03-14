import os
import urllib.request
import json
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

products = [
      { 'id': 'c1', 'image': 'https://www.bigbasket.com/media/uploads/p/xxl/40107568_4-himalaya-purifying-neem-face-wash.jpg'},
      { 'id': 'c2', 'image': 'https://mamaearth.in/cdn/shop/files/1_d6ea38a1-0f92-4cfe-8490-5ecc60b1c559.jpg'},
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
      { 'id': 't1', 'image': 'https://mamaearth.in/cdn/shop/files/skin-illuminate-toner.jpg'},
      { 'id': 't2', 'image': 'https://plumgoodness.com/cdn/shop/products/green-tea-pore-cleansing-face-toner.jpg'},
      { 'id': 'mk1', 'image': 'https://mcaffeine.com/cdn/shop/products/coffee-face-pack.jpg'},
      { 'id': 'mk2', 'image': 'https://mamaearth.in/cdn/shop/files/multani-mitti-face-pack.jpg'}
]

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for p in products:
    url = p['image']
    dest = os.path.join('frontend', 'assets', f"{p['id']}.jpg")
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=10) as response, open(dest, 'wb') as out_file:
            data = response.read()
            out_file.write(data)
        print(f"Downloaded {p['id']}")
    except Exception as e:
        print(f"Failed {p['id']}: {e}")
