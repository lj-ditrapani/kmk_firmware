import board

from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.encoder import EncoderHandler
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitType
from kmk.modules.oneshot import OneShot

keyboard = KMKKeyboard()
layers = Layers()
split = Split(
    split_flip=True,  # If both halves are the same, but flipped, set this True
    split_type=SplitType.UART,  # Defaults to UART
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.RX,  # The primary data pin to talk to the secondary device with
    data_pin2=board.TX,  # Second uart pin to allow 2 way communication
    use_pio=True,  # allows for UART to be used with PIO
)
oneshot = OneShot()
keyboard.modules = [layers, split, oneshot]

xxx = KC.NO
UNDO = KC.LCTL(KC.Z)
CUT = KC.LCTL(KC.X)
COPY = KC.LCTL(KC.C)
PASTE = KC.LCTL(KC.V)
osctrl = KC.OS(KC.LSFT)
ossft = KC.OS(KC.LSFT)
osgui = KC.OS(KC.LSFT)
osalt = KC.OS(KC.LSFT)

keyboard.keymap = [
    [  # Dvorak
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE---|# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,
        KC.ESC,   KC.QUOT,  KC.COMM,  KC.DOT,   KC.P,     KC.Y,     KC.F,     KC.G,     KC.C,     KC.R,     KC.L,     KC.BSPC,
        KC.LSFT,  KC.A,     KC.O,     KC.E,     KC.U,     KC.I,     KC.D,     KC.H,     KC.T,     KC.N,     KC.S,     KC.RSFT,
        KC.TAB,   KC.SCOLON,KC.Q,     KC.J,     KC.K,     KC.X,     KC.B,     KC.M,     KC.W,     KC.V,     KC.Z,     KC.ENTER,
        xxx,      KC.MO(7), KC.MO(3), KC.MO(1), KC.MO(5), xxx,      xxx,      KC.MO(6), KC.MO(2), KC.MO(4), KC.MO(8), xxx,
    ],
    [  # alpha right
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE---|# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,
        xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      KC.F,     KC.G,     KC.C,     KC.R,     KC.L,     KC.BSPC,
        xxx,      KC.LALT,  KC.LGUI,  KC.LSFT,  KC.LCTL,  xxx,      KC.D,     KC.H,     KC.T,     KC.N,     KC.S,     KC.RSFT,
        xxx,      osalt,    osgui,    ossft,    osctrl,   xxx,      KC.B,     KC.M,     KC.W,     KC.V,     KC.Z,     KC.ENTER,
        xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      KC.ENTER, KC.SPACE, KC.BSPC,  xxx,      xxx,
    ],
    [  # alpha left
        # HERE----# HERE----# HERE----# HERE----# HERE----# HERE---|# HERE----# HERE----# HERE----# HERE----# HERE----# HERE----
        xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,
        KC.ESC,   KC.QUOT,  KC.COMM,  KC.DOT,   KC.P,     KC.Y,     xxx,      xxx,      xxx,      xxx,      xxx,      xxx,
        KC.LSFT,  KC.A,     KC.O,     KC.E,     KC.U,     KC.I,     xxx,      KC.RCTL,  KC.RSFT,  KC.RGUI,  KC.RALT,  xxx,
        KC.TAB,   KC.SCOLON,KC.Q,     KC.J,     KC.K,     KC.X,     xxx,      osctrl,   ossft,    osgui,    osalt,    xxx,
        xxx,      xxx,      KC.ESC,   KC.SPACE, KC.TAB,   xxx,      xxx,      xxx,      xxx,      xxx,      xxx,      xxx,
    ]
]

encoder_handler = EncoderHandler()
encoder_handler.pins = ((keyboard.encoder_pin_1, keyboard.encoder_pin_0, None, False),)
encoder_handler.map = (
    ((KC.VOLD, KC.VOLU),),  # base layer
    ((KC.VOLD, KC.VOLU),),  # Raise
    ((KC.VOLD, KC.VOLU),),  # Lower
)

keyboard.modules.append(encoder_handler)

if __name__ == '__main__':
    keyboard.go()
