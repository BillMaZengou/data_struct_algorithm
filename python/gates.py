class LogicGate(object):
    def __init__(self, n):
        self.label = n
        self.output = None

    def getLabel(self):
        return self.label

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

class BinaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        input_value = int(input("Enter Pin A input for gate " + str(self.getLabel()) + "--->"))
        input_value = 1 if input_value > 0 else 0
        return input_value

    def getPinB(self):
        input_value = int(input("Enter Pin B input for gate " + str(self.getLabel()) + "--->"))
        input_value = 1 if input_value > 0 else 0
        return input_value

class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        input_value = int(input("Enter Pin input for gate " + str(self.getLabel()) + "--->"))
        input_value = 1 if input_value > 0 else 0
        return input_value

class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        input_value = self.getPin()
        input_value = 0 if input_value == 1 else 1
        return input_value

g1 = AndGate("G1")
g2 = OrGate("G2")
g3 = NotGate("G3")
# print(g1.getOutput())
# print(g2.getOutput())
# print(g3.getOutput())
