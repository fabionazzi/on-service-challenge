from httpx import Client, HTTPTransport


class APIClientFactory:

    @staticmethod
    def create(retries: int, timeout: float) -> Client:
        transport = HTTPTransport(retries=retries)
        return Client(transport=transport, timeout=timeout)
