def BR_u(ku):
    Rtot = 0.9999997600269808 + 7.54647401235431e-08*ku + 3.256109531287398e-08*ku**2
    BRbb = 0.54394342/Rtot
    BRgaga = (0.9999548821589315 + 2.5410954926918805e-05*ku + 1.6583239290232296e-10*ku**2)*0.002584254/Rtot
    return  2.*BRgaga*BRbb

def BR_d(kd):
    Rtot = 0.9999996321758218 - 1.1600186494709064e-07*kd + 5.943951815427372e-07*kd**2
    BRbb = 0.54394342/Rtot
    BRgaga = (0.9999999210723374 + 1.0421549903605332e-07*kd + 1.438923307763018e-14*kd**2)*0.002584254/Rtot
    return  2.*BRgaga*BRbb

def BR_ud(ku, kd):
    Rtot = 0.9999993781469615 + 7.546852769898962e-08*ku - 1.1599013547887742e-07*kd + 2.178545083799722e-14*ku*kd + 3.256109642125316e-08*ku**2 + 5.943951720268824e-07*kd**2 
    BRbb = 0.54394342/Rtot
    BRgaga = (0.9999546327354687 + 2.5410799186505123e-05*ku + 1.0422091492272555e-07*kd + 1.311401628522688e-12*ku*kd + 1.6580058013292403e-10*ku**2 + 1.8775051110443945e-14*kd**2)*0.002584254/Rtot
    return 2.*BRgaga*BRbb
    

    
def sigmahh_kl(kl, channel, confusion):
    coef = confusion[channel]
    return (coef['tri']*kl**2 - coef['int']*kl + coef['box'] + coef['tth+bbh'] + coef['bbxaa'])

def sigmahh_kukl(ku, kl, channel, confusion):
    coef = confusion[channel]
    return ((coef['ku']*(ku**2)/1600.**2 + coef['tri']*kl**2 - coef['int']*kl + coef['box'])*BR_u(ku)/BR_u(1.) + coef['tth+bbh'] + coef['bbxaa'])

def sigmahh_kdkl(kd, kl, channel, confusion):
    coef = confusion[channel]
    return ((coef['kd']*(kd**2)/800.**2 + coef['tri']*kl**2 - coef['int']*kl + coef['box'])*BR_d(kd)/BR_d(1.) + coef['tth+bbh'] + coef['bbxaa'])

def sigmahh_kukd(ku, kd, channel, confusion):
    coef = confusion[channel]
    return ((coef['ku']*(ku**2)/1600.**2 + coef['kd']*(kd**2)/800.**2 + coef['hhsm'])*BR_ud(ku, kd)/BR_ud(1., 1.) + coef['tth+bbh'] + coef['bbxaa'])

def sigmahh_kukdkl(ku, kd, kl, channel, confusion):
    coef = confusion[channel]
    return ((coef['ku']*(ku**2)/1600.**2 + coef['kd']*(kd**2)/800.**2 + coef['tri']*kl**2 - coef['int']*kl + coef['box'])*BR_ud(ku, kd)/BR_ud(1., 1.) + coef['tth+bbh'] + coef['bbxaa'])

def sigmahh_ku(ku, channel, confusion):
    coef = confusion[channel]
    return ((coef['ku']*(ku**2)/1600.**2 + coef['hhsm'])*BR_u(ku)/BR_u(1.) + coef['tth+bbh'] + coef['bbxaa'])

def sigmahh_kd(kd, channel, confusion):
    coef = confusion[channel]
    return ((coef['kd']*(kd**2)/800.**2 + coef['hhsm'])*BR_d(kd)/BR_d(1.) + coef['tth+bbh'] + coef['bbxaa'])