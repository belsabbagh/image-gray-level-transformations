def quantize_intensity(r, min_level=0, max_level=255):
    return min_level if r < min_level else (max_level if r > max_level else round(r))
