import tensorflow
from tensorflow.keras.layers import Conv2D, BatchNormalization, GlobalAveragePooling2D, Input, Dense, MaxPooling2D
from tensorflow.python.keras import activations


def functional_model():
    my_input = Input(shape=(28,28,1))
    x = Conv2D(32, (3,3), activation='relu')(my_input)
    x = Conv2D(64, (3,3), activation='relu')(x)
    x = MaxPooling2D()(x)
    x = BatchNormalization()(x)
    
    x = Conv2D(128, (3,3), activation='relu')(x)
    x = MaxPooling2D()(x)
    x = BatchNormalization()(x)
    
    x = GlobalAveragePooling2D()(x)
    x = Dense(64, activation='relu')(x)
    x = Dense(10, activation='softmax')(x)
    
    model = tensorflow.keras.Model(inputs=my_input, outputs=x)
    
    return model

class MyCustomModel(tensorflow.keras.Model):
    def __init__(self):
        super().__init__()
        self.conv1 = Conv2D(32, (3,3), activation='relu')
        self.conv2 = Conv2D(64, (3,3), activation='relu')
        self.maxpool1 = MaxPooling2D()
        self.batchnorm1 = BatchNormalization()
        
        self.conv3 = Conv2D(128, (3,3), activation='relu')
        self.maxpool2 = MaxPooling2D()
        self.batchnorm2 = BatchNormalization()
        
        self.globalmaxpool1 = GlobalAveragePooling2D()
        self.dense1 = Dense(64, activation='relu')
        self.dense2 = Dense(10, activation='softmax')
        
    def call(self,my_input):
        x = self.conv1(my_input)
        x = self.conv2(x)
        x = self.maxpool1(x)
        x = self.batchnorm1(x)
        
        x = self.conv3(x)
        x = self.maxpool2(x)
        x = self.batchnorm2(x)
        x = self.globalmaxpool1(x)
        x = self.dense1(x)
        x = self.dense2(x)

        return x
    
def street_model(nbr_classes):
    my_input = Input(shape=(60,60,3))
    
    x = Conv2D(32, (3,3), activation='relu')(my_input)
    x = MaxPooling2D()(x)
    x = BatchNormalization()(x)
    
    x = Conv2D(64, (3,3), activation='relu')(x)
    x = MaxPooling2D()(x)
    x = BatchNormalization()(x)
    
    x = Conv2D(128, (3,3), activation='relu')(x)
    x = MaxPooling2D()(x)
    x = BatchNormalization()(x)
    
    x = GlobalAveragePooling2D()(x)
    x = Dense(128, activation='relu')(x)
    x = Dense(nbr_classes, activation='softmax')(x)
    
    model = tensorflow.keras.Model(inputs=my_input, outputs=x)
    
    return model


if __name__ == "__main__":
    model = street_model(10)
    model.summary()