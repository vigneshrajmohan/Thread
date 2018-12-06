from scene import *
import ui
import photos

class MyScene (Scene):
    global ui_image
    def setup(self):
        all_assets = photos.get_assets()[-1]
        ui_image = all_assets.get_ui_image()


        self.background_color = 'lightgray'

        img = ui.Button(name='image')
        img.frame = (25,25,self.size.x-50,self.size.y-50)
        img.background_image = ui_image
        img.enable = False
        img.hidden = True
        self.view.add_subview(img)

        b = ui.Button()
        b.frame = (100,0,60,32)
        b.title = 'tap'
        b.action = self.disp_photo
        self.view.add_subview(b)



    def disp_photo(self,sender):
        img = sender.superview['image']
        img.hidden = not img.hidden

if __name__ == '__main__':
    run(MyScene())
