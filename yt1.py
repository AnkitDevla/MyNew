class telephone():
    def calling(self):
        print("Clling.....")


class mobile(telephone):
    def message(self):
        print("Messaging...")


class smartphone(mobile):
    def touchscreen(self):
        print("Touch working....")

obj = smartphone()
obj.calling()
obj.message()
obj.touchscreen()

