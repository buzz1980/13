input.onGesture(Gesture.Shake, function () {
    stappen += 1
})
input.onButtonPressed(Button.AB, function () {
    stappen = 0
})
let stappen = 0
stappen = 0
basic.forever(function () {
    basic.showNumber(stappen)
})
