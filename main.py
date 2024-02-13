from kivy.config import Config

Config.set("graphics", "resizable", 0)

from kivy.app import *
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from random import *
from math import *
from kivy.uix.scatter import Scatter
from kivy.core.window import Window

class Table(Widget):

    size_hint = (None, None)
    size = (150, 100)

    def __init__(self,**kwargs):
        super(Table, self).__init__(**kwargs)

        with self.canvas:
            Color(0, 0, 0)
            SmoothRoundedRectangle(size = self.size, radius = [3])
            Color(114 / 255, 79 / 255, 56 / 255)
            SmoothRoundedRectangle(pos = (2, 2), size = (self.size[0] - 4, self.size[1] - 4), radius = [3])
    
    def on_touch_up(self, touch):
        r = radians(self.parent.rotation)
        scale = self.parent.scale
        x, y = 150, 100
        x, y = (x * abs(cos(r)) + y * abs(sin(r)), x * abs(sin(r)) + y * abs(cos(r)))
        self.size = (x * scale, y * scale) 

        window_width, window_height = Window.size
        pos = self.parent.pos
        self.parent.pos = (max(40, min(pos[0], window_width - 40 - self.size[0])), max(40, min(pos[1], window_height - 90 - self.size[1])))
        

class Chair(Widget):
    
    size_hint = (None, None)
    size = (60, 60)

    def __init__(self,**kwargs):
        super(Chair, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0)
            Ellipse(pos = (0, 0), size = self.size)
            Color(114 / 255, 79 / 255, 56 / 255)
            Ellipse(pos = (2, 2), size = (self.size[0] - 4, self.size[1] - 4))
            Color((randint(0, 255) % 215 + 40) / 255, (randint(0, 255) % 215 + 40) / 255, (randint(0, 255) % 215 + 40) / 255)
            Ellipse(pos = (10, 10), size = (40, 40))

    def on_touch_up(self, touch):
        r = radians(self.parent.rotation)
        scale = self.parent.scale
        x, y = 60, 60
        x, y = (x * abs(cos(r)) + y * abs(sin(r)), x * abs(sin(r)) + y * abs(cos(r)))
        self.size = (x * scale, y * scale) 

        window_width, window_height = Window.size
        pos = self.parent.pos
        self.parent.pos = (max(40, min(pos[0], window_width - 40 - self.size[0])), max(40, min(pos[1], window_height - 90 - self.size[1])))

class Wardrobe(Widget):
    
    size_hint = (None, None)
    size = (200, 80)

    def __init__(self,**kwargs):
        super(Wardrobe, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0)
            SmoothRoundedRectangle(size = self.size, radius = [3])
            Color(83 / 255, 68 / 255, 54 / 255)
            SmoothRoundedRectangle(pos = (2, 2), size = (self.size[0] - 4, self.size[1] - 4), radius = [3])

    def on_touch_up(self, touch):
        r = radians(self.parent.rotation)
        scale = self.parent.scale
        x, y = 200, 80
        x, y = (x * abs(cos(r)) + y * abs(sin(r)), x * abs(sin(r)) + y * abs(cos(r)))
        self.size = (x * scale, y * scale) 
    
        window_width, window_height = Window.size
        pos = self.parent.pos
        self.parent.pos = (max(40, min(pos[0], window_width - 40 - self.size[0])), max(40, min(pos[1], window_height - 90 - self.size[1])))

class Armchair(Widget):
    
    size_hint = (None, None)
    size = (103, 117)

    def __init__(self,**kwargs):
        super(Armchair, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (10, 12), size = (94, 94), radius = [3])
            r, g, b = randint(0, 255) % 215 + 40, randint(0, 255) % 215 + 40, randint(0, 255) % 215 + 40
            Color(r / 255, g / 255, b / 255)
            SmoothRoundedRectangle(pos = (12, 14), size = (90, 90), radius = [3])

            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (5, 0), size = (94, 24), radius = [3])
            Color((r - 40) / 255, (g - 40) / 255, (b - 40) / 255)
            SmoothRoundedRectangle(pos = (7, 2), size = (90, 20), radius = [3])

            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (5, 95), size = (94, 24), radius = [3])
            Color((r - 40) / 255, (g - 40) / 255, (b - 40) / 255)
            SmoothRoundedRectangle(pos = (7, 97), size = (90, 20), radius = [3])

            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (0, 12), size = (24, 94), radius = [3])
            Color((r - 40) / 255, (g - 40) / 255, (b - 40) / 255)
            SmoothRoundedRectangle(pos = (2, 14), size = (20, 90), radius = [3])

    def on_touch_up(self, touch):
        r = radians(self.parent.rotation)
        scale = self.parent.scale
        x, y = 103, 117
        x, y = (x * abs(cos(r)) + y * abs(sin(r)), x * abs(sin(r)) + y * abs(cos(r)))
        self.size = (x * scale, y * scale) 

        window_width, window_height = Window.size
        pos = self.parent.pos
        self.parent.pos = (max(40, min(pos[0], window_width - 40 - self.size[0])), max(40, min(pos[1], window_height - 90 - self.size[1])))

