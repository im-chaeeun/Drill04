from pico2d import*

# 2022182035 임채은

open_canvas()

character=load_image('character_sheet.png')
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
tuk_ground=load_image('TUK_GROUND.png')

def handle_events():
    global running, x, dir, updown

    events=get_events()
    for event in events:
        if event.type==SDL_QUIT:
            running=False
        elif event.type==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dir+=1
            elif event.key == SDLK_LEFT:
                dir-=1
            elif event.key == SDLK_UP:
                updown+=1
            elif event.key ==SDLK_DOWN:
                updown-=1
            elif event.key==SDLK_ESCAPE:
                running=False
        elif event.type == SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dir-=1
            elif event.key==SDLK_LEFT:
                dir+=1
            elif event.key==SDLK_UP:
                updown-=1
            elif event.key==SDLK_DOWN:
                updown+=1


running=True
x, y = 800//2, 90
frame, frame_up, frame_down = 0, 0, 0
dir, updown = 0, 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2 , TUK_HEIGHT//2)

    if x<30:
        x=30
    elif x>=765:
        x=765
    if y<28:
        y=28
    elif y>=575:
        y=575

    if dir == 1:
        if updown == 1:
                character.clip_draw(frame_up * 95 + 40, 90, 95, 120, x, y)
        elif updown == -1:
                character.clip_draw(frame_down * 165, 210, 165, 100, x, y)
        elif updown == 0:
                 character.clip_draw(frame * 85, 315, 85, 68, x, y)
    elif dir == -1:
        if updown == 1:
                character.clip_composite_draw(frame_up * 95 + 40, 90, 95, 120, 0, 'h', x, y, 95, 120)
        elif updown == -1:
                character.clip_composite_draw(frame_down * 165, 210, 165, 100, 0, 'h', x, y, 165, 100)
        elif updown == 0:
                character.clip_composite_draw(frame * 85, 315, 85, 68, 0, 'h', x, y, 85, 65)
    elif dir == 0:
        if updown == 1:
                character.clip_draw(frame_up * 95 + 40, 90, 95, 120, x, y)
        elif updown == -1:
                character.clip_draw(frame_down * 165, 210, 165, 100, x, y)
        elif updown == 0:
                character.clip_draw(frame * 85, 315, 85, 68, x, y)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 10
    frame_up = (frame_up + 1) % 8
    frame_down = (frame_down + 1) % 3
    x+=dir*5
    y+=updown*5
    delay(0.05)

close_canvas()