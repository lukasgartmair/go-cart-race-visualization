def OpenTxt(str_path):
    ### opens txt.file ###
    fobj = open(str_path, 'r')
    return fobj

def CloseTxt(fobj):
    ### closes txt.file ###
    fobj.close()

def ReadOut(fobj):
    ###reads the txt and stores it into the data bin###
    data = []
    data = [line.rstrip() for line in fobj]

    return data
def ReadOutColumns(data):
#### determine the columns as follows
    laps = []
    PE = []
    CZ = []
    CK = []
    LG = []
    NR = []
    DH = []
    JB = []
    NV = []

    content = []

    for (x,line) in enumerate(data):

        if x > 0:
        
            content  = line.split()
            if content == []:
                pass

            else:
                laps.append(float(content[0]))
                PE.append(float(content[1]))
                CZ.append(float(content[2]))
                CK.append(float(content[3]))
                LG.append(float(content[4]))
                NR.append(float(content[5]))
                DH.append(float(content[6]))
                JB.append(float(content[7]))
                NV.append(float(content[8]))
                
                # empty content again
                content = []
            
    return [laps, PE, CZ, CK, LG, NR, DH, JB, NV]

def LoadRaceStats():

    str_path = 'race.txt'
    fobj = OpenTxt(str_path)
    data =  ReadOut(fobj)
    CloseTxt(fobj)
    columns = ReadOutColumns(data)
    return columns 
