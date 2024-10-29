import cv2
import numpy as np
from scipy import ndimage
from skimage.feature import peak_local_max
from skimage.segmentation import watershed
import os

image_files = ['img.jpg', 'img3.jpg']
for img_file in image_files:
    if os.path.exists(img_file):
        image = cv2.imread(img_file)

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        thresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)[1]

        distance_map = ndimage.distance_transform_edt(thresh)
        local_max = peak_local_max(distance_map, min_distance=10, labels=thresh)

        coordinates = peak_local_max(distance_map, min_distance=20)
        markers = np.zeros_like(distance_map, dtype=int)
        for i, coord in enumerate(coordinates):
            markers[coord[0], coord[1]] = i + 1

        labels = watershed(-distance_map, markers, mask=thresh)

        total_area = 0
        for label in np.unique(labels):
            if label == 0:
                continue

            mask = np.zeros(gray.shape, dtype="uint8")
            mask[labels == label] = 255

            cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            cnts = cnts[0] if len(cnts) == 2 else cnts[1]
            c = max(cnts, key=cv2.contourArea)
            area = cv2.contourArea(c)
            total_area += area

            cv2.drawContours(image, [c], -1, (36, 255, 12), 4)

        print(f'Total area for {img_file}: {total_area}')

        if img_file == 'img3.jpg':
            image = cv2.resize(image, (600, 750))

        cv2.imshow(f'image {img_file}', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f'File {img_file} not found.')
