electrons = int(input())

shells = []
counter = 0
while electrons > 0:
    counter += 1
    electron_per_shell = 2 * counter ** 2

    if electron_per_shell > electrons:
        electron_per_shell = electrons

    electrons -= electron_per_shell
    shells.append(electron_per_shell)

print(shells)
