cells = input("Enter cells: ")
print("---------\n",
      f"| {' '.join(map(str, cells[:3]))} |\n",
      f"| {' '.join(map(str, cells[3:6]))} |\n",
      f"| {' '.join(map(str, cells[6:]))} |\n",
      "---------",
      sep="")
