from io import BytesIO


def resize_image(image, width, height, keep_aspect_ratio):     #* keep_aspect_ratio: آیا نسبت طول به عرض تصویر حفظ شود یا نه
    if keep_aspect_ratio:                                      
        image.thumbnail((width, height))            #* thumbnail(): نسبت طول به عرض را خودش نگه میدارد
                                                    #*      تا تصویر کشیده، فشرده و قناص نشود.
    else:
        image = image.resize((width, height))       #* resize(): نسبت طول به عرض را نگه نمیدارد و 
                                                    #* هر چیزی برای طول و عرض کاربر وارد کند به همان تبدیل میکند
    return image


def convert_image_type(image, output_format):
    if output_format.lower() == "jpeg":
        output_format = "JPEG"
    elif output_format.lower() == "png":
        output_format = "PNG"
    buffer = BytesIO()                  #! یک حافظه موقت ایجاد میکنیم
    image.save(buffer, format=output_format)  #! save image inside the buffer 
                                              #!which is a 'temprory memory', 
                                              #!with the selected format(output_format).
    return buffer                              
                                              #! in fact, return 'BytesIO'
                                              #!So, `app.py` can use it to download the image.  
