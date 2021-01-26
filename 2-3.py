from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

import random,time
while True:
    x,y,z =  mc.player.getTilePos()
    
    cfrom mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()
while True:
    color = random.randrange(0,16)
    mc.setBlocks(x+1,y,z,x-1,y,z,46,color)
    time.sleep(1)