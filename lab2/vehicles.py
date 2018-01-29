import matplotlib

matplotlib.use('Agg')

from pandas import Series, DataFrame
import pandas as pd

import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np  


# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed()  # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
    df = pd.read_csv('./vehicles.csv')
    print(df.columns)
    data1 = df.dropna()

####current sleet
    dataset1 = data1.values.T[0]

    plotdata1 = DataFrame(np.vstack((np.arange(79), dataset1)).T, columns=[df.columns[0], df.columns[0]+' MPG count'])

    sns_plot = sns.lmplot(plotdata1.columns[0], plotdata1.columns[1], data=plotdata1, fit_reg=False)

    sns_plot.axes[0, 0].set_ylim(0, )
    sns_plot.axes[0, 0].set_xlim(0, )

    sns_plot.savefig("current_fleet_plot.png", bbox_inches='tight')
    sns_plot.savefig("current_fleet_plot.pdf", bbox_inches='tight')

    print('\nMeasures of central tendency on current fleet:')
    print(("Mean: %f") % (np.mean(dataset1)))
    print(("Median: %f") % (np.median(dataset1)))
    print('Measurements of dispersion on current fleet:')
    print(("Var: %f") % (np.var(dataset1)))
    print(("std: %f") % (np.std(dataset1)))
    print(("MAD: %f") % (mad(dataset1)))

    plt.clf()
    sns_plot2 = sns.distplot(dataset1, bins=20, kde=False, rug=True).get_figure()

    axes2 = plt.gca()
    axes2.set_xlabel(plotdata1.columns[0])
    axes2.set_ylabel(plotdata1.columns[1])

    sns_plot2.savefig("current_fleet_histogram.png", bbox_inches='tight')
    sns_plot2.savefig("current_fleet_histogram.pdf", bbox_inches='tight')


####proposed sleet
    dataset2 = data1.values.T[1]

    plotdata2 = DataFrame(np.vstack((np.arange(79), dataset2)).T, columns=[df.columns[1], df.columns[1]+' MPG count'])

    sns_plot3 = sns.lmplot(plotdata2.columns[0], plotdata2.columns[1], data=plotdata2, fit_reg=False)

    sns_plot3.axes[0, 0].set_ylim(0, )
    sns_plot3.axes[0, 0].set_xlim(0, )

    sns_plot3.savefig("proposed_fleet_plot.png", bbox_inches='tight')
    sns_plot3.savefig("proposed_fleet_plot.pdf", bbox_inches='tight')

    print('\nMeasures of central tendency on proposed fleet:')
    print(("Mean: %f") % (np.mean(dataset2)))
    print(("Median: %f") % (np.median(dataset2)))
    print('Measurements of dispersion on proposed fleet:')
    print(("Var: %f") % (np.var(dataset2)))
    print(("std: %f") % (np.std(dataset2)))
    print(("MAD: %f") % (mad(dataset2)))

    plt.clf()
    sns_plot4 = sns.distplot(dataset2, bins=20, kde=False, rug=True).get_figure()

    axes4 = plt.gca()
    axes4.set_xlabel(plotdata2.columns[0])
    axes4.set_ylabel(plotdata2.columns[1])

    sns_plot4.savefig("proposed_fleet_histogram.png", bbox_inches='tight')
    sns_plot4.savefig("proposed_fleet_histogram.pdf", bbox_inches='tight')


