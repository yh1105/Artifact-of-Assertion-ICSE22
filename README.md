# Artifact of "Automated Assertion Generation via Information Retrieval and Its Integration with Deep Learning"

## Usage
Depedency:
* pytorch
* javalang

### Step1: Dataset
unzip Dataset in ./Result and create a config file to indicate data path like:
```
SomeWhere/TrainMethod.txt
SomeWhere/TestMethod.txt
SomeWhere/TrainAssertion.txt
SomeWhere/TestAssertion.txt
SomeWhere/ValMethod.txt
SomeWhere/ValAssertion.txt
```

### Step2: Retrieval
```
python ./Retrieval/IR.py $input_config $result_path
```

### Step3: Adaption by Heuristic

New DataSet
```
python ./Retrieval/IR.py  $result_path 
New 
```

Old DataSet 
```
python ./Retrieval/IR.py  $result_path Old
```
### Step4: Training Neural Models

#### Train:

Data Preparation
```
python ./NeuralModel/DataPrepration $input_config $result_path $neural_data_path_train train
```
Model Training
```
python ./NeuralModel/main $neural_data_path_train $neural_result_path train
```
#### Inference:

Data Preparation
```
python ./NeuralModel/DataPrepration.py $input_config $result_path $neural_data_path_evaluate evaluate
```
Model Evaluating
```
python ./NeuralModel/main.py $neural_data_path_evaluate  $neural_result_path evaluate
```
### Step5: Evaluating
1. Before Evaluate Integrated Approach, Use a deep learning generative model (i.e. [ATLAS](https://gitlab.com/cawatson/atlas---deep-learning-assert-statements/-/tree/master/)) to generate result. 

2. Generate Result from Adapt NN and Integration
```
python AdaptionIntegration.py $input_config $result_path $neural_result_path $integration_threshold
```
3. Evaluate Result

Old Dataset
```
python countMultiOldDataSet.py $result_path
```
New Dataset
```
python countMultiNewDataSet.py $result_path
```
