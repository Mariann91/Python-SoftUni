def numbers_searching(*args):
    start = min(args)
    end = max(args)

    missing_number = 0
    duplicates = []

    for num in range(start, end + 1):

        if num not in args:
            missing_number = num

        if args.count(num) > 1 and num not in duplicates:
            duplicates.append(num)

    return [missing_number, sorted(duplicates)]