class Sofa(Widget):
    
    size_hint = (None, None)
    size = (106, 222)

    def __init__(self,**kwargs):
        super(Sofa, self).__init__(**kwargs)
        with self.canvas:
            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (13, 19), size = (94, 184), radius = [3])
            r, g, b = randint(0, 255) % 215 + 40, randint(0, 255) % 215 + 40, randint(0, 255) % 215 + 40
            Color(r / 255, g / 255, b / 255)
            SmoothRoundedRectangle(pos = (15, 21), size = (90, 180), radius = [3])

            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (8, 0), size = (94, 30), radius = [3])
            Color((r - 40) / 255, (g - 40) / 255, (b - 40) / 255)
            SmoothRoundedRectangle(pos = (10, 2), size = (90, 26), radius = [3])

            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (8, 193), size = (94, 30), radius = [3])
            Color((r - 40) / 255, (g - 40) / 255, (b - 40) / 255)
            SmoothRoundedRectangle(pos = (10, 195), size = (90, 26), radius = [3])

            Color(0, 0, 0)
            SmoothRoundedRectangle(pos = (0, 19), size = (30, 184), radius = [3])
            Color((r - 40) / 255, (g - 40) / 255, (b - 40) / 255)
            SmoothRoundedRectangle(pos = (2, 21), size = (26, 180), radius = [3])

    def on_touch_up(self, touch):
        r = radians(self.parent.rotation)
        scale = self.parent.scale
        x, y = 106, 222
        x, y = (x * abs(cos(r)) + y * abs(sin(r)), x * abs(sin(r)) + y * abs(cos(r)))
        self.size = (x * scale, y * scale) 

        window_width, window_height = Window.size
        pos = self.parent.pos
        self.parent.pos = (max(40, min(pos[0], window_width - 40 - self.size[0])), max(40, min(pos[1], window_height - 90 - self.size[1])))
        
class MyWindow(Widget):

    rect = None
    border = None
    size = (120, 34)
    wall = None

    def __init__(self, **kwargs):
        super(MyWindow, self).__init__(**kwargs)
        
        self.wall = 'DOWN'

        with self.canvas:
            Color(0, 0, 0)
            self.border = Rectangle(size = self.size)

            Color(164 / 255, 199 / 255, 205 / 255)
            self.rect = Rectangle(size = (120, 30), pos = (0, 2))

    def on_touch_move(self, touch):
        prev = self.wall
        window_width, window_height = Window.size
        x, y = self.parent.pos[0] + touch.pos[0], self.parent.pos[1] + touch.pos[1]
        if (40 <= x <= window_width - 40 and 10 <= y <= 40):
            self.wall = 'DOWN'
            self.size = (120, 34)
            self.border.size = self.size
            self.rect.size = (self.size[0], self.size[1] - 4)
            self.rect.pos = (0, 2)
        elif (40 <= x <= window_width - 40 and window_height - 90 <= y <= window_height - 60):
            self.wall = 'UP'
            self.size = (120, 34)
            self.border.size = self.size
            self.rect.size = (self.size[0], self.size[1] - 4)
            self.rect.pos = (0, 2)
        elif (10 <= x <= 40 and 40 <= y <= window_height - 90):
            self.wall = 'LEFT'
            self.size = (34, 120)
            self.border.size = self.size
            self.rect.size = (self.size[0] - 4, self.size[1])
            self.rect.pos = (2, 0)
        elif (window_width - 40 <= x <= window_width - 10 and 40 <= y <= window_height - 90):
            self.wall = 'RIGHT'
            self.size = (34, 120)
            self.border.size = self.size
            self.rect.size = (self.size[0] - 4, self.size[1])
            self.rect.pos = (2, 0)
        self.parent.size = self.size
        pos = self.parent.pos
        if prev in ['UP', 'DOWN'] and self.wall in ['LEFT', 'RIGHT'] or prev in ['LEFT', 'RIGHT'] and self.wall in ['UP', 'DOWN']:
            self.parent.pos = pos[0] + touch.pos[0] - touch.pos[1], pos[1] + touch.pos[1] - touch.pos[0]

    def on_touch_up(self, touch):
        window_width, window_height = Window.size
        pos = self.parent.pos
        if self.wall == 'DOWN':
            x, y = max(40, min(pos[0], window_width - 40 - self.size[0])), 10
        elif self.wall == 'UP':
            x, y = max(40, min(pos[0], window_width - 40 - self.size[0])), window_height - 90
        elif self.wall == 'LEFT':
            x, y = 10, max(40, min(pos[1], window_height - 90 - self.size[1]))
        elif self.wall == 'RIGHT':
            x, y = window_width - 40, max(40, min(pos[1], window_height - 90 - self.size[1]))
        self.parent.pos = (x, y)

