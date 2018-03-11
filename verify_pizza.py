from ..classify_image import set_image, classify

def verify(imagePath):
    set_image(imagePath)
    result = classify()
    if("pizza" in result[0]):
        return u'🍕'
    else:
        return result[0]