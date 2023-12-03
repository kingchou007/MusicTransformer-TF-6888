# MusicTransformer-SYSEN 6888

How to Run the code

```bash
git clone https://github.com/kingchou007/MusicTransformer-TF-6888.git
```

## Midi Download

```bash
sh dataset/script/{ecomp_piano_downloader, midi_world_downloader, ...}.sh
```


## Prepare Dataset

```bash
$ python preprocess.py {midi_load_dir} {dataset_save_dir}
```

## Trainig


* ```bash
  $ python train.py --epochs={NUM_EPOCHS} --load_path={NONE_OR_LOADING_DIR} --save_path={SAVING_DIR} --max_seq={SEQ_LENGTH} --pickle_dir={DATA_PATH} --batch_size={BATCH_SIZE} --l_r={LEARNING_RATE}
  ```

## Hyper Parameter

* learning rate : Scheduled learning rate ( see: [CustomSchedule](custom/callback.py) )
* head size : 4
* number of layers : 6
* seqence length : 2048
* embedding dim : 256 (dh = 256 / 4 = 64)
* batch size : 2

## Result

- Baseline Transformer ( Green, Gray Color ) vs Music Transformer ( Blue, Red Color )

* Loss

  ![loss](readme_src/loss.svg)
* Accuracy

  ![accuracy](readme_src/accuracy.svg)

## Generate Music

* mt.generate() can generate music automatically.

  ```python
  from model import MusicTransformerDecoder
  mt = MusicTransformerDecoder(
    	embedding_dim=256, vocab_size=par.vocab_size, 
    	num_layer=6, 
    	max_seq=max_seq,
    	dropout=0.1,
    	debug=False
  )
  mt.generate(prior=[64], length=2048)
  ```
* If you want to generate with shell wise, see this.

  ```bash
  $ python generate.py --load_path={CKPT_CONFIG_PATH} --length={GENERATE_SEQ_LENGTH} --beam={NONE_OR_BEAM_SIZE}
  ```
