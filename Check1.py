import cv2
import numpy as np

def checker(image):
    titul=cv2.imread("1.jpg")
    titul_rgb=cv2.cvtColor(titul,cv2.COLOR_BGR2RGB)
    titul_gray=cv2.cvtColor(titul,cv2.COLOR_BGR2GRAY)
    titul_blur=cv2.GaussianBlur(titul_gray,(7,7),0)
    _,binary_titul=cv2.threshold(titul_blur,200,255,cv2.THRESH_BINARY)

    image=cv2.resize(image,(578,752))
    image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    image_gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    image_blur=cv2.GaussianBlur(image_gray,(7,7),0)
    _,binary_image=cv2.threshold(image_blur,200,255,cv2.THRESH_BINARY)

    def getKataklar(binary):
        contours, hierarachy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

        katakchalar = []

        for i in range(len(contours)-1,0,-1):
            area = cv2.contourArea(contours[i])
            if area > 1000 and area < 2300:
                x,y,w,h = cv2.boundingRect(contours[i])
                katak = binary[y:y+h,x:x+w]
                katakchalar.append(katak)
        return katakchalar
    image_list = getKataklar(binary_image)
    titul_list = getKataklar(binary_titul)

    titul_dict ={'A': 0,
             'B': 0,
             'C': 0,
             'D': 0,
             'E': 0,
             'F': 0}
    k=0
    for i in titul_dict.keys():
        titul_dict[i] = titul_list[k]
        k = k + 1

    def dictanc(img1,img2):
        difference = cv2.subtract(img1, img2)
        return cv2.countNonZero(difference)

    true_answers = np.array(['B','B','B','B','B','B','B','B'])
    my_answers=[]
    try:
        count=0
        for j in range(8):
            for i in titul_dict.keys():
                image_list[count]=cv2.resize(image_list[count],(titul_dict[i].shape[1],titul_dict[i].shape[0]))
                if 1100>dictanc(titul_dict[i],image_list[count])>1000:
                    my_answers.append(i)
                count+=1
    except:
        print("Xato Belgilangan")

    k = 0
    for i in range(10):
        try:
            if true_answers[i] == my_answers[i]:
                k = k+1
        except:
            pass
    return f"to'g'ri javoblar soni {k} ta. Natija {k*10} % "