from __future__ import annotations
from abc import ABC, abstractmethod


"""
Basic class of factory
"""


class MusicManager(ABC):
    @abstractmethod
    def get_connection(self):
        pass

    def download_music(self) -> str:
        service = self.get_connection()
        url = "'https:some_url'"
        output = f"{service.download_by_url(url)} \n"
        output += f"Downloaded music from: {service.name}"
        return output


"""
Concrete factories that overriding basic factory
"""


class SpotifyManager(MusicManager):
    def get_connection(self) -> Service:
        return SpotifyService()


class YouTubeManager(MusicManager):
    def get_connection(self) -> Service:
        return YouTubeService()


class SoundCloudManager(MusicManager):
    def get_connection(self) -> Service:
        return SoundCloudService()


"""
Abstract service of factory
"""


class Service(ABC):
    @abstractmethod
    def download_by_url(self, url: str) -> str:
        pass


"""
Concrete services that overriding abstract service
"""


class SpotifyService(Service):
    name = "Spotify"

    def download_by_url(self, url) -> str:
        return f"Downloaded music by url: {url}"


class YouTubeService(Service):
    name = "YouTube"

    def download_by_url(self, url: str) -> str:
        return f"Downloaded music by url: {url}"


class SoundCloudService(Service):
    name = "SoundCloud"

    def download_by_url(self, url: str) -> str:
        return f"Downloaded music by url: {url}"


"""
Client method, that's using factory for connecting to service
"""


def client_code(manager: MusicManager) -> None:
    print(f"{manager.download_music()}")


if __name__ == '__main__':
    print("App: Launched with the Spotify")
    client_code(SpotifyManager())
    print('\n')
    print("App: Launched with the SoundCloud")
    client_code(SoundCloudManager())



