from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random()
while True:
    x,y,z = mc.player.getTilePos()
    ecolor = random.randrange(0,8)
    mc.setBlock(x,y,z,38,ecolor)