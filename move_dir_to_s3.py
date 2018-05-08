import boto3
from datetime import datetime, timedelta
from os import listdir
from os.path import isfile, join

# get date
d = datetime.now()

# set root_dir
root_dir = "/<path>/<to>/<dir>/"
file_paths = [f for f in listdir(root_dir) if isfile(join(root_dir, f))]

# set aws resource (uses ~/.aws/credentials)
s3 = boto3.resource('s3')

# iterate through file_paths list
for file_path in file_paths:

    # open file
    file = open(file_path)

    # get file date
    data = file.read()

    # create needed strings for s3
    s3_file_path = file_path.replace(root_dir, "")
    s3_key = '<s3_root_dir>/{}'.format(s3_file_path)

    # send file to s3
    s3.Bucket('<s3_bucket>').put_object(Key=s3_key, Body=data)

    # close the file
    file.close()

