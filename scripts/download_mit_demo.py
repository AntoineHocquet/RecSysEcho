import os
import gdown

#count_data:
#  https://drive.google.com/file/d/1uL5PZmkETQQeGq7a5zh1Jln7ukwLwqK0/view?usp=sharing
FILE_ID_1='1uL5PZmkETQQeGq7a5zh1Jln7ukwLwqK0'

#song_data:
#  https://drive.google.com/file/d/1OUGOtBPrnvTwQ71b35zhImptMI-OAoTy/view?usp=sharing
FILE_ID_2='1OUGOtBPrnvTwQ71b35zhImptMI-OAoTy'


os.makedirs("data/sample", exist_ok=True)

files = {
    "song_data_mit.csv": FILE_ID_2,
    "count_data_mit.csv": FILE_ID_1
}

for filename, file_id in files.items():
    url = f"https://drive.google.com/uc?id={file_id}"
    output_path = os.path.join("data/sample/mit-demo", filename)

    if not os.path.exists(output_path):
        print(f"⬇️  Downloading {filename} from Google Drive...")
        gdown.download(url, output_path, quiet=False)
    else:
        print(f"✅ {filename} already exists at {output_path}")
