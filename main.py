import magiccube
import re

def faces(alg):
    #allowed = "UDLRFBudlrfbw2' "
    allowed = "UDLRFBw2' "
    
    for a in alg:
        if a not in allowed:
            print("#>",a)
            return "BBBBBBBBB"
    
    cube = magiccube.Cube(
        3, "YYYYYYYYYRRRRRRRRRGGGGGGGGGOOOOOOOOOBBBBBBBBBWWWWWWWWW")
    
    cube.reset()
    cube.rotate("Z Z")
    cube.rotate(alg)

    c = str(cube)
    lines = [line.strip().replace(" ","") for line in c.strip().split('\n')]

    top = lines[0] + lines[1] + lines[2]
    bottom = lines[-3] + lines[-2] + lines[-1]
    
    left = lines[3][:3] + lines[4][:3] + lines[5][:3]
    front = lines[3][3:6] + lines[4][3:6] + lines[5][3:6]
    right = lines[3][6:9] + lines[4][6:9] + lines[5][6:9]
    back = lines[3][9:12] + lines[4][9:12] + lines[5][9:12]
    
    faces = [top,bottom,left,front,right,back]

    return faces

print("Enter scrambles, each in own line >")
scrm = []
while 1:
    s = input()
    if s == "":
        break
    
    scrm.append(s)

PATTERN = r"^\d+[\.\)]\s*"

scrm = [re.sub(PATTERN, "", scramble) for scramble in scrm]

all_fac = []
for s in scrm:
    cube = faces(s)
    all_fac.append(cube)
    
#print(all_fac)

print("Enter the patter on side of one of the cubes in this order:")
print("UL UM UR ML MM(center) MR DL DM DR (Up,Down,Left,Right,Middle)") 
print("and with first letter of color (White,Green,Red,Blue,Orange,Yellow)")
print("eg for checkerboard on U face: WYWYWYWYW")
pat = input(">").upper()


def rotate_face(face):
    rotated = [''] * len(face)
    for i, char in enumerate("741852963"):
        rotated[i] = face[int(char) - 1]
        
    return ''.join(rotated)


found = None
for _ in range(5):
    for i in range(len(all_fac)):
        c_cube = all_fac[i]
        if pat in c_cube:
            found = i
    
    if not found is None:
        break
    pat = rotate_face(pat)


if found is None:
    print("Cube not found")
    exit()
    
print(f"Found: {i+1} - {scrm[i]}")
