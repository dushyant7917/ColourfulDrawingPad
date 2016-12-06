from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.core.window import WindowBase
from kivy.core.window import Window

class MyPaintWidget(Widget):

    def on_touch_down(self, touch):
        color = (random(), 1, 1)
        with self.canvas:
            Color(*color, mode='hsv')
            d = 30.
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


class MyPaintApp(App):

    def build(self):

        parent = Widget()

        self.painter = MyPaintWidget()
        clearbtn = Button(text='Clear', pos=(0, parent.height-100))
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)

        self.saver = MyPaintWidget()
        saveimage = Button(text='Save', pos=(0, parent.height))
        saveimage.bind(on_release=self.print_screen)
        parent.add_widget(self.saver)
        parent.add_widget(saveimage)

        return parent

    def print_screen(self, obj):
        Window.screenshot(name='screenshot.png' )

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyPaintApp().run()
