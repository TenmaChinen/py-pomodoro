from colorsys import rgb_to_hls, hls_to_rgb

def brightess(hex_color, pct):
    hex_color = hex_color.strip('#')
    r, g, b = [int(hex_color[i:i+2], 16) for i in range(0, 6, 2)]
    h, l, s = rgb_to_hls(r, g, b)
    l = min(l * pct,170)
    r, g, b = [int(x) for x in hls_to_rgb(h, l, s)]
    hex_color = '#%02X%02X%02X' % (r, g, b)
    return hex_color
