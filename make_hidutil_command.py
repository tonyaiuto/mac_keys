# Turn keyboard map into an hidutil command

import sys


def main(args):
  if len(args) < 2:
    print('usage: %s input' % args[0])
    return 1

  comments = []
  commands = []
  with open(args[1], 'r') as inp:
    for line in inp:
      if not line.startswith('remap'):
        continue
      line = line.strip()
      comment = line.find('#')
      if comment > 0:
        comments.append(line[comment:])
        line = line[0:comment]
      line = line.strip()
      x = line.split()
      commands.append('{"HIDKeyboardModifierMappingSrc":%s,"HIDKeyboardModifierMappingDst":%s}' % (
        x[1], x[2]))

  print("""#!/bin/bash""")
  print('\n'.join(comments))
  print("""hidutil property --set '{"UserKeyMapping":[""")
  print(',\n'.join(commands))
  print("""]}'""")


if __name__ == "__main__":
  main(sys.argv)
