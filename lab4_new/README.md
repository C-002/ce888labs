# Lab4  

## Lab Exercises  

- [ ] Load the data from the file ``jester-data-1.csv''  
	* The data is from [http://eigentaste.berkeley.edu/dataset/](http://eigentaste.berkeley.edu/dataset/) and it contains the ratings of 101 jokes from 24,983 users  
	* You can find the jokes in the website [http://eigentaste.berkeley.edu/dataset/jester_dataset_1_joke_texts.zip](http://eigentaste.berkeley.edu/dataset/jester_dataset_1_joke_texts.zip)  
- [ ] Label approx 10% of the dataset cells as 99, to denote they are part of the validation set. Keep the the actual values of the cells so you can use them later.  
- [ ] Use latent factor modeling to infer the hidden ratings of the users (they are labeled as "99" in the dataset) on the training set  
- [ ] Calculate the performance of the algorithm on the validation dataset  
- [ ] Change hyper-parameters (i.e. learning rates, number of iterations, number of latent factors etc) as needed so you can get good results  
- [ ] Report the MSE on the test dataset  

- [ ] (if you have time) Use pandas to find the best and the worst rated jokes  

- [ ] Once you are done, save your changes in github  
	* Go inside your lab directory and do  
      * ``git add -A -v``  
      * ``git commit -m <message>``  
      * ``git push origin master``  

## Log  

### single thread   
- n_features = 5, 6 with iterations = 100000: mse > 500  
  
- n_features = 7 with iterations = 100000 (first 100 line):  
    * mse = 158.55902514891935  
    * predictions : ![csv](./predictions_7f_10.csv?raw=true)  
    * latent_user_preferences : ![csv](./latent_user_preferences_7f_10.csv?raw=true)  
    * latent_item_features : ![csv](./latent_item_features_7f_10.csv?raw=true)  
    
- n_features = 10 with iterations = 85000 (first 100 line):[abandon]  
    * mse >2k
    * predictions : ![csv](./predictions_10f_10.csv?raw=true)  
    * latent_user_preferences : ![csv](./latent_user_preferences_f_10.csv?raw=true)  
    * latent_item_features : ![csv](./latent_item_features_10f_10.csv?raw=true)  

- Change at 13/02/2018

        mse = (np.array(error) ** 2).mean()  
        err_mse = mse - err_mse_log  
        if (err_mse>0):  
            print(mse, err_mse, err_mse_log)  
            break  
        err_mse_log = mse  
       
- Delete first column of data  
    
        #these are the usernames!  
        del data[data.columns[0]]  
        

