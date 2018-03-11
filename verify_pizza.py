classify_image = __import__('verification.ecspizza-ispizza.classify_image')

def verify(imagePath):
    classify_image.set_image(imagePath)
    result = classify_image.classify()
    if("pizza" in result[0]):
        return u'🍕'
    else:
        return result[0]