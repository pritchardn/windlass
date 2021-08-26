# (c) Nicholas Pritchard 2021
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

from Experiments.tools.labTools import single_trial_single


def main(method):
    for _ in range(10):
        single_trial_single(method, './graphs/', './' + method + '_')


if __name__ == "__main__":
    main('thrashThread4')
