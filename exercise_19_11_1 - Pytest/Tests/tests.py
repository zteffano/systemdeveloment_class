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


"""
Simple Test cases for a Television class:
def test_():
    #ARRANGE
    
    #ACT

    #ASSERT
"""

def test_tvConstructor_default():
    # no constructor, should have a default start setting. (on=False, channel=1, volume=10, mute=False)
    tvObj = Television() 
    assert tvObj.on == False
    assert tvObj.channel == 1
    assert tvObj.volume == 10
    assert tvObj.mute == False



def test_tvOnOff():
    #ARRANGE
    tvObj = Television() 

    #ACT
    tvObj.tvOnOff()

    #ASSERT
    assert tvObj.on == True

def test_chUp():
    #ARRANGE
    tvObj = Television() 

    #ACT
    tvObj.chUp()

    #ASSERT
    assert tvObj.chUp == 2

def test_chDown():
    #ARRANGE
    tvObj = Television() 

    #ACT
    tvObj.chDown()

    #ASSERT
    assert tvObj.chUp == 0

def test_getCh():
    #ARRANGE
    tvObj = Television() 

    #ACT

    #ASSERT
    assert tvObj.getCh() == 1

def test_volUp():
    #ARRANGE
    tvObj = Television() 

    #ACT
    tvObj.getCh()

    #ASSERT
    assert tvObj.volume == 11

def test_getVol():
    #ARRANGE
    tvObj = Television() 

    #ACT

    #ASSERT
    assert tvObj.getVol() == 10

def test_mute():
    #ARRANGE
    tvObj = Television()
   
    #ACT
    tvObj.mute = True
    tvObj.mute()

    #ASSERT
    assert tvObj.mute == True

def test_getMuted():
    #ARRANGE
    tvObj = Television()
   
    #ACT

    #ASSERT
    assert tvObj.mute == False
