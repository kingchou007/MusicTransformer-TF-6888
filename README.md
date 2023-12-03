# MusicTransformer - SYSEN 6888

How to Run the code

```bash
git clone https://github.com/kingchou007/MusicTransformer-TF-6888.git
```

## Midi Download

```bash
wget -O midi.zip https://www.dropbox.com/scl/fi/dc1dvys5ae1v6wdab3azd/midi.zip?rlkey=lwk7qcpbfn3dqkjrjsam83k2f&dl=0
```

## Prepare Dataset

```bash
python preprocess.py {midi_load_dir} {dataset_save_dir}
```

## Trainig

```bash
python train.py --epochs={NUM_EPOCHS} --load_path={NONE_OR_LOADING_DIR} --save_path={SAVING_DIR} --max_seq={SEQ_LENGTH} --pickle_dir={DATA_PATH} --batch_size={BATCH_SIZE} --l_r={LEARNING_RATE}
```

## Generate Music

```bash
python generate.py --load_path={CKPT_CONFIG_PATH} --length={GENERATE_SEQ_LENGTH} --beam={NONE_OR_BEAM_SIZE}
```
