import cv2
import matplotlib.pyplot as plt
 
image_path = 'flowers.jpeg'
image = cv2.imread(image_path)

image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

height, width, _= image_rgb.shape

rec1_width, rec1_height = 50, 50
topL1= (20,20)
bottomR1= (topL1[0] + rec1_width, topL1[1]+ rec1_height)
cv2.rectangle(image_rgb, topL1, bottomR1,(0, 255, 255), 3)

rec2_width, rec2_height =100, 50
topL2 = (width - rec2_width - 20, height - rec2_height - 20)
bottomR2 = (topL2[0] + rec2_width, topL2[1] + rec2_height)
cv2.rectangle(image_rgb, topL2, bottomR2, (255, 0, 255), 3)


cen1_x = topL1[0] + rec1_width // 2
cen1_y = topL1[1] + rec1_height // 2
cen2_x = topL2[0] + rec2_width // 2
cen2_y = topL2[1] + rec2_height // 2
cv2.circle(image_rgb, (cen1_x, cen1_y), 15, (0, 255, 0), -1)
cv2.circle(image_rgb, (cen2_x, cen2_y), 15, (0, 255, 0), -1)

cv2.line(image_rgb, (cen1_x, cen1_y), (cen2_x, cen2_y), (0, 255, 0), 3)

font= cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image_rgb, 'Top Left', (topL1[0], topL1[1] - 10), font, 0.7, (0, 255, 255), 2,
cv2.LINE_AA)
cv2.putText(image_rgb, 'Bottom Right', (topL2[0], topL2[1] - 10), font, 0.7, (255, 255, 255),2, cv2.LINE_AA)

arrow_start = (width - 50, 20)
arrow_end = (width - 50, height-20)

cv2.arrowedLine(image_rgb, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
cv2.arrowedLine(image_rgb, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)

plt.figure(figsize=(12, 8))
plt.imshow(image_rgb)
plt.title(' !!Annotated Image!! ')
plt.axis('off') 
plt.show()