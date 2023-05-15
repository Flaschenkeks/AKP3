# def xor(list):
#

seedA = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]  # 1FFFF
seedB = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


def a1a(start, cycles):
    output = []
    register_state = start.copy()
    for x in range(cycles):
        feedbackloop = (register_state[16] + register_state[5]) % 2
        output.append(register_state[16])
        for x in range(16, 0, -1):
            register_state[x] = register_state[x - 1]
        register_state[0] = feedbackloop
        # print(f"cycle {x} register state: {register_state}")
    return output


def lfsr(seed, cycles):
    register_state = seed.copy()
    for x in range(cycles):
        feedbackloop = (register_state[16] + register_state[5]) % 2
        # output.append(register_state[16])
        for x in range(16, 0, -1):
            register_state[x] = register_state[x - 1]
        register_state[0] = feedbackloop
        # print(f"cycle {x} register state: {register_state}")
    return register_state


def lfsr_period_check(seed):
    b = True
    start_state = seed.copy()
    print(f"Start Registerzustand: {start_state}")
    register_state = lfsr(seed, 1)
    cycles = 1
    print(f"Zyklus {cycles} Registerzustand: {register_state}")

    while register_state != start_state:
        register_state = lfsr(register_state, 1)
        cycles += 1
        print(f"Zyklus {cycles} Registerzustand: {register_state}")


output = a1a(seedA, 64)
print(output)

dumbstr = ''
for x in range(len(output)):
    dumbstr += str(output[x])
print(dumbstr)
#
# print(lfsr_period_check(seedB))

lfsr_period_check(seedB)

#  A2:
#  Zyklus 131071 Registerzustand: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
