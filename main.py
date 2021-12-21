
def count_batteries_by_usage(cycles):
  count_low=0
  count_medium=0
  count_high=0
  for i in cycles:
    if i<150:
      count_low += 1
    elif i>=150 and i<=649 :
      count_medium +=1
    elif i>=650 :
      count_high += 1
  return {
    "lowCount": count_low,
    "mediumCount": count_medium,
    "highCount": count_high
  }


def test_bucketing_by_number_of_cycles():
  print("Counting batteries by usage cycles...\n");
  counts = count_batteries_by_usage([100, 300, 500, 600, 900, 1000])
  print(counts)
  assert(counts["lowCount"] == 1)
  assert(counts["mediumCount"] == 3)
  assert(counts["highCount"] == 2)
  print("Done counting :)")


if _name_ == '_main_':
  test_bucketing_by_number_of_cycles()
