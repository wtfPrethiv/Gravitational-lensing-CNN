from PIL import Image
import os


def toPNG(in_path, out_path): # ion think i even need ts 
    
    try:
        with Image.open(in_path) as img:
            img.save(out_path, 'png')
            print('Done !!')
            
    except (FileNotFoundError, Exception) as e:
        print(f'Error occurred {e}')
        
        
def crop(in_path, out_path):

    img_names = os.listdir('data/orig')
    
    for img_name in img_names:
        
        try:
            with Image.open(f'{in_path}/{img_name}') as img:
                
                width,height = img.size
                new_height = 338
                
                top = (height - new_height) // 2
                bottom = top + new_height
                
                img_crop = img.crop((0, top, width, bottom))
                
                
                img_crop.save(f'{out_path}/{img_name[:-4]}.png', format='PNG')

        except (FileExistsError, FileNotFoundError) as e:
            print(e)
            
            
# os.mkdir('GLensing')

crop('data/orig', 'data/GLensing')
  