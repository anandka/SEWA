import fileinput
import sys
import os
import config

def modify_config(variable, new_value):
    """
    Modify Config file variable with new values
    """
    config_file = os.path.dirname(os.path.realpath(__file__)) + "/config.py"
    variable_found = False
    variable_already_set = False
    variable = str(variable)
    new_value = str(new_value)
    #use quotes if setting has spaces #
    if ' ' in new_value:
        new_value = '"%s"' % new_value

    for line in fileinput.input(config_file, inplace = 1):
        # process lines that look like config settings #
        if not line.lstrip(' ').startswith('#') and '=' in line:
            _infile_var = str(line.split('=')[0].rstrip(' '))
            _infile_set = str(line.split('=')[1].lstrip(' ').rstrip())
            # only change the first matching occurrence #
            if variable_found == False and _infile_var.rstrip(' ') == variable:
                variable_found = True
                # don't change it if it is already set #
                if _infile_set.lstrip(' ') == new_value:
                    variable_already_set = True
                else:
                    #line = "%s = %s\n" % (variable, new_value)
                    line = variable+ " = '" + new_value + "'"

        sys.stdout.write(line)


    # Append the variable if it wasn't found #
    if not variable_found:
        with open(config_file, "a") as f:
            f.write("%s = %s\n" % (variable, new_value))
    return

def settings_modification(migration_folder):
    modify_config("MIGRATION_FOLDER", migration_folder)

if __name__ == "__main__":
    total = len(sys.argv)
    if total == 2:
        migration_folder = sys.argv[1]
        settings_modification(migration_folder)
    else:
        print "Give correct input -> setup.py <migration folder path>"