jlass Television:
    """
    Represents a television with basic functionality.

    Attributes:
        MIN_VOLUME (int): The minimum volume level.
        MAX_VOLUME (int): The maximum volume level.
        MIN_CHANNEL (int): The minimum channel number.
        MAX_CHANNEL (int): The maximum channel number.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes the television with default settings.

        The television is initially turned off, unmuted, with the volume set to the minimum and the channel set to the minimum.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL

    def power(self) -> None:
        """
        Toggles the power state of the television.

        If the television is currently on, it will be turned off. If the television is currently off, it will be turned on.
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True
        return None

    def mute(self) -> None:
        """
        Toggles the mute state of the television.

        If the television is currently muted, it will be unmuted. If the television is currently unmuted, it will be muted.
        """
        if self.__status and self.__muted:
            self.__muted = False
        elif self.__status and not self.__muted:
            self.__muted = True
        return None

    def channel_up(self) -> None:
        """
        Increases the channel number of the television.

        If the television is on and the current channel is less than the maximum channel, the channel number is incremented by 1.
        If the television is on and the current channel is the maximum channel, the channel number is set to the minimum channel.
        """
        if self.__status and self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
        elif self.__status and self.__channel == Television.MAX_CHANNEL:
            self.__channel = Television.MIN_CHANNEL
        return None

    def channel_down(self) -> None:
        """
        Decreases the channel number of the television.

        If the television is on and the current channel is greater than the minimum channel, the channel number is decremented by 1.
        If the television is on and the current channel is the minimum channel, the channel number is set to the maximum channel.
        """
        if self.__status and self.__channel > Television.MIN_CHANNEL:
            self.__channel -= 1
        elif self.__status and self.__channel == Television.MIN_CHANNEL:
            self.__channel = Television.MAX_CHANNEL
        return None

    def volume_up(self) -> None:
        """
        Increases the volume of the television.

        If the television is on and the current volume is less than the maximum volume, the volume is incremented by 1.
        If the television is on and the current volume is the maximum volume, the volume remains unchanged.
        If the television is muted, the mute state is toggled.
        """
        if self.__status and self.__volume < Television.MAX_VOLUME:
            if self.__muted:
                self.mute()
            self.__volume += 1
        elif self.__status and self.__volume == Television.MAX_VOLUME:
            pass
        return None

    def volume_down(self) -> None:
        """
        Decreases the volume of the television.

        If the television is on and the current volume is greater than the minimum volume, the volume is decremented by 1.
        If the television is on and the current volume is the minimum volume, the volume remains unchanged.
        If the television is muted, the mute state is toggled.
        """
        if self.__status and self.__volume > Television.MIN_VOLUME:
            if self.__muted:
                self.mute()
            self.__volume -= 1
        elif self.__status and self.__volume == Television.MIN_VOLUME:
            pass
        return None

    def __str__(self) -> str:
        """
        Returns a string representation of the current state of the television.

        If the television is muted, the volume is displayed as 0. Otherwise, the actual volume level is displayed.
        """
        if self.__muted:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = 0"
        else:
            return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}"
