from aiohttp import web

async def do(req):

   import time
   time.sleep(10)

   return web.Response(text="Done\n")

async def handle(req):
    return web.Response(text="Wow\n") 

app = web.Application()

app.router.add_get("/",handle)
app.router.add_get("/do",do)

web.run_app(app,host="localhost",port=8080)

