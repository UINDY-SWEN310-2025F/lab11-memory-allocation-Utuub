import pytest
import os
from pathlib import Path


def test_code_content1():
  cwd = os.getcwd()
  ansfile1 = cwd + "/answer/contiguous.c"
  f = open(ansfile1)
  ans1_content = f.read()
  f.close()

  substring = "computePartitionAddresses"
  count = ans1_content.count(substring)
  # print count
  if count >= 2:
    assert True
  else:
    assert False

def test_code_content2():
  cwd = os.getcwd()
  ansfile2 = cwd + "/answer/contiguous.c"
  f = open(ansfile2)
  ans2_content = f.read()
  f.close()

  substring = "printSummary"
  count = ans2_content.count(substring)
  # print count
  if count >= 4:
    assert True
  else:
    assert False

def test_code_content3():
  cwd = os.getcwd()
  ansfile3 = cwd + "/answer/contiguous.c"
  f = open(ansfile3)
  ans3_content = f.read()
  f.close()

  substring = "firstFit"
  count = ans3_content.count(substring)
  # print count
  if count >= 1:
    assert True
  else:
    assert False

def test_code_content4():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/contiguous.c"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "bestFit"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_code_content5():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/contiguous.c"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "worstFit"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 1:
    assert True
  else:
    assert False


def test_code_content6():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/contiguous.c"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "MAX"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 3:
    assert True
  else:
    assert False


def test_code_content7():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/mem_monitor.sh"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "while"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count > 0:
    assert False
  else:
    assert True


def test_code_content8():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/mem_monitor.sh"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "for"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count > 0:
    assert False
  else:
    assert True


def test_code_content9():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/mem_monitor.sh"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "Showing memory usage every 2 seconds"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 1:
    assert True
  else:
    assert False
    
def test_code_content10():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/vmstat_output"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "si"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 1:
    assert True
  else:
    assert False

def test_code_content10():
  cwd = os.getcwd()
  ansfile4 = cwd + "/answer/vmstat_output"
  f = open(ansfile4)
  ans4_content = f.read()
  f.close()

  substring = "so"
  count = ans4_content.count(substring)
  print(count)
  # print count
  if count >= 1:
    assert True
  else:
    assert False
    