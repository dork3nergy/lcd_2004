import lcd_2004
from time import sleep

#Usage: lcd_2004(Device Address, SCL PIN, SDA PIN)

lcd=lcd_2004.lcd(39,22,21)
lcd.lcd_backlight(True)
lcd.lcd_print("Long strings will wrap to the next line....",1,0)
sleep(2)
lcd.lcd_clear()
lcd.lcd_print("Print more text than the display can handle, it will cut it off",2,0)
print("OK")
sleep(2)
lcd.lcd_clear()
lcd.lcd_print("Backlight Goes Off",1,0)
sleep(1)
lcd.lcd_backlight(False)
sleep(1)
lcd.lcd_clear()
lcd.lcd_print("Backlight Goes On",1,0)
sleep(1)
lcd.lcd_backlight(True)
