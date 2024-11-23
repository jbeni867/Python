class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self):
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self):
        if self.__status and self.__muted:
            self.__muted = False
        elif self.__status and not self.__muted:
            self.__muted = True

    def channel_up(self):
        if self.__status and self.__channel < self.MAX_CHANNEL:
            self.__channel += 1
        elif self.__status and self.__channel == self.MAX_CHANNEL:
            self.__channel = self.MIN_CHANNEL

    def channel_down(self):
        if self.__status and self.__channel > self.MIN_CHANNEL:
            self.__channel -= 1
        elif self.__status and self.__channel == self.MIN_CHANNEL:
            self.__channel = self.MAX_CHANNEL

    def volume_up(self):
        if self.__status and self.__volume < self.MAX_VOLUME:
            if self.__muted:
                self.mute()
            self.__volume += 1
        elif self.__status and self.__volume == self.MAX_VOLUME:
            pass

    def volume_down(self):
        if self.__status and self.__volume > self.MIN_VOLUME:
            if self.__muted:
                self.mute()
            self.__volume -= 1
        elif self.__status and self.__volume == self.MIN_VOLUME:
            pass

    def __str__(self) -> str:
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
