import unittest

import xdo

class AppTestCase(unittest.TestCase):

    def test_move(self):
        self.assertEqual(xdo.move(0, 0), '')

    def test_mouse(self):
        data = xdo.mouse()
        self.assertEqual(len(data), 4)
        self.assertIsInstance(data['x'], int)
        self.assertIsInstance(data['y'], int)
        self.assertIsInstance(data['screen'], int)
        self.assertIsInstance(data['window'], int)
        cur = xdo.cur()
        self.assertIsInstance(cur[0], int)
        self.assertIsInstance(cur[1], int)

    @unittest.skip('Visual studio focus test.')
    def test_win(self):
        win = xdo.win('Visual Studio Code') 
        self.assertIsInstance(win, int)
        win = xdo.win('Bogus') 
        self.assertIsNone(win)

    @unittest.skip('Focusing a terminal.')
    def test_act(self):
        win_id = xdo.win('dan@okay') 
        self.assertIsNone(xdo.act(win_id))

    @unittest.skip('Resizing and moving a terminal.')
    def test_move_win(self):
        win_id = xdo.win('dan@okay') 
        xdo.act(win_id)
        self.assertEqual(xdo.size_win(win_id, 200, 200), '')
        self.assertEqual(xdo.move_win(win_id, 150, 0), '')