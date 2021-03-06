import graphics as gp
import time
from colorama import init, Fore, Style

import sort

init(convert=True)

BAR_WIDTH = 12
BAR_HEIGHT = 12
BAR_COLOR = gp.color_rgb(242, 164, 54)
BG_COLOR = gp.color_rgb(43, 137, 164)
WINDOW_X = BAR_WIDTH * sort.DATA_NUM
WINDOW_Y = BAR_HEIGHT * (sort.DATA_MAX + 5)
STEP = 0.04


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
    win.update()


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


def clear_screen(win):
    for i in win.items[:]:
        i.undraw()
    win.update()


def remove_duplicates(playback_list):
    new_list = []
    for ds in playback_list:
        if ds not in new_list:
            new_list.append(ds)
    return new_list


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


def print_header(header):
    print('\n' + Style.BRIGHT + Fore.CYAN + header + ' :' + Style.RESET_ALL)


def print_subheader(subheader):
    print('\n' + Style.BRIGHT + Fore.LIGHTGREEN_EX + subheader + Style.RESET_ALL)


def print_command(command, description):
    print(Style.BRIGHT + command + Style.RESET_ALL + ' - ' + description)


def main():
    win = gp.GraphWin('sortpy', WINDOW_X, WINDOW_Y, autoflush=False)
    win.setBackground(color=gp.color_rgb(43, 137, 164))

    print_logo()
    first_input = True
    while 1:
        clear_screen(win)
        ds = sort.generate_dataset(sort.DATA_NUM, repeat=False)
        bars = []
        draw_bars(ds, win, bars)
        sort.playback_list = []

        valid_command = False
        if first_input:
            command = input('Type help to view commands\n')
            first_input = False
        else:
            command = input('')
        while not valid_command:
            if command == 'help':
                print_header('Sorting algorithms')
                print_subheader('Bubble sorts')
                print_command('bubble', 'Bubble sort')
                print_command('cocktail', 'Cocktail shaker sort')
                print_command('comb', 'Comb sort')
                print_command('oddeven', 'Odd-even sort')
                print_subheader('Insertion sorts')
                print_command('insertion', 'Insertion sort')
                print_command('shell', 'Shellsort')
                print_command('gnome', 'Gnome sort')
                print_subheader('Divide and conquer')
                print_command('merge', 'Merge sort')
                print_command('quick', 'Quicksort')
                print_subheader('Other')
                print_command('selection', 'Selection sort')
                print_command('stooge', 'Stooge sort')

                print_header('Options')
                print_command('quit', 'Exit sortpy')

                print('\n')
                print('Click on the window after sorting finishes to select a new algorithm')
                command = input('\n')
            elif command == 'bubble':
                valid_command = True
            elif command == 'cocktail':
                valid_command = True
            elif command == 'comb':
                valid_command = True
            elif command == 'oddeven':
                valid_command = True
            elif command == 'insertion':
                valid_command = True
            elif command == 'shell':
                valid_command = True
            elif command == 'gnome':
                valid_command = True
            elif command == 'merge':
                valid_command = True
            elif command == 'quick':
                valid_command = True
            elif command == 'selection':
                valid_command = True
            elif command == 'stooge':
                valid_command = True
            elif command == 'quit':
                win.close()
                return
            else:
                print('Command not found - type help to view commands')
                command = input('\n')

        sort.playback_list.append(ds[:])
        if command == 'insertion':
            sort.insertion_sort(ds)
        elif command == 'bubble':
            sort.bubble_sort(ds)
        elif command == 'cocktail':
            sort.cocktail_sort(ds)
        elif command == 'selection':
            sort.selection_sort(ds)
        elif command == 'merge':
            sort.merge_sort(ds, 0, sort.DATA_NUM - 1)
        elif command == 'quick':
            sort.quick_sort(ds, 0, sort.DATA_NUM - 1)
        elif command == 'shell':
            sort.shell_sort(ds)
        elif command == 'gnome':
            sort.gnome_sort(ds)
        elif command == 'oddeven':
            sort.odd_even_sort(ds)
        elif command == 'comb':
            sort.comb_sort(ds)
        elif command == 'stooge':
            sort.stooge_sort(ds, 0, sort.DATA_NUM - 1)
        sort.playback_list = remove_duplicates(sort.playback_list)
        play_animation(ds, win, bars)
        win.getMouse()


main()
