from contextlib import contextmanager
import time

class cm_timer_1:

    def __init__(self):
        self._start_time = None

    def start(self):
        self._start_time = time.perf_counter()

    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print("time: ", elapsed_time)

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

@contextmanager
def cm_timer_2():
    try:
        start_time = time.perf_counter()
        yield start_time
    finally:
        elapsed_time = time.perf_counter() - start_time
        print("time: ", elapsed_time)

if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)
    with cm_timer_2():
        time.sleep(5.5)