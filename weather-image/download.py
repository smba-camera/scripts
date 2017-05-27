import urllib2
import datetime
import time
import sys

def downloadPicAndWeather(lat,long,pic_url):
	img_response = urllib2.urlopen(pic_url)
	img_data = img_response.read()
	json_response = urllib2.urlopen('http://api.openweathermap.org/data/2.5/weather?lat='+lat+'&lon='+long+'&units=metric&appid=46679918719fde122879f1ddd83235b8')
	json_data = json_response.read()
	unique_filename = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H%M%S')
	file_ = open("data/"+unique_filename+".jpg", 'w')
	file_.write(img_data)
	file_.close()
	file_ = open("data/"+unique_filename+".json", 'w')
	file_.write(json_data)
	file_.close()

lat = "48.23"
long = "11.63"
pic_url = "http://www.bayerninfo.de/webcams/images/A9Munich-Nuremberg/a9-km522-brn.jpg"

if len(sys.argv)==4 :
	lat = sys.argv[1]
	long = sys.argv[2]
	pic_url = sys.argv[3]
else :
	print "incorrect input arguments, defaults will be used"

print "started download 1 pic/minute ctrl+c to stop"
while True:
	downloadPicAndWeather(lat,long,pic_url)
	time.sleep(60)
	pass