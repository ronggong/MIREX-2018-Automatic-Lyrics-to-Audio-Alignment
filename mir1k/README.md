# MIR1k dataset annotation

For the detailed information about the original MIR1k dataset, 
please check [this link](https://sites.google.com/site/unvoicedsoundseparation/mir-1k).
Here is the [link](http://mirlab.org/dataset/public/MIR-1K.rar) to download the dataset.

The annotation in this folder is derived from the `Lyrics` folder in the original dataset. We have done two
modifications:
1) We converted the traditional Mandarin lyrics into simplified Mandarin by using 
[opencc-python](https://github.com/yichen0831/opencc-python), and segmented the lyrics into word-level by using
[FoolNLTK](https://github.com/rockyzhengwu/FoolNLTK). 
Please notice that we haven't verified the Mandarin conversion and word segmentation qualities.

2) We converted the simplified Mandarin lyrics into [pinyin](https://en.wikipedia.org/wiki/Pinyin) format by using
[pinyin](https://pypi.org/project/pinyin/) python package. We have verified the conversion quality and corrected the errors.

## Content
* File names with `_phrase_char.txt` postfix are the lyrics in simplified Mandarin characters.
* File names with `_phrase_pinyin.txt` postfix are the lyrics in pinyin format.

## TODO
- [ ] Correct lyrics segmentation errors
