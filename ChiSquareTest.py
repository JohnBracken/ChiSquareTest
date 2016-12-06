#The following code sample is an example of a chi-square statistical test.
#This example takes a total of 200 people and shows the distribution of the number of
#people of each observed blood type they have in the following order: A, B, AB and O.  The
#expected number of people having each blood type is also given
#with a breakdown of 41% having type A, 10% having type B, 4% having type AB
#and 45% having type O.  In this test, we wish to determine if the
#observed number of people of each blood type falls into the expected proportions
#for each blood type, or if instead the observed propotions show something
#different than the expected values.


#Import the statistical module from the Scipy library.
from scipy import stats


#Perform the chi-square test on the categorical blood type data.  For each
#list, the blood types are shown in the order of A, B, AB, O.  The first
#list is the observed number of people with each blood type, and the second
#list is the expected number of people with each blood type based on the
#proportions mentioned above.  The test will generate the chi-square statistic
#value and also the corresponding p-value for the statistic.
#A significance value of p = 0.05 is chosen, so if the p-value is less than
#or equal to 0.05, then the null hypothesis can be rejected and in fact the sampled
#proportions for each blood type are different than what was expected.  For
#p > 0.05, the null hypothesis cannot be rejected, meaning that the observed values
#do fall within the expected proportions for each blood type.
a = stats.chisquare([89, 18, 12, 81], f_exp= [82, 20, 8, 90])


#Text file output showing the results, write the results to the text file.
text_file = open('ChisquareResults.txt', 'w')


#Generate a sequence of lines to be written to the text file.
#One line is for the Chi square test statistic, and the other line is for the p value.
seq = ['Chi Square Test Statistic:  ' +  str(a[0]) + '\n', 'p Value:  ' + str(a[1])]


#Write all the lines to the text file.  In this case the p-value for the calculated test
#statistic was > 0.05, so the null hypothesis was unable to be rejected and the observed blood type
#proportions fell within the expected distribution of blood type.
text_file.writelines(seq)


#Close the text file.
text_file.close()
