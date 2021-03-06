"""CPU functionality."""

import sys

ADD = 0b10100000
LDI = 0b10000010
PRN = 0b01000111
HLT = 0b00000001
MUL = 0b10100010
PUSH = 0b01000101
POP = 0b01000110
CALL = 0b01010000
RET = 0b00010001
CMP = 0b10100111
JMP = 0b01010100
JEQ = 0b01010101
JNE = 0b01010110
AND = 0b10101000
OR = 0b10101010
XOR = 0b10101011
NOT = 0b01101001

sp = 7

class CPU:
    """Main CPU class."""


    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0] * 256
        self.reg = [0] * 8
        self.pc = 0
        self.reg[sp] = 0xF4
        self.FL = 0b00000000
        # FLAG = 0b00000LGE
        # need to set up functionality needs

    def ram_read(self, ram_address):
        ram_value = self.ram[ram_address]
        return ram_value

    def ram_write(self, ram_value, ram_address):
        self.ram[ram_address] = ram_value

    def load(self):
        """Load a program into memory."""

        address = 0

        with open(sys.argv[1]) as f:
            for line in f:
                l_value = line.split("#")[0].strip()
                if l_value == '':
                    continue
                val = int(l_value, 2)
                self.ram[address] = val
                address += 1
            #     print(line)
            # exit(1)


        # Removing the hardcoded program
        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        # for instruction in program:
        #     self.ram[address] = instruction
        #     address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == ADD:
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc
        elif op == MUL:
            self.reg[reg_a] *= self.reg[reg_b]
        elif op == CMP:
            self.FL = 0b00000000
            # FLAG = 0b00000LGE
            if self.reg[reg_a] == self.reg[reg_b]:
                self.FL = 0b00000001
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.FL = 0b00000100
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.FL = 0b00000010
        elif op == AND:
            self.reg[reg_a] = self.reg[reg_a] & self.reg[reg_b]
        elif op == OR:
            self.reg[reg_a] = self.reg[reg_a] | self.reg[reg_b]
        elif op == NOT:
            self.reg[reg_a] = ~ self.reg[reg_a]
        elif op == XOR:
            self.reg[reg_a] = self.reg[reg_a] ^ self.reg[reg_b]
        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""
        running = True

        while running:
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc + 1)
            operand_b = self.ram_read(self.pc + 2)
            # print()
            # print(f'Reg 0: {self.reg[0]}')
            # print(f'Reg 1: {self.reg[1]}')
            # print(f'Reg 2: {self.reg[2]}')
            # print(f'FLAG: {self.FL}')
            # print()
            # print(ir) 

            if ir == LDI:
                self.reg[operand_a] = operand_b

            elif ir == PRN:
                print_item = self.ram[self.pc + 1]
                print(self.reg[print_item])

            elif ir == HLT:
                running = False
            
            elif ir == ADD:
                self.alu(ir, operand_a, operand_b)
            
            elif ir == MUL:
                self.alu(ir, operand_a, operand_b)

            elif ir == CMP:
                self.alu(ir, operand_a, operand_b)

            elif ir == PUSH:
                self.reg[sp] -= 1
                self.ram[self.reg[sp]] = self.reg[operand_a]
            
            elif ir == POP:
                self.reg[operand_a] = self.ram[self.reg[sp]]
                self.reg[sp] += 1

            elif ir == CALL:
                self.reg[sp] -= 1
                jump_point = self.pc + (ir >> 6) + 1
                self.ram[self.reg[sp]] = jump_point
                self.pc = self.reg[operand_a]
                continue
                
            elif ir == RET:
                ret_value = self.ram[self.reg[sp]]
                self.pc = ret_value
                self.reg[sp] += 1
                continue
            
            elif ir == JMP:
                self.pc = self.reg[operand_a]
                continue

            elif ir == JEQ:
                if self.FL == 1:
                    self.pc = self.reg[operand_a]
                    continue


            elif ir == JNE:
                if self.FL & 0b00000001 == 0:
                    self.pc = self.reg[operand_a]
                    continue
            
            elif ir == AND:
                self.alu(ir, operand_a, operand_b)
            
            elif ir == OR:
                self.alu(ir, operand_a, operand_b)
            
            elif ir == XOR:
                self.alu(ir, operand_a, operand_b)
            
            elif ir == NOT:
                self.alu(ir, operand_a, operand_b)
            
            else:
                print('Not working')
                running = False
            
            self.pc += (ir >> 6) + 1 

