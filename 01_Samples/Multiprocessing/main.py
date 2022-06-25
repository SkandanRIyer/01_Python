import time
import multiprocessing


def do_nothing(sleep_time) -> None:
    i = 0
    while i < 20:
        time.sleep(sleep_time)
        i += 1
    print("Done Sleeping.....😴😴😴\n")


def start_process() -> None:
    # p1 = multiprocessing.Process(target=do_nothing)
    # p2 = multiprocessing.Process(target=do_nothing)
    #
    # p1.start()
    # p2.start()
    #
    # p1.join()
    # p2.join()

    processes = []
    for _ in range(10):
        p = multiprocessing.Process(target=do_nothing, args=(10,))
        p.start()
        processes.append(p)

    for process in processes:
        process.join()


if __name__ == '__main__':
    start = time.perf_counter()
    start_process()
    end = time.perf_counter()
    print(f'Finished in {round(end - start, 2)} second(s)')
