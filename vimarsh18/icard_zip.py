import boto3
import botocore
import inspect
import zipfile
from aws_key import access_id, access_key
from io import BytesIO

BUCKET_NAME = 'yuvacentral'
s3 = boto3.resource('s3',aws_access_key_id=access_id,
         aws_secret_access_key= access_key)

s3_client = boto3.client('s3',aws_access_key_id=access_id,
         aws_secret_access_key= access_key)

bucket = s3.Bucket(BUCKET_NAME)

obj_list = bucket.objects.filter(Prefix = 'media/id_cards')

i=0
j=0
byte_read = BytesIO()
z = zipfile.ZipFile('new_zip.zip','a')
alist = z.namelist()
#print(alist)
for o in obj_list:
        filename = o.key.split('/')[-1]
        #print(o.key)
        #file1 = s3.get_object(bucket = BUCKET_NAME, Key = o.key)
        #print(type(s3))
        #print(type(bucket))
        if not filename in alist:
            with open('temp.png', 'wb') as data:
                s3_client.download_fileobj(BUCKET_NAME, o.key, data)
            z.write('temp.png',arcname=filename, compress_type = zipfile.ZIP_DEFLATED )
            j+=1
        #s3_client.download_fileobj(BUCKET_NAME, o.key, byte_read)
        #z = zipfile.ZipFile('new_zip.zip','w')
        #z.write(byte_read)
        #bucket.download_file(filename, o.key)
        #print(type(data))
        i+=1
print(i)
print(j)