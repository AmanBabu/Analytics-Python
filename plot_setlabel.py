import pandas as pd
import matplotlib.pyplot as plt

readfile = pd.read_csv('unrate.csv')
readfile['DATE'] = pd.to_datetime(readfile['DATE'])

#get first 12 values in the Date column
xvalues = readfile.loc[:12, 'DATE']
#get first 12 values in the Value column
yvalues = readfile.loc[:12, 'VALUE']

plt.xticks(rotation=90) # rotate x-axis by 90 degree
plt.xlabel('Month')
plt.ylabel('Unemployment Rate')
plt.title('Monthly Unemployment Trends, 1948')

plt.plot(xvalues, yvalues)
plt.show()

#------------------------------------------------------------------------------------------#

# Generate 2 line charts on the same figure:
#	One that visualizes the percentages of Biology degrees awarded to women over time. Set the line color to "blue" and the label to "Women".
#	One that visualizes the percentages of Biology degrees awarded to men over time. Set the line color to "green" and the label to "Men".
# Set the title of the chart to "Percentage of Biology Degrees Awarded By Gender".
# Generate a legend and place it in the "upper right" location.
# Display the chart.

plt.plot( women_degrees['Year'], women_degrees['Biology'],c='blue', label='Women') # c for color of line, label for label in legend
plt.plot(women_degrees['Year'], 100-women_degrees['Biology'], c='green', label='Men')
plt.title('Percentage of Biology Degrees Awarded By Gender')
plt.legend(loc='upper right') # loc - where to show legend 
plt.show()

# remove tick marks from the plot
plt.tick_params(bottom="off", left="off",right="off", top="off")

#-------------------------------------------------------------------------------------------#
#To hide all of the spines, we need to:

#access each Spine object in the dictionary
#call the Spine.set_visible() method
#pass in the Boolean value False
#The following line of code removes the spines for the right axis:
#	ax.spines["right"].set_visible(False)


fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
# Add your code here
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()


#----------------------------------------------------------------------------------------------#
major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women') # set linewidth=3 for of line
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Add your code here.
    ax.set_xlim(1968,2011)
    ax.set_ylim(0,100)
    for key,spine in ax.spines.items(): # set all spines to false
        spine.set_visible(False)
    ax.tick_params(bottom='off', right='off', left='off', top='off')
    ax.set_title(major_cats[sp])
# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()

# ------------------------------------------------------------------------------------------------ #

ax.text(2005, 87, 'Men') # set text annotations instead of legend ,parameters - x-axis value, y-axis value and text to display

#-----------------------------------------------------------------------------------------------------#

   # plot histogram with kernel density graph
import seaborn as sns
import matplotlib.pyplot as plt
sns.distplot(titanic['Age'])
plt.show()

#--------------------------------------------------------------------------------------------------#
sns.set_style('white') # white background and coordinate grid hidden
sns.kdeplot(titanic['Age'], shade=True)
plt.xlabel('Age')
sns.despine(left=True, right=True, top=True, bottom=True) # remove spines from all sides of the plot
plt.show()
# ------------------------------------------------------------------------------------------------------#
#Use a FacetGrid instance to generate three plots on the same row:
#    One for each unique value of Pclass.
#    Each plot should be a kernel density plot of the "Age" column, with the area under the curve shaded.
#    Each plot should have a height of 6 inches.
#Remove all of the spines using seaborn.despine().
#Display the plots.

g = sns.FacetGrid(titanic, col='Pclass', size=6)
g.map(sns.kdeplot, 'Age', shade=True)
sns.despine(left=True, right=True, bottom=True, top=True)
plt.show()

# -------------------------------------------------------------------------------------------------------#
#Creating Conditional Plots Using Three Conditions

g = sns.FacetGrid(titanic, col="Survived", row="Pclass", hue='Sex' , size=3)
g.map(sns.kdeplot, "Age", shade=True)   # g = (g.map(sns.kdeplot, 'Age', shade=True).add_legend()) to add legend on hue
sns.despine(left=True, bottom=True)
plt.show()
# ---------------------------------------------------------------------------------------------------#