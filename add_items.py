from login import login
from client import ClientError
import time

with login() as client:
	for item in xrange(90, 1000):
		try:
			client.add_item(item)
			#time.sleep(0.5)
		except ClientError:
			pass