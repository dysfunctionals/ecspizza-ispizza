set_image = __import__('verification.ecspizza-ispizza.classify_image').set_image
classify = __import__('verification.ecspizza-ispizza.classify_image').classify

def verify(imagePath):
    set_image(imagePath)
    result = classify()
    if("pizza" in result[0]):
        return u'🍕'
    else:
        return result[0]