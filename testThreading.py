
import threading
import subprocess
import time
import testSimulator

if __name__ == '__main__':

    testSimulatorClass = testSimulator.testSimulator();

    thread = threading.Thread(target=testSimulatorClass.run)
    thread.start()
    
    print ('inside of testSpawn.__main__')

    #testSimulatorClass.run()
    
    #result = subprocess.run(["python", "testSimulator.py"])
    #print (result)
    
    #if result.returncode == 0:
    #    print(result.stdout)

    time.sleep(5)

    thread.kill()

    testSimulatorClass.quit()

    print ('About to exit from testSpawn.__main')

#def spawn_python_program(path_to_script):
#    """Spawns a separate Python program.#

#    Args:
#        path_to_script: The path to the Python script to be spawned.
#    """
#    subprocess.run(["python", path_to_script])

#if __name__ == "__main__":
#    script_path = "/path/to/your/script.py"  # Replace with the actual path
#    spawn_python_program(script_path)

#thread = threading.Thread(target=my_function) thread.start()
