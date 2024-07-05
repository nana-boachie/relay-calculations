IEC
def xxxx(psm,tms): IEC
  operating_time = tms * (k / ((psm **a) - 1))



def long_time_inverse(psm, tms):  # A IEC
    operating_time = tms * (120 / (psm - 1))
    return operating_time


def standard_inverse(psm, tms):  # B IEC
    operating_time = tms * (0.14 / ((psm ** 0.02) - 1))
    return operating_time


def very_inverse(psm, tms):  # C IEC
    operating_time = tms * (13.5 / (psm - 1))
    return operating_time


def extremely_inverse(psm, tms):  # D IEC
    operating_time = tms * (80 / ((psm ** 2) - 1))
    return operating_time



#psm =I/IS

#tsm time multiplier setting



def xxx(psm,tms): # IEEE
  operating_time = td*((A/((psm**p)-1))+B)
