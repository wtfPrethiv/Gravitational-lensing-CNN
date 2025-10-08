from bs4 import BeautifulSoup
import requests
import os

def image_ext(li: list, path):

    for i in li:
        url_lens = f'{url}{i}'
        
        _res = requests.get(url=url_lens, headers=headers)
        _soup = BeautifulSoup(_res.text, 'html.parser')
        imgs = _soup.findAll('image')
        
        if imgs:
            
            for img in imgs:
                gif_link = img.get('src')
                
                img_dat = requests.get(f'{url_lens[:47]}/{gif_link}', headers=headers).content
                
                filename = os.path.basename(gif_link)
                file_path = os.path.join(path, filename)
                
                with open(file_path, 'wb') as f:
                    f.write(img_dat)
        
            
        


url = 'https://lweb.cfa.harvard.edu/castles/'
headers = {"User-Agent": "Mozilla/5.0"}

res = requests.get(url=url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

lens_names = []
for a in soup.select('table td a'):
    name = a['href']
    if not name.find('Individual'):
        lens_names.append(name)
        
os.chdir('data')
os.mkdir('orig')

image_ext(lens_names, 'orig')