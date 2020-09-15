import numpy as np
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets

#parametros iniciales
Ai = 1
Bi = -0.3
Ci = 7   
wi = 8
#tiempo
t = np.arange(-10.0,10.0,0.01)
#funcion
x = Ai * np.exp(Bi*t) * np.sin(wi*t+Ci)


fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)

ax.set_xlim(-10,10)

l, = plt.plot(t,x)

ax.margins(x=0)

#añadimos los axes donde estaran los sliders
axescolor = 'lightgoldenrodyellow'
Aaxe = plt.axes([0.1, 0.15, 0.8, 0.03], facecolor=axescolor)
Baxe = plt.axes([0.1, 0.1, 0.8, 0.03], facecolor=axescolor)
#añadimos los sliders
Aslider = widgets.Slider(Aaxe, 'A', 0.0, 10.0, valinit=Ai, valstep=0.1)
Bslider = widgets.Slider(Baxe, 'B', -1.0, 1.0, valinit=Bi, valstep=0.05)

def update(val):
    A = Aslider.val
    B = Bslider.val
    C = 7
    w = 8
    l.set_ydata(A * np.exp(B*t) * np.sin(w*t+C))
    fig.canvas.draw_idle()

#relacionados el evento de cambio con la funcion
Aslider.on_changed(update)
Bslider.on_changed(update)

#añadimos un boton de reinicio
resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
button = widgets.Button(resetax, 'Reset', color=axescolor, hovercolor='0.975')


def reset(event):
    Aslider.reset()
    Bslider.reset()
#relacionamos el evento
button.on_clicked(reset)

plt.show()
