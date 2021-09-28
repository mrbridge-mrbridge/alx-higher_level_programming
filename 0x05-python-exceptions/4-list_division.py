#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new = []
    for i in range(list_length):
        try:
            n = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError):
            n = 0
        except TypeError:
            print('wrong type')
        except ZeroDivisionError:
            print('division by 0')
        except IndexError:
            print('out of range')
        finally:
            new.append(n)
    return new


