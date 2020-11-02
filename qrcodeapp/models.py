from django.core.files import File
from PIL import Image, ImageDraw
from django.db import models
from io import BytesIO
import io
import qrcode
import os

from BadgeProject.settings import BASE_DIR
from memberships.models import StudentMembership

class QRcodeModel(models.Model):
    name = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        # create qr-code image
        # qrcode = qrcode.QRCode(box_size=2)
        # url = "http://127.0.0.1:8000/static/images/Badges/teams/" + "Course" + "/" + "studentname" + "_" + "studentid" + ".jpg"
        url = "http://127.0.0.1:8000/static/images/Badges/teams/dsa/suraj_25.jpg"
        qrcode1 = qrcode.make(url)
        size = 800, 800

        qrcode_img = qrcode1.resize(size, Image.ANTIALIAS)
        img_bg = Image.open(os.path.join(BASE_DIR,"static/images/Badges/achievementsports.jpg"))
        
        position = (img_bg.size[0] - qrcode_img.size[0], img_bg.size[1] - qrcode_img.size[1])
        img_bg.paste(qrcode_img, position)
        
        img_path = os.path.join(BASE_DIR,"static/images/Badges/input_image.jpg")
        img_bg.save(img_path, 'JPEG')

        fname = f'qr_code-{self.name}.png'
        # buffer = BytesIO()
        buffer = io.BytesIO()
        
        qrcode_img.save(buffer,'PNG')       # 'path/of/dest.png'
        # destination_file = open(buffer, 'rb')   # 'path/of/dest.png'
        
        self.qr_code.save(fname, File(buffer), save=False) # destination_file
        super(QRcodeModel, self).save(*args, **kwargs)

        # destination_file.close()
        img_bg.close()
        qrcode_img.close()





# # make qrcode image
# qr = qrcode.QRCode(box_size=2)
# qr.add_data("KrunalPatil")
# qr1 = qr.make_image()
# qr1.save("out.jpg", dpi=(300,300))

# # qrcode_img = qr.make(self.name)
# # img_qr = qr.make_image()

# # canvas = Image.new('RGB', (290, 290), 'white')
# # draw = ImageDraw.Draw(canvas)

# img_bg = Image.open(os.path.join(BASE_DIR,"static/images/Badges/achievementsports.jpg"))
# position = (img_bg.size[0] - qr1.size[0], img_bg.size[1] - qr1.size[1])
# img_bg.paste(qr1, position)
# img_bg.save("out.jpg")       # 'path/of/dest.png'

# # # img_bg.paste(qrcode_img, (3517, 2493))

# # buffer = BytesIO()
# # # canvas.save(buffer,'PNG')       # 'path/of/dest.png'
# # destination_file = open(buffer, 'rb')   # 'path/of/dest.png'

# # fname = f'qr_code-{self.name}.png'
# # self.qr_code.save(fname, File(buffer), save=False) # destination_file

# # destination_file.close()
# # super(QRcodeModel, self).save(*args, **kwargs)

# # # canvas.close()
# # qrcode_img.close()
# # img_bg.close()



        # # create qr-code image
        # qr = qrcode.QRCode(box_size=2)
        # qrcode1 = qr.add_data(self.name)
        # qrcode_img = qrcode1.make_image()
        # size = 300, 300
        # qrcode_img = qrcode_img.resize(size, Image.ANTIALIAS)


        # # qr1.save("out.jpg", dpi=(300,300))
        
        # # canvas = Image.new('RGB', (290, 290), 'white')
        # # draw = ImageDraw.Draw(canvas)
        # # img_qr = qr.make_image()

        # img_bg = Image.open(os.path.join(BASE_DIR,"static/images/Badges/achievementsports.jpg"))
        # position = (img_bg.size[0] - qrcode_img.size[0], img_bg.size[1] - qrcode_img.size[1])
        
        # img_bg.paste(qrcode_img, position)

        # fname = f'qr_code-{self.name}.png'
        # buffer = BytesIO()
        # canvas.save(buffer,'PNG')       # 'path/of/dest.png'
        # destination_file = open(buffer, 'rb')   # 'path/of/dest.png'
        # self.qr_code.save(fname, File(buffer), save=False) # destination_file
        # destination_file.close()
        # super(QRcodeModel, self).save(*args, **kwargs)
        # canvas.close()
        # qrcode_img.close()
