from television import Television

class Test():
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        self.tv = None

    def test_init(self):
        """Test the initial state of the TV."""
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_power(self):
        """Test toggling the power."""
        self.tv.power()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.power()
        assert str(self.tv) == "Power = False, Channel = 0, Volume = 0"

    def test_mute(self):
        """Test muting and unmuting the TV."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.mute()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"

    def test_channel_up(self):
        """Test increasing the channel."""
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"
        for _ in range(4):  # Test wraparound
            self.tv.channel_up()
        assert str(self.tv) == "Power = True, Channel = 1, Volume = 0"

    def test_channel_down(self):
        """Test decreasing the channel."""
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 3, Volume = 0"  # Wraparound
        self.tv.channel_down()
        assert str(self.tv) == "Power = True, Channel = 2, Volume = 0"

    def test_volume_up(self):
        """Test increasing the volume."""
        self.tv.power()
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_up()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"
        self.tv.volume_up()  # No effect beyond max volume
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 2"

    def test_volume_down(self):
        """Test decreasing the volume."""
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 1"
        self.tv.volume_down()
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"
        self.tv.volume_down()  # No effect below min volume
        assert str(self.tv) == "Power = True, Channel = 0, Volume = 0"

