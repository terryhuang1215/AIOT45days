import v4l2
import fcntl

vd = open("/dev/video0", "r")

cp = v4l2.v4l2_capability()

fcntl.ioctl(vd, v4l2.VIDIOC_QUERYCAP, cp)

print("cp.driver: ", cp.driver)
print("cp.card: ", cp.card)
