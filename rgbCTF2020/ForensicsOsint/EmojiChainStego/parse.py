from PIL import Image
import numpy as np
import scipy.stats
import sys

image = Image.open("emoji_chain_stego.png")
array = np.array(image).astype(np.int64)

N = 31
tile_height = array.shape[0] // N
tile_width = array.shape[1]

tiles = []

for i in range(N):
    tile = array[i*tile_height:(i+1)*tile_height,:,:]
    tiles.append(tile)

tiles = np.array(tiles)
tiles = tiles[:,16:144,16:144,:]
AVG = scipy.stats.mode(tiles, axis=0)[0][0]

tile_height = tiles.shape[1]
tile_width = tiles.shape[2]


ss = (np.sum(tiles[1:] - AVG, axis=0)[:,:,2])

def print_tile(t):
    assert t.shape == AVG.shape
    assert np.all(t[:,:,0] == AVG[:,:,0])
    assert np.all(t[:,:,1] == AVG[:,:,1])
    assert np.all(t[:,:,3] == AVG[:,:,3])

    assert np.all(t >= AVG)
    assert np.all(t <= AVG + 1)
    diff = t[:,:,2] - AVG[:,:,2]
    assert np.all(diff >= 0)
    assert np.all(diff <= 1)

    row = ""
    for i in range(tile_height):
        in_row = False
        row = ""
        for j in range(tile_width):
            if diff[i,j] == 1:
                if in_row:
                    row += f" {j}"
                else:
                    row = f"{i}: {j}"
                    in_row = True
        if in_row:
            print(row)

for i in range(1, N):
    print(i)
    print_tile(tiles[i])
    print()
