    # libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.animation as animation


# %matplotlib inline

def replace_line(line_num, text):
    lines = open('feelings.txt', 'r').readlines()
    lines[line_num] = text
    out = open('feelings.txt', 'w')
    out.writelines(lines)
    out.close()

def get_feeling_num(feeling):
    feeling_num = 0
    with open('feelings.txt', 'r') as fp:
        lines = fp.readlines()
        feeling_num = int(lines[feeling].split(":")[1])
    return feeling_num

def update_feelings(feeling):
    feeling_sum = get_feeling_num(feeling) + 1

    if feeling == 1:
        replace_line(feeling, "depends: "  + str(feeling_sum) + "\n")
    elif feeling == 2:
        replace_line(feeling, "worried: "  + str(feeling_sum) + "\n")
    else:
        replace_line(feeling, "fine: "  + str(feeling_sum) + "\n")


def barplot():
    # Make a fake dataset
    height = [get_feeling_num(0), get_feeling_num(1), get_feeling_num(2)]
    bars = ('feelin\' fine', 'depends', 'lil\' worried')
    y_pos = np.arange(len(bars))


    d = {'feelin\' fine': height[0], 'depends': height[1], 'lil\' worried': height[2]}
    # df = pd.DataFrame(data=d)

    plt.style.use('ggplot')
    plt.barh(bars, height, color=['green', 'orange', 'blue'])
    # plt.xlabel('Amount', fontsize=15)
    # plt.ylabel('Feeling', fontsize=15)
    plt.title('How People Feel')


    # Custimization
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=0.8
    # plt.rcParams['xtick.color']='#333F4B'
    # plt.rcParams['ytick.color']='#333F4B'

    my_range = [0,1,2]
    fig, ax = plt.subplots(figsize=(5,3.5))
    plt.hlines(y=my_range, xmin=0, xmax=height, color='#007acc', alpha=0.2, linewidth=5)
    plt.plot(height, my_range, "o", markersize=5, color='#007acc', alpha=0.6)

    # set labels style
    ax.set_xlabel('Amount', fontsize=15, fontweight='black', color = '#333F4B')
    ax.set_ylabel('Feeling')

    # change the style of the axis spines
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)
    plt.show()

def barplot2():
    # import libraries
    height = [get_feeling_num(0), get_feeling_num(1), get_feeling_num(2)]
    bars = ('feelin\' fine', 'depends', 'lil\' worried')

    # set font
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.sans-serif'] = 'Helvetica'

    # set the style of the axes and the text color
    plt.rcParams['axes.edgecolor']='#333F4B'
    plt.rcParams['axes.linewidth']=1
    plt.rcParams['xtick.color']='#333F4B'
    plt.rcParams['ytick.color']='#333F4B'
    plt.rcParams['text.color']='#333F4B'

    # create some fake data
    percentages = pd.Series([get_feeling_num(0), get_feeling_num(1), get_feeling_num(2)],
                            index=['feelin\' fine', 'depends', 'lil\' worried'])
    df = pd.DataFrame({'feeling' : percentages})
    df = df.sort_values(by='feeling')

    # we first need a numeric placeholder for the y axis
    my_range=list(range(1,len(df.index)+1))

    fig, ax = plt.subplots(figsize=(15,10))

    # create for each expense type an horizontal line that starts at x = 0 with the length
    # represented by the specific expense percentage value.
    plt.hlines(y=my_range, xmin=0, xmax=df['feeling'], color='#007ACC', alpha=0.2, linewidth=5)

    # create for each expense type a dot at the level of the expense percentage value
    plt.plot(df['feeling'], my_range, "o", markersize=5, alpha=0.6)

    # set labels
    ax.set_xlabel('Feeling', fontsize=15, fontweight='black', color = '#333F4B')
    ax.set_ylabel('')

    # set axis
    ax.tick_params(axis='both', which='major', labelsize=12)
    plt.yticks(my_range, df.index)

    # add an horizonal label for the y axis
    fig.text(-0.23, 0.96, 'Transaction Type', fontsize=15, fontweight='black', color = '#333F4B')

    # change the style of the axis spines
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_smart_bounds(True)
    ax.spines['bottom'].set_smart_bounds(True)

    # set the spines position
    ax.spines['bottom'].set_position(('axes', -0.04))
    ax.spines['left'].set_position(('axes', 0.015))

    plt.show()
    # plt.savefig('hist2.png', dpi=300, bbox_inches='tight')

def barplot3():
    fig = plt.figure()

    x = ['feelin\' fine', 'depends', 'lil\' worried']
    y = [get_feeling_num(0), get_feeling_num(1), get_feeling_num(2)]


    data = np.column_stack([np.linspace(0, yi, 50) for yi in y])

    rects = plt.bar(x, data[0], color='c')
    # line, = plt.plot(x, data[0], color='r')
    plt.ylim(0, max(y))
    def animate(i):
        for rect, yi in zip(rects, data[i]):
            rect.set_height(yi)
        # line.set_data(x, data[i])
        return rects#, line

    anim = animation.FuncAnimation(fig, animate, frames=len(data), interval=40)
    plt.show()

barplot3()
