#------------------------------------------------------------------------------------------------------------------
#Imports
from PIL import Image
import os
import random
#------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------
#Input file loading
bg=[f'bgs\\{x}' for x in os.listdir('bgs')]
body=[f'body\\{x}' for x in os.listdir('body')]
eyes=[f'eyes\\{x}' for x in os.listdir('eyes')]
nose=[f'nose\\{x}' for x in os.listdir('nose')]
snout=[f'snout\\{x}' for x in os.listdir('snout')]
#------------------------------------------------------------------------------------------------------------------
#Initialization
generated=[]
counter=0
f=open('generated.txt')
r=f.read().split('\n')
if len(r)>1:
    generated=eval(r[0])
    counter=int(r[1])

f.close()

#------------------------------------------------------------------------------------------------------------------
#Generation
for i in range(10000):
    g_bg=random.choice(bg)
    g_body=random.choice(body)
    g_eye=random.choice(eyes)
    g_nose=random.choice(nose)
    g_snout=random.choice(snout)

    if (g_bg,g_body,g_eye,g_nose,g_snout) not in generated:
        gen_img=Image.new('RGBA',(1400,1400))
        gen_img.paste(Image.open(g_bg),(0,0))
        gen_img.alpha_composite(Image.open(g_body),(0,0),(0,0))
        gen_img.alpha_composite(Image.open(g_eye),(0,0),(0,0))
        gen_img.alpha_composite(Image.open(g_snout),(0,0),(0,0))
        gen_img.alpha_composite(Image.open(g_nose),(0,0),(0,0))
        counter+=1
        gen_img.save(f"generated\{counter}.png")
        generated.append((g_bg,g_body,g_eye,g_nose,g_snout))
        print("Unique Image no.: ",counter)
print(f"Generated {counter} images")
f=open("generated.txt",'w')
f.writelines(f'{generated}')
f.write('\n'+str(counter))
f.close()
#------------------------------------------------------------------------------------------------------------------