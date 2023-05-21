from PIL import Image


# ConvertDataToPixels: This function takes the row data from the SQLite table and converts it into pixel positions
# for the source and destination tiles, returning the left, upper, right, and lower pixel coordinates for both
# positions.
def convertDataToPixels(row, square_size=43):
    left_src = row[0] * square_size
    upper_src = row[1] * square_size
    right_src = left_src + square_size
    lower_src = upper_src + square_size
    left_dst = row[2] * square_size
    upper_dst = row[3] * square_size
    right_dts = left_dst + square_size
    lower_dst = upper_dst + square_size
    return left_src, upper_src, right_src, lower_src, left_dst, upper_dst, right_dts, lower_dst


# RearrangeSquare: This function extracts a tile from the original image, rotates it based on the provided direction,
# and pastes it into the new image at the specified position.
def rearrangeSquare(source_position, destination_position, rotation, scrambled_image, new_image):
    tile = scrambled_image.crop(destination_position)
    tile = tile.transpose(Image.ROTATE_90 if rotation == 'right' else Image.ROTATE_270)
    new_image.paste(tile, source_position)
