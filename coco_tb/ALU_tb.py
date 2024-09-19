import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, ReadOnly, Timer

async def try_addition(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 5
    dut.B.value = -7
    c_exp = -2 & 0xFF
    dut.Opcode.value = 0
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The addition process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The addition process failed with C: " +                       str(dut.C.value))
        
async def try_subtraction(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 3
    dut.B.value = -4
    c_exp = 7 & 0xFF
    dut.Opcode.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The subtraction process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The subtraction process failed with C: " +                       str(dut.C.value))
        
async def try_multiplication(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 5
    dut.B.value = -2
    c_exp = -10 & 0xFF
    dut.Opcode.value = 2
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The multiplication process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The multiplication process failed with C: " +                       str(dut.C.value))
        
async def try_division(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 6
    dut.B.value = -3
    c_exp = -2 & 0xFF
    dut.Opcode.value = 3
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The division process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The division process failed with C: " +                       str(dut.C.value))

@cocotb.test()
async def tb_top(dut):
    cocotb.log.info("STARTING SIMULATION")
    CLK = Clock(dut.clk, 10, units="ns")
    dut.reset.value = 0 
    await cocotb.start(CLK.start())
    await Timer(20, units="ns")
    await cocotb.start_soon(try_addition(dut))
    cocotb.log.info("After try_addition")
    await cocotb.start_soon(try_subtraction(dut))
    cocotb.log.info("After try_subtraction")
    await cocotb.start_soon(try_multiplication(dut))
    cocotb.log.info("After try_multiplication")
    await cocotb.start_soon(try_division(dut))
    cocotb.log.info("After try_division")

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge, RisingEdge, ReadOnly, Timer

async def try_addition(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 5
    dut.B.value = -7
    c_exp = -2 & 0xFF
    dut.Opcode.value = 0
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The addition process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The addition process failed with C: " +                       str(dut.C.value))
        
async def try_subtraction(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 3
    dut.B.value = -4
    c_exp = 7 & 0xFF
    dut.Opcode.value = 1
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The subtraction process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The subtraction process failed with C: " +                       str(dut.C.value))
        
async def try_multiplication(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 5
    dut.B.value = -2
    c_exp = -10 & 0xFF
    dut.Opcode.value = 2
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The multiplication process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The multiplication process failed with C: " +                       str(dut.C.value))
        
async def try_division(dut):
    await FallingEdge(dut.clk)
    dut.reset.value = 1 
    dut.A.value = 6
    dut.B.value = -3
    c_exp = -2 & 0xFF
    dut.Opcode.value = 3
    await RisingEdge(dut.clk)
    await ReadOnly()
    if dut.C.value == c_exp: 
        cocotb.log.info("The division process passed with C: " +                       str(dut.C.value))
    else: 
        cocotb.log.info("The division process failed with C: " +                       str(dut.C.value))

@cocotb.test()
async def tb_top(dut):
    cocotb.log.info("STARTING SIMULATION")
    CLK = Clock(dut.clk, 10, units="ns")
    dut.reset.value = 0 
    await cocotb.start(CLK.start())
    await Timer(20, units="ns")
    await cocotb.start_soon(try_addition(dut))
    cocotb.log.info("After try_addition")
    await cocotb.start_soon(try_subtraction(dut))
    cocotb.log.info("After try_subtraction")
    await cocotb.start_soon(try_multiplication(dut))
    cocotb.log.info("After try_multiplication")
    await cocotb.start_soon(try_division(dut))
    cocotb.log.info("After try_division")
    cocotb.log.info("ENDING SIMULATION")

