import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

# grab the image from online
imgurl = 'http://static.dDJV5bda1KqIHZ2aM97bfDjHimWAeXjuu1k1m2Nmnaindia.com/sites/default/files/styles/full/public/2017/06/21/586145-salman-khan-062117.jpg'

imgbytes = image_helpers.get_image_from_url(imgurl)

rekresp = client.recognize_celebrities(Image={'Bytes': imgbytes})
# pprint(rekresp['CelebrityFaces'])
for face in rekresp['CelebrityFaces']:
    print(face['Name'],'Match:', face['MatchConfidence'], 'url:',face['Urls'])
