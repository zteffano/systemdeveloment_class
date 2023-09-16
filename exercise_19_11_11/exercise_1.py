
class Television():

    """
    a class representing a television

    fields:
        + on: boolean
        + channel: int
        + volume: int
        + mute: boolean
    methods:
        + tvOnOff(): void
        + chUp(): void
        + chDown(): void
        + getCh(): int
        + volUp(): void
        + volDown(): void
        + getVol(): int
        + toggleMute(): void
        + getMuted(): boolean

    Obs: currently no contraints on channel and volume
    """

    def __init__(self): # Valgte at køre med en default state for tv'et.
        self.on = False
        self.channel = 1
        self.volume = 10
        self.mute = False

    def tvOnOff(self):
        self.on = not self.on

    def chUp(self):
        self.channel += 1

    def chDown(self):
        self.channel -= 1

    def getCh(self):
        return self.channel

    def volUp(self):
        self.volume += 1

    def volDown(self):
        self.volume -= 1

    def getVol(self):
        return self.volume

    def toggleMute(self): # blev nød til at ændre navnet fra mute til toggleMute, da python ikke tillader at en metode har samme navn som et field.(fik error)
        self.mute = not self.mute

    def getMuted(self):
        return self.mute

    def __str__(self):
        return f"Television: on={self.on}\nchannel={self.channel}\nvolume={self.volume}\nmute={self.mute}"

    def __repr__(self):
        return str(self)  
