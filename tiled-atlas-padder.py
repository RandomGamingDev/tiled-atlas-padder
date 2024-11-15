from PIL import Image

# Params:
atlas_name = "atlas.png" # Name of the atlas image file
tile_res = (16, 16) # Side length of tile
padding_size = 1 # Size of padding in pixels
padding_color = (0, 0, 0, 0) # Color used for the padding
output_name = "res.png" # Name of the output file

with Image.open(atlas_name) as im:
	w, h = im.size # width, height
	rw, rh = w // tile_res[0], h // tile_res[1] # resolution width, resolution height
	ptile_res = [dim + padding_size for dim in tile_res] # Padded side length of tile
	nw, nh = rw * ptile_res[0], rh * ptile_res[1] # new width, new height
	new_im = Image.new(mode=im.mode, size=(nw, nh), color=padding_color)
	for x in range(rw):
		for y in range(rh):
			tile_pos = x * tile_res[0], y * tile_res[1]
			tile = im.crop((tile_pos[0], tile_pos[1], tile_pos[0] + tile_res[0], tile_pos[1] + tile_res[1]))
			new_im.paste(tile, (x * ptile_res[0], y * ptile_res[1]))
	new_im.save(output_name)