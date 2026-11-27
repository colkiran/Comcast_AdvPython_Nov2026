
import sys
# print(dir(sys))
# print(sys.path)
sys.path.append(r"C:\Delhi")

for pth in sys.path:
    print(pth)


from gurgaon.mymodule import Greet
Greet("Rohit")
