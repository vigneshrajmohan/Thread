#Draw a red circle filling the entire canvas
import canvas
w = h = 512
canvas.set_size(w, h)
canvas.set_fill_color(1, 0, 0)
canvas.fill_ellipse(0, 0, w/2, h/2)
