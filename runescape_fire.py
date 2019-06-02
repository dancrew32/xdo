import xdo

win_id = xdo.win('Old School Runescape')
xdo.act(win_id)
xdo.wait(3)
xdo.move(1046, 532)
xdo.wait(1)
for x in range(0, 5):
    cur = xdo.cur()
    xdo.move(1133, 464)  # tinderbox
    xdo.click()
    xdo.move(*cur)
    xdo.click()
    xdo.wait(10)

    xdo.rel(40, 0)
    cur = xdo.cur()
    xdo.move(1133, 464)  # tinderbox
    xdo.click()
    xdo.move(*cur)
    xdo.click()
    xdo.wait(10)

    xdo.rel(40, 0)
    cur = xdo.cur()
    xdo.move(1133, 464)  # tinderbox
    xdo.click()
    xdo.move(*cur)
    xdo.click()
    xdo.wait(10)

    xdo.rel(40, 0)
    cur = xdo.cur()
    xdo.move(1133, 464)  # tinderbox
    xdo.click()
    xdo.move(*cur)
    xdo.click()
    xdo.wait(10)
    xdo.wait(10)
    xdo.negrel(-120, 40)
