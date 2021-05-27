#!/usr/bin/python3
import sys
from miasm.analysis.binary import Container
from miasm.analysis.machine import Machine
from miasm.core.locationdb import LocationDB
from miasm.expression.expression import ExprId, ExprInt
from miasm.ir.symbexec import SymbolicExecutionEngine
from msynth import Simplifier

# check arguments
if len(sys.argv) != 2:
    print(f"[*] Syntax: {sys.argv[0]} <address>")
    exit()

# parse and set arguments
file_path = "./samples/finspy"
oracle_path = "./oracle.pickle"
start_addr = int(sys.argv[1], 16)

# set of addresses to exit SE
ADDRESSES_DISPATCHER_JOIN = set([0x412c6b, 0x40514b, 0x40978f])

# MBA simplifier
simplifier = Simplifier(oracle_path, enforce_equivalence=True)

# symbol table
loc_db = LocationDB()

# open the binary for analysis
container = Container.from_stream(open(file_path, 'rb'), loc_db)

# cpu abstraction
machine = Machine(container.arch)

# init disassemble engine
mdis = machine.dis_engine(container.bin_stream, loc_db=loc_db)

# initialize lifter to intermediate representation
lifter = machine.lifter_model_call(mdis.loc_db)

# disassemble the function at address
asm_cfg = mdis.dis_multiblock(start_addr)

# translate asm_cfg into ira_cfg
ira_cfg = lifter.new_ircfg_from_asmcfg(asm_cfg)

# init SE engine
sb = SymbolicExecutionEngine(lifter)

# init worklist for automatic symbolic exploration
worklist = [ExprInt(start_addr, 64)]

# automatic symbolic exploration
while len(worklist) != 0:
    # current basic block
    current_block = worklist.pop(0)

    # exit if next block is unknown
    if current_block.is_int() and int(current_block) in ADDRESSES_DISPATCHER_JOIN:
        break

    print(f"current block: {current_block}")

    # symbolically execute basic block
    next_block = sb.run_block_at(ira_cfg, current_block)

    # simplify next block
    next_block = simplifier.simplify(next_block)
    print(f"next block: {next_block}")

    # if next basic block is clear, add to worklist
    if next_block.is_int() or next_block.is_loc():
        worklist.append(next_block)

# dump SE state
print("Dumping SE state:")
for k, v in sb.modified():
    simplified = simplifier.simplify(v)
    print("\n\n")
    if v == simplified:
        print(f"{k} = {v} (unmodified)")    
    else:
        print(f"{k} = {v} (original)")
        print(f"{k} = {simplifier.simplify(v)} (simplified)")
