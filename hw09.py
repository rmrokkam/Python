def total_hours(fname, employee):
    '''
    Purpose: Determines the total number of hours a single employee has
        worked from looking at the hours reported in the selected file.
    Input Parameter(s):
        fname: name of file countaining the employee total_hours
        employee: name of the employee selected to see their total amount
            of hours worked.
    Return Value: The total amount of hours an employee reported within the
        selected file. If the employee has multiple amount of hours reported
        then the program should return the sum of all the hours the employee
        reported. If the employee selected has no hours reported then the
        program should return 0 for the number of hours reported. If fname
        does not exist then the return value should be -1.
    '''
    try:
        fp = open(fname)
        hours = 0
        for line in fp:
            line_split = line.split(',')
            if line_split[0] == employee:
                hours += int(line_split[1])
        fp.close()
        return hours
    except FileNotFoundError:
        return -1

def add_docstring(fname):
    '''
    Purpose: Creates a new file that is titled the fname with 'doctring_'
        attached to the beginning of it. The new file is a copy of fname
        but adds a docstring to the beginning of all the functions within
        the copy.
    Input Parameter(s):
        fname: the name of the file wanted to be copied.
    Return Value: The total amount of functions within the new file. If
        fname does not exist then the return value is -1.
    '''
    try:
        fname_new = 'docstring_'+fname
        fp = open(fname, 'r')
        f = open(fname_new, 'w')
        docstring = "    '''\n    Purpose: FILL ME IN\n    Input Parameters: FILL ME IN\n    Return Value: FILL ME IN\n    '''\n"
        total_functions = 0
        for line in fp:
            line_split = line.split(' ')
            f.write(line)
            if line_split[0] == 'def':
                f.write(docstring)
                total_functions += 1
        return total_functions
    except FileNotFoundError:
        return -1

def widen_model(fname_in, fname_out):
    '''
    Purpose: Creates a copy of a selected OBJ 3D model and widens the
        x-values of each vertex within the copy by multiplying the x-values
        by 2.
    Input Parameter(s):
        fname_in: selected OBJ 3D model wanted to be copied and widened within
            said copy.
        fname_out: the new copied and widened OBJ 3D model version of the
            originally selected OBJ 3D model.
    Return Value: The total amount of x_values, within each vertex, widened.
        If fname_in does not exist then the return value is -1.
    '''
    try:
        f_in = open(fname_in, 'r')
        f_out = open(fname_out, 'w')
        total_widened = 0
        for line in f_in:
            line_split = line.split(' ')
            if line_split[0] == 'v':
                line_split[1] = str(2 * float(line_split[1]))
                line_join = ' '.join(line_split)
                total_widened += 1
                f_out.write(line_join)
            elif line_split[0] == 'f':
                f_out.write(line)
        return total_widened
    except FileNotFoundError:
        return -1
