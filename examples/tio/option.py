"""
Shows the action of the getOption method

Author: Will Hossack: The University of Edinburgh
"""


import poptics.tio as t

def main():
    while True:
        opts = "exit","quit","continue","restart","reset"
        opt,name = t.getOption("Option",opts)
        t.tprint("Option Number ",opt," Option name ", name)
        if opt == 0 or opt == 1:
            break

main()
