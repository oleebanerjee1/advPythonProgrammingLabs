class Time:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)

    # convert the Time into seconds and return an int
    def timeInSeconds(self):
        return self.hours*3600 + self.minutes*60 + self.seconds

    # change values of hours, minutes, and seconds of the Time
    def changeTime(self, newHours, newMinutes, newSeconds):
        self.hours = newHours
        self.minutes = newMinutes
        self.seconds = newSeconds

    # convert the military Time to the twelve-hour clock and add the "am" or "pm"
    def twelveHourClock(self):
        if self.hours >= 12:
            if self.hours == 12:
                return "12:" + str(self.minutes) + ":" + str(self.seconds) + " pm"
            else:
                return str(self.hours-12) + ":" + str(self.minutes) + ":" + str(self.seconds) + " pm"
        else:
            return str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds) + " am"

    # determine what time of day it is: nighttime, morning, afternoon, or evening
    def timeOfDay(self):
        if (self.hours < 6) or (22 < self.hours <= 24):
            return "nighttime"
        elif self.hours <= 11:
            return "morning"
        elif self.hours <= 16:
            return "afternoon"
        elif self.hours <= 21:
            return "evening"
        else:
            return "uhhh something went wrong, time to debug lol"

    # return the difference in times, in seconds
    def compareTo(self, otherTime):
        return str(self.timeInSeconds() - otherTime.timeInSeconds())


time1 = Time(3, 30, 20)
print(str(time1))
print(str(time1.timeInSeconds()))
time1.changeTime(13, 40, 30)
print(str(time1))
print(time1.twelveHourClock())
print(time1.timeOfDay())
time2 = Time(3, 30, 20)
print(time1.compareTo(time2))
