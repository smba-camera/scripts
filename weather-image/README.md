Usage:
python download.py [48.13 11.14 www.yourimageurlhere.com/image.jpg]
[The optional parameters are: latitude, longitude,image url]

download.py a script that: 
1) Downloads one road image from:
http://www.bayerninfo.de/webcams/images/A9Munich-Nuremberg/a9-km522-brn.jpg
2) Downloads the current weather information as json and extracts the relevant info:
	sun ,wind, rain, snow, visibility (if exists)
3) Renames the image and the information with the current time stamp
4) saves both in the data folder under the same timestamp (YYYY-MM-DD-hhmmss(.jpg/.json))

API key: 46679918719fde122879f1ddd83235b8

TODOS:
	*Filter out the unnecessary info from the weather json
	*Consider adding a JSON NOSQL database and concatenate all data under a single [JSON array that includes both weather and image data] 