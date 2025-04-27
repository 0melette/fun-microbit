# this was the original

from microbit import *
import music

solid_square = Image("99999:"
                     "99999:"
                     "99999:"
                     "99999:"
                     "99999:")

hollow_square = Image("99999:"
                      "90009:"
                      "90009:"
                      "90009:"
                      "99999:")

while True:
    if button_a.was_pressed():
        display.show(solid_square)
        music.play(music.POWER_UP)
        print("BACK")  # Send 'BACK' to Discord bot
    elif button_b.was_pressed():
        display.show(hollow_square)
        music.play(music.POWER_DOWN)
        print("LEAVING")  # Send 'LEAVING' to Discord bot

    sleep(100)  # Small sleep to not waste CPU
