This may exist elsewhere but here is a library to control to a 20x4 LCD display that uses a SPLC780D control IC.

I wrote it for use on an ESP32.  Not sure if it work on a 8266.

USAGE:

  lcd = lcd_2004.lcd(device address, SCL Pin Number, SDA Pin Number)

Functions implemented are :

  lcd_clear() - Clear Screen<br>
  lcd_backlight(boolean) - Set Backlight on or off<br>
  lcd_print(string,x,y) - print string starting on row y(0-3) and column x(0-19)<br>
<p>
Long strings will wrap to the next line.
If you try to print beyond the bottom of the screen it simply cuts it off.

It's a bit basic but it works.

Many thanks to the other examples of this type of library out there for helping me figure out how to get this running.
