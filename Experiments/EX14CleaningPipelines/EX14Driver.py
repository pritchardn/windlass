# (c) Nicholas Pritchard 2021
# Ensure a DALiuGE Master Manager is running on port 9000
# Ensure a DALiuGE Daemon is running on port 8000

import csv

from dlg.common.reproducibility.constants import ReproducibilityFlags

from Experiments.tools.labTools import full_trial_single


def main(methods, st, end):
    for method in methods:
        for i in range(st, end):
            prefix = method + '_' + str(i)
            print(prefix)
            full_trial_single(prefix, './graphs/', './' + prefix + '_')


def write_summary(methods, st, end, outname, rmode: ReproducibilityFlags):
    with open(outname+'.csv', 'w') as csvf:
        fieldnames = ['Method']
        for i in range(st, end):
            fieldnames.append(str(i))
        writer = csv.DictWriter(csvf, fieldnames=fieldnames)
        writer.writeheader()
        for method in methods:
            row = {fieldnames[0]: method}
            for i in range(st, end):
                prefix = method+'_' + str(i)
                fname = prefix + '_out.csv'
                hashes = csv.DictReader(open(fname))
                for line in hashes:
                    if line['Hash'] == str(rmode):
                        row[fieldnames[i]] = line[prefix]
            writer.writerow(row)


if __name__ == "__main__":
    graphs = ['Yanda_Cont_Img']
    first = 0
    last = 2
    main(graphs, first, last)
    write_summary(graphs, first, last, 'rerun', ReproducibilityFlags.RERUN)
    write_summary(graphs, first, last, 'repeat', ReproducibilityFlags.REPEAT)
    write_summary(graphs, first, last, 'recompute', ReproducibilityFlags.RECOMPUTE)
    write_summary(graphs, first, last, 'reproduce', ReproducibilityFlags.REPRODUCE)
    write_summary(graphs, first, last, 'replicate_sci', ReproducibilityFlags.REPLICATE_SCI)
    write_summary(graphs, first, last, 'replicate_comp', ReproducibilityFlags.REPLICATE_COMP)
    write_summary(graphs, first, last, 'replicate_total', ReproducibilityFlags.REPLICATE_TOTAL)
