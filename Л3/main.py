from turtle import color
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np


with open("DS3.txt", 'r') as file:
    points = [list(map(lambda x: int(x), line.strip().split())) for line in file]
    points = np.array(points)
file.close()

hull = ConvexHull(points)
with open('ConvexHull_points.txt', 'w') as f:
    for point in points[hull.vertices]:
        f.write(str(point[0]))
        f.write(' ')
        f.write(str(point[1]))
        f.write('\n')
f.close()

for plot_id in (1, 2):
    fig, ax = plt.subplots(ncols=1, figsize=(960/96, 540/96))
    if plot_id == 1:
        ax.set_title('Опукла оболонка')
        ax.plot(points[hull.vertices, 0], points[hull.vertices, 1], color="darkblue", lw=2)
        plt.ylim(ymin=0)
        plt.ylabel("y", loc='top', rotation=0)
        plt.xlabel("x", loc='right')
    else:
        ax.set_title('Опукла оболонка з вихідними точками датасету')
        ax.plot(points[:, 0], points[:, 1], '.', color='k')
        ax.plot(points[hull.vertices, 0], points[hull.vertices, 1], color="darkblue", lw=2)
        plt.ylim(ymin=0)
        plt.ylabel("y", loc='top', rotation=0)
        plt.xlabel("x", loc='right')
plt.show()