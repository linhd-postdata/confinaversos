import glob
from pathlib import Path
import datetime

path = Path().absolute().parent /'corpus'/'es'

for file in glob.glob(f"{path}/*.txt"):
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    filename = file.split('/')[-1]
    author_lc = filename.split('_')[0].replace('-', ' ')
    author = ' '.join([word.capitalize() for word in author_lc.split(' ')]).replace('#', '')
    title = filename.split('_')[-1].replace('-', ' ').replace('.txt', '').replace('#', '').capitalize()
    with open(file, 'r') as f:
        text = f.read().replace('\n', '  \n')
    md_string = f"""Title: {title}
Date: {date}
Category: Confinaversos
Tags: Poesía, Confinamiento
Slug: {author}_{title}
Authors: {author}

{text}  
  
*(Contribuído por {author})*
    """
    with open(f'content/{filename}.md', 'w') as md_output:
        md_output.write(md_string)