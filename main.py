@namespace
class SpriteKind:
    foodenemy = SpriteKind.create()
    runningshoe = SpriteKind.create()
level = 0

def on_on_overlap(sprite, otherSprite):
    global count, KIND_SpriteKind
    count += 1
    info.change_score_by(1)
    sprites.destroy(otherSprite)
    otherSprite.start_effect(effects.smiles)
    if count > 0 + KIND_SpriteKind:
        KIND_SpriteKind += 1
        startlevel()
    else:
        music.play(music.melody_playable(music.ba_ding),
            music.PlaybackMode.IN_BACKGROUND)
sprites.on_overlap(SpriteKind.player, SpriteKind.runningshoe, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(otherSprite2, effects.fire, 500)
    music.play(music.melody_playable(music.power_down),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.foodenemy, on_on_overlap2)

def startlevel():
    global count, runningshoe2
    scene.set_background_color(randint(3, 7))
    count = 0
    index = 0
    while index <= 10 - level:
        runningshoe2 = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . . . . . . f f . . . . . . . 
                            . . . . . . f b b f . . . . . . 
                            . . f f . . . f 6 f . . . . . . 
                            . f 6 6 f . . . f b f f . . . . 
                            f 6 6 6 f . . f 6 6 1 b f f . . 
                            f 6 6 6 6 f f 6 f 1 6 1 b 1 f f 
                            f 6 6 6 6 6 6 6 f f 1 6 1 b 1 f 
                            f 6 6 6 6 6 6 f 1 1 f f 6 1 6 f 
                            f 6 6 6 6 6 f 1 1 f 1 1 f f f f 
                            f f 6 6 6 f 1 1 f 1 1 f 6 6 f f 
                            f b f 6 f 1 1 f 1 1 f 6 6 f b f 
                            f 1 b f f f f f f f f f f b 1 f 
                            . f 1 1 1 1 1 1 1 1 1 1 1 1 f . 
                            . . f f f f f f f f f f f f . .
            """),
            SpriteKind.runningshoe)
        runningshoe2.set_position(randint(20, 140), randint(20, 100))
        index += 1
    info.start_countdown(10)

def on_on_overlap3(sprite3, otherSprite3):
    sprites.destroy(otherSprite3, effects.spray, 500)
    music.play(music.melody_playable(music.ba_ding),
        music.PlaybackMode.IN_BACKGROUND)
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap3)

mySprite3: Sprite = None
mySprite2: Sprite = None
runningshoe2: Sprite = None
KIND_SpriteKind = 0
count = 0
scene.set_background_color(10)
mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . . 
            . . f f f f f f f f . . . . . . 
            . f f f f f f f f f f . . . . . 
            . f f f f c f f c f f f . . . . 
            f f c f f c c f f c f f f . . . 
            f f c c f f f f f f c c f f . . 
            f f f f f f f f e f f f f f . . 
            f f f e e f f f e e f f f f . . 
            f f f e 4 e b f e e f f f . . . 
            . f f f f e 1 f 4 4 f f . . . . 
            . 4 4 4 4 e 4 4 4 4 f . . . . . 
            . e 4 4 4 e e e e f f 1 1 1 1 1 
            . f e e e f 7 7 7 7 f 1 e 1 e 1 
            . f f f f f 6 6 6 6 f f e e e e 
            . f f f f f f f f f f . . . . . 
            . . f f . . . . f f . . . . . .
    """),
    SpriteKind.player)
mySprite.set_position(7, 108)
info.set_score(3)
info.set_life(3)
controller.move_sprite(mySprite, 100, 0)
mySprite.set_stay_in_screen(True)
info.start_countdown(30)

def on_update_interval():
    global mySprite2, mySprite3
    mySprite2 = sprites.create(img("""
            . . . . . . . e c 7 . . . . . . 
                    . . . . e e e c 7 7 e e . . . . 
                    . . c e e e e c 7 e 2 2 e e . . 
                    . c e e e e e c 6 e e 2 2 2 e . 
                    . c e e e 2 e c c 2 4 5 4 2 e . 
                    c e e e 2 2 2 2 2 2 4 5 5 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 4 4 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 2 2 e 
                    c e e 2 2 2 2 2 2 2 2 2 2 4 2 e 
                    . e e e 2 2 2 2 2 2 2 2 2 4 e . 
                    . 2 e e 2 2 2 2 2 2 2 2 4 2 e . 
                    . . 2 e e 2 2 2 2 2 4 4 2 e . . 
                    . . . 2 2 e e 4 4 4 2 e e . . . 
                    . . . . . 2 2 e e e e . . . . .
        """),
        SpriteKind.food)
    mySprite2.set_position(randint(0, scene.screen_width()), 5)
    mySprite2.set_velocity(0, 50)
    mySprite3 = sprites.create(img("""
            . . . . c c c b b b b b . . . . 
                    . . c c b 4 4 4 4 4 4 b b b . . 
                    . c c 4 4 4 4 4 5 4 4 4 4 b c . 
                    . e 4 4 4 4 4 4 4 4 4 5 4 4 e . 
                    e b 4 5 4 4 5 4 4 4 4 4 4 4 b c 
                    e b 4 4 4 4 4 4 4 4 4 4 5 4 4 e 
                    e b b 4 4 4 4 4 4 4 4 4 4 4 b e 
                    . e b 4 4 4 4 4 5 4 4 4 4 b e . 
                    8 7 e e b 4 4 4 4 4 4 b e e 6 8 
                    8 7 2 e e e e e e e e e e 2 7 8 
                    e 6 6 2 2 2 2 2 2 2 2 2 2 6 c e 
                    e c 6 7 6 6 7 7 7 6 6 7 6 c c e 
                    e b e 8 8 c c 8 8 c c c 8 e b e 
                    e e b e c c e e e e e c e b e e 
                    . e e b b 4 4 4 4 4 4 4 4 e e . 
                    . . . c c c c c e e e e e . . .
        """),
        SpriteKind.foodenemy)
    mySprite3.set_position(randint(0, scene.screen_width()), 5)
    mySprite3.set_velocity(0, 31)
game.on_update_interval(500, on_update_interval)
