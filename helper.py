import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(scores, mean_scores, red_scores, green_scores):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training...')
    plt.xlabel('Number of Games')
    plt.ylabel('Score')
    plt.plot(scores)
    plt.plot(mean_scores)
    plt.plot(red_scores, 'r')
    plt.plot(green_scores, 'g')
    plt.ylim(ymin=0)
    plt.text(len(scores)-1, scores[-1], str(scores[-1]))
    plt.text(len(mean_scores)-1, mean_scores[-1], str(mean_scores[-1]))
    plt.text(len(red_scores)-1, red_scores[-1], str(red_scores[-1]))
    plt.text(len(green_scores)-1, green_scores[-1], str(green_scores[-1]))
    plt.show(block=False)
    plt.pause(.1)