# import matplotlib.pyplot to create graghs
import matplotlib.pyplot as plt

# difine variables you need when create a bar gragh
LanguagePercentage={'JavaScript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5} #create a dictionary
languages=list(LanguagePercentage.keys())
percentages=list(LanguagePercentage.values())

# create a bar gragh
plt.bar(languages,percentages)

# set the labels and title of the bar gragh
plt.xlabel('Promgramming languages')
plt.ylabel('Percentages of developers')
plt.title('Programming language popularity')

plt.show()

# You could modify 'SelectedLanguage' to return the percentage of other language.
SelectedLanguage='Python'
print('The percentage of developers who use',SelectedLanguage,'is',LanguagePercentage[SelectedLanguage])