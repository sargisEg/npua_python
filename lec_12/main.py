import random
import time

def benchmark(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(func.__name__ + " executed in " + str(execution_time) + " seconds")
        return result
    return wrapper

def create_file(name_of_file):
    with open(name_of_file, 'w') as file:
        for _ in range(100):
          line = ""
          for _ in range(20):
            line += str(random.randint(1, 100)) + ","
          file.write(line[:-1] + '\n')

def write_to_file(name_of_file, data):
    with open(name_of_file, 'w') as file:
        for line in data:
            line_str = ",".join(map(str, line))
            file.write(line_str + '\n')
@benchmark
def read_file_as_generator(name_of_file):
    with open(name_of_file, 'r') as file:
        for line in file:
            yield line

def convert_to_int(string_of_numbers):
  return list(map(int, string_of_numbers.split(",")))

@benchmark
def filter_nums(numbers):
  return list(filter(lambda x: (x % 13 == 0), numbers))


name_of_file = "name"
create_file(name_of_file)
with open(name_of_file, 'r') as file:
  file_lines = []
  for line in file:
    new_line = filter_nums(convert_to_int(line))
    file_lines.append(new_line)
  write_to_file(name_of_file, file_lines)

generator = read_file_as_generator(name_of_file)
for line in generator:
  print(line)
