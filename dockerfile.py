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
  current_line = ''
  for line in input_file:
    if line.startswith('#') or not line.strip():
      continue
    current_line += line
    if line.rstrip()[-1] != '\\':
      result.append(current_line)
      current_line = ''
  return result

