# Lab6
  
## Lab Exercises 

- [ ] Use a seaborn pairplot ``sns.pairplot()'' to visualise your data
- [ ] Loop over different cluster size starting from 2 until 10, using all the features present and pick the one with the lowest silhouette score
- [ ] (Optional) Save 10 runs for each cluster size and use a seaborn pointplot [http://seaborn.pydata.org/generated/seaborn.pointplot.html](http://seaborn.pydata.org/generated/seaborn.pointplot.html) without joining the lines 
to plot the confidence intervals for the silhouette score
- [ ] Change your clusterer to ``AgglomerativeClustering'' see here for more [http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html](http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html) and re-do the above experiment - what do you observe?

- [ ] Once you are done, save your changes in github
	* Go inside your lab directory and do 
      * ``git add -A -v``
      * ``git commit -m <message>``
      * ``git push origin master``
