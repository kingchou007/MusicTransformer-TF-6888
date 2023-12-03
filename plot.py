import tensorflow as tf
import matplotlib.pyplot as plt
train_event_file = "logs/mt_decoder/20231203-031448/eval/events.out.tfevents.1701591288.Jinzhous-MacBook-Pro.local.2470.1.v2" 
eval_event_file = "/Users/kingchou/Documents/6888/Music-Transformer-TensorFlow/logs/mt_decoder/20231203-031448/train/events.out.tfevents.1701591288.Jinzhous-MacBook-Pro.local.2470.0.v2"

train_loss_values = []
eval_loss_values = []

for e in tf.compat.v1.train.summary_iterator(train_event_file):
    for v in e.summary.value:
        if v.tag == 'loss': 
            train_loss_values.append(v.simple_value)

for e in tf.compat.v1.train.summary_iterator(eval_event_file):
    for v in e.summary.value:
        if v.tag == 'loss': 
            eval_loss_values.append(v.simple_value)

plt.plot(train_loss_values, label='Train Loss')
plt.plot(eval_loss_values, label='Eval Loss')
plt.title('Training and Evaluation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()


plt.show()
