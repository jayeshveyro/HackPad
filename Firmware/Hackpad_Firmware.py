import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import KeysScanner

keyboard = KMKKeyboard()

# Your 9 switches wired directly to D0 through D8
PINS = [
    board.D0, board.D1, board.D2,
    board.D3, board.D4, board.D5,
    board.D6, board.D7, board.D8,
]

# Configure direct-pin scanning (no diodes, active-low to GND)
keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Customize your 9 key shortcuts here (SW1 to SW9)
keyboard.keymap = [
    [
        KC.LCTL(KC.C), KC.LCTL(KC.V), KC.LCTL(KC.Z),  # SW1: Copy, SW2: Paste, SW3: Undo
        KC.MPRV,       KC.MPLY,       KC.MNXT,        # SW4: Prev Track, SW5: Play/Pause, SW6: Next Track
        KC.VOLD,       KC.MUTE,       KC.VOLU,        # SW7: Vol Down, SW8: Mute, SW9: Vol Up
    ]
]

if __name__ == '__main__':
    keyboard.go()
