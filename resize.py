from skimage import io,transform,data
import matplotlib.pyplot as plt
img = io.imread('depth_38.jpg')
print (img.shape)
dst=transform.resize(img, (120,160))
print(type(dst))
plt.figure('resize')

plt.subplot(121)
plt.title('before resize')
plt.imshow(img,plt.cm.gray)

plt.subplot(122)
plt.title('after resize')
plt.imshow(dst,plt.cm.gray)

plt.show()
