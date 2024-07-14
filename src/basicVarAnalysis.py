# TODO:
# - use BASIC code variable parsing to identify variables that are not yet initialized
# - more custom row/col testing
# - identify more sword of fargoal variables

import math
import re
from dataclasses import dataclass, field

FLOAT_TYPE = 0
STR_TYPE = 1
FN_TYPE = 2  # not used
INT_TYPE = 3

INDENT = " " * 3


@dataclass
class VarRefsForLineNumber():
    """
    A class that holds a BASIC line number, and the variables that were read
    and/or modified on that line.
    """    
    line_num: int = 0
    vars_read: list[str] = field(default_factory=list)
    vars_mod: list[str] = field(default_factory=list)


@dataclass
class LineNumbersForVarRefs():
    """
    A class that holds a BASIC variable name, and the BASIC line number where
    that variable was read and/or modified.  These instances are created as a
    pivot from VarRefsForLineNumber instances.
    """
    var_name: str = ""
    read_lines: list[int] = field(default_factory=list)
    mod_lines: list[int] = field(default_factory=list)


@dataclass
class VarFormatting():
    """
    A class that holds display formatting options for a BASIC variable.

    Attribute:
        width (int): The minimum width of the variable value display, 0 = no padding
        row (int):  Specifies the BASIC array dimension index to display as a row
                    -1 == default, None is no row display, int is the dimension index
        col (int):  Same as row, but for column.
        comment (str):  Free text comment string or None
    """
    width: int = 0 
    row: int = -1
    col: int = -1
    comment: str = None


class BasicV2Entry:
    """
    A class that holds data for a V2 BASIC variable.

    Attributes:
        name (str):  Name of basic variable (e.g., X, A$, CD%, etc.)
        type (int):  Type of variable (FLOAT_TYPE, STR_TYPE, or INT_TYPE)
        value:  Variable's value in memory capture.  Scalar of type, or if
                an array, then a dict with values of type.
        dim_sizes:  If array, an ordered list of dimension cardinalities
    """
    def __init__(self, name, type, value, dim_sizes = None):
        self.name = name
        self.type = type
        self.value = value
        self.dim_sizes = dim_sizes

    def is_array(self):
        return self.dim_sizes is not None and len(self.dim_sizes) > 0

    def __lt__(self, other):
        return self.name < other.name


