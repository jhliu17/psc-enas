DATA_PATH=./data

# download
wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz -O $DATA_PATH/cifar10.tar.gz

# tar
tar xf $DATA_PATH/cifar10.tar.gz
mv cifar-10-batches-py cifar10