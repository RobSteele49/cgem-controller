import os

def file_exists(file_path):
  """Checks if a file exists at the given path.

  Args:
    file_path: The path to the file.

  Returns:
    True if the file exists, False otherwise.
  """
  return os.path.exists(file_path) and os.path.isfile(file_path)

if __name__ == '__main__':
    print ('Testing file exists')

    port = 'dev/ttyUSB0'

    print (f'Result from file_exists: {file_exists(port)}')
    
