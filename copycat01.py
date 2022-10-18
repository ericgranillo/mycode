#!/usr/bin/env/ python3

"""ALTA3 | EGranillo | Pushing files around using shutil and os from the standard library"""

import shutil
import os

def main():

    # establish a working directory
    os.chdir("/home/student/mycode/")

    # copy a file from point A to point B
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # copy the entire dirctory A to directory B
    os.system("rm -rf /home/student/mycode/5g_research_backup/")

    shutil.copytree("5g_research/", "5g_research_backup/")

main()
