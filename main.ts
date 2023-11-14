namespace SpriteKind {
    export const foodenemy = SpriteKind.create()
    export const runningshoe = SpriteKind.create()
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.foodenemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.fire, 500)
    music.play(music.melodyPlayable(music.powerDown), music.PlaybackMode.InBackground)
    info.changeLifeBy(-1)
})
function start_new_level () {
    scene.setBackgroundColor(2)
    mySprite = sprites.create(img`
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
        `, SpriteKind.Player)
    mySprite.setPosition(7, 108)
    info.setScore(3)
    info.setLife(3)
    controller.moveSprite(mySprite, 100, 0)
    mySprite.setStayInScreen(true)
    info.startCountdown(30)
}
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.spray, 500)
    music.play(music.melodyPlayable(music.baDing), music.PlaybackMode.InBackground)
    info.changeScoreBy(1)
})
let mySprite3: Sprite = null
let mySprite2: Sprite = null
let mySprite: Sprite = null
scene.setBackgroundColor(10)
mySprite = sprites.create(img`
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
    `, SpriteKind.Player)
mySprite.setPosition(7, 108)
info.setScore(3)
info.setLife(3)
controller.moveSprite(mySprite, 100, 0)
mySprite.setStayInScreen(true)
info.startCountdown(30)
game.onUpdateInterval(500, function () {
    mySprite2 = sprites.create(img`
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
        `, SpriteKind.Food)
    mySprite2.setPosition(randint(0, scene.screenWidth()), 5)
    mySprite2.setVelocity(0, 50)
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.foodenemy)
    mySprite3.setPosition(randint(0, scene.screenWidth()), 5)
    mySprite3.setVelocity(0, 31)
})
