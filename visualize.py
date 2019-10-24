import os
import cv2


class Icdar2019Visualizer():
    def __init__(self, years, img_pth, lbl_pth):
        img_names = os.listdir(img_pth)
        self.images_path = [os.path.join(img_pth, img) for img in img_names]
        self.labels_path = [os.path.join(lbl_pth, img.replace("jpg", "txt")) for img in img_names]
        self.years = years

    def _string2rect(self, line):
        line = line.split(',')
        [x1,y1,x2,y2] = [int(float(p)) for p in line[:4]]
        poly = [
            (x1,y1),
            (x2,y1),
            (x2,y2),
            (x1,y2) ]
        name = line[-1].replace("\n", "")
        return poly, name

    def _string2polygon(self, line):
        line = line.split(',')
        poly = [int(float(p)) for p in line[:8]]
        poly = [(poly[i], poly[i + 1]) for i in range(0, 8, 2)]
        name = line[-1].replace("\n", "")
        return poly, name

    def _label2polygon(self, labels_path):
        polygon = []
        f = open(labels_path)
        lines = f.readlines()
        for line in lines:
            if self.years == '2015':
                poly = self._string2rect(line)
            else:
                poly = self._string2polygon(line)
            polygon.append(poly)
        f.close()
        return polygon

    def _draw_polygon(self, img, polygon):
        for p_item in polygon:
            poly, name = p_item
            for i in range(len(poly)):
                cv2.line(img, poly[i], poly[(i + 1) % 4], (255, 255, 255), 2)
            cv2.putText(img, name, poly[0], cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 0))
        return img

    def _draw_icdar(self, img_path, labels_path):
        polygon = self._label2polygon(labels_path)
        img = cv2.imread(img_path)
        img = self._draw_polygon(img, polygon)
        return img

    def slide_show(self):
        for i_path, l_path in zip(self.images_path, self.labels_path):
            img = self._draw_icdar(i_path, l_path)
            cv2.imshow("vis", img)
            cv2.waitKey(500)
