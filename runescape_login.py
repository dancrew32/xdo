from os import environ

import xdo

xdo.move(274, 882)
xdo.click()
xdo.wait(10)
win_id = xdo.win('Old School Runescape')
xdo.act(win_id)
xdo.move(475, 641)  # worlds
xdo.click()
xdo.wait(3)
xdo.move(492, 202)  # free world
xdo.wait(1)
xdo.click()
xdo.click()
xdo.wait(7)
xdo.move(875, 448)  # existing
xdo.click()
xdo.wait(3)
xdo.text(environ['RUNESCAPE_PASSWORD'])
xdo.move(721, 482)
xdo.click()
xdo.wait(5)
xdo.move(816, 474)
xdo.click()
xdo.wait(5)
