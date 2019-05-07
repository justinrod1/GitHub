from gamelib import*#import game library

game = Game (800,600,"Cops & Robbers")

#titlescreen
bk=Image("bk.jpg",game)
bk.resizeTo(800,600)
title1=Image("title1.jpg",game)
play=Image("play.png",game)
title1.moveTo(400,150)
play.moveTo(400,300)

while not game.over:
    game.processInput()
    play.draw()
    bk.draw()
    title1.draw()
    if keys.Pressed[K_SPACE]:
        game.over = True
    game.drawText("Press [SPACE BAR] to start the game",game.width/2-150,game.height/2+20)
    game.update(30)
    
game.over = False


game = Game(800,600,"Zombie Attack")
bk = Image("pac.jpg",game)
bk.resizeTo(800,600)

cop = Image("cop.png",game)
cop.resizeBy(-85)
cop.setSpeed(4,60)#sets speed inorder to move

key = Image("key.png",game)
key.resizeBy(-95)
key.setSpeed(4,70)

robber = Image("robber.png",game)
robber.moveTo(mouse.x,mouse.y)
robber.resizeBy(-80)

while not game.over: #runs until game is over
    game.processInput()
    bk.draw()
    cop.move(True)
    key.move(True)
    robber.move()
    robber.moveTo(mouse.x,mouse.y)
    if key.collidedWith(mouse)and mouse.LeftButton:#if statement,a condition to be tested to be true, if true theres an action
        game.score+=1#Accumilator
        key.moveTo(randint(100,700),randint(100,500))

    if cop.collidedWith(key):
        key.resizeBy(-10)
        key.moveTo(randint(100,700),randint(100,500))
        game.score-=1#Accumilator

    if game.score>=10:
         game.drawText("you win",100,5)
         

    if cop.collidedWith(mouse)and mouse.LeftButton:
        game.drawText("YOU GOT CAUGHT! MISSION FAILED.",100,40)
        game.over = True
        
    if game.score>=5:
        game.drawText("YOU HAVE ESCAPED! NOW RUN!!!!",100,40)
        game.over= True
    game.displayScore()
    game.update(50)
    

