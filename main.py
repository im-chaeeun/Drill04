from pico2d import*

open_canvas()

character=load_image('character_sheet.png')
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
tuk_ground=load_image('TUK_GROUND.png')

def handle_events():
    global running, x, dir

    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dir+=1
            elif event.key == SDLK_LEFT:
                dir-=1
            elif event.key==SDLK_ESCAPE:
                running=False
        elif event.type == SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dir-=1
            elif event.key==SDLK_LEFT:
                dir+=1

running=True
x=800//2
frame=0
dir=0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if dir == 0 or dir == 1:
        character.clip_draw(frame * 85, 315, 85, 68, x, 90)
    elif dir == -1:
        character.clip_composite_draw(frame * 85, 315, 85, 68, 0, 'h', x, 90, 85, 65)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    x+=dir*5
    delay(0.05)

close_canvas()