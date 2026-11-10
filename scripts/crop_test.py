from PIL import Image

im = Image.open('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/.user_uploaded/media_1794307621470_23e2f760.jpg')
w, h = im.size
print('Size:', w, h)

# Let's crop candidate regions in a grid:
# In the screenshot, the pins start below the search bar (y ~ 180 to 200).
# Row 1: y ~ 190 to 410
# Row 2: y ~ 430 to 640
# Columns:
# Col 1: x ~ 65 to 235
# Col 2: x ~ 250 to 420
# Col 3: x ~ 435 to 605
# Col 4: x ~ 620 to 790
# Col 5: x ~ 805 to 975

# Let's save each of these boxes:
c_mog = im.crop((60, 480, 235, 640)) # wait, let's see row 2 col 1
c_mog.save('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/test_mog.jpg')

c_smirk = im.crop((245, 190, 420, 425))
c_smirk.save('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/test_smirk.jpg')

c_fedora = im.crop((615, 540, 795, 640)) # let's check
c_fedora.save('C:/Users/Thoufeek/.gemini/antigravity/brain/ab5d6534-892b-4bbc-b5f5-13c218bbb0bb/test_fedora.jpg')

print('Test crops saved')