class Door(Widget):

    rect = None
    border = None
    size = (124, 34)
    wall = None

    def __init__(self, **kwargs):
        super(Door, self).__init__(**kwargs)
        
        self.wall = 'DOWN'

        with self.canvas:
            Color(0, 0, 0)
            self.border = Rectangle(size = self.size)

            Color(97 / 255, 79 / 255, 70 / 255)
            self.rect = Rectangle(size = (120, 30), pos = (2, 2))

    def on_touch_move(self, touch):
        prev = self.wall
        window_width, window_height = Window.size
        x, y = self.parent.pos[0] + touch.pos[0], self.parent.pos[1] + touch.pos[1]
        if (40 <= x <= window_width - 40 and 10 <= y <= 40):
            self.wall = 'DOWN'
            self.size = (124, 34)
            self.border.size = self.size
        elif (40 <= x <= window_width - 40 and window_height - 90 <= y <= window_height - 60):
            self.wall = 'UP'
            self.size = (124, 34)
            self.border.size = self.size
        elif (10 <= x <= 40 and 40 <= y <= window_height - 90):
            self.wall = 'LEFT'
            self.size = (34, 124)
            self.border.size = self.size
        elif (window_width - 40 <= x <= window_width - 10 and 40 <= y <= window_height - 90):
            self.wall = 'RIGHT'
            self.size = (34, 124)
            self.border.size = self.size
        self.rect.size = (self.size[0] - 4, self.size[1] - 4)
        self.rect.pos = (2, 2)
        self.parent.size = self.size
        pos = self.parent.pos
        if prev in ['UP', 'DOWN'] and self.wall in ['LEFT', 'RIGHT'] or prev in ['LEFT', 'RIGHT'] and self.wall in ['UP', 'DOWN']:
            self.parent.pos = pos[0] + touch.pos[0] - touch.pos[1], pos[1] + touch.pos[1] - touch.pos[0]

    def on_touch_up(self, touch):
        window_width, window_height = Window.size
        pos = self.parent.pos
        if self.wall == 'DOWN':
            x, y = max(40, min(pos[0], window_width - 40 - self.size[0])), 10
        elif self.wall == 'UP':
            x, y = max(40, min(pos[0], window_width - 40 - self.size[0])), window_height - 90
        elif self.wall == 'LEFT':
            x, y = 10, max(40, min(pos[1], window_height - 90 - self.size[1]))
        elif self.wall == 'RIGHT':
            x, y = window_width - 40, max(40, min(pos[1], window_height - 90 - self.size[1]))
        self.parent.pos = (x, y)


