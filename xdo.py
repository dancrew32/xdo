from time import sleep
from subprocess import check_output, CalledProcessError

# http://manpages.ubuntu.com/manpages/trusty/man1/xdotool.1.html


def do(*args):
    out = check_output(['xdotool'] + list(args))
    return out.decode('utf-8')


def move(x: int, y: int, relative=False):
    return do('mousemove', str(x), str(y))


def rel(x: int, y: int):
    return do('mousemove_relative', str(x), str(y))

def negrel(x: int, y: int):
    return do('mousemove_relative', '--', str(x), str(y))


def mouse():
    data = do('getmouselocation').strip()
    out = {}
    for part in data.split(' '):
        key, value = part.split(':')
        out[key] = int(value)
    return out


def cur():
    data = mouse()
    return data['x'], data['y']


def click():
    do('click', '1')


def win(search: str, index=0):
    try:
        data = do('search', search).strip()
    except CalledProcessError:
        return None
    try:
        win_id_str = data.split('\n')[index]
    except IndexError:
        return None
    return int(win_id_str)


def act(win_id: int):
    return do('windowactivate', str(win_id)).strip()


def move_win(win_id: int, x: int, y: int):
    return do('getactivewindow', 'windowmove', str(win_id), str(x), str(y))


def size_win(win_id: int, x: int, y: int):
    return do('getactivewindow', 'windowsize', str(win_id), str(x), str(y))


def text(text: str):
    return do('type', text)


def wait(seconds: int):
    return sleep(seconds)
