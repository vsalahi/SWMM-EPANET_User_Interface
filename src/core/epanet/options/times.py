﻿from core.inputfile import Section
from enum import Enum


class StatisticOptions(Enum):
    """statistical post-processing setting"""
    NONE = 1
    AVERAGED = 2
    MINIMUM = 3
    MAXIMUM = 4
    RANGE = 5


class TimesOptions(Section):
    """Defines various time step parameters used in the simulation"""

    SECTION_NAME = "[TIMES]"

    field_dict = {
        "Duration": "duration",
        "Hydraulic Timestep": "hydraulic_timestep",
        "Quality Timestep": "quality_timestep",
        "Rule Timestep": "rule_timestep",
        "Pattern Timestep": "pattern_timestep",
        "Pattern Start": "pattern_start",
        "Report Timestep": "report_timestep",
        "Report Start": "report_start",
        "Start ClockTime": "start_clocktime",
        "Statistic": "statistic"}
    """Mapping from label used in file to field name"""

    def __init__(self):
        Section.__init__(self)

        self.duration = "0"			            # hours:minutes
        """duration of the simulation; the default of zero runs a single period snapshot analysis."""

        self.hydraulic_timestep = "1:00"	    # hours:minutes
        """determines how often a new hydraulic state of the network is computed"""

        self.quality_timestep = "0:05"		    # hours:minutes
        """time step used to track changes in water quality throughout the network"""

        self.rule_timestep = "0:05" 		    # hours:minutes
        """ime step used to check for changes in system status due to activation of rule-based controls"""

        self.pattern_timestep = "1:00" 		    # hours:minutes
        """interval between time periods in all time patterns"""

        self.pattern_start = "0:00"	            # hours:minutes
        """time offset at which all patterns will start"""

        self.report_timestep = "1:00"		    # hours:minutes
        """time interval between which output results are reported"""

        self.report_start = "0:00"	            # hours:minutes
        """length of time into the simulation at which output results begin to be reported"""

        self.start_clocktime = "12 am"		    # hours:minutes AM/PM
        """time of day (e.g., 3:00 PM) at which the simulation begins"""

        self.statistic = StatisticOptions.NONE  # NONE/AVERAGED/MINIMUM/MAXIMUM/RANGE
        """determines what kind of statistical post-processing to do on simulation results"""