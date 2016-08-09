while True:
    try:
        x = int(input('Please put the number:'))
        break
    except (TypeError, NameError, ValueError):
        print("This is not valid number")
    except NameError:

     print('once more!')