class MemoryDump:
    """
    A class that loads, processes, and stores a memory dump for BASIC variable analysis.

    Attributes:
        system (str):  'C64', 'VIC20', 'VIC20+3K', 'VIC20+8K+', 'PETROM1.0' or
                       'PETROM2.0+'  
    """
    def __init__(self, system):
        '''
        VIC-20 RAM:
            $0000-$03FF: 1K
            $1000-$1FFF: 4K
            $2000-$3FFF: 8K expansion block 1
            $4000-$5FFF: 8K expansion block 2
            $6000-$7FFF: 8K expansion block 3  

        http://www.6502.org/users/andre/petindex/progmod.html
        PET RAM:
            $0000-$0FFF or up to $7FFF, depending on model
            $8000-$8FFF: Screen memory            
        '''

        # values that describe the BASIC RAM layout in the memory dump
        self.TXTTAB_val = self.VARTAB_val = self.ARYTAB_val = self.STREND_val \
            = self.FRETOP_val = self.MEMSIZ_val = self.CURLIN_val = self.OLDLIN_val \
            = self.TXTTAB_default = self.data = self.system = None

        # collections of discovered variables
        self.floats = []; self.integers = []; self.strings = []
        self.float_arrays = []; self.integer_arrays = []; self.string_arrays = []
        self.var_display_formats = {}; self.refs_for_line_nums = {}
        self.line_nums_for_refs = {}       

        self.systems = ['C64', 'VIC20', 'VIC20+3K', 'VIC20+8K+', 'PETROM1.0',
                       'PETROM4.0']

        if system not in self.systems:
            exit('Error: unrecognized system "%s"' % system)
        self.system = system

        if system == 'C64' or system.startswith('VIC20'):
            self.TXTTAB = 0x002b  # Pointer to start of BASIC
            self.VARTAB = 0x002d  # Pointer to start of variables (right after BASIC)
            self.ARYTAB = 0x002f  # Pointer to start of arrays
            self.STREND = 0x0031  # Pointer to end of arrays (exclusive)
            self.FRETOP = 0x0033  # Pointer to bottom (end) of strings
            self.MEMSIZ = 0x0037  # Pointer to top (start) of strings (and BASIC RAM end)
            self.CURLIN = 0x0039  # Current BASIC line number (if program running)
            self.OLDLIN = 0x003b  # BASIC line number of last END or STOP executed
            if self.system == 'C64':
                self.TXTTAB_default = 0x801
            # https://techtinkering.com/articles/basic-line-storage-on-the-vic-20/
            elif self.system == 'VIC20':
                self.TXTTAB_default = 0x1001
            elif self.system == 'VIC20+3K':
                self.TXTTAB_default = 0x0401
            else:
                self.TXTTAB_default = 0x1201 # 'VIC20+8K+'
                
        elif system == 'PETROM4.0':
            self.TXTTAB = 0x0028
            self.VARTAB = 0x002a
            self.ARYTAB = 0x002c
            self.STREND = 0x002e
            self.FRETOP = 0x0030
            self.MEMSIZ = 0x0034
            self.CURLIN = 0x0036
            self.OLDLIN = 0x0038
            self.TXTTAB_default = 0x0401

        else:  # system == 'PETROM1.0'
            self.TXTTAB = 0x007a
            self.VARTAB = 0x007c
            self.ARYTAB = 0x007e
            self.STREND = 0x0080
            self.FRETOP = 0x0082
            self.MEMSIZ = 0x0086
            self.CURLIN = 0x0088
            self.OLDLIN = 0x008a
            self.TXTTAB_default = 0x0401    

    def find_vars(self, filename):
        """
            1) Loads the memory dump.
            2) Parses the RAM for variables.
            3) Parses the BASIC code for cross references of variable reads/modifications.
        """
        mem = self.load_mem_dump(filename)

        self.floats, self.integers, self.strings = self.parse_ram_for_vars()
        self.float_arrays, self.integer_arrays, self.string_arrays = self.parse_ram_for_arrays()
        
        self.refs_for_line_nums = self.parse_code_for_var_refs()

        # Pivot the line number / variable references index
        self.line_nums_for_refs = {}
        for ref in self.refs_for_line_nums.values():
            for var_read in ref.vars_read:
                if var_read in self.line_nums_for_refs:
                    self.line_nums_for_refs[var_read].read_lines.append(ref.line_num)
                else:
                    self.line_nums_for_refs[var_read] = LineNumbersForVarRefs(
                        var_read, [ref.line_num], [])
            for var_mod in ref.vars_mod:
                if var_mod in self.line_nums_for_refs:
                    self.line_nums_for_refs[var_mod].mod_lines.append(ref.line_num)
                else:
                    self.line_nums_for_refs[var_mod] = LineNumbersForVarRefs(
                        var_mod, [], [ref.line_num])

        return mem

    def load_mem_dump(self, filename):
        """
        Load the memory dump file and parse BASIC memory layout
        """
        print("reading %s..." % filename)
        with open(filename, 'rb') as f:
            self.data = f.read()
            if filename.lower().endswith(".prg"):
                self.data = data[2:]
            if self.data[0] + self.data[1] == 0:
                print("stripped off what looked like a load address")
                self.data = data[2:]

        (self.TXTTAB_val, self.VARTAB_val, self.ARYTAB_val, self.STREND_val, 
            self.FRETOP_val, self.MEMSIZ_val, self.CURLIN_val,self.OLDLIN_val) \
            = [self.data[addr] + self.data[addr+1]*256 for addr in
                (self.TXTTAB, self.VARTAB, self.ARYTAB, self.STREND, 
                self.FRETOP, self.MEMSIZ, self.CURLIN, self.OLDLIN)]

        if self.MEMSIZ_val < len(self.data):
            exit("Error: dump too small, please dump at least $0000 to $%04X"
                % (self.MEMSIZ_val - 1))

    def parse_name_and_type(self, bytes):
        """
        Convert bytes into variable name and type

        Parameters:
            bytes (bytes):  Two bytes that contain the variable name and type to be parsed
        
        Returns:
            var_name (str):  String representation of variable name
            var_type (int):  FLOAT_TYPE, STR_TYPE, or INT_TYPE
        """
        var_name = chr(bytes[0] & 0x7f) + chr(bytes[1] & 0x7f)
        var_type = ((bytes[0] & 128) >> 6) + ((bytes[1] & 128) >> 7)

        if var_name[1] == '\x00':  # if single-char var name
            var_name = var_name[0]
        if var_type == STR_TYPE:
            var_name += '$'
        elif var_type == INT_TYPE:
            var_name += '%'

        return var_name, var_type

    def parse_float(self, var_bytes):
        """
        Convert bytes into a float value (as string)

        Parameters:
            bytes (bytes):  The last 5 of the 7 bytes of raw variable data

        Returns:
            val_str (str):  Float representation (in exponential notation as needed)
        """        
        if var_bytes[0] == 0:
            val = 0
        else:
            # Used a formula from "Programming the Commodore 64: The Definitive Guide"
            # by Raeto Collin West.
            # P153 has a long equation to do the conversion, however, it doesn't work with
            # negatives.  The "(M1 AND 128)" would have to be shifted right by 7, but i'll use an
            # 'if' statement instead:
            if (var_bytes[1] & 128) == 0:
                val = 1
            else:
                val = -1
            val *= 2 ** (var_bytes[0] - 129)
            val *= (1 + ((var_bytes[1] & 127) + (var_bytes[2] + (var_bytes[3] +
                var_bytes[4] / 256) / 256) / 256) / 128)

        # Commodore-ish float formatting (frequently looks like an int)
        if val==0:
            val_str = "0"
        else:
            if (10**-38 < abs(val) < 0.01) or abs(val) >= 999999999.2: 
                val_str = "%E" % val
                val_str = re.sub('0+E', 'E', val_str)
                val_str = re.sub('\.E', 'E', val_str)
            else:
                neg = val < 0
                if neg:
                    val *= -1
                val_str = "%.9f" % val
                val_str = val_str.strip('0')
                val_str = re.sub('\.$', '', val_str)  
                if neg:
                    val_str = '-' + val_str
        return val_str

    def parse_string(self, var_bytes):
        """
        Convert bytes into a string value

        Parameters:
            bytes (bytes):  The last 5 of the 7 bytes of raw variable data

        Returns:
            val_str (str):  Variable's string value, prefaced with "c" if string
                            stored in BASIC code area, or "h" if stored in string heap.
        """
        start = var_bytes[1] + var_bytes[2]*256  # l.e. 
        end = start + var_bytes[0]
        val_str = '"%s"' % self.data[start:end].decode('latin-1')
        # add string location indicators
        if start < self.VARTAB_val:
            # if string in basic code area
            val_str = "c" + val_str
        else:
            # if string in string heap (grows downward)
            val_str = "h" + val_str
        return val_str

    def parse_integer(self, var_bytes):
        """
        Convert bytes into an integer value (as string)

        Parameters:
            bytes (bytes):  The last 5 of the 7 bytes of raw variable data

        Returns:
            val_str (str):  Variable's integer value.
        """        
        val = var_bytes[0]*256 + var_bytes[1]  # signed b.e.
        if val > 0x7fff:  # handle negative values
            val = -(val ^ 0xffff) - 1
        val_str = str(val)
        return val_str

    def parse_ram_for_vars(self):
        """
        Parse the 7-byte variable records stored immediately after the end of the BASIC code
        """
        if (self.ARYTAB_val - self.VARTAB_val) % 7 != 0:  # each variable descriptor is 7 bytes
            exit("Error: variables malformed")

        floats = []; integers = []; strings = []
        for i in range(self.VARTAB_val, self.ARYTAB_val, 7):
            var_name, var_type = self.parse_name_and_type(self.data[i:i+2])
            var_bytes = self.data[i+2:i+7]

            if var_type == FLOAT_TYPE:
                floats.append(BasicV2Entry(var_name, var_type, self.parse_float(var_bytes)))
            elif var_type == STR_TYPE:  
                if var_bytes[3] + var_bytes[4] != 0:
                    exit("Error: malformed string")
                strings.append(BasicV2Entry(var_name, var_type, self.parse_string(var_bytes)))
            elif var_type == INT_TYPE:  
                if var_bytes[2] + var_bytes[3] + var_bytes[4] != 0:
                    exit("Error: malformed integer")
                integers.append(BasicV2Entry(var_name, var_type, self.parse_integer(var_bytes)))

        floats.sort(); integers.sort(); strings.sort()

        return floats, integers, strings

    def parse_ram_for_arrays(self):
        """
        Parse the array records that follow the 7-byte variable records
        """
        float_arrays = []; integer_arrays = []; string_arrays = []

        i = self.ARYTAB_val
        while i < self.STREND_val:
            values = {}
            array_name, array_type = self.parse_name_and_type(self.data[i:i+2])
            struct_size = self.data[i+2] + self.data[i+3] * 256  # le
            num_dims = self.data[i+4]
            if not (0 < num_dims < 15):  # largest example: DIM A(0,0,0,0,0,0,0,0,0,0,0,0,0,0)
                exit("Error: malformed integer")
            payload_size = struct_size - 5 - 2 * num_dims                
            struct_start = i
            struct_end = struct_start + struct_size              
            i += 5

            dim_sizes = []
            dim_sizes_end = i + num_dims * 2
            while i < dim_sizes_end:
                # dimension sizes stored (in C64) in reverse order of how defined
                dim_sizes.insert(0, self.data[i] * 256 + self.data[i+1])  # be
                i += 2
            num_exp_entries = math.prod(dim_sizes)

            indexes = [0] * len(dim_sizes)
            while i < struct_end:
                if array_type == FLOAT_TYPE:
                    values[tuple(indexes)] = self.parse_float(self.data[i:i+5])
                    i += 5
                elif array_type == INT_TYPE:
                    values[tuple(indexes)] = self.parse_integer(self.data[i:i+2])
                    i += 2
                else:  # array_type == STRING_TYPE
                    values[tuple(indexes)] = self.parse_string(self.data[i:i+3])
                    i += 3

                # from p147 of the West book:  An array's data is "held in ascending
                # order of argument, with the lattermost arguments changing least
                # often.  For example, DIM A(1,2) stores its variables in the order
                # A(0,0) A(1,0) A(0,1) A(1,1) A(0,2) A(1,2)"
                for j in range(len(indexes)):
                    indexes[j] += 1
                    if indexes[j] < dim_sizes[j]:
                        break
                    indexes[j] = 0

            if len(values.keys()) != num_exp_entries:
                 exit("Error: malformed array")

            # Our array_name representation doesn't have parenthesis attached here
            entry = BasicV2Entry(array_name, array_type, values, dim_sizes)

            if array_type == FLOAT_TYPE:
                float_arrays.append(entry)
            elif array_type == INT_TYPE:
                integer_arrays.append(entry)
            else:
                string_arrays.append(entry)

        float_arrays.sort(); integer_arrays.sort(); string_arrays.sort()

        return float_arrays, integer_arrays, string_arrays

    def add_formatting(self,
        in_var_name, width = 0, col = -1, row = -1, comment = None):
        """
        Add display formatting to be used with a variable (if found in RAM)
        """        
        self.var_display_formats[in_var_name.upper()] = \
            VarFormatting(width = width, col = col, row = row, comment = comment)

    def get_formatting(self, name):
        """
        Get the formatting associated with a variable name
        """          
        if name in self.var_display_formats:
            return self.var_display_formats[name]
        return None

    def print_read_write_lines(self, variable):
        """
        For a given variable name, print the BASIC lines that read and modify that variable.
        """         
        name = variable.name
        if variable.is_array():
            name += '()'
        if name in self.line_nums_for_refs:
            read_lines = self.line_nums_for_refs[name].read_lines
            mod_lines = self.line_nums_for_refs[name].mod_lines
            if len(read_lines) > 0:
                print("read: %s" % ', '.join(str(l) for l in read_lines))
            if len(mod_lines) > 0:
                print("modified: %s" % ', '.join(str(l) for l in mod_lines))

    def print_scalar(self, variable):
        """
        Display a scalar variable
        """           
        formatting = self.get_formatting(variable.name)
        print("%s: %s" % (variable.name, variable.value))
        self.print_read_write_lines(variable)
        if formatting is not None and formatting.comment is not None:
            print("Comment: %s" % formatting.comment)        
        print()

    def print_array(self, variable):
        """
        Display an array variable
        """
        formatting = self.get_formatting(variable.name + '()')
        padding = 0
        if variable.type == STR_TYPE:
            row = col = None
        else:
            row = col = -1
        if formatting is not None:
            padding = formatting.width
            row = formatting.row
            col = formatting.col

        # handle default row/col settings.  Row will usually be rightmost index
        # if not specified, and if col,row (x/y) not specified, they will usually
        # be the rightmost and 2nd-to-rightmost respectively.
        if not (row is None and col is None):
            if len(variable.dim_sizes) == 1:
                if row == -1 and col >= 0:
                    row = None
                elif col == -1 and row >= 0:
                    col = None
                elif row == -1 and col == -1:
                    col = None
                elif row is not None and col is not None:
                    exit("Error: can't specify both a row and col on 1-dim array")
            if row is not None and row > 0 and row == col:
                exit("Error: can't specify row equal to col")

            rightmost_dim = len(variable.dim_sizes) - 1
            if row == -1:
                if col == -1 or col == rightmost_dim:
                    col = rightmost_dim
                    row = col - 1
                else:  # col is None or 0 <= col <= rightmost_dim-1
                    row = rightmost_dim
            if col == -1:  # row is None or row >= 0
                if row is None or row < rightmost_dim:
                    col = rightmost_dim
                else:
                    col = rightmost_dim-1

        # create dimension groupings based on row/col settings
        # If row and col both None, then no groupings
        iter_groups = {}  # sets aren't ordered, so using a keys-only dict as a set
        for indexes_key in variable.value.keys():
            ik = list(indexes_key)
            if row is not None:
                ik[row] = 'col 0-%d' % (variable.dim_sizes[row] - 1)
            if col is not None:
                ik[col] = 'row 0-%d' % (variable.dim_sizes[col] - 1)
            iter_groups[tuple(ik)] = None
        iter_groups = [list(x) for x in iter_groups]

        for i, indexes_key in enumerate(iter_groups):
            key = indexes_key[:]
            if row is not None:  # if organized by row
                print("%s(%s) = " % (variable.name, ', '.join([str(x) for x in indexes_key])), end='')
                if col is not None:  # if also organized by col
                    print()
                    for c in range(variable.dim_sizes[col]):
                        key[col]=c
                        print("%s" % INDENT, end='')
                        for r in range(variable.dim_sizes[row]):
                            key[row]=r
                            value = variable.value[tuple(key)]
                            if r < variable.dim_sizes[row]-1:
                                end = ', '
                            else:
                                end = ''
                            print("%s" % str(value).rjust(padding), end=end)
                        print()
                else: # if organized by row but not col
                    for r in range(variable.dim_sizes[row]):
                        key[row]=r
                        value = variable.value[tuple(key)]
                        if r < variable.dim_sizes[row]-1:
                            end = ', '
                        else:
                            end = ''                        
                        print("%s" % str(value).rjust(padding), end=end)
                    print()              
            elif col is not None:  # if organized by col but not row
                print("%s(%s) = " % (variable.name, ', '.join([str(x) for x in indexes_key])), end='')
                print()
                for c in range(variable.dim_sizes[col]):
                    key[col]=c
                    value = variable.value[tuple(key)]
                    print("%s%s" % (INDENT, str(value).rjust(padding)))
            else: # if not organized by row or col
                if i == 0:
                    print("%s(%s) = " % (variable.name, ', '.join([str(x) for x in variable.dim_sizes])))
                print("%s%s(%s) = %s" %
                    (INDENT, variable.name, ', '.join([str(x) for x in indexes_key]),
                    variable.value[tuple(key)].rjust(padding)))

        self.print_read_write_lines(variable)
        if formatting is not None and formatting.comment is not None:
            print("Comment: %s" % formatting.comment)
        print()

    def _print_mem_loc_info(self, loc, default, text):
        if self.data[loc] != default:
            print("- PEEK(%d)==%d, %s (%d to restore)" 
                % (loc, self.data[loc], text, default))

    def print_basic_ranges(self):
        """
        Display info about memory dump and BASIC RAM layout
        """ 
        print("\nparsing vars from memory dump...")
        print("- %d bytes (assuming $0000 to $%04X)" % (len(self.data), len(self.data) - 1))

        print("- BASIC line number: ", end='')
        if self.data[self.CURLIN+1] == 255:
            print("none (in immediate mode)")
        else:
            print("%d" % (self.data[self.CURLIN] + self.data[self.CURLIN+1] * 256))
        print("- BASIC line number on last exit: %d" %
            (self.data[self.OLDLIN] + self.data[self.OLDLIN+1] * 256))

        if self.system == 'C64':
            self._print_mem_loc_info(774, 26, "so LISTing may be disabled")
            self._print_mem_loc_info(775, 167, "so LISTing may be disabled")
            self._print_mem_loc_info(792, 71, "so RESTORE key may be disabled")
            self._print_mem_loc_info(793, 254, "so RESTORE key may be disabled")
            self._print_mem_loc_info(808, 237, "so RUN/STOP key and/or LISTing may be disabled")
            self._print_mem_loc_info(809, 246, "so RUN/STOP key and/or LISTing may be disabled")
        elif self.system.startswith('VIC20'):
            self._print_mem_loc_info(808, 112, "so RUN/STOP key and/or LISTing may be disabled")
            # TODO: more could go here
        elif self.system.startswith('PET'):
            pass # TODO: more could go here

        print("\nBASIC ranges:")
        print("-------------")
        print("TXTTAB $%04X/%d: start of BASIC (default $%04X/%d), %d-byte extent" %
            (self.TXTTAB_val, self.TXTTAB_val, self.TXTTAB_default, self.TXTTAB_default, 
            self.VARTAB_val - self.TXTTAB_val + 1))
        print("VARTAB $%04X/%d: start of variables, %d-byte extent" %
            (self.VARTAB_val, self.VARTAB_val, self.ARYTAB_val - self.VARTAB_val))
        print("ARYTAB $%04X/%d: start of arrays, %d-byte extent" %
            (self.ARYTAB_val, self.ARYTAB_val, self.STREND_val - self.ARYTAB_val))
        print("STREND $%04X/%d: end of arrays (exclusive)" % (self.STREND_val, self.STREND_val))
        print("FRETOP $%04X/%d: end (bottom) of string heap, %d-byte extent" %
            (self.FRETOP_val, self.FRETOP_val, self.MEMSIZ_val - self.FRETOP_val))
        print("MEMSIZ $%04X/%d: start (top) of string heap + 1" % (self.MEMSIZ_val, self.MEMSIZ_val))

    def print_variables(self):
        """
        Print up to 6 collections of variable types
        """         
        if len(self.floats) > 0:
            print("\nfloats:")
            print("-------")
            for entry in self.floats:
                self.print_scalar(entry)
        
        if len(self.integers) > 0:
            print("\nintegers:")
            print("---------")
            for entry in self.integers:
                self.print_scalar(entry)

        if len(self.strings) > 0:
            print("\nstrings:")
            print("--------")
            for entry in self.strings:
                self.print_scalar(entry)

        if len(self.float_arrays) > 0:
            print("\nfloat arrays:")
            print("-------------")
            for entry in self.float_arrays:
                self.print_array(entry)

        if len(self.integer_arrays) > 0:
            print("\ninteger arrays:")
            print("---------------")
            for entry in self.integer_arrays:
                self.print_array(entry)

        if len(self.string_arrays) > 0:
            print("\nstring arrays:")
            print("--------------")
            for entry in self.string_arrays:
                self.print_array(entry)

    def parse_code_for_var_refs(self):
        """
        Entry point for finding variable xrefs in BASIC for reads and modifications.
        This function iterates over each BASIC line and hands it off to
        proc_statements_in_line() for more processing.
        """         
        line_vars_dict = {}
        i = self.TXTTAB_val - 1
        while True:  # iterate over BASIC code lines
            if self.data[i] != 0:
                exit("Error: malformed BASIC code, expected pre-line indicator")
            next_line_offset = self.data[i+1] + self.data[i+2] * 256
            if next_line_offset == 0:
                break  # end of BASIC code
            line_number = self.data[i+3] + self.data[i+4] * 256

            start_line = i
            i = next_line_offset - 1
            # +5 is first character of code on line
            refs_for_line_nums = self.proc_statements_in_line(line_number, start_line+5, i)
            line_vars_dict[line_number] = refs_for_line_nums

        return line_vars_dict

    def proc_statements_in_line(self, line_number, start_line, end_line):
        """
        This function breaks up a BASIC line into 0-to-many statements, which
        proc_vars_in_statement() will mine for read/mod xrefs.
        """
        line_statements = []
        line = []
        in_quotes = False
        i = start_line - 1
        while i < end_line:  # iterate over line of BASIC
            i += 1
            b = self.data[i]
            
            if b == ord('"'):
                in_quotes = not in_quotes
                if not in_quotes:
                    # will (ultimately) output a pair of empty double quotes
                    # (dropping what they contained)
                    line.append(ord('"'))
            if in_quotes:
                continue
            
            if b == 0x8f:  # REM (skip rest of line)
                line = ""
                break

            if b == 0x96:  # DEF (skip this statement)
                while i < end_line and self.data[i] != ':':
                    i += 1
                continue
            
            if b == 0x8B:  # IF
                # gather bytes until THEN or GOTO, and make bytes their own statement
                # approach should be able to handle stuff like
                #    IFA=1THENIFA=1THENIFA=1THENPRINT"Y" without BNF grammar handling
                # also, anything past THEN is a new statement that could contain a
                # write, such as IFA=0THENDIMA$(20)       
                while i < end_line and self.data[i] not in [0xA7, 0x89]:
                    line.append(self.data[i])                    
                    i += 1
                line_statements.append(line)
                line = []
                continue
            
            if b == ord(':'):  # end of statement
                line_statements.append(line)
                line = []
            else:
                line.append(b)

        if len(line) > 0:
            line_statements.append(line)

        vars_read_in_line = set(); vars_modified_in_line = set()
        for statement in line_statements:
            # drop leading spaces
            while len(statement) > 0 and statement[0] == ord(' '):
                statement = statement[1:]
            if len(statement) > 0:
                vars_read, vars_mod = self.proc_vars_in_statement(statement)
                vars_read_in_line.update(vars_read)
                vars_modified_in_line.update(vars_mod)

        #print("DEBUG: read: %s, written: %s" % (vars_read_in_line, vars_modified_in_line))
        
        return VarRefsForLineNumber(line_number, list(vars_read_in_line), list(vars_modified_in_line))

    def add_var_to_variables(self, c, tmp_var, variables):
        if c == '(':
            tmp_var += '()'
        variables.append(tmp_var)
        return ""

    def proc_vars_in_statement(self, statement):
        """
        This function takes a statement, and identifies all the variables therein.
        After that, it determines if each variable reference is read or modified.
        """

        # First, parse out the variable names from the code
        variables = []
        vars_read = []
        vars_mod = []
        tmp_var = ""

        for c in statement:
            c = chr(c)            
            if len(tmp_var) == 0:
                if 'A' <= c <= 'Z':
                    tmp_var += c
            elif len(tmp_var) == 1:
                if ('A' <= c <= 'Z') or ('0' <= c <= '9') or c in ['%', '$']:
                    tmp_var += c
                else:
                    tmp_var = self.add_var_to_variables(c, tmp_var, variables)
            elif tmp_var[-1] not in ['%', '$']:  # tmp_var len is >= 2
                if c in ['%', '$']:
                    tmp_var += c
                else:
                    tmp_var = self.add_var_to_variables(c, tmp_var, variables)
            elif tmp_var[-1] in ['%', '$']:  # tmp_var len is >= 2
                tmp_var = self.add_var_to_variables(c, tmp_var, variables)

        # Second, determine if it's a read or write reference
        if len(variables) == 0:
            return [], []

        # if FOR or DIM, first var is modded, remainder are read
        if statement[0] in [0x81, 0x86]:
            vars_mod.append(variables[0])
            if len(variables) > 1:
                vars_read.extend(variables[1:])

        # handle INPUT#, INPUT, READ, GET/GET# (all of which can take multiple modded params)
        elif statement[0] in [0x84, 0x85, 0x87, 0xa1]:
            vars_mod.extend(variables)
        
        # if first byte is a token (not already handled above)
        # this handles IF tokens (since THEN clause already in its own statement)
        # and also handles things like PRINTA=A being a read for boolean, not a write.
        elif statement[0] & 0x80 != 0:
            vars_read.extend(variables)

        # handle '=' (token $b2) for assignments (IF already handled)
        # e.g. s8(x0,y0)=z0, only the s8 is write
        #      A=B=B, only A is write (write a -1, because B==B)
        elif 0xb2 in statement:
            vars_mod.append(variables[0])
            if len(variables) > 1:
                vars_read.extend(variables[1:])            

        else:
            exit("Error: shouldn't reach this else clause")

        return vars_read, vars_mod


if __name__ == "__main__":
    print("library present")

