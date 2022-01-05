# 汉语学习者文本多维标注数据集YACLC V1.0

[中文](#简介) | [English](#Introduction)

汉语学习者文本多维标注数据集（Yet Another Chinese Learner Corpus，YACLC）由北京语言大学、清华大学、北京师范大学、云南师范大学、东北大学、上海财经大学等高校组成的团队共同发布。主要项目负责人有杨麟儿、杨尔弘、孙茂松、张宝林、胡韧奋、何姗、岳岩、饶高琦、刘正皓、陈云等。

### 简介

汉语学习者文本多维标注数据集（Yet Another Chinese Learner Corpus，YACLC）是一个大规模的、提供偏误多维标注的汉语学习者文本数据集。我们招募了百余位汉语国际教育、语言学及应用语言学等专业背景的研究生组成标注团队，并采用众包策略分组标注。每个句子由10位标注员进行标注，每位标注员需要给出0或1的**句子可接受度评分**，以及**纠偏标注**（Grammatical Error Correction）和**流利标注**（Fluency based Correction）两个维度的标注结果。纠偏标注是从语法层面对偏误句进行修改，遵循忠实原意、最小改动的原则，将偏误句修改为符合汉语语法规范的句子；流利标注是将句子修改得更为流利和地道，符合母语者的表达习惯。在标注时，若句子可接受度评分为0，则标注员至少需要完成一条纠偏标注，同时可以进行流利标注。若句子可接受度评分为1，则标注员只需给出流利标注。本数据集可用于语法纠错、文本校对等自然语言处理任务，也可为汉语二语教学与习得、语料库语言学等研究领域提供数据支持。

### 数据规模
训练集规模为8,000条，每条数据包括原始句子及其多种纠偏标注与流利标注。验证集和测试集规模都为1,000条，每条数据包括原始句子及其全部纠偏标注与流利标注。

### 数据格式
每条数据中包含汉语学习者所写的待标注句子及其id、所属篇章id、所属篇章标题、标注员数量以及多维标注信息。其中，多维度标注信息包括：

- 标注维度，"1"表示纠偏标注，"0"表示流利标注；
- 标注后的正确文本；
- 标注中的修改操作数量；
- 提供该标注的标注员数量。

**注意：测试集数据无标注者和多维标注信息。**

数据样例如下：

```
{
  "sentence_id": 4308, // 句子id
  "sentence_text": "我只可以是坐飞机去的，因为巴西离英国到远极了。", // 学习者原句文本
  "article_id": 7267, // 该句所属的篇章id
  "article_name": "我放假的打算", // 篇章标题
  "total_annotators": 10, // 共多少个标注者参与了该句的标注
  "sentence_annos": [ // 多维标注信息
    {
      "is_grammatical": 1, // 标注维度：1表示纠偏标注，0表示流利标注
      "correction": "我只能坐飞机去，因为巴西离英国远极了。", // 修改后的正确文本
      "edits_count": 3, // 共有几处修改操作
      "annotator_count": 6 // 共有几个标注者修改为了这一结果
    },
    { // 下同
      "is_grammatical": 1,
      "correction": "我只能是坐飞机去的，因为巴西离英国远极了。",
      "edits_count": 2,
      "annotator_count": 1
    },
    {
      "is_grammatical": 1,
      "correction": "我只可以坐飞机去，因为巴西离英国远极了。",
      "edits_count": 3,
      "annotator_count": 2
    },
    {
      "is_grammatical": 0,
      "correction": "我只能坐飞机去，因为巴西离英国太远了。",
      "edits_count": 6,
      "annotator_count": 2
    }
  ]
}
```
### 评测代码使用

提交结果为文本文件，每行为一个修改后的句子，并与测试集中的数据逐条对应。

- 每条测试集中的数据仅需给出一条修改结果；
- **修改结果需使用[THULAC](https://github.com/thunlp/THULAC)工具包分词**，请提交分词后的结果。

对于提交的结果文件`output_file`，后台将调用`eval.py`将其同标准答案文件`test_gold_m2`进行比较：

```shell
python eval.py output_file test_gold_m2
```

评测指标为F_0.5，输出结果示例：

```json
{
  "Precision": 70.63,	
  "Recall": 37.04,
  "F_0.5": 59.79
}
```

### 引用

如果您使用了本数据集，请引用以下技术报告：
```
@article{wang-etal-2021-yaclc,
  title={YACLC: A Chinese Learner Corpus with Multidimensional Annotation}, 
  author={Yingying Wang, Cunliang Kong, Liner Yang, Yijun Wang, Xiaorong Lu, Renfen Hu, Shan He, Zhenghao Liu, Yun Chen, Erhong Yang, Maosong Sun},
  journal={arXiv preprint arXiv:2112.15043},
  year = {2021}
}
```

### 相关资源

“文心·写作”演示系统：https://writer.wenmind.net/

语法改错论文列表： https://github.com/blcuicall/GEC-Reading-List

------

### Introduction

YACLC is a large-scale Chinese learner text dataset, providing multi-dimensional annotations, jointly released by a team composed of Beijing Language and Culture University, Tsinghua University, Beijing Normal University, Yunnan Normal University, Northeastern University, Shanghai University of Finance and Economics. 

We recruited more than 100 students majoring in Chinese International Education, Linguistics, and Applied Linguistics for crowdsourcing annotation. Each sentence is annotated by 10 annotators, and each annotator needs to give a **sentence acceptability score** of 0 or 1, as well as **grammatical error correction** and **fluency-based correction**. The grammatical corrections follows the principle of minimum modification to make the learners' text meet the Chinese grammatical standards. The fluency-based correction modifies the sentence to be more fluent and authentic, in line with the expression habits of native speakers. This dataset can be used for multiple NLP tasks such as grammatical error correction and spell checking. It can also provide data support for research fields such as Chinese second language teaching and acquisition, corpus linguistics, etc.

### Size

YACLC V1.0 contains the train (8,000 instances), validation (1,000 instances) and test (1,000 instances) sets. Each instance of train set includes 1 sentence written by Chinese learner, various grammatical error corrections and fluent error corrections of the sentence. While, each instance in the validation and test set includes all the corrections provided by the annotators. 

### Format

Each instance is composed of the informations of the sentence, annotators and the multi-dimensional annotations.  The multi-dimensional annotation includes:

- dimensioning, "1" indicates grammatical error correction, and "0" indicates fluency-based correction;
- correct sentence after annotation;
- number of edit operations in this annotation;
- number of annotators for this annotation.

Here is an example:

```
{
  "sentence_id": 4308, // 
  "sentence_text": "我只可以是坐飞机去的，因为巴西离英国到远极了。",
  "article_id": 7267, // the article id that this sentence belongs to
  "article_name": "我放假的打算", // the title of this sentence
  "total_annotators": 10, // the number of annotators for this sentence
  "sentence_annos": [ // multi-dimensional annotations
    {
      "is_grammatical": 1, // 1: grammatical, 0: fluent
      "correction": "我只能坐飞机去，因为巴西离英国远极了。", // corrected sentence 
      "edits_count": 3, // the number of edits of this annotation
      "annotator_count": 6 // the number of annotators for this annotation
    },
    { 
      "is_grammatical": 1,
      "correction": "我只能是坐飞机去的，因为巴西离英国远极了。",
      "edits_count": 2,
      "annotator_count": 1
    },
    {
      "is_grammatical": 1,
      "correction": "我只可以坐飞机去，因为巴西离英国远极了。",
      "edits_count": 3,
      "annotator_count": 2
    },
    {
      "is_grammatical": 0,
      "correction": "我只能坐飞机去，因为巴西离英国太远了。",
      "edits_count": 6,
      "annotator_count": 2
    }
  ]
}
```

### Usage of the Evaluation Code

The submission result is a text file, where each line is a corrected sentence and corresponds to the instance in the test set one by one.

- Only one correction needs to be given for the each instance in the test set.
- **Please submit results after word segmentation using the [THULAC](https://github.com/thunlp/THULAC) toolkit**.

For a submitted result file `output_file`，we will call the script `eval.py` to compare it with the golden standard `test_gold_m2`：

```shell
python eval.py output_file test_gold_m2
```

The Evaluation Metric is F_0.5：

```json
{
  "Precision": 70.63,
  "Recall": 37.04,
  "F_0.5": 59.79
}
```

### Citation

Please cite our technical report if you use this dataset:

```
@article{wang-etal-2021-yaclc,
  title={YACLC: A Chinese Learner Corpus with Multidimensional Annotation},
  author={Yingying Wang, Cunliang Kong, Liner Yang, Yijun Wang, Xiaorong Lu, Renfen Hu, Shan He, Zhenghao Liu, Yun Chen, Erhong Yang, Maosong Sun},
  journal={arXiv preprint arXiv:2112.15043},
  year = {2021}
}
```

