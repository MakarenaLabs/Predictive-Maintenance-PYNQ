import multiprocessing as mp


def init_mp(process_mode="fork"):
    if process_mode != "fork":
        print("currently not supported, supporting only fork")
    mp.set_start_method(process_mode)
