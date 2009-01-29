from pymt.ui.widget import MTWidget

class HVLayout(MTWidget):
    '''Horizontal / Vertical layout.

    :Parameters:
        `alignment` : str, default is 'horizontal'
            Alignment of widget inside layout, can be `horizontal` or `vertical`
        `spacing` : int, default to 1
            Spacing between widgets
        `uniform_width` : bool, default to False
            Try to have same width for all children
        `uniform_height` : bool, default to False
            Try to have same height for all children

    :Events:
        `on_layout`
            Fired when layout function have been called
        `on_content_resize`
            Fired when content_width or content_height have changed
    '''

    def __init__(self, **kwargs):
        kwargs.setdefault('alignment', 'horizontal')
        kwargs.setdefault('spacing', 1)
        kwargs.setdefault('uniform_width', False)
        kwargs.setdefault('uniform_height', False)

        if kwargs.get('alignment') not in ['horizontal', 'vertical']:
            raise Exception('Invalid alignment, only horizontal/vertical are supported')

        super(HVLayout, self).__init__(**kwargs)
        self.register_event_type('on_layout')
        self.register_event_type('on_content_resize')
        self.spacing        = kwargs.get('spacing')
        self.alignment      = kwargs.get('alignment')
        self.uniform_width  = kwargs.get('uniform_width')
        self.uniform_height = kwargs.get('uniform_height')
        self.content_height = 0
        self.content_width  = 0

    def add_widget(self, w):
        super(HVLayout, self).add_widget(w)
        self.layout()

    def on_move(self, x, y):
        self.layout()
        super(HVLayout, self).on_move(x, y)

    def on_content_resize(self, w, h):
        pass

    def on_layout(self):
        pass

    def layout(self):
        '''Recalculate position for every subwidget, fire
        on_layout when finished. If content size have changed,
        fire on_content_resize too. Uniform width/height are handled
        after on_content_resize.
        '''
        start_x = cur_x = self.x
        start_y = cur_y = self.y
        current_width = current_height = 0
        for w in self.children:
            try:
                w.x = cur_x
                w.y = cur_y
                if w.height > current_height:
                    current_height = w.height
                if w.width > current_width:
                    current_width = w.width
                if self.alignment == 'horizontal':
                    cur_x += w.width + self.spacing
                elif self.alignment == 'vertical':
                    cur_y += w.height + self.spacing
            except:
                pass

        # update content size
        max_w_height = new_height = current_height
        max_w_width  = new_width  = current_width
        if self.alignment == 'horizontal':
            new_width = cur_x - start_x
        elif self.alignment == 'vertical':
            new_height = cur_y - start_y

        do_event_content_resize = (self.content_width != new_width) or (self.content_height != new_height)
        self.content_width = new_width
        self.content_height = new_height
        if do_event_content_resize:
            self.dispatch_event('on_content_resize',
                self.content_width, self.content_height)
            if self.uniform_width:
                for w in self.children:
                    w.width = max_w_width
            if self.uniform_height:
                for w in self.children:
                    w.height = max_w_height

        # we just do a layout, dispatch event
        self.dispatch_event('on_layout')

