This may exist elsewhere but here is a library to control to a 20x4 LCD display that uses a SPLC780D control IC.

I wrote it for use on an ESP32.  Not sure if it work on a 8266.

USAGE:

  lcd = lcd_2004.lcd(device address, SCL Pin Number, SDA Pin Number)

Functions implemented are :

  <b>lcd_clear()</b> - <i>Clear Screen</i><br>
  <b>lcd_backlight(boolean)</b> - <i>Set Backlight on or off</i><br>
  <b>lcd_print(string,line,column)</b> - <i>print string starting on row y(1-4) and column x(0-19)</i><br>

Long strings will wrap to the next line.
If you try to print beyond the bottom of the screen it simply cuts it off.

It's a bit basic but it works.

Many thanks to the other examples of this type of library out there for helping me figure out how to get this running.
