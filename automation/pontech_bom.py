#
# Example python script to generate a BOM from a KiCad generic netlist
#
# Example: Sorted and Grouped HTML BOM with advanced grouping
#

"""
    @package
    Generate a PONTECH BOM from a KiCad schematic.
    Based on bom_html_with_advanced_grouping.py

    Components are sorted and grouped by value
    Fields are (if exist)
    Ref, Quantity, Value, Part, Footprint, Description, Vendor

    Command line:
    python "pathToFile/pontech_bom.py" "%I" "%O.bom"
"""

from __future__ import print_function

# Import the KiCad python helper module and the csv formatter
import sys

sys.path.append('/usr/share/kicad/plugins')
import kicad_netlist_reader

company = "PONTECH"

print(sys.version)

# Start with a basic html template
html = """
<!--COMPANY--> KiCad BOM Example Output
<!--SOURCE-->
<!--DATE-->
<!--TOOL-->
<!--COMPCOUNT-->

"""


def myEqu(self, other):
    """myEqu is a more advanced equivalence function for components which is
    used by component grouping. Normal operation is to group components based
    on their Value and Footprint.

    In this example of a more advanced equivalency operator we also compare the
    custom fields Voltage, Tolerance and Manufacturer as well as the assigned
    footprint. If these fields are not used in some parts they will simply be
    ignored (they will match as both will be empty strings).

    """
    result = True
    if self.getValue() != other.getValue():
        result = False
    elif self.getPartName() != other.getPartName():
        result = False
    elif self.getFootprint() != other.getFootprint():
        result = False
    elif self.getField("Tolerance") != other.getField("Tolerance"):
        result = False
    elif self.getField("Manufacturer") != other.getField("Manufacturer"):
        result = False
    elif self.getField("Voltage") != other.getField("Voltage"):
        result = False
    elif self.getField("DNI") != other.getField("DNI"):
        result = False

    return result


# Override the component equivalence operator - it is important to do this
# before loading the netlist, otherwise all components will have the original
# equivalency operator.
kicad_netlist_reader.comp.__eq__ = myEqu

# Generate an instance of a generic netlist, and load the netlist tree from
# <file>.tmp. If the file doesn't exist, execution will stop
net = kicad_netlist_reader.netlist(sys.argv[1])

# Open a file to write too, if the file cannot be opened output to stdout
# instead
try:
    f = open(sys.argv[2], 'w')
except IOError:
    e = "Can't open output file for writing: " + sys.argv[2]
    print(__file__, ":", e, file=sys.stderr)
    f = sys.stdout

# Output a set of rows for a header providing general information
html = html.replace('<!--COMPANY-->', company)
html = html.replace('<!--SOURCE-->', net.getSource())
html = html.replace('<!--DATE-->', net.getDate())
html = html.replace('<!--TOOL-->', net.getTool())
html = html.replace('<!--COMPCOUNT-->', "Component Count:" + str(len(net.components)))

print(html, file=f)

row = "\t"
row += "Qty\t"
row += "DNI\t"
row += "Ref\t"
row += "Value\t"
# row += "SymbolLib\t"
# row += "Symbol\t"
# row += "FootprintLib:Footprint\t"
# row += "Description\t"
# row += "Vendor\t"
print(row, file=f)

# getIntrestingComponentes() doesn't always find every component
#components = net.getInterestingComponents()
components = net.components

# Get all of the components in groups of matching parts + values
# (see kicad_netlist_reader.py)
grouped = net.groupComponents(components)

# Output all of the component information
for group in grouped:
    refs = ""

    # Add the reference of every component in the group and keep a reference
    # to the component so that the other data can be filled in once per group
    for component in group:
        if len(refs) > 0:
            refs += ", "
        refs += component.getRef()
        c = component

    row = "\t"
    if c.getField("DNI") == "":
        row += str(len(group)) + "\t"  # Quantity
        row += c.getField("DNI") + "\t"  # DNI
    else:
        row += "0" + "\t"  # Quantity
        row += str(len(group)) + "\t"  # DNI

    row += refs + "\t"  # Referance Designator
    row += c.getValue() + "\t"  # PONTECH Part Number
    #    row += c.getLibName() + "\t" # Symbol Library
    #    row += c.getPartName() + "\t" # Symbol
    #    row += c.getFootprint() + "\t" # FootprintLib:Footprint
    #    row += c.getDescription() + "\t" # Description
    #    row += c.getField("Vendor") + "\t" # Vendor

    print(row, file=f)

# The following code prints out each component on its own line.
# print("", file=f)
# print("============================", file=f)
#
# count = 1
# for c in net.components:
#     row = "\t"
#     row += str(count) + "\t"
#     row += c.getRef() + "\t"
#     row += c.getValue() + "\t"  # PONTECH Part Number
#     print(row, file=f)
#     count += 1

f.close()

# Attempt to print out the raw objects (doesn't work)
# print( repr(components), file=f )
# print( repr(net), file=f )
