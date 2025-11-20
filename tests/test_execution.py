import pytest
import os
from pathlib import Path
import filecmp


# def test_check_sum():
#   cwd = os.getcwd()
#   stdout_file = cwd + "/tests/thread_child_join_out"
#   f = open(stdout_file)
#   stdout_file_content = f.read()
#   f.close()

#   #ARRRRG sum is 12079685
#   arr = stdout_file_content.split()

#   if int(arr[3]) != 10000000:
#     assert True
#   else:
#     assert False


def test_contiguous_output1():
  cwd = os.getcwd()
  stdout_file = cwd + "/tests/contiguous_out1"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()

  substring = "Enter number of partitions: Enter partition sizes: Enter starting memory address for the FIRST partition: Enter pre-allocated memory (0=available, >0=occupied) for each partition: Enter number of processes: Enter process sizes: --- FIRST FIT --- === SEGMENTS INFO === Partition 0: Start=600300 Size=100 Occupied=YES Partition 1: Start=600400 Size=200 Occupied=YES Partition 2: Start=600600 Size=300 Occupied=YES Allocated Processes: Process 0 (size=223) -> Partition 2 | Start=600600 End=600823 Process 1 (size=123) -> Partition 1 | Start=600400 End=600523 Unallocated Processes: (none) --- BEST FIT --- === SEGMENTS INFO === Partition 0: Start=600300 Size=100 Occupied=YES Partition 1: Start=600400 Size=200 Occupied=YES Partition 2: Start=600600 Size=300 Occupied=YES Allocated Processes: Process 0 (size=223) -> Partition 2 | Start=600600 End=600823 Process 1 (size=123) -> Partition 1 | Start=600400 End=600523 Unallocated Processes: (none) --- WORST FIT --- === SEGMENTS INFO === Partition 0: Start=600300 Size=100 Occupied=YES Partition 1: Start=600400 Size=200 Occupied=YES Partition 2: Start=600600 Size=300 Occupied=YES Allocated Processes: Process 0 (size=223) -> Partition 2 | Start=600600 End=600823 Process 1 (size=123) -> Partition 1 | Start=600400 End=600523 Unallocated Processes: (none)"
  count = stdout_file_content.count(substring)

  if count == 1:
    assert True
  else:
    assert False

def test_contiguous_output2():
  cwd = os.getcwd()
  stdout_file = cwd + "/tests/contiguous_out2"
  f = open(stdout_file)
  stdout_file_content = f.read()
  f.close()

  substring = "Enter number of partitions: Enter partition sizes: Enter starting memory address for the FIRST partition: Enter pre-allocated memory (0=available, >0=occupied) for each partition: Enter number of processes: Enter process sizes: --- FIRST FIT --- === SEGMENTS INFO === Partition 0: Start=611300 Size=200 Occupied=YES Partition 1: Start=611500 Size=200 Occupied=YES Partition 2: Start=611700 Size=300 Occupied=YES Allocated Processes: Process 0 (size=213) -> Partition 2 | Start=611700 End=611913 Process 1 (size=123) -> Partition 1 | Start=611500 End=611623 Unallocated Processes: Process 2 (size=673) could NOT be allocated --- BEST FIT --- === SEGMENTS INFO === Partition 0: Start=611300 Size=200 Occupied=YES Partition 1: Start=611500 Size=200 Occupied=YES Partition 2: Start=611700 Size=300 Occupied=YES Allocated Processes: Process 0 (size=213) -> Partition 2 | Start=611700 End=611913 Process 1 (size=123) -> Partition 1 | Start=611500 End=611623 Unallocated Processes: Process 2 (size=673) could NOT be allocated --- WORST FIT --- === SEGMENTS INFO === Partition 0: Start=611300 Size=200 Occupied=YES Partition 1: Start=611500 Size=200 Occupied=YES Partition 2: Start=611700 Size=300 Occupied=YES Allocated Processes: Process 0 (size=213) -> Partition 2 | Start=611700 End=611913 Process 1 (size=123) -> Partition 1 | Start=611500 End=611623 Unallocated Processes: Process 2 (size=673) could NOT be allocated"
  count = stdout_file_content.count(substring)

  if count == 1:
    assert True
  else:
    assert False

