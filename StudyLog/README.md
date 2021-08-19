# README - Manual of Submission

* Title : Homomorphic Encryption-based Secure Viral Strain Classification
* Team : SeoulTech Data Science
* Track II
* date : August 18, 2021

---
<br>
<br>
<br>

# Introduction
This is a description of our submission (Team SeoulTech Data Science, Track II. Homomorphic Encryption-based Secure Viral Strain Classification). We divide our solution into two docker images, one for preprocessing, the another for inference. In the preprocessing container, putting test dataset as a single line fasta format, you can get a `data.csv` after preprocessing. After that, in the inference container, putting `data.csv`, the result of preprocessing, you can get a `result.csv`, the evaluation of each class for each sample. 
Each image's structure is as followings:
```
- preprocessing_seoultech.tar //preprocessing image
    - /home/
        - preprocessing/
            - preprocessing.exe //executable file for preprocess
            - src/
                - main.cpp //source code of preprocessor
                - preprocessing.py //spare preprocessor

- model_seoultech.tar //inference image
    - /home/HEAAN_pub/HEAAN/HEAAN/
        - run/
            - TestHEAAN //executable file for inference
            - test.cpp
        - src/
            - EvaluatorUtil.cpp //functions related to IO
            - TestScheme.cpp //functions related to homomorphic classification
            - ...
        - lib/
```
The following is a detail explanation of each phase.  We use two terminals to separate work inside and outside docker. Note the comment mark of terminal at the top of the shell command.

<br>
<br>

# Preprocessing

<br>
<br>


## 1. load docker image and run
1. load image of preprocessing
```sh
# terminal 1
sudo docker load -i preprocessing_seoultech.tar
```
2. you can run the container from the image
```sh
# terminal 1
sudo docker run -it preprocessing_seoultech bin/bash
```

3. check your container id

```sh
# terminal 2
sudo docker ps
```

```sh
# result of above
$ CONTAINER ID         IMAGE           			COMMAND	    CREATED	    STATUS	    PORTS	    NAMES
$ <your_container_id>  preprocessing_seoultech	
```

<br>

4. you can limit the container cpu core

```sh
# terminal 2
sudo docker update —cpuset-cpus=1 <your_container_id>
```

<br>
<br>





## 2. put your input file

2. put your input fasta file to the container
    - <your_input_fasta_file> : Your fasta file to preprocess, which should be a single line fasta format
```sh
# terminal 2
sudo docker cp <your_input_fasta_file> <your_container_id>:/home/preprocessor/
```

<br>
<br>

## 3. preprocess
1. change directory and rename your input file

```sh
# terminal 1
cd /home/preprocessor
mv <your_input_fasta_file> data.fa
```

2. run our preprocessor
>output file is data.csv

```sh
# terminal 1
./preprocessing.exe
```

3. export the result of preprocessing
```sh
# terminal 2
sudo docker cp <your_container_id>:/home/preprocessor/data.csv ./data.csv
```

4. exit from preprocessing container
```sh
# terminal 1
exit
```

<br>
<br>
<br>



# Inference
>You would have got "./data.csv" from above

## 1. load docker image and run
1. load image of inference
```sh
# terminal 1
sudo docker load -i model_seoultech.tar
```
2. you can run the container from the image
```sh
# terminal 1
sudo docker run -it model_seoultech bin/bash
```
3. check your container id

```sh
# terminal 2
sudo docker ps
```

```sh
# result of above
$ CONTAINER ID          IMAGE           			COMMAND	    CREATED	    STATUS	    PORTS	    NAMES
$ <your_container_id2>  model_seoultech	
```

<br>
<br>




## 2. put the preprocessed data

1. put the result of preprocessing into the container for inference
```sh
# terminal 2
sudo docker cp ./data.csv <your_container_id2>:/home/HEAAN_pub/HEAAN/HEAAN/run/data/
```

<br>
<br>



## 3. inference

1. change directory and run our model
>output file is result.csv
```sh
# terminal 1
cd /home/HEAAN_pub/HEAAN/HEAAN/run
./TestHEAAN Classify
```

2. export the result of inference
```sh
# terminal 2
sudo docker cp <your_container_id2>:/home/HEAAN_pub/HEAAN/HEAAN/run/result.csv ./result.csv
```

3. exit from inference container
```sh
# terminal 1
exit
```

<br>
<br>






# I/O Interface
## Input fasta file
> As you mentioned, the input fasta file should be a single line fasta file including 2000 test data set.
#### ex)
```sh
# <your_input_fasta_file>
>some_label_of_test_data_0001
AGATACAA...GA
>some_label_of_test_data_0002
ATTTAGCA...TT
```

<br>
<br>


## Output
> The output file contains logit value of each viral strain for each sample in order.
> The first line indicates the name of each viral strain.
#### ex)
```sh
# result.csv
B.1.427,B.1.1.7,P.1,B.1.526
-0.0021423,-0.2412432,0.8425321,-0.2512321
0.215522,0.34113124,-0.6122332,0.0001423
...
```
