import re
import os
import json
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import cloudscraper

products = [
      { 'id': 'c1', 'name': 'Himalaya Purifying Neem Face Wash 100ml'},
      { 'id': 'c2', 'name': 'Mamaearth Tea Tree Face Wash'},
      { 'id': 'c3', 'name': 'Cetaphil Gentle Skin Cleanser 125ml'},
      { 'id': 'c4', 'name': 'Beardo Activated Charcoal Face Wash'},
      { 'id': 'm1', 'name': 'Neutrogena Hydro Boost Water Gel'},
      { 'id': 'm2', 'name': 'Dot & Key Barrier Repair Ceramide Cream'},
      { 'id': 'm3', 'name': 'Plum Green Tea Renewed Clarity Night Gel'},
      { 'id': 'm4', 'name': 'The Man Company Daily Face Moisturizer'},
      { 'id': 's1', 'name': 'Minimalist 10% Niacinamide Serum'},
      { 'id': 's2', 'name': 'Dot & Key 20% Vitamin C Serum'},
      { 'id': 's3', 'name': 'The Derma Co 2% Salicylic Acid Serum'},
      { 'id': 's4', 'name': 'Beardo Anti-Acne Serum'},
      { 'id': 'su1', 'name': "Re'equil Ultra Matte Dry Touch Sunscreen"},
      { 'id': 'su2', 'name': 'Lotus Herbals Safe Sun UV Screen Matte Gel'},
      { 'id': 'su3', 'name': 'Aqualogica Glow+ Dewy Sunscreen'},
      { 'id': 'su4', 'name': 'The Man Company Sunscreen Gel SPF 50'},
      { 'id': 't1', 'name': 'Mamaearth Skin Illuminate Vitamin C Toner'},
      { 'id': 't2', 'name': 'Plum Green Tea Alcohol-Free Toner'},
      { 'id': 'mk1', 'name': 'mCaffeine Coffee Face Mask'},
      { 'id': 'mk2', 'name': 'Mamaearth Multani Mitti Face Pack'}
]

scraper = cloudscraper.create_scraper()

results = {}

for prod in products:
    query = urllib.parse.quote(f"{prod['name']} amazon")
    url = f"https://html.duckduckgo.com/html/?q={query}"
    
    try:
        response = scraper.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find exactly an amazon.in link
        a_tags = soup.find_all('a', class_='result__snippet')
        amazon_url = None
        for a in a_tags:
            href = a.get('href', '')
            if 'amazon.in/dp/' in href or 'amazon.in/' in href:
                # Extract URL from duckduckgo redirect
                # Usually DDG puts it in the 'href' directly or in 'href' param
                match = re.search(r'uddg=(https.*?)(&|$)', href)
                if match:
                    amazon_url = urllib.parse.unquote(match.group(1))
                else:
                    amazon_url = href
                break
        
        if amazon_url:
            print(f"Found Amazon URL for {prod['id']}: {amazon_url}")
            # Now fetch the amazon page to get the image
            amz_res = scraper.get(amazon_url)
            amz_soup = BeautifulSoup(amz_res.text, 'html.parser')
            # Look for landingImage or dynamicImage
            img = amz_soup.find('img', id='landingImage')
            if img:
                img_url = img.get('src')
                # get highest res by stripping trailing stuff if necessary or just use the src
                print(f"  -> Image: {img_url}")
                results[prod['id']] = img_url
            else:
                 # fallback for amazon
                 img_data = re.search(r'"large":"(https://m\.media-amazon\.com/images/I/[^"]+\.jpg)"', amz_res.text)
                 if img_data:
                     print(f"  -> Image (Regex): {img_data.group(1)}")
                     results[prod['id']] = img_data.group(1)
                 else:
                     print(f"  -> Could not find image on amazon page")
        else:
            print(f"No Amazon URL for {prod['id']}")
            
    except Exception as e:
        print(f"Error for {prod['id']}: {e}")

with open('image_links.json', 'w') as f:
    json.dump(results, f, indent=2)

print("Done")
