# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 23:54:07 2024

@author: muozi
"""

def rgb_to_hex(rgb):
    # RGB tuple'ını alır ve hexadecimal formata çevirir
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

# Kullanım örneği
rgb_color = (255, 0, 0)  # Turuncu bir renk (RGB formatında)
hex_color = rgb_to_hex(rgb_color)
print("Hexadecimal Format:", hex_color)  # #ff5733
