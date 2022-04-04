from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
zipurl = 'https://files.grouplens.org/datasets/movielens/ml-1m.zip'
with urlopen(zipurl) as zipresp:
    print('Downloading zip....')
    with ZipFile(BytesIO(zipresp.read())) as zfile:
        print('Extracting...')
        zfile.extractall(r'/home/hduser/dataset/')
print('Extracted...')