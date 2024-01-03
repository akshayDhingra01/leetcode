class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res_beams = 0
        previous_beams = self.getbeams(bank[0])

        for beams in range(1, len(bank)):
            beamsInString = self.getbeams(bank[beams])
            if beamsInString == 0:
                continue
            else:
                tot_beams = beamsInString * previous_beams
                res_beams +=  tot_beams
                previous_beams = beamsInString

        return res_beams

    def getbeams(self, stringBeam):
        beams = 0
        for beam in stringBeam:
            if beam == '1':
                beams += 1
        
        return beams