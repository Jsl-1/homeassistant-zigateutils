"""Serve ZigateNetworkView."""

# import logging
# from aiohttp import web
# from ...zigateviewbase import ZigateViewBase

# _LOGGER = logging.getLogger("custom_components.zigate.frontend")


# class NetworkView(ZigateViewBase):
class ZigateNetworkView():
    """Serve ZigateNetworkView."""

    name = "zigate_network"

    # def __init__(self):
    #     """Initilize."""
    #     self.url = "zigate/network"

    # async def get(self, request):
    #     content = "Zigate Network"
    #     return web.Response(
    #         body=content,
    #         content_type="text/html",
    #         charset="utf-8")