class Room(FloatLayout):

    floor = None
    wall = None    
    tables = []
    chairs = []
    wardrobes = []
    armchairs = []
    sofas = []
    windows = []
    doors = []

    def __init__(self, **kwargs):
        super(Room, self).__init__(**kwargs)

        self.bind(
            size = self._update_rect,
            pos = self._update_rect
        )

        with self.canvas:
            Color(140 / 255, 140 / 255, 140 / 255)
            self.wall = Rectangle(
                size = self.size,
                pos = self.pos
            )
            Color(255, 255, 255)
            self.floor = Rectangle(
                size = (self.size[0] - 60, self.size[1] - 60),
                pos = (self.pos[0] + 30, self.pos[1] + 30)
            )

    def _update_rect(self, instance, value):
        self.floor.pos = (instance.pos[0] + 30, instance.pos[1] + 30)
        self.floor.size = (instance.size[0] - 60, instance.size[1] - 60)
        self.wall.pos = instance.pos
        self.wall.size = instance.size

    def add_Table(self):
        if len(self.tables) < 5:
            scatter = Scatter(size_hint = (None, None), size = Table.size, scale_min = .5, scale_max = 1.5)
            scatter.add_widget(Table())
            self.tables.append(scatter)
            self.add_widget(scatter)

    def remove_Table(self):
        if len(self.tables) > 0:
            self.remove_widget(self.tables.pop())

    def add_Chair(self):
        if len(self.chairs) < 8:
            scatter = Scatter(size_hint = (None, None), size = Chair.size, scale_min = .5, scale_max = 1.5)
            scatter.add_widget(Chair())
            self.chairs.append(scatter)
            self.add_widget(scatter)

    def remove_Chair(self):
        if len(self.chairs) > 0:
            self.remove_widget(self.chairs.pop())

    def add_Wardrobe(self):
        if len(self.wardrobes) < 5:
            scatter = Scatter(size_hint = (None, None), size = Wardrobe.size, scale_min = .5, scale_max = 1.5)
            scatter.add_widget(Wardrobe())
            self.wardrobes.append(scatter)
            self.add_widget(scatter)

    def remove_Wardrobe(self):
        if len(self.wardrobes) > 0:
            self.remove_widget(self.wardrobes.pop())

    def add_Armchair(self):
        if len(self.armchairs) < 5:
            scatter = Scatter(size_hint = (None, None), size = Armchair.size, scale_min = .5, scale_max = 1.5)
            scatter.add_widget(Armchair())
            self.armchairs.append(scatter)
            self.add_widget(scatter)

    def remove_Armchair(self):
        if len(self.armchairs) > 0:
            self.remove_widget(self.armchairs.pop())

    def add_Sofa(self):
        if len(self.sofas) < 5:
            scatter = Scatter(size_hint = (None, None), size = Sofa.size, scale_min = .5, scale_max = 1.5)
            scatter.add_widget(Sofa())
            self.sofas.append(scatter)
            self.add_widget(scatter)

    def remove_Sofa(self):
        if len(self.sofas) > 0:
            self.remove_widget(self.sofas.pop())

    def add_Window(self):
        if len(self.windows) < 5:
            scatter = Scatter(size_hint = (None, None), size = MyWindow.size, do_rotation = False, do_scale = False, scale_min = 1, scale_max = 1)
            scatter.add_widget(MyWindow())
            self.windows.append(scatter)
            self.add_widget(scatter)

    def remove_Window(self):
        if len(self.windows) > 0:
            self.remove_widget(self.windows.pop())

    def add_Door(self):
        if len(self.doors) < 3:
            scatter = Scatter(size_hint = (None, None), size = Door.size, do_rotation = False, do_scale = False, scale_min = 1, scale_max = 1)
            scatter.add_widget(Door())
            self.doors.append(scatter)
            self.add_widget(scatter)

    def remove_Door(self):
        if len(self.doors) > 0:
            self.remove_widget(self.doors.pop())


class RoomBuilderApp(App):

    room = Room()
    mainbutton = None
    dropdown = None
    furniture = ['стол', 'стул', 'кресло', 'диван', 'шкаф', 'окно', 'дверь']
    

    def build(self):
        main_vbox = GridLayout(rows = 2, padding = 10)

        btns_gbox = BoxLayout(orientation = 'horizontal', spacing = 5, padding = 5, size_hint_y = None, height = 50)
        btns_gbox.add_widget(Button(text = '-', font_size = 25, on_press = self.remove_furniture))

        self.dropdown = DropDown()       
        for i in self.furniture:
            btn = Button(text='%s' % i, size_hint_y = None, height = 40)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)
        self.mainbutton = Button(text = 'Выберите мебель', font_size = 20, size_hint_x = None, width = 200)
        self.mainbutton.bind(on_press = self.dropdown.open)
        self.dropdown.bind(on_select = lambda instance, x: setattr(self.mainbutton, 'text', x))

        btns_gbox.add_widget(self.mainbutton)
        btns_gbox.add_widget(Button(text = '+', font_size = 25, on_press = self.add_furniture))

        main_vbox.add_widget(btns_gbox)

        main_vbox.add_widget(self.room)
        
        return main_vbox
    
    def add_furniture(self, instance):
        match self.mainbutton.text:
            case 'стол':
                self.room.add_Table()
            case 'стул':
                self.room.add_Chair()
            case 'шкаф':
                self.room.add_Wardrobe()
            case 'кресло':
                self.room.add_Armchair()
            case 'диван':
                self.room.add_Sofa()
            case 'окно':
                self.room.add_Window()
            case 'дверь':
                self.room.add_Door()
            case _:
                print('Мебель не выбрана!')

    def remove_furniture(self, instance):
        match self.mainbutton.text:
            case 'стол':
                self.room.remove_Table()
            case 'стул':
                self.room.remove_Chair()
            case 'шкаф':
                self.room.remove_Wardrobe()
            case 'кресло':
                self.room.remove_Armchair()
            case 'диван':
                self.room.remove_Sofa()
            case 'окно':
                self.room.remove_Window()
            case 'дверь':
                self.room.remove_Door()
            case _:
                print('Мебель не выбрана!')
        


if __name__ == '__main__':
    RoomBuilderApp().run()
