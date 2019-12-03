# Advent of Code day 2
input = [1, 12, 2, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 10, 1, 19, 2, 9, 19, 23, 2, 13, 23, 27, 1, 6, 27, 31, 2, 6, 31, 35, 2, 13, 35, 39, 1, 39, 10, 43, 2, 43, 13, 47, 1, 9, 47, 51, 1, 51, 13, 55, 1, 55, 13, 59, 2,
         59, 13, 63, 1, 63, 6, 67, 2, 6, 67, 71, 1, 5, 71, 75, 2, 6, 75, 79, 1, 5, 79, 83, 2, 83, 6, 87, 1, 5, 87, 91, 1, 6, 91, 95, 2, 95, 6, 99, 1, 5, 99, 103, 1, 6, 103, 107, 1, 107, 2, 111, 1, 111, 5, 0, 99, 2, 14, 0, 0]

pos = 0
output = 0
noun = 0
verb = 0
day1answer = 0

while output != 19690720:
    inputCopy = input.copy()

    inputCopy[1] = noun
    inputCopy[2] = verb

    while inputCopy[pos] != 99:
        opcode1 = inputCopy[pos]
        if opcode1 == 99:
            break
        opcode2 = inputCopy[pos+1]
        opcode3 = inputCopy[pos+2]
        opcode4 = inputCopy[pos+3]

        if opcode1 == 1:
            inputCopy[opcode4] = inputCopy[opcode2] + inputCopy[opcode3]

        if opcode1 == 2:
            inputCopy[opcode4] = inputCopy[opcode2] * inputCopy[opcode3]

        pos = pos+4

    output = inputCopy[0]
    if output == 19690720:
        break

    if noun == 12 and verb == 2:
        day1answer = output

    pos = 0

    verb += 1
    if verb == 100:
        noun += 1
        verb = 0

    if noun == 100:
        print("Program failed.")
        break

print("output: " + str(output))
print("noun: " + str(noun))
print("verb: " + str(verb))
print("Day 1 Answer: " + str(day1answer))
print("Day 2 Answer: " + str(100 * noun + verb))
