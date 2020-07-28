"""
Different Types of Logic Gates (e.g AND, OR)
are all under the LogicGate Class. Depending on
the number of input, they can be further categorise
into BinaryGate and UnaryGate Classes.
"""
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
        if self.pinA == None:
            input_value = int(input("Enter Pin A input for gate " + str(self.getLabel()) + "--->"))
            input_value = 1 if input_value > 0 else 0
            return input_value
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            input_value = int(input("Enter Pin B input for gate " + str(self.getLabel()) + "--->"))
            input_value = 1 if input_value > 0 else 0
            return input_value
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class UnaryGate(LogicGate):

    def __init__(self, n):
        super().__init__(n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            input_value = int(input("Enter Pin input for gate " + str(self.getLabel()) + "--->"))
            input_value = 1 if input_value > 0 else 0
            return input_value
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if self.pinA == None and self.pinB == None:
            a = self.getPinA()
            b = self.getPinB()
        else:
            a = self.pinA
            b = self.pinB

        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        if self.pinA == None and self.pinB == None:
            a = self.getPinA()
            b = self.getPinB()
        else:
            a = self.pinA
            b = self.pinB

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

"""
Connector is used to connect two Logic Gates
"""
class Connector(object):
    """docstring for Connector."""

    def __init__(self, fgate, tgate):
        super(Connector, self).__init__()
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

"""
Other types of Gates can be
constructed by combining existing gates
"""
class NOrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
        self.orGate = OrGate("Or")
        self.notGate = NotGate("Not")
        self.connector = Connector(self.orGate, self.notGate)

    def performGateLogic(self):
        return self.notGate.getOutput()

class NAndGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
        self.andGate = AndGate("And")
        self.notGate = NotGate("Not")
        self.connector = Connector(self.andGate, self.notGate)

    def performGateLogic(self):
        return self.notGate.getOutput()

class XOrGate(BinaryGate):
    def __init__(self, n):
        super().__init__(n)
        self.nandGate = NAndGate("NAnd")
        self.orGate = OrGate("Or")
        self.andGate = AndGate("And")
        self.connector1 = Connector(self.nandGate, self.andGate)
        self.connector2 = Connector(self.orGate, self.andGate)

    def getPinA(self):
        input_value = int(input("Enter Pin A input for gate " + str(self.getLabel()) + "--->"))
        input_value = 1 if input_value > 0 else 0
        return input_value

    def getPinB(self):
        input_value = int(input("Enter Pin B input for gate " + str(self.getLabel()) + "--->"))
        input_value = 1 if input_value > 0 else 0
        return input_value

    def performGateLogic(self):
        a = self.getPinA()
        b = self.getPinB()
        self.nandGate.pinA = a
        self.nandGate.pinB = b
        self.orGate.pinA = b
        self.orGate.pinB = a

        # print(self.andGate.pinA.getFrom().getOutput())
        return self.andGate.getOutput()


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
g5 = NOrGate("G5")
g6 = XOrGate("G6")
g7 = NAndGate("G7")
# c1 = Connector(g1, g3)
# c2 = Connector(g2, g3)
# c3 = Connector(g3, g4)
print(g6.getOutput())
# print(g1.getOutput())
# print(g2.getOutput())
# print(g3.getOutput())
