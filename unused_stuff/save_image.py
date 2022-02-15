async with aiohttp.ClientSession() as cs:
  async with cs.get(url) as r:
    image=await r.read()
    with open("reverse.png","wb") as f:
      f.write(image)