# (c) Nicholas Pritchard 2021
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

# Note, input data comes from https://developer.skatelescope.org/projects/icrar-leap-accelerate/en/latest/md/Docker.html
# This is also useful https://developer.skao.int/_/downloads/icrar-leap-accelerate/en/stable/pdf/
import csv

from dlg.common.reproducibility.constants import ReproducibilityFlags

from Experiments.tools.labTools import full_trial_single


def main(methods):
    for method in methods:
        full_trial_single(method, './graphs/', './' + method + '_')


def write_summary(methods, outname, rmode: ReproducibilityFlags):
    with open(outname + '.csv', 'w') as csvf:
        fieldnames = ['Graph', 'Hash']
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        for method in methods:
            row = {fieldnames[0]: method}
            fname = method + '_out.csv'
            hashes = csv.DictReader(open(fname))
            for line in hashes:
                if line['Hash'] == str(rmode):
                    row[fieldnames[1]] = line[method]
            writer.writerow(row)


if __name__ == "__main__":
    graphs = ['LEAP_CLI_0', 'LEAP_CLI_1', 'LEAP_0', 'LEAP_1']
    main(graphs)
    write_summary(graphs, 'rerun', ReproducibilityFlags.RERUN)
    write_summary(graphs, 'repeat', ReproducibilityFlags.REPEAT)
    write_summary(graphs, 'recompute', ReproducibilityFlags.RECOMPUTE)
    write_summary(graphs, 'reproduce', ReproducibilityFlags.REPRODUCE)
    write_summary(graphs, 'replicate_sci', ReproducibilityFlags.REPLICATE_SCI)
    write_summary(graphs, 'replicate_comp', ReproducibilityFlags.REPLICATE_COMP)
    write_summary(graphs, 'replicate_total', ReproducibilityFlags.REPLICATE_TOTAL)
