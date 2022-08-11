import imp
import stitching
import cv2
stitcher = stitching.Stitcher(confidence_threshold=0.5)
panorama = stitcher.stitch(["data/CMU3/medium0.png","data/CMU3/medium1.png","data/CMU3/medium2.png","data/CMU3/medium3.png","data/CMU3/medium4.png","data/CMU3/medium5.png","data/CMU3/medium6.png","data/CMU3/medium7.png","data/CMU3/medium8.png","data/CMU3/medium9.png","data/CMU3/medium10.png","data/CMU3/medium11.png","data/CMU3/medium12.png","data/CMU3/medium13.png","data/CMU3/medium14.png","data/CMU3/medium15.png","data/CMU3/medium16.png","data/CMU3/medium17.png","data/CMU3/medium18.png","data/CMU3/medium19.png","data/CMU3/medium20.png","data/CMU3/medium21.png","data/CMU3/medium22.png","data/CMU3/medium23.png","data/CMU3/medium24.png","data/CMU3/medium25.png","data/CMU3/medium26.png","data/CMU3/medium27.png","data/CMU3/medium28.png","data/CMU3/medium29.png","data/CMU3/medium30.png","data/CMU3/medium31.png","data/CMU3/medium32.png","data/CMU3/medium33.png","data/CMU3/medium34.png","data/CMU3/medium35.png","data/CMU3/medium36.png","data/CMU3/medium37.png"])

print(type(panorama))

print(panorama)

cv2.imshow("sa",panorama)

cv2.waitKey(10000)

cv2.imwrite("output.jpg",panorama)