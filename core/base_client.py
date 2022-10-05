import asyncio
import logging
from typing import Optional

from config import settings as config
from requests import JSONDecodeError, Session
from requests import Session


settings = config.get_settings()
logger = logging.getLogger(settings.LOGGING)


class BaseClient:
    TIMEOUT = 120

    async def exec_request(self, method: str, url: str, data: Optional[dict] = None,
                           json: Optional[dict] = None) -> tuple([dict, int]):
        """Execute a request to an url with the method and data provided. By default tries to use
           the Bearer authentication method.

        Args:
           method (str): method to use. It includes all HTTP methods
           url (str): url to request
           data (Optional[dict]): data to send in the request
           auth (str, optional): Authentication method. Defaults to AuthMethods.BEARER.

        Returns:
           dict: response from the API
        """
        session = Session()

        values = {
            "url": url,
            "timeout": self.TIMEOUT
        }

        if data:
            values["data"] = data
        elif json:
            values["json"] = json

        def _make_request():
            return getattr(session, method)(**values)

        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, _make_request)
        response = await future
        try:
            json_response = response.json()
        except JSONDecodeError:
            json_response = {
                "error": response.text,
                "status": response.status_code
            }

        return json_response, response.status_code
