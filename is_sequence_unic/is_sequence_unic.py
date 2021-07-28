def is_sequence_unic(seq):
  return len(seq) == len(set(seq))

print (is_sequence_unic([x for x in range(42)]))