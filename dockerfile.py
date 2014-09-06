from collections import deque


def parse_raw_dockerfile(input_file):
  '''
  Parse Dockerfile and output list of "actual"
  commands that will be invoked.

  Example input:

  RUN foo && \
    bar
  CMD /bin/true

  Should return (more or less):
  ['RUN foo && bar', 'CMD /bin/true']
  '''
  result = []
  current_line = deque()
  for line in input_file:
    if line.startswith('#') or not line.strip():
      continue
    current_line.append(line)
    if line.rstrip()[-1] != '\\':
      result.append(''.join(current_line))
      current_line.clear()
  return result

