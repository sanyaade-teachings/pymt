'''
Kinetic: kinetic abstraction
'''

__all__ = ['MTKinetic']

from pyglet.gl import *
from ..factory import MTWidgetFactory
from ...vector import Vector
from ...mtpyglet import getFrameDt
from stencilcontainer import MTStencilContainer
from widget import MTWidget

class MTKinetic(MTWidget):
    '''Kinetic container.
    All widgets inside this container will have the kinetic applied
    to the touches. Kinetic is applied only if an children is touched
    on on_touch_down event.

    Kinetic will enter in the game when the on_touch_up append.
    Container will continue to send on_touch_move to children, until
    the velocity Vector is under `velstop` and sending on_touch_up ::

        from pymt import *
        k = MTKinetic()
        # theses widget will have kinetic movement
        MTKinetic.add_widget(MTScatterSvg(filename = 'sun.svg'))
        MTKinetic.add_widget(MTScatterSvg(filename = 'cloud.svg'))
        w = MTWindow()
        w.add_widget(k)
        runTouchApp()

    .. warning::
        In the on_touch_move/on_touch_up, the touchID will not exists in
        the touches arguments.

    :Parameters:
        `friction` : float, defaults to 10
            The Pseudo-friction of the pseudo-kinetic scrolling.
            Formula for friction is ::
                acceleration = 1 + friction * frame_delta_time
        `velstop` : float, default to 1.0
            The distance of velocity vector to stop animation
    '''
    def __init__(self, **kwargs):
        kwargs.setdefault('no_css', True)
        kwargs.setdefault('friction', 10)
        kwargs.setdefault('velstop', 1.0)
        super(MTKinetic, self).__init__(**kwargs)
        self.friction   = kwargs.get('friction')
        self.velstop    = kwargs.get('velstop')
        self.touch      = {} # internals
        self.touches    = [] # from tuio, needed to simulate on_touch_down

    def on_touch_down(self, touches, touchID, x, y):
        if super(MTKinetic, self).on_touch_down(touches, touchID, x, y):
            self.touch[touchID] = {
                'vx': 0, 'vy': 0, 'ox': x, 'oy': y,
                'xmot': 0, 'ymot': 0, 'mode': 'touching',
            }

    def on_touch_move(self, touches, touchID, x, y):
        if touchID in self.touch:
            o = self.touch[touchID]
            o['xmot'] = x - o['ox']
            o['ymot'] = y - o['oy']
            o['ox'] = x
            o['oy'] = y
        return super(MTKinetic, self).on_touch_move(touches, touchID, x, y)

    def on_touch_up(self, touches, touchID, x, y):
        self.touches = touches
        if touchID in self.touch:
            o = self.touch[touchID]
            o['vx'] = o['xmot']
            o['vy'] = o['ymot']
            o['mode'] = 'spinning'

    def process_kinetic(self):
        '''Processing of kinetic, called in draw time.'''
        dt = getFrameDt()
        todelete = []
        for touchID in self.touch:
            o = self.touch[touchID]
            if o['mode'] != 'spinning':
                continue
            o['ox'] += o['vx']
            o['oy'] += o['vy']
            o['vx'] /= 1 + (self.friction * dt)
            o['vy'] /= 1 + (self.friction * dt)
            if Vector(o['vx'], o['vy']).length() < self.velstop:
                super(MTKinetic, self).on_touch_up(self.touches, touchID, o['ox'], o['oy'])
                todelete.append(touchID)
            else:
                super(MTKinetic, self).on_touch_move(self.touches, touchID, o['ox'], o['oy'])
        for touchID in todelete:
            del self.touch[touchID]

    def draw(self):
        self.process_kinetic()

MTWidgetFactory.register('MTKinetic', MTKinetic)
