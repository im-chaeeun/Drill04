from pico2d import*

open_canvas()

character=load_image('character_sheet.png')
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
tuk_ground=load_image('TUK_GROUND.png')

frame=0
for x in range(0, 850, 10):
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    character.clip_draw(frame*85, 315, 85, 68, x, 90)
    update_canvas()
    frame=(frame+1)%10
    delay(0.05)

close_canvas()