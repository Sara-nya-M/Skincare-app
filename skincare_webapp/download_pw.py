import asyncio
from playwright.async_api import async_playwright
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

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
        
        for prod in products:
            img_path = os.path.join('frontend', 'assets', f"{prod['id']}.jpg")
            url = prod['image']
            try:
                # Wait until network is mostly idle to ensure image loads
                response = await page.goto(url, wait_until="networkidle", timeout=15000)
                
                # BigBasket and others often just return the image directly.
                # If the URL is loaded directly as an image, Playwright creates an <img> wrapper.
                # Let's just take a screenshot of the image element.
                img_locator = page.locator("img").first
                if await img_locator.count() > 0:
                    await img_locator.screenshot(path=img_path)
                    print(f"Downloaded {prod['id']}")
                else:
                    print(f"Failed to find image element for {prod['id']}")
            except Exception as e:
                print(f"Failed {prod['id']}: {e}")
                
        await browser.close()

asyncio.run(main())
