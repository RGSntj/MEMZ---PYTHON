from win32api import RGB, GetSystemMetrics, Sleep
from win32gui import *
from win32ui import *
from win32con import *
from win32file import *
from random import *
import time, rotatescreen as rs

def main():
  if MessageBox("Trojan", "WARNING", MB_ICONERROR):
    return

for i in range(0, 5):
  main()

desk = GetDC(0)

x = GetSystemMetrics(0)
y = GetSystemMetrics(1)

for i in range(0, 100):
  brush = CreateSolidBrush(RGB(
    randrange(255),
    randrange(255),
    randrange(255)
  ))
  SelectObject(desk, brush)
  PatBlt(desk, randrange(y), randrange(x), randrange(y), PATCOPY, PATINVERT)
  Sleep(10)

pd = rs.get_primary_display()
angel_list = [90, 180, 270, 0]
for i in range(5):
  for x in angel_list:
    pd.rotate_to(x)
    time.sleep(0.2)