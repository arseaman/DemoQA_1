import subprocess


def run_tests():
    print("Tests launch ...")
    try:
        subprocess.run(["pytest", "-v", "-s"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error pytest: {e}")
    print("All Tests Complete. Waiting for next tests session launch ...")


run_tests()

