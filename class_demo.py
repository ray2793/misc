class Musician (object):
    def __init__(self, sounds, name):
        self.sounds = sounds
        self.name = name
    def solo (self, length):
        for i in range (length):
            # print sound at repetition
            print (self.sounds[i % len(self.sounds)], end = " ")
        print ()
        
class Bassist (Musician):
    def __init__(self):
        super().__init__(["twang", "trumb", "sploot"])

class Guitarist (Musician):
    def __init__(self, name):
        super().__init__(["thump", "ding", "dong"], name)
    def tune(self):
        print ("Be with you in a minute, tuning")
    print ()

class Drummer (Musician):
    def __init__(self, name):
        super().__init__(["clack", "dack", "tack"], name)
    def count (self, number):
        for x in range (number):
            print (x+1)
    def combust (self):
        print ("Spontaneously combusting!")
    print ()
    
class Band (Musician):
    def __init__(self):
        self.memberList = []
    def hireMusician (self, Musician):
        self.memberList.append(Musician)
    def fireMusician (self, Musician):
        self.memberList.remove(Musician)
    def bandsolo(self, length):
        len(self.memberList)
        for x in range(len(self.memberList)):
            if type(self.memberList[x]) == Drummer:
                self.memberList[x].count(length)
            else:
                self.memberList[x].solo(length)

if __name__ == '__main__':
    # derek = Musician(["clunk", "thump", "clank"])
    # print (*derek.sounds)
    # derek.solo(5)
    doug = Drummer("doug")
    # doug.solo(10)
    # doug.combust()
    # doug.count(4)
    nigel = Guitarist("nigel")
    # nigel.solo(6)
    # print(nigel.sounds)
    nickelback = Band()
    
    nickelback.hireMusician(doug)
    nickelback.hireMusician(nigel)
    nickelback.bandsolo(10)
    