from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
mc.setSign(x,y,z+1,63,0,"我愛minecraft","也愛Python")