# Lab8

For this lab, we will train a network to do sentiment analysis on IMDB data sets - actual data from here [http://ai.stanford.edu/~amaas/data/sentiment/](http://ai.stanford.edu/~amaas/data/sentiment/)

## Lab Exercises Log 

- [x] run ``python imdb.py`` and note somewhere the test accuracy score  
	Test score: 0.6878998550915718  
	Test accuracy: 0.8366  
    ![logo](./imdb_py_log.html?raw=true)  
      
      
- [x] Modify the code to add one more layer of 64 ``relu`` units after the embedding layer record the score (i.e. add a dense followed by an "activation" layer)
	```
	x = inputs
	x = Embedding(max_features, 128, dropout=0.2)(inputs)
	x = Flatten()(x)
	x = Dense(64, activation='relu')(x)
	x = Dropout(0.25)(x)
	x = Dense(1)(x)
	predictions = Activation("sigmoid")(x)
	model = Model(input=inputs, output=predictions)
	model.compile(loss='mse',
              optimizer='adam',
              metrics=['accuracy'])
	```
	```
	_________________________________________________________________
	Layer (type)                 Output Shape              Param #   
	=================================================================
	input_3 (InputLayer)         (None, 80)                0         
	_________________________________________________________________
	embedding_25 (Embedding)     (None, 80, 128)           2560000   
	_________________________________________________________________
	flatten_18 (Flatten)         (None, 10240)             0         
	_________________________________________________________________
	dense_55 (Dense)             (None, 64)                655424    
	_________________________________________________________________
	dropout_28 (Dropout)         (None, 64)                0         
	_________________________________________________________________
	dense_56 (Dense)             (None, 1)                 65        
	_________________________________________________________________
	activation_6 (Activation)    (None, 1)                 0         
	=================================================================
	Total params: 3,215,489
	Trainable params: 3,215,489
	Non-trainable params: 0
	```  
	Test score: 0.18518264630556105  
	Test accuracy: 0.79772
	  
- [x] Modify the code and add a dropout layer after the relu layer
- [x] Remove the layers you have added previously and add a Convolution layer followed by a relu non-linearity and global max pooling (see lecture notes)
- [x] Modify the code and add an LSTM layer in place of the convolution layer
- [x] (Optional - and quite advanced) use both an LSTM layer and a Convolution layer and merge the results with a Merge layer  
	
	```
	inputs = Input(shape=(maxlen,))
	x = inputs
	x = Embedding(max_features, 128, dropout=0.2)(x)
	x1 = LSTM(32)(x)
	x2 = Conv1D(filters=32, kernel_size=3, padding="same")(x)
	x2 = GlobalMaxPooling1D()(x2)
	x = Dot(axes=-1)([x1, x2])
	x = Dense(1)(x)
	predictions = Activation("sigmoid")(x)

	model = Model(input=inputs, output=predictions)
	model.compile(loss='binary_crossentropy',
		optimizer='adam',
		metrics=['accuracy'])
	```
    ```
    __________________________________________________________________________________________________
    Layer (type)                    Output Shape         Param #     Connected to                     
    ==================================================================================================
    input_4 (InputLayer)            (None, 80)           0                                            
    __________________________________________________________________________________________________
    embedding_4 (Embedding)         (None, 80, 128)      2560000     input_4[0][0]                    
    __________________________________________________________________________________________________
    conv1d_4 (Conv1D)               (None, 80, 32)       12320       embedding_4[0][0]                
    __________________________________________________________________________________________________
    lstm_4 (LSTM)                   (None, 32)           20608       embedding_4[0][0]                
    __________________________________________________________________________________________________
    global_max_pooling1d_4 (GlobalM (None, 32)           0           conv1d_4[0][0]                   
    __________________________________________________________________________________________________
    dot_3 (Dot)                     (None, 1)            0           lstm_4[0][0]                     
                                                                     global_max_pooling1d_4[0][0]     
    __________________________________________________________________________________________________
    dense_3 (Dense)                 (None, 1)            2           dot_3[0][0]                      
    __________________________________________________________________________________________________
    activation_2 (Activation)       (None, 1)            0           dense_3[0][0]                    
    ==================================================================================================
    Total params: 2,592,930
    Trainable params: 2,592,930
        Non-trainable params: 0
    ____________________________
    ```
    Test score: 1.192910744406581  
    Test accuracy: 0.81056  

- [x] Once you are done, save your changes in github
	* Go inside your lab directory and do 
      * ``git add -A -v``
      * ``git commit -m <message>``
      * ``git push origin master``  
      
