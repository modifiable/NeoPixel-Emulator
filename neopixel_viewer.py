from emulator_backend import Adafruit_NeoPixel
from neopixel_effects import NeoPixel_Effects
import numpy as np
from musicData.beatDetection import brightness_values
from musicData.beatDetection import timestamps


def run():
    pixels = Adafruit_NeoPixel(500,6,"NEO_GRB + NEO_KHZ800")
    effects = NeoPixel_Effects(pixels)
    pixels.begin()

    original_array = brightness_values

    # Find the minimum and maximum values
    min_value = np.min(original_array)
    max_value = np.max(original_array)

    # Scale the array to range from 0 to 100
    scaled_array = ((original_array - min_value) / (max_value - min_value)) * 100

    print("Original array:", original_array)
    print("Scaled array:", scaled_array)

    # for brightness_value in scaled_array:
    #     pixels.setBrightness(brightness_value)
    #     pixels.fill(pixels.Color(255,255,255),0,500)
    #     pixels.delay(500)
    #     pixels.show()

    for i in range(len(scaled_array)):
        pixels.setBrightness(scaled_array[i])
        pixels.fill(pixels.Color(255,255,255),0,500)
        if not (i+1 >= len(timestamps)):
            print((timestamps[i+1] - timestamps[i])*1000)
            pixels.delay((timestamps[i+1] - timestamps[i])*1000)
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
