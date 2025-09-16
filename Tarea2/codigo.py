# pip install schemdraw
import schemdraw
import schemdraw.elements as e

# ---- Config general: fuente grande y unidad amplia
schemdraw.config(fontsize=15)
d = schemdraw.Drawing(unit=1.0)  # más grande que el default

# ====== Marco central: ESP32 ======
cx, cy = 0, 0
esp_w, esp_h = 10, 16
d.add(e.Rect(width=esp_w, height=esp_h).at((cx-esp_w/2, cy-esp_h/2)).label('ESP32 DEV KIT', loc='center'))

# Puntos de pines (distribución vertical cada 3 unidades)
def pin_row(side, idx):
    y = cy + 6.5 - 3*idx
    x = cx - esp_w/2 if side=='L' else cx + esp_w/2
    return (x, y)

pin_left = {
    'PIN 2':    pin_row('L', 0),
    'PIN 30':   pin_row('L', 1),
    'PIN 17':   pin_row('L', 2),
    'PIN 48':   pin_row('L', 3),
    'TRIG 52':  pin_row('L', 4),
    'ECHO 53':  pin_row('L', 5),
}
pin_right = {
    'PIN 34':   pin_row('R', 1),
    'SCL 22':   pin_row('R', 2),
    'SDA 21':   pin_row('R', 3),
    'PIN 51':   pin_row('R', 4),
}

def dot_label(xy, txt, side='left'):
    return d.add(e.Dot().at(xy).label(txt, loc=side))

def route(p_from, p_to, midx=None, midy=None):
    """Ruteo en codo. Usa midx/midy para despejar textos."""
    x1,y1 = p_from; x2,y2 = p_to
    if midx is not None:
        d.add(e.Line().at((x1,y1)).to((midx,y1)))
        d.add(e.Line().at((midx,y1)).to((midx,y2)))
        d.add(e.Line().at((midx,y2)).to((x2,y2)))
    elif midy is not None:
        d.add(e.Line().at((x1,y1)).to((x1,midy)))
        d.add(e.Line().at((x1,midy)).to((x2,midy)))
        d.add(e.Line().at((x2,midy)).to((x2,y2)))
    else:
        d.add(e.Line().at((x1,y1)).to((x2,y1)))
        d.add(e.Line().at((x2,y1)).to((x2,y2)))

# Dots visibles en los pines
for name,pos in pin_left.items():
    dot_label(pos, name, 'left')
for name,pos in pin_right.items():
    dot_label(pos, name, 'right')

# ====== LADO IZQUIERDO (módulos) ======
xL = -24  # bien lejos para que no se encime
gapV = 3  # altura de cada “banda”

# Interrupción (PIN 2) pull‑up 10k a 5V
y0 = pin_left['PIN 2'][1]
d.add(e.RBox(w=6, h=2).at((xL, y0-1)).label('Pulsador Interrupción', loc='center'))
# 5V -> 10k -> switch -> pin
d.add(e.SourceV().up().at((xL-2, y0+0.8)).label('5V', loc='left'))
d.add(e.Resistor().right().label('10 kΩ', loc='top'))
sw1 = d.add(e.Switch().right().label('INT', loc='top'))
route(sw1.end, pin_left['PIN 2'], midy=y0)  # horizontal limpio
d.add(e.Ground().at((xL+1.8, y0-1.2)))

# Vaciado manual (PIN 30) pull‑down 4.8k
y1 = pin_left['PIN 30'][1]
d.add(e.RBox(w=6, h=2).at((xL, y1-1)).label('Switch Vaciado', loc='center'))
sw2 = d.add(e.Switch().right().at((xL-0.2, y1)).label('VAC', loc='top'))
route(sw2.end, pin_left['PIN 30'], midy=y1)
tap = (pin_left['PIN 30'][0]-3.0, y1)
d.add(e.Dot().at(tap))
d.add(e.Resistor().down().at(tap).label('4.8 kΩ', loc='right'))
d.add(e.Ground().at((tap[0], tap[1]-2.2)))

