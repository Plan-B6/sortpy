import graphics as gp
import time
import sort


BAR_WIDTH = 12
BAR_HEIGHT = 12
BAR_COLOR = gp.color_rgb(242, 164, 54)
BG_COLOR = gp.color_rgb(43, 137, 164)
WINDOW_X = BAR_WIDTH * sort.DATA_NUM
WINDOW_Y = BAR_HEIGHT * (sort.DATA_MAX + 5)
STEP = 0.05


# Initialize bar object from dataset entry
def set_bar_rectangle(ds, i):
    top_left_point = gp.Point(i * BAR_WIDTH, WINDOW_Y - ds[i] * BAR_HEIGHT)
    bottom_right_point = gp.Point((i + 1) * BAR_WIDTH, WINDOW_Y)
    bar = gp.Rectangle(top_left_point, bottom_right_point)
    bar.setOutline(BG_COLOR)
    bar.setFill(BAR_COLOR)
    return bar


def draw_bars(ds, win, bars, cbars=None):
    assert len(ds) == sort.DATA_NUM
    for i in range(sort.DATA_NUM):
        bar = set_bar_rectangle(ds, i)
        bars.append(bar)
        if cbars:
            if i in cbars:
                bar.draw(win)
        else:
            bar.draw(win)


def get_changed_bars(current_index, prev_index, playback_list):
    cbars = []
    assert current_index == prev_index + 1
    assert len(playback_list[current_index]) == len(playback_list[prev_index])
    for index, i in enumerate(playback_list[current_index]):
        if i != playback_list[prev_index][index]:
            cbars.append(index)
    return cbars


def update_bars(ds, win, bars, cbars):
    for index, i in enumerate(bars):
        if index in cbars:
            t = i
            t.setOutline(BG_COLOR)
            t.setFill(BG_COLOR)
            t.undraw()
            t.draw(win)
    bars.clear()
    draw_bars(ds, win, bars, cbars)
    win.update()
    assert len(bars) == sort.DATA_NUM


def play_animation(ds, win, bars):
    for index, i in enumerate(sort.playback_list):
        if index > 0:
            cbars = get_changed_bars(index, index - 1, sort.playback_list)
        else:
            cbars = [-1, -1]
        update_bars(i, win, bars, cbars)
        time.sleep(STEP)

def print_logo():
    print('                    __             ')
    print('   _________  _____/ /_____  __  __')
    print('  / ___/ __ \/ ___/ __/ __ \/ / / /')
    print(' (__  ) /_/ / /  / /_/ /_/ / /_/ / ')
    print('/____/\____/_/   \__/ .___/\__, /  ')
    print('                   /_/    /____/   \n')

def main():
    # Initialization
    win = gp.GraphWin('sortpy', WINDOW_X, WINDOW_Y, autoflush=False)
    win.setBackground(color=gp.color_rgb(43, 137, 164))
    ds = sort.generate_dataset(sort.DATA_NUM)
    bars = []
    draw_bars(ds, win, bars)

    # Input loop
    print_logo()
    valid_command = False
    command = input('Type help to view commands\n')
    while not valid_command:
        if command == 'help':
            print('Sorting algorithms :')
            print('insertion - Insertion sort\n')
            print('quit - Exit the program')
            command = input('\n')
        elif command == 'insertion':
            valid_command = True
        elif command == 'quit':
            return
        else:
            print('Command not found - type help to view commands')
            command = input('\n')

    sort.playback_list.append(ds[:])
    if command == 'insertion':
        ds = sort.insertion_sort(ds)
        play_animation(ds, win, bars)
    win.getMouse()

    win.close()


main()
