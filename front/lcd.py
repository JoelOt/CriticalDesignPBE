# display multiline string
def lcd_display(self, multi):
for i, line in enumerate(multi.splitlines()):
self.lcd_display_string(line, i+1)

//ús 
import i2c_lcd
lcd = i2c_lcd.lcd()
text = input() // introduir el text q es vol a cada línia
self.lcd_display(text);
