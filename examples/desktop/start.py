from __future__ import with_statement
from pymt import *

plugins = MTPlugins(plugin_paths=['..'])
plugins.search_plugins()

def gesture_add_default(gdb):
    # Circle
    g = gdb.str_to_gesture('eNqllttqHEcURd/7R6SXiHO//IDzGtAHBMcWxsSJBkmG+O+zqzzqbkOSEkQIBma6dp86a5/L7efLtz9e7j49PL98fXrYfr5+Xmi7/Xjh7f7m+eXp8feH55vtItvtl4tut/944n4+tl1snHOcuzx+/vNlHItxLP/l2C/jqe1S41Tj1DccYNre0Z0Em4pIumoL5fZ8f/PX+JW3dz/RHbWyZVMkpUil6Pb82/v/fAnLvJNun17fkFTc5mRFZgWFT1d1fFsmJdyIIrxjLT4vzr6LXwMXs+a04kNcmqqKuJPYs8rX4jHF81Wc3ajS2zLcvfkkrmGqppZajltkrsVn8rlfxakCEXYZro30utmhbqRVotH4mQL5X6rLNJLwd/UBbqRdNTwqjCFzCh65IiSGiZAb3GsdvEymors8zrJ1tGoSqZ3FI0haQkIbzhrvXYlPpuK7OA6VWYwMmSR7nNSTI6sRvat76NoxMqFKHuoNM0AhBkO8x/9X7JOq9K4+wJVLwc2kqXISl4A/xYiMPLhrKa4Tqh5QTZtV0kzgdXD7wZBXs1SjZBtFuFSfTPVg6hQtrY6sRJfiakctpTZuFoCBJhFvSIxOqHpAdYORUxPSXv6DZbiaETSaA+rJON6gPqHqAdUL2YbX0cHg6D6l/UiJgm5yvUF9QtU+qcMXrt1ehhZ4LtXX/tKEemVBGEt5m1iNl/KjSSRMSq5gju4G56/VJ1Y7YQ2F9VwarhR423d1IRRBGvwo47W+zoxNqnai6sKS1Ggp3ZkRh3gHcMAqGYCasTakTah2gnqNGb7QMTtyF9dizA0UMHojAqA3iE+mdjC1rChCxMXoBNxH5OgxaL7oDLASUpTrQvVJ1E+FyoGxVIlPaoyHg6hzkjBAF5zYzusG5hOoH0AxkUsLZhlj2XOv05EwlC3DkoViM6RnLf59kTj1Xq5sVClzBDROgcM7yQqbq6CaZO1Enzz94MmY1lZXPyoPideUV2UKHCSGG+kbzOKTpx88MTKJUH8ocbTxqDpChzlhok4kpTAUfR16TKDB+7B2wZIRCWBowBx2hK5olZkH1jXQmEBjX5B47CnoitiAxNEk9dB2TJM2VBcyx3N1WmlPnrHvR4Mm+i1mg5OigupUn0zo8di/HPsfpspae/KMfT0SpzGNGp8eKYcyo5tHaZM7YpY1zJgwY9+NBJMM86Cxe5Hx7HpXbUZdQhcUUKSR64TkJJk7SbQUHQ0Ve2/BJnr0FDI0GthSQ3msY7xuhzlJ5k5SsVEVveaF8rTq4pWYS0g3aANr9Mz3+L+/eXn88vD0/s8PD9i70SqmJX7847GWX2P49fL0+PHrh5fxsG/vCtI06xVZb+x5w913fwPv4lI1')
    g.label = 'Circle'
    g.id = 'circle'
    gdb.add_gesture(g)

    # up_left, bottom_left, bottom_right, up_right
    g = gdb.str_to_gesture('eNqllt1qHEcQhe/nRaSbiPr/eQHlNqAHCI4tjIljLdo1xG+fMy1pZwRJesBiQRcz/U13nVOn+vbL6cdfl7vPj+fL9+fH5dfX/ydabj+deHm4OV+en/58PN8sJ1luv550uf3XFQ/jteVk6zrHutPTl2+XdVmsy/I/lv22vrWcal3VWPUDC5iWe7rjcDNSjzRLco3l/HDz9/qYl/tf6E5NNNRUIzKLupfzHx/+9yMs40y6fH75AnmmFVmTi3YGL+fPV3hac2hle9f6ZMYe52Z/YYNASeZJ2eySSl72M/QY9LzSuVQyvblTxVR0B1dhfFzUmBUbyDl9VJ/7SpcgIYqo6lAhlR2dwsK7M5PUXGRKl+Ek4Ssdp9ci9qD0orRd2aVDqL3SWVt9zh6Kil7ZxkYWJZImKDLFjk1NSkykanBUzP0iQ1PxI3QWLqdgZbeO9ckMPiSVPAInbqlwJm8qh2l0jh+aSu/wzekkWUkBV+YrHvQqQyt0MrFZQ5opXYemumlq0qZsWixJ1X6FC0cwtTiMg3Y70KU6NNWdpvCZd8Dl7vjMtU1Xq++feM+trkNS9QNw02TRNC9uPdSlOiTVPALPYmutKHPStgNlGYLqEUE9XKUKHhJ0aNR85zb0tE1PQWOyWrVRw5cZG7ypo6s7wnEqnTvdhqC2CYp6uhqRCPodwb7tPIhFQhHmwogCrzl8CGqboEyhbs5OTvCeblYMZitJIc7SlAPsoadteiI7sslYrNDiSCjZFA0UOlLVPaSreN6iNhS1fhtH2B57YVQYWI4w2Ngm4txOjdxC7M5r7kNQ5zc2qtqJXZWUoiq92/e7NEa6zNlDT7+OURw3U6OJMIZh6Z2cyt2Oo+CDEB15OmW/XB/8ja3vayKy+VA7KstKS53ogMl9yOl5ZaPxiBFWQoEZmrV15/vQyrmWPrT03mqiYW5laO2CKeInMiuGlrFpWeWckl0IV0GAXNn8bm6zz30SQ8vQORsZUy24JXkVHI75PIcPMcM3uGo1Jn70enlT20+4vc748LzkMeSMPEJvhkG0ROFvnIHnRowhaPQBOlIMzmyhslzTdr71HIrmpmgUkZm3YhbTGMDbfYtVMTcFGYAg5rnNc0iam6Tv7ski+3sopgM3it2yThMZ8PX3cHN5+vr4/OHbx0dcuNOGuej9H6/38dct/H56fvr0/eNlfdmX+7pDxFqs84fXARJr1t79A9YLUNw=')
    g.label = 'Square'
    g.id = 'square'
    gdb.add_gesture(g)

    # Up
    g = gdb.str_to_gesture('eNq1ltuO2jAQQN/zI/BSNPexf4C+VuIDqr2g1arbJQJW6v597YE4UHWbtigICQlnjh2fmbGXz/379+PqaXs4vu233efzbw/d8rHHbrM4HPe7b9vDouupW7703C1/G7GJx7peapyWuH73/HqsYVbD/IOwL/Wprk81Kpeo9xKA0K0/wcpYmABdhZNmc+sOm8WPOo7dGlagisoKyR0zZeDUHe7v/jgLUrwUd0/nKTShpQqXjESJCuJpoIPbMLUkYZmmx6ujjnSFnCwJISgZc76JbkH3kQ6OFK+eSNQqYqCLcUL1lMW57Bv8xc6EAMzz0CmSibDRpcQ1dwzgF3TMWQ0FYhiAp+lhlUarAkYK7VPGG53LegfbYOg+TQ+rpDPRwyqNVpkNXIYNuMgYSol9ECIuNs0Op5TnYHMY5dEo6Yf5gmp++rdMXJ7BaXoYZZ6JHkZZZ6KHUR6NYiK1oVySKF7QkTK39oMwnS8cTjnPQ5ewKqNVhAQgDaJDnZYhAEx2rlIvbVphOmskvArPxg+zMpqFXzpwsssJrurYVaf54VZ8Nn7YlbPdQACDD2eg5dZsKh/BuB1dWI6ySb6GX8XZ+OFXufGZWFo/zMnlNvzpbqEN70bQjgrLeLn7JWGolTRhms4eDbvqAx6p7E8rrbI/l/Qs0IqOPE/DQ63mWeAWXq15xeur0VVZ/Ts8pFqTikmT1mw/3QHkNngotaa05AvCsO5E5VAf4cQ+9jMux+s0PYxaM0qKJufFIYxH4H/SQ6k1peX+eJntOd1E93DqzSlDMqvkU7mC3kYPqd6kMkv21FoBT9Lrd7M47l62+7vXh225lZfirtkB1x+sl/bzGr72+93j28OxPqzdmkueYmk/XmKsXCprd7hf/QS75FeQ')
    g.label = 'Up'
    g.id = 'up'
    gdb.add_gesture(g)

    # NUI-wave
    g = gdb.str_to_gesture('eNq1lttqHEcURd/7R6SXiHO//IDzGtAHBMcehIljDZoxxH+f3eXRdCskKSVBQiDBTK2urnVqn3P76fjtt/Pdw+F0/vp0WH68/D3ScvvxyMv9zen89Pjr4XSzHGW5/XzU5fYvV9yPry1HW9c51h0fP305r8tiXZZ/s+yn9VvLsdZVjVXfsIBpefcD3UmIsXqGRlJY53K6v/l9/ZzH566cxmSqUe0kupx+ef+PT2EZL6XLw+URXKwq1i7lXVpAPPx3+nh19o0u5MJRZumcSv2/6DHoeaUTNyepKouWcOaOziWSLl3uphGvoA8B3N/pgFtpp6iZaZp3x0a3xosRNl1SRh0xpcsoJuFnOmN3wu6VUZQELRvccS6R3GQW4tVz+JAq+jbw4VT8Cs/I9GC8u7CY1A4O0xmc5WRUrjKHD6WSz3ARo5RmYm5D4fgGR2lSi7alkBK7zeHDqFyNimNnEa1Nirq0XakrXc5K2ztzvnEdPpVfwRbL9hRvL+eIVxS6Dp969SlM7kBHkDcV7SqRn5+I68TwPvepw6duPtk7rEhw5oqwsR1cu1DqzpZJXjo/ch0+Nd8GPnzqdkPd2bWf76Lnrs6pG06DqTWQPO5Tug2jxrt0+VP48g4f7mIlyS6pmllz/pBqW/Jie6nZRNGs1cq7w6GX4Ug0TxgbXm2XvZHF1YVcRAmOgB140OHDJI2MEXKa4a/Y/jBr+Vb44db6ihepkM5GRqnUNcLWo/GSwOlzw2+6zuE+1PqmFp2hJQm7L8LFtdjogT6oKCwRD0O6zS+UD7G+iUVOJSNQ0HbQemR3Moxgcyorx01FWs6t+vdhYrMqHdxAX0BpGzwzuUClxnXoeYb5UOqbUvQM5hDUZDRSfjsV8ZdGc84ePn3zyQj25nZDL0VHlR0cV9WIQGVBSPA8CGL4DH4b+NAZu3uajSpnU5BCBZlzpasrGhJhColgdL15KcbwGZtP5Na+FNVyo1fCaSG8DNNH1TzDYhiNa/ySWpWiYSIMRdE86wqHzn9XLTGMxpa+mLgK9XyZs1AvGxsdryoKyUmJf+fwHEZzOh6BHSh8YShJk5ael2IOoblNR425DU0jVD00a3cmUetIhD6uyN7ucffX3/ub8+Pnw9P7Lx8OGL5x51YMvfzhdTa/7ODn49Pjx68fzuuXfXlnd4FpBhdK1kMThD7Ad38A6q5S7Q==')
    g.label = 'NUI-wave'
    g.id = 'menu'
    gdb.add_gesture(g)

    #A (without cross-bar)
    g = gdb.str_to_gesture('eNq1lttu00AQQN/9I+0L1dwvPwCvSP0AxCWqKgq1miDB3zNeJ7a5lC0PTqImqXfOxnN2Z+f6fvzx5XRzdzievj0dhjfn9xGG608jDrdXx9PT4+fD8WoYabh+GHm4/mvEbRs2jDLFacWNj/dfT1OYTWH+TNjbadQwxhSVFfWjAhCG16/ghl2ckJIxU1U4huPt1ffpOrbrBmqU4c6WAOY6HD+8/+csSO2meLg7T7HAwRIx1Yfj3ZmuzkCIgY4WTEl9ert11JXOEYpOnkFoXNdXuoAgSRiYmCZEn26N7gsd6xdSZsxzBPNKl7RkIdK6JUg279ObAMyFDg7sLOaIpOkhW7zEf6aG2moinPFFJxclwyxuTmnaJL6+1X8u6YfAPr1pJd6J3rSSXujIhhLkBOjBFraBU4hqmjCp1ue+VWpWyfeBN6mUFzhpZSYcLACkWLjCqaZyZp13lHEfzk0p4z7wZpQXo6z1rO1pbGpW7jZwiEhwmVe8UH+tcxPKug+8CeVFaKUiuSjgyFKwjVB0iKpw5+RUGejDm1BehEpwurDG/FdzA1dRqa05T1E1sguXJlQWoSqJiX7ROq23BU64rS+RfXgTKotQg2dzjgANK16DsKpyH96Eiq5pSYFEQQ2GOjg22x9+r7v9/S/NqPhO9KZUFqVct2/IpS8Nqu5eyu4ER4QkZTB11xcY1WZUcRd2E6qLUHT562qpK4heRY2sZowa0/epcw+hu7CbTfVd2M2lZvccKniQVK0HiMQwesHetybTcB94s2lrY1SLYT74VZwD1lVeNVFq9xtBariiZL+aW/NpuhO9GbVNY+Q5t3MUptOyXuFpKlKlx1zEUfuNizWllrvAvSl1XBtGyd873jO8qExmUqkCpDrBuuxm1PutbrGryfsj5dPr9ur0+HB4ev/146G6bpe2tuDXB05N+fknvBufHj99+3iaBuvwWm/q4FSvZqtaVKiSOYFvfgJuKVKI')
    g.label = 'A (no cross-bar)'
    g.id = 'contextmenu'
    gdb.add_gesture(g)

    #X up_letf, bottom_right, top_right, bottom_left
    g = gdb.str_to_gesture('eNq1VttqHFcQfJ8fkV4s+n75Afk1oA8Iji2EiWMt2jXEf+86x6udSXAySoTFgmB3Tk2fqq7qvv54+PrH6ebh/nj68nS/vD3/P9By/eHAy93V8fT0+Pv98Wo5yHL96aDL9Q9P3M3HloONc45zh8ePn0/jWIxj+Q/HfhlPLYcapxqnvuIA03JLN0rRaZqhWekmthzvrv4cP/Ny+4ZuwiLYQtLFODt9Of727l9fwjLvpMvD9zeIFCBYVCOSvHM5PpzB3UzIuqqjO6RtH3xenP0ZnCusxQyvyGZqXcEts7VbKqW6m19QeUzwfAanCGJyofakSK1N6Sqpms5NTYb3v6D0yT73z0GX2UnCF3TyjHZPJg7z0uYVXkyJ8D1ol3JT2YefospZVECwUOpojm5L7ZQVnQrNBLHxQUuV0D7zMmUV/1nwU1jJFb4S93dJUZCvaWf4wZt2ZZYwwxXmQbEPP5WVvsADldukS4XImGSFTxKXMjzhqqW+T71OZZUv6MrtClEzGbZlXdG5DHqjl6IotGOfGZ266qorqE0rZwdFzlQrM+IQA1cipWQQU/vgU1VdVTXqaoVLnQilV6zgMGiUE37wthdIqlNSXSWVZBBaicZQJAnpK7CnnrrRE2dhUAaniDES+//YNtW0VU3EAJrFuxGwhUToV5BiU01b1YTLxc1RdilC1hAmr4GfetoavlQYCSg+3CtktNszdCUcrCyiaKawfQ/Z1NNyL9iH0BAD9mxDDiSPebKHPfW0S/JKob7sptJw5F9vepww4pC9LRyktp+7PvX0S+4qIBBbYERdi3LDCQliBWOuNMHVuNEe9pTT10lqsLYaI0EUTW65Gn/YPTFMkYnerPuc+PcNYtXScV2sAKRu4bmdFkRIkxFj4RjgmKgvyBWfcvo6SjtYGd1YiKhEM24GNWH/QJcmVScumLyfLD4V9XWWGjcbo3a2wj7hm1nK/3mDialpbDzKSPJA1xhsIgKCN7OUqzFBysAgyM/eh5+yxsalTcHesCL4xbKCfl3hG50+8ixHr3Ptz4uYysZmliKriwkxQGh6uQy7kfYBf2IDSeQl9sDa92lMYWOTu6gQVSO4YJcxOjcb2OAbPoA6ngYR9tGnrrFJ3sZ64hLCWE6hYW+Wx7+15b6fcuqam0lqCjsSvAT2kZXb1dRDMGURcHiDIW/20aesqZtphwmH1TMZmwbyZLPD/HCrHp+7q9Pjp/und5/f32MHh1TT3H/947Gin2v49fD0+OHL+9N42JdbHz4eaT5gDWoD9+YbKhZUkQ==')
    g.label = 'X'
    g.id = 'close'
    gdb.add_gesture(g)







