#!/usr/bin/env python3
# PulsePoint Incident Types
# See https://www.pulsepoint.org/incident-types

from enum import Enum

class IncidentTypes(Enum):
    # AID
    AA = 'Auto Aid'
    MU = 'Mutual Aid'
    ST = 'Strike Team/Task Force'

    # AIRCRAFT 
    AC = 'Aircraft Crash'
    AE = 'Aircraft Emergency'
    AES = 'Aircraft Emergency Standby'
    LZ = 'Landing Zone'

    #ALARM
    AED = 'AED Alarm'
    OA = 'Alarm'
    CMA = 'Carbon Monoxide'
    FA = 'Fire Alarm'
    MA = 'Manual Alarm'
    SD = 'Smoke Detector'
    TRBL = 'Trouble Alarm'
    WFA = 'Waterflow Alarm'

    # ASSIST
    FL = 'Flooding'
    LR = 'Ladder Request'
    LA = 'Lift Assist'
    PA = 'Police Assist'
    PS = 'Public Service'
    SH = 'Sheared Hydrant'

    # EXPLOSION
    EX = 'Explosion'
    PE = 'Pipeline Emergency'
    TE = 'Transformer Explosion'

    # FIRE
    AF = 'Appliance Fire'
    CHIM = 'Chimney Fire'
    CF = 'Commercial Fire'
    WSF = 'Confirmed Structure Fire'
    WVEG = 'Confirmed Vegetation Fire'
    CB = 'Controlled Burn/Prescribed Fire'
    ELF = 'Electrical Fire'
    EF = 'Extinguished Fire'
    FIRE = 'Fire'
    FULL = 'Full Assignment'
    IF = 'Illegal Fire'
    MF = 'Marine Fire'
    OF = 'Outside Fire'
    PF = 'Pole Fire'
    GF = 'Refuse/Garbage Fire'
    RF = 'Residential Fire'
    SF = 'Structure Fire'
    VEG = 'Vegetation Fire'
    VF = 'Vehicle Fire'
    WCF = 'Working Commercial Fire'
    WRF = 'Working Residential Fire'

    # HAZARD
    BT = 'Bomb Threat'
    EE = 'Electrical Emergency'
    EM = 'Emergency'
    ER = 'Emergency Response'
    GAS = 'Gas Leak'
    HC = 'Hazardous Condition'
    HMR = 'Hazmat Response'
    TD = 'Tree Down'
    WE = 'Water Emergency'

    # INVESTIGATION
    AI = 'Arson Investigation'
    HMI = 'Hazmat Investigation'
    INV = 'Investigation'
    OI = 'Odor Investigation'
    SI = 'Smoke Investigation'

    # LOCKOUT
    CL = 'Commercial Lockout'
    LO = 'Lockout'
    RL = 'Residential Lockout'
    VL = 'Vehicle Lockout'

    # MEDICAL
    CPR = 'CPR Needed'
    IFT = 'Interfacility Transfer'
    ME = 'Medical Emergency'
    MCI = 'Multi Casualty'

    # NATURAL DISASTER
    EQ = 'Earthquake'
    FLW = 'Flood Warning'
    TOW = 'Tornado Warning'
    TSW = 'Tsunami Warning'

    # OTHER
    CA = 'Community Activity'
    FW = 'Fire Watch'
    NO = 'Notification'
    STBY = 'Standby'
    TEST = 'Test'
    TRNG = 'Training'

    # RESCUE
    AR = 'Animal Rescue'
    CR = 'Cliff Rescue'
    CSR = 'Confined Space Rescue'
    ELR = 'Elevator Rescue'
    RES = 'Rescue'
    RR = 'Rope Rescue'
    TR = 'Technical Rescue'
    TNR = 'Trench Rescue'
    USAR = 'Urban Search and Rescue'
    VS = 'Vessel Sinking'
    WR = 'Water Rescue'

    # VEHICLE
    TCE = 'Expanded Traffic Collision'
    RTE = 'Railroad/Train Emergency'
    TC = 'Traffic Collision'
    TCS = 'Traffic Collision Involving Structure'
    TCT = 'Traffic Collision Involving Train'

    # WIRES
    WA = 'Wires Arcing'
    WD = 'Wires Down'