# DHT11 (DATA->PIN 17) + pull‑up 10k
y2 = pin_left['PIN 17'][1]
d.add(e.RBox(w=6.5, h=2.2).at((xL, y2-1.1)).label('DHT11', loc='center'))
route((xL+6.5, y2), pin_left['PIN 17'], midy=y2)
tap2 = (pin_left['PIN 17'][0]-3.0, y2)
d.add(e.Dot().at(tap2))
d.add(e.Resistor().up().at(tap2).label('10 kΩ', loc='left'))
d.add(e.SourceV().up().at((tap2[0], tap2[1]+2.2)).label('5V', loc='left'))
d.add(e.Ground().at((xL+5.4, y2-1.9)))

# Sonda DS18B20 (DATA->PIN 48) + pull‑up 4.8k
y3 = pin_left['PIN 48'][1]
d.add(e.RBox(w=7.2, h=2.2).at((xL, y3-1.1)).label('Sonda DS18B20', loc='center'))
route((xL+7.2, y3), pin_left['PIN 48'], midy=y3)
tap3 = (pin_left['PIN 48'][0]-3.0, y3)
d.add(e.Dot().at(tap3))
d.add(e.Resistor().up().at(tap3).label('4.8 kΩ', loc='right'))
d.add(e.SourceV().up().at((tap3[0], tap3[1]+2.2)).label('5V', loc='left'))
d.add(e.Ground().at((xL+6.0, y3-2.0)))

# HC‑SR04 (TRIG/ECHO)
y4 = pin_left['TRIG 52'][1]  # banda para TRIG
d.add(e.RBox(w=7.5, h=2.6).at((xL, y4-1.3)).label('HC-SR04', loc='center'))
route((xL+7.5, y4+0.6), pin_left['TRIG 52'], midy=y4+0.6)
route((xL+7.5, y4-0.6), pin_left['ECHO 53'], midy=y4-0.6)
d.add(e.SourceV().up().at((xL+1.0, y4+0.9)).label('5V', loc='left'))
d.add(e.Ground().at((xL+6.2, y4-2.2)))

# ====== LADO DERECHO (módulos) ======
xR = 24

# Relay + Bomba
yR0 = pin_right['PIN 34'][1]
d.add(e.RBox(w=7.0, h=2.2).at((xR, yR0-1.1)).label('Módulo Relay', loc='center'))
route(pin_right['PIN 34'], (xR, yR0+0.9), midy=yR0+0.9)
d.add(e.RBox(w=7.2, h=2.2).at((xR+9.0, yR0-1.1)).label('Bomba 93W', loc='center'))
d.add(e.Line().at((xR+7.0, yR0+0.9)).to((xR+9.0, yR0+0.9)))
d.add(e.SourceV().up().at((xR+1.0, yR0-0.2)).label('5V', loc='left'))
d.add(e.Ground().at((xR+3.8, yR0-0.4)))
d.add(e.Ground().at((xR+15.2, yR0-0.4)))

# LCD I2C
yR1 = pin_right['SCL 22'][1]
lcd = d.add(e.RBox(w=9.0, h=2.6).at((xR, yR1-1.3)).label('LCD 16x2 (I2C)', loc='center'))
route(pin_right['SCL 22'], (xR, yR1+0.8), midy=yR1+0.8)
route(pin_right['SDA 21'], (xR, yR1-0.8), midy=yR1-0.8)
d.add(e.SourceV().up().at((xR+1.0, yR1-1.9)).label('5V', loc='left'))
d.add(e.Ground().at((xR+7.6, yR1-2.1)))

# Buzzer
yR2 = pin_right['PIN 51'][1]
d.add(e.RBox(w=6.0, h=2.0).at((xR, yR2-1.0)).label('Buzzer', loc='center'))
route(pin_right['PIN 51'], (xR, yR2+0.8), midy=yR2+0.8)
d.add(e.Ground().at((xR+5.0, yR2-1.8)))

# Exporta
d.draw()
d.save('circuito_limpio.png')
d.save('circuito_limpio.svg')  # por si quieres vector
print('Listo -> circuito_limpio.png / .svg')
