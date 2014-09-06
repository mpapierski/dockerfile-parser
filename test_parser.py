from StringIO import StringIO
from nose.tools import assert_list_equal
from dockerfile import parse_raw_dockerfile

dockerfile = '''
### Comment

FROM ubuntu

#########
#########

RUN apt-get install -y python && \\
  mkdir /app && \\
  { \\
    echo "print 42" > /app/app.py \\
  }
EXPOSE 4242
WORKDIR /app
ENTRYPOINT python app.py

'''
def test_parse():
  parsed = parse_raw_dockerfile(StringIO(dockerfile))
  assert_list_equal(parsed, [
    'FROM ubuntu\n',
    'RUN apt-get install -y python && \\\n  mkdir /app && \\\n  { \\\n    echo "print 42" > /app/app.py \\\n  }\n',
    'EXPOSE 4242\n',
    'WORKDIR /app\n',
    'ENTRYPOINT python app.py\n'])

if __name__ == '__main__':
  test_parse()