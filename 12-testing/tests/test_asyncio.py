import unittest
from unittest import IsolatedAsyncioTestCase

import aiohttp

events = []

class Test(IsolatedAsyncioTestCase):


    def setUp(self):
        events.append("setUp")

    async def asyncSetUp(self):
        self._client_session = aiohttp.ClientSession()
        events.append("asyncSetUp")

    async def test_response(self):
        events.append("test_response")
        async def get_request():
            async with self._client_session.get("http://python.org") as response:
                self.assertEqual(response.status, 200)
        self.addAsyncCleanup(self.on_cleanup)

    def tearDown(self):
        events.append("tearDown")

    async def asyncTearDown(self):
        await self._client_session.close()
        events.append("asyncTearDown")

    async def on_cleanup(self):
        events.append("cleanup")
        print(events)

if __name__ == "__main__":
    unittest.main()