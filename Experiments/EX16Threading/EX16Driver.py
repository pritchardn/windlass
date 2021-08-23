# (c) Nicholas Pritchard 2021
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

# Note, input data comes from https://developer.skatelescope.org/projects/icrar-leap-accelerate/en/latest/md/Docker.html
# This is also useful https://developer.skao.int/_/downloads/icrar-leap-accelerate/en/stable/pdf/

from Experiments.tools.labTools import single_trial_single


def main(methods):
    for method in methods:
        single_trial_single(method, './graphs/', './' + method + '_')


if __name__ == "__main__":
    graphs = ['thrashThread4']
    main(graphs)
