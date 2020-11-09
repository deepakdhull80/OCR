try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os

pytesseract.pytesseract.tesseract_cmd ="C:/Program Files (x86)/Tesseract-OCR/tesseract"

tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'


# f=open("files/f1.pdf",'rb')
# a=f.read()

# d=open("files/f1.png",'wb')
# d.write(a)
# f.close()
# d.close()

files='files'
filename='files/2.jpg'

def getFileName(files):
	for file in os.listdir(files):
		with open(file.split('.')[0]+".txt",'w') as p:
			p.write(getData(files+'/'+file))


def getData(filename):
	image=Image.open(filename)
	data=pytesseract.image_to_string(image,config=tessdata_dir_config)
	return data

getFileName(files)

# with open("data.txt",'w') as p:
# 	p.write(getData(filename))