def action_close_menu(menu, w, args):
    menu.parent.remove_widget(menu)
    del menu

def action_launch_plugin(menu, w, args):
    name, plugin = args

    win = MTInnerWindow(size=(320,280), pos=w.pos)
    plugins.activate(plugin, win)
    menu.parent.add_widget(win)

    action_close_menu(menu, w, None)

class MTActionButton(MTButton):
    def __init__(self, **kwargs):
        kwargs.setdefault('action', None)
        kwargs.setdefault('args', None)
        super(MTActionButton, self).__init__(**kwargs)
        self.height = self.label_obj.content_height + 10
        self.width = self.label_obj.content_width + 10
        self.action = kwargs.get('action')
        self.args = kwargs.get('args')

    def on_touch_up(self, touches, touchID, x, y):
        if not self.collide_point(x, y):
            return
        if self.action:
            self.action(self.parent, self, self.args)

class MTMenu(MTBoxLayout):
    def __init__(self, **kwargs):
        kwargs.setdefault('orientation', 'vertical')
        kwargs.setdefault('uniform_width', True)
        kwargs.setdefault('uniform_height', True)
        kwargs.setdefault('color', (0,0,0,0))
        super(MTMenu, self).__init__(**kwargs)

        self.orig_x = self.x
        self.orig_y = self.y
        self.color = kwargs.get('color')

        plist = plugins.list()
        while len(plist):
            name, plugin = plist.popitem()
            infos = plugins.get_infos(plugin)
            w = MTActionButton(label=infos.get('title'), bgcolor=self.color,
                    action=action_launch_plugin, args=[name, plugin])
            self.add_widget(w)

        self.add_widget(MTActionButton(
            label='Close menu', action=action_close_menu))

    def on_draw(self):
        with gx_blending:
            super(MTMenu, self).on_draw()

    def on_move(self, x, y):
        pass

    def on_layout(self):
        # center layout
        self.x = self.orig_x - self.content_width / 2
        self.y = self.orig_y - self.content_height / 2


class MTGestureDetector(MTGestureWidget):
    def __init__(self, gdb, **kwargs):
        super(MTGestureDetector, self).__init__(**kwargs)
        self.gdb = gdb

    def draw(self):
        drawLabel('Draw a nui-wave to show menu',
            pos=(10, 10), center=False, font_size=20)

    def on_gesture(self, gesture, x, y):
        try:
            score, best = self.gdb.find(gesture)
        except Exception, e:
            return

        if best.id == 'menu':
            menu = MTMenu(pos=(x, y), color=(.2, .2, .2, .5))
            self.parent.add_widget(menu)

        if best.id == 'close':
            menu = MTMenu(pos=(x, y), color=(.2, .2, .2, .5))
            self.parent.add_widget(menu)


if __name__ == '__main__':
    # Create and fill gesture database
    gdb = GestureDatabase()
    gesture_add_default(gdb)

    # Create background window
    w = MTWallpaperWindow(wallpaper='wallpaper.jpg')
    g = MTGestureDetector(gdb)
    w.add_widget(g)

    runTouchApp()
