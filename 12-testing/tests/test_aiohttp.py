from aiohttp.test_utils import AioHTTPTestCase
from aiohttp import web

class MyAppTestCase(AioHTTPTestCase):

    async def get_application(self):
        """
        Override the get_app method to return your application.
        """
        async def hello(request):
            return web.Response(text='Hello, world')

        app = web.Application()
        app.router.add_get('/', hello)
        return app

    async def test_example(self):
        async with self.client.get("/") as resp:
            self.assertEqual(resp.status, 200)
            text = await resp.text()
        self.assertIn("Hello, world", text)