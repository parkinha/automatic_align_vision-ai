import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# 모델 정의
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(256, 256, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),  # Adjusted to a smaller number of units
    layers.Dense(1, activation='sigmoid')  # Binary classification 예시
])

model.compile(optimizer='adam',
              loss='binary_crossentropy',  # Binary classification 예시
              metrics=['accuracy'])

# 모델 구조 확인
model.summary()

# 데이터 경로 설정
train_dir = 'C:/Users/Administrator/Downloads/True/'
validation_dir = 'C:/Users/Administrator/Downloads/backup_ai/'

# 이미지 전처리 및 데이터 증강
train_datagen = ImageDataGenerator(rescale=1./255,
                                   rotation_range=20,
                                   width_shift_range=0.2,
                                   height_shift_range=0.2,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   fill_mode='nearest')

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(256, 256),  # Adjusted to match input shape
    batch_size=32,
    class_mode='binary'  # Binary classification 예시
)

validation_datagen = ImageDataGenerator(rescale=1./255)

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(256, 256),  # Adjusted to match input shape
    batch_size=32,
    class_mode='binary'  # Binary classification 예시
)

if train_generator.samples == 0 or validation_generator.samples == 0:
    raise ValueError("No images found in the specified directories.")

history = model.fit(
    train_generator,
    steps_per_epoch=train_generator.samples // train_generator.batch_size,
    epochs=10,
    validation_data=validation_generator,
    validation_steps=validation_generator.samples // validation_generator.batch_size
)
model.save('ai_model.h5')
model.save_weights('ai_model_weights.h5')
# 훈련과 검증 데이터에 대한 정확도 및 손실을 그래프로 표시
acc = history.history['accuracy']
val_acc = history.history['val_accuracy']
loss = history.history['loss']
val_loss = history.history['val_loss']

epochs = range(len(acc))

plt.plot(epochs, acc, 'bo', label='Training accuracy')
plt.plot(epochs, val_acc, 'b', label='Validation accuracy')
plt.title('Training and validation accuracy')
plt.legend()

plt.figure()

plt.plot(epochs, loss, 'bo', label='Training Loss')
plt.plot(epochs, val_loss, 'b', label='Validation Loss')
plt.title('Training and validation loss')
plt.legend()

plt.show()
