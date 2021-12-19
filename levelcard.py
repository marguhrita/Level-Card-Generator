import pygame as pg

pg.font.init()

#variables
xp = 0
totalXp = 100
level = "level"

#width and height of your generated image
width = 500
height = 200

#colours
white = (255, 255, 255)
black = (0, 0, 0)
limeGreen = (50, 205, 50)

# create the display window
win = pg.display.set_mode((width, height))

#title bar caption
pg.display.set_caption("Pygame draw levelcard and save")

# default background is black, so make it white
win.fill(white)

#create a font object which can be rendered
myUsernameFont = pg.font.SysFont('Arial', 30)
myXpFont = pg.font.SysFont('Arial', 15)

#username
textsurface = myUsernameFont.render("username", False, (0, 0, 0))
#display username onto screen
win.blit(textsurface, (130, 28))

#levelText
levelText = myXpFont.render(f"Level {level}", False, (0, 0, 0))
win.blit(levelText, (130, 80))

#loads an image onto pygame and resizes it
avatar = pg.image.load("profilepicture.png")
avatar = pg.transform.scale(avatar, (60, 60))

#draws the avatar onto the screen with its starting coordinates
win.blit(avatar, (30, 25))

#xp bar back
pg.draw.rect(win, black, pg.Rect(30, 115, 435, 40))

#xp bar bar
barLength = (int(xp)/int(totalXp))*425
pg.draw.rect(win, limeGreen, pg.Rect(35, 120, barLength, 30))

#totalXp text
xpText = myXpFont.render(f"{xp}/{totalXp} xp", False, (0, 0, 0))
win.blit(xpText, (400, 80))


# now save the drawing
# can save as .bmp .tga .png or .jpg
fname = "levelcard.png"
pg.image.save(win, fname)
print("file {} has been saved".format(fname))

# update the display window to show the drawing
pg.display.flip()

pg.quit()
