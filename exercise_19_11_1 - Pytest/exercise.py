"""
class Television:
- fields:
    + on: boolean
    + channel: int
    + volume: int
    + mute: boolean
- methods:
    + tvOnOff(): void
    + chUp(): void
    + chDown(): void
    + getCh(): int
    + volUp(): void
    + volDown(): void
    + getVol(): int
    + mute(): void 
    + getMuted(): boolean
"""

class Television():

    def __init__(self):
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

    def toggleMute(self):
        self.mute = not self.mute
    
    def getMuted(self):
        return self.mute
    
    