# blankcollapse
This code is the Python implementation for the method **blank collapse** proposed in the paper [Blank Collapse: Compressing CTC emission for the faster decoding](https://arxiv.org/abs/2210.17017) accepted to [Interspeech 2023](https://interspeech2023.org/).

This repository includes the function for blank collapse and its jupyter test code using [torchaudio](https://pytorch.org/audio/stable/index.html).

## Results
* The following figure shows the resulting image from blank collapse method whose total length is shrunk by collapsing unnecessary blank frames.

![collapse_fig1](https://github.com/minkjung/blankcollapse/assets/66266065/b97238a2-57e5-4c26-898d-93f33f45fff6)

* This table shows how much this method can save the time in beam search decoding.
<img width="543" alt="image" src="https://github.com/minkjung/blankcollapse/assets/66266065/212bb427-5e7c-472a-9315-6eedf2be3cdc">
