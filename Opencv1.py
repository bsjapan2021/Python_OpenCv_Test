import cv2
img_basic = cv2.imread("2.png", cv2.IMREAD_COLOR) #원본대로 읽고 투명부분은 안읽음
cv2.imshow('Image Basic', img_basic)  # 이미지출력
cv2.waitKey(0)                        # 사용자 키입력 대기
cv2.imwrite('result1.png', img_basic) # 다른이름으로 저장

cv2. destroyAllWindows()

img_gray = cv2.cvtColor(img_basic, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image Basic', img_gray)  # 이미지출력
cv2.waitKey(0)                        # 사용자 키입력 대기
cv2.imwrite('result2.png', img_gray) # 다른이름으로 저장





