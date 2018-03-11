from classify_image import set_image, classify

set_image('/home/kch/Downloads/pizzazz.jpg')
result = classify()
print(result[0] + " " + str(result[1]))