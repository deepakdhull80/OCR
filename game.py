try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd ="C:/Program Files (x86)/Tesseract-OCR/tesseract"

tessdata_dir_config = '--tessdata-dir "C:/Program Files (x86)/Tesseract-OCR/tessdata"'


# f=open("files/f1.pdf",'rb')
# a=f.read()

# d=open("files/f1.png",'wb')
# d.write(a)
# f.close()
# d.close()

image=Image.open('files/2.jpg')

data=pytesseract.image_to_string(image,config=tessdata_dir_config)

with open("data.txt",'w') as p:
	p.write(data)
# print(data)

