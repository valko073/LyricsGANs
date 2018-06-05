# LyricsGANs

Welcome to the Repository of ai.write_lyrics(). This project is part of the course `SOW-MKI61-2017-PER3-V: 1718 Cognitive Computational Modeling of Language and Web Interaction` at Radboud University.

## The Problem

Most modern music today have predictable lyrics and share a lot of their topics and even vocabulary to an extent that there even is an [online lyrics generator](https://www.song-lyrics-generator.org.uk/). Although the generator offers a large range of genres and even artists to generate texts to, they just fill a simple template, further reinforcing the idea that there is no creativity in modern music.

We want to fix this serious problem that humanity is facing. But, since writing our own songs to combat modern lyrical uniformity seems futile with the huge amounts of monotone music published daily - and our writing skills are admittedly lacking - we decided to tackle the problem programmatically. A simple template approach like the [online lyrics generator](https://www.song-lyrics-generator.org.uk/) mentioned above will not suffice, as it will only deem us to repeat the mistakes of modern musicians. What we need is... **Machine Learning**!

## The Approach

We will train a set of Generative Adversarial Networks to generate music in a given style. One network will generate new songs while the second network will try to distinguish between original and generated text. Although considered infeasible due to the discrete nature of text, recent approaches to tackle the problem have shown promising results (Guo et al., 2017; Press, Bar, Bogin, Berant, & Wolf, 2017; Wang, Qin, & Wan, 2017).
The GAN code was adapted from https://github.com/amirbar/rnn.wgan (last reference)

## The Dataset
Everybody knows, that to train the collection of if-statements commonly denoted as 'Neural Network' you need a lot of data. Luckily, the friendly people over at Kaggle have composed a [dataset of over 55 thousand english lyrics](https://www.kaggle.com/mousehead/songlyrics).

## The Group
This revolutionary project proposal was brought to you by:
Mathis Sackers (@MathisSackers) & Valentin Koch (@valko073) aka. "ai.write_lyrics()"™

## References

Song Lyrics Generator
https://www.song-lyrics-generator.org.uk/


Lyrics for 55000+ songs in English from LyricsFreak
https://www.kaggle.com/mousehead/songlyrics


Sutskever, Ilya, James Martens, and Geoffrey E. Hinton. "Generating text with recurrent neural networks." Proceedings of the 28th International Conference on Machine Learning (ICML-11). 2011.
http://www.cs.utoronto.ca/~ilya/pubs/2011/LANG-RNN.pdf


Taneja, Pratiksha, and Karun Guide Verma. Text Generation Using Different Recurrent Neural Networks. Diss. 2017.
http://dspace.thapar.edu:8080/jspui/handle/10266/4646


H. Wang, Z. Qin, and T. Wan, ‘Text Generation Based on Generative Adversarial Nets with Latent Variable’, arXiv:1712.00170 [cs], Nov. 2017.
https://arxiv.org/pdf/1712.00170.pdf


J. Guo, S. Lu, H. Cai, W. Zhang, Y. Yu, and J. Wang, ‘Long Text Generation via Adversarial Training with Leaked Information’, arXiv:1709.08624 [cs], Sep. 2017.
https://arxiv.org/pdf/1709.08624.pdf


O. Press, A. Bar, B. Bogin, J. Berant, and L. Wolf, ‘Language Generation with Recurrent Generative Adversarial Networks without Pre-training’, arXiv:1706.01399 [cs], Jun. 2017.
https://arxiv.org/pdf/1706.01399.pdf
