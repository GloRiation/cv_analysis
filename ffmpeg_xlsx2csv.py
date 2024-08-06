#ffmpeg_xlsx2csv.py

import pandas as pd 
import os

dirname = os.path.dirname(__file__)
filename = 'ffmpeg_automate_filname.xlsx'
full_path = os.path.join(dirname, filename)

#normalized_path = os.path.normpath(full_path)
normalized_path = "ffmpeg_automate_filename.xlsx" 

print(normalized_path)
cols = [2]

data = pd.read_excel(normalized_path, sheet_name='Sheet1', usecols=cols)
data.to_csv('ffmpeg_automate_filename.csv', index=False)
