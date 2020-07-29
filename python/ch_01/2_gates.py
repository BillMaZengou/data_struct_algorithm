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

    def __init__(self, n, gate=None):
        super().__init__(n)
        self.pinA = None
        self.pinB = None
        self.gate = gate

    def getPinA(self):
        if self.gate is not None:
            self.pinA = self.gate.pinA
        else:
            if self.pinA == None:
                input_value = int(input("Enter Pin A input for gate " + str(self.getLabel()) + "--->"))
                input_value = 1 if input_value > 0 else 0
                self.pinA = input_value
            else:
                self.pinA = self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.gate is not None:
            self.pinB = self.gate.pinB
        else:
            if self.pinB == None:
                input_value = int(input("Enter Pin B input for gate " + str(self.getLabel()) + "--->"))
                input_value = 1 if input_value > 0 else 0
                self.pinB = input_value
            else:
                self.pinB = self.pinB.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
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
            self.pin = input_value
        else:
            self.pin = self.pin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            raise RuntimeError("Error: NO EMPTY PINS")

class AndGate(BinaryGate):
    def __init__(self, n, gate=None):
        super().__init__(n, gate)

    def performGateLogic(self):
        self.getPinA()
        self.getPinB()

        if self.pinA == 1 and self.pinB == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self, n, gate=None):
        super().__init__(n, gate)

    def performGateLogic(self):
        self.getPinA()
        self.getPinB()

        if self.pinA == 1 or self.pinB == 1:
            return 1
        else:
            return 0

class NotGate(UnaryGate):
    def __init__(self, n):
        super().__init__(n)

    def performGateLogic(self):
        self.getPin()
        result = 0 if self.pin == 1 else 1
        return result

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
    def __init__(self, n, gate=None):
        super().__init__(n, gate)
        self.orGate = OrGate(n)
        self.notGate = NotGate(n)
        self.connector = Connector(self.orGate, self.notGate)

    def performGateLogic(self):
        result = self.notGate.getOutput()
        self.pinA = self.orGate.pinA
        self.pinB = self.orGate.pinB
        return result

class NAndGate(BinaryGate):
    def __init__(self, n, gate=None):
        super().__init__(n, gate)
        self.andGate = AndGate(n)
        self.notGate = NotGate(n)
        self.connector = Connector(self.andGate, self.notGate)

    def performGateLogic(self):
        result = self.notGate.getOutput()
        self.pinA = self.andGate.pinA
        self.pinB = self.andGate.pinB
        return result

class XOrGate(BinaryGate):
    def __init__(self, n, gate=None):
        super().__init__(n, gate)
        self.nandGate = NAndGate(n)
        self.orGate = OrGate(n, self.nandGate)
        self.andGate = AndGate(n)
        self.connector1 = Connector(self.nandGate, self.andGate)
        self.connector2 = Connector(self.orGate, self.andGate)

    def performGateLogic(self):
        result = self.andGate.getOutput()
        self.pinA = self.nandGate.pinA
        self.pinB = self.nandGate.pinB
        return result


g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
g5 = NOrGate("G5")
g6 = NAndGate("G6")
g7 = XOrGate("G7")
# print(g7.getOutput())

"""
Half-Adder
"""
class HalfAdder(BinaryGate):
    """docstring for HalfAdder."""

    def __init__(self, n, gate=None):
        super().__init__(n, gate)
        self.xor = XOrGate(n)
        self.an = AndGate(n, self.xor)

    def performGateLogic(self):
        s = self.xor.getOutput()
        c = self.an.getOutput()
        self.pinA = self.xor.pinA
        self.pinB = self.xor.pinB
        return c, s

a1 = HalfAdder("ADDER")
print(a1.getOutput())

# TODO: Finish the full-adder
"""
Full-Adder
"""
class FullAdder(LogicGate):
    def __init__(self, n, gate=None):
        super().__init__(n, gate)
        self.pinA = None
        self.pinB = None
        self.pinCin = None
        self.gate = gate

        self.half1 = HalfAdder(n)
        self.half2 = HalfAdder(n)

    def getPinA(self):
        if self.gate is not None:
            self.pinA = self.gate.pinA
        else:
            if self.pinA == None:
                input_value = int(input("Enter Pin A input for gate " + str(self.getLabel()) + "--->"))
                input_value = 1 if input_value > 0 else 0
                self.pinA = input_value
            else:
                self.pinA = self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.gate is not None:
            self.pinB = self.gate.pinB
        else:
            if self.pinB == None:
                input_value = int(input("Enter Pin B input for gate " + str(self.getLabel()) + "--->"))
                input_value = 1 if input_value > 0 else 0
                self.pinB = input_value
            else:
                self.pinB = self.pinB.getFrom().getOutput()

    def getPinC(self):
        if self.gate is not None:
            """ NOTE: The connect pin is pinA """
            self.pinCin = self.gate.pinA
        else:
            if self.pinCin == None:
                input_value = int(input("Enter Pin B input for gate " + str(self.getLabel()) + "--->"))
                input_value = 1 if input_value > 0 else 0
                self.pinCin = input_value
            else:
                self.pinCin = self.pinCin.getFrom().getOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")
