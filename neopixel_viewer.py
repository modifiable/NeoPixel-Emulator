from emulator_backend import Adafruit_NeoPixel
from neopixel_effects import NeoPixel_Effects
from musicData.beatDetection import brightness_values

def run():
    pixels = Adafruit_NeoPixel(100,6,"NEO_GRB + NEO_KHZ800")
    effects = NeoPixel_Effects(pixels)
    pixels.begin()

    brightness_values_scaled = [int(b * 10000) for b in brightness_values]

    print(brightness_values_scaled)

    for brightness_value in brightness_values_scaled:
        pixels.setBrightness(brightness_value)
        pixels.fill(pixels.Color(255,255,255),0,100)
        pixels.delay(500)
        pixels.show()

    #pixels.fill(pixels.Color(177,160,240),4,10)
    #pixels.show()
    #pixels.delay(1000)
    #pixels.clear()
    #pixels.setBrightness(70)
    #effects.colorWipe(pixels.Color(200,12,70),50)
    #pixels.clear()
    #pixels.show()
    #pixels.delay(1000)
    # for i in range(5):
    #     effects.colorWipe(pixels.Color(200,0,200),10)
    #     pixels.clear()
    # pixels.setBrightness(90)
    # effects.rainbow(20)
    # effects.colorWipe(pixels.Color(150,150,0),40)
    # effects.rainbowCycle(20,2)

run()